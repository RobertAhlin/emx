from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Event
from .forms import SignUpForm
from django.urls import reverse


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('event_date')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        signed_up = event.signed_up.filter(
            approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get a list of existing start numbers or an empty list if there are none
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
            sign_up_form = SignUpForm()

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "signed_up": signed_up,
                "signed": True,
                "liked": liked,
                "sign_up_form": SignUpForm(),
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