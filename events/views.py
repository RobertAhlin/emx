from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event
from .forms import SignUpForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
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

        return render(
            request,
            "event_detail.html",
            {
                "event": event,
                "signed_up": signed_up,
                "signed": False,
                "liked": liked,
                "sign_up_form": SignUpForm(),
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