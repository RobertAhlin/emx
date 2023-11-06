from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Event


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        sign = get_object_or_404(queryset, slug=slug)
        signed_up = sign.signed_up.filter(
            approved=True).order_by("-created_on")
        liked = False
        if sign.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "event_detail.html",
            {
                "sign": sign,
                "signed_up": signed_up,
                "liked": liked,
            },
        )
