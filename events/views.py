from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Event, SignUp
from .forms import SignUpForm
from django.urls import reverse
from django.utils import timezone


class EventList(generic.ListView):
    model = Event
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        today = timezone.now().date()
        return Event.objects.filter(status=1, event_date__gte=today).order_by('event_date')


class OldEventList(generic.ListView):
    model = Event
    template_name = 'old_events.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        today = timezone.now().date()
        return Event.objects.filter(status=1, event_date__lt=today).order_by('event_date')


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        signed_up = event.signed_up.filter(
            approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True

        # List of existing start numbers or an empty list if there are none
        existing_start_numbers = [str(sign.start_number)
                                  for sign in signed_up if sign.start_number]

        sign_up_form = SignUpForm()
        sign_up_form.fields['start_number'].widget.attrs['data-existing-start-numbers'] = ','.join(
            existing_start_numbers)

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "signed_up": signed_up,
                "signed": False,
                "liked": liked,
                "sign_up_form": sign_up_form,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        signed_up = event.signed_up.filter(
            approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True

        sign_up_form = SignUpForm(data=request.POST)

        if sign_up_form.is_valid():
            sign_up_form.instance.email = request.user.email
            sign_up_form.instance.name = request.user.username
            sign_up = sign_up_form.save(commit=False)
            sign_up.sign = event
            sign_up.save()

            messages.success(
                request, "You have successfully signed up for the event.")
        else:
            # Form is not valid, set the data-existing-start-numbers attribute
            existing_start_numbers = [str(sign.start_number)
                                    for sign in signed_up if sign.start_number]
            sign_up_form.fields['start_number'].widget.attrs['data-existing-start-numbers'] = ','.join(
                existing_start_numbers)

            print(sign_up_form.errors)
            messages.error(
                request, "Failed to sign up. Please check the form.")

        # Always render the template, whether the form is valid or not
        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "signed_up": signed_up,
                "signed": False,
                "liked": liked,
                "sign_up_form": sign_up_form,
            },
        )


class EventLike(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class DeleteSignUp(View):
    def post(self, request, slug, signup_id):
        # Ensure that the user can only delete their own sign-up
        sign_up = get_object_or_404(
            SignUp, id=signup_id, sign__slug=slug, name=request.user.username)
        sign_up.delete()
        return redirect('event_detail', slug=slug)
