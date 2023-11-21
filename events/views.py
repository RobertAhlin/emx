from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Event, SignUp
from .forms import SignUpForm
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic.edit import UpdateView


class EventList(generic.ListView):
    """
    Displays a list of upcoming events.
    Paginates the event list by 6 per page.
    Filters events based on status and event date.
    Orders events by event date.
    """
    model = Event
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        today = timezone.now().date()
        return Event.objects.filter(
            status=1,
            event_date__gte=today
            ).order_by('event_date')


class OldEventList(generic.ListView):
    """
    Displays a list of past events.
    Filters events based on status and past event date.
    Orders events by event date.
    """
    model = Event
    template_name = 'old_events.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        today = timezone.now().date()
        return Event.objects.filter(
            status=1,
            event_date__lt=today
            ).order_by('event_date')


class EventDetail(View):
    """
    Handles displaying event details and sign-ups.
    Renders event details and sign-up form.
    """
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
            sign_up_form = SignUpForm()

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "signed_up": signed_up,
                "signed": True,
                "liked": liked,
                "sign_up_form": sign_up_form,
            },
        )


class EventLike(View):
    """
    Handles liking/unliking an event.
    Adds or removes the current user from the event likes.
    """
    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class EditSignUp(UpdateView):
    """
    Handles editing sign-ups for events.
    Displays form for editing sign-up details.
    """
    model = SignUp
    form_class = SignUpForm
    template_name = 'edit_signup.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        signup_id = self.kwargs.get('signup_id')
        return get_object_or_404(
            SignUp, id=signup_id,
            sign__slug=slug,
            name=self.request.user.username
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        context['signup_id'] = self.kwargs.get('signup_id')
        context['form'] = self.get_form()  # Change this line
        return context

    def form_valid(self, form):
        # Retrieve the existing start number from the database
        existing_start_number = SignUp.objects.get(
            id=form.instance.id).start_number

        # Set the retrieved start number in the form
        form.instance.start_number = existing_start_number

        # Success message on edit sign up.
        messages.success(
            self.request, 'Your sign up details updated successfully.')

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the event detail page after successful form submission
        return reverse('event_detail', args=[self.kwargs['slug']])


class DeleteSignUp(View):
    """
    Handles deleting a sign-up from an event.
    """
    def post(self, request, slug, signup_id):
        # Ensure that the user can only delete their own sign-up
        sign_up = get_object_or_404(
            SignUp, id=signup_id, sign__slug=slug, name=request.user.username)
        sign_up.delete()

        # Message to confirm removed sign up.
        messages.success(
            request, f'You have removed {sign_up.first_name} {sign_up.last_name} from the event.')

        return redirect('event_detail', slug=slug)
