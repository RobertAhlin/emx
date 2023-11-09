from django.contrib import admin
from .models import Event, SignUp
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):

    list_display = ('title', 'event_date', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_field = ('content')


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):

    list_display = ('approved', 'fname', 'lname', 'start_number',
                    'transponder', 'created_on', 'sign', 'name')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'start_number')
    actions = ['approve_sign_ups']

    def approve_sign_ups(self, request, queryset):
        queryset.update(approved=True)
