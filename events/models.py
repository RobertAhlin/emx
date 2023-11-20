from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Active"))

# Event model to create events
class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="emx_events"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    event_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='event_likes', blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @property
    def number_of_likes(self):
        return self.likes.count()

# SignUp model to use when signing up participants to event.
class SignUp(models.Model):
    sign = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='signed_up'
    )
    name = models.CharField(max_length=80)  # Username
    first_name = models.CharField(max_length=80) # First name
    last_name = models.CharField(max_length=80) # Last name
    email = models.EmailField()
    start_number = models.CharField(
        max_length=8,
        blank=True,
        null=True
    )
    transponder = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.name}, signed up {self.created_on}"
