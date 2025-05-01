# StechApp/admin.py

from django.contrib import admin
from .models import Project , OurClient ,Job,ContactUs,Feedback ,ServiceRequest,JobApplication

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at')   # remove 'profile_link'
    # list_filter = ('created_at', )                  # remove any reference to profile_link
    search_fields = ('title',)


@admin.register(OurClient)
class OurClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email')
    search_fields = ('name', 'location', 'email')



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "salary", "posted_at")
    list_filter  = ("location", "posted_at")
    search_fields = ("title", "description")




@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display   = ('name', 'email', 'service', 'submitted_at')
    list_filter    = ('service', 'submitted_at')
    search_fields  = ('name', 'email', 'message')
    ordering       = ('-submitted_at',)


class FeedbackAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('name', 'email', 'rating', 'created_at', 'image')

    # Add filters and search options
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'email', 'feedback')

    # Optional: Make fields editable from list view
    list_editable = ('rating',)

    # Show a more detailed view for feedback
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'rating', 'feedback', 'image')
        }),
        ('Additional Info', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    # Hide or show created_at in list view
    readonly_fields = ('created_at',)

# Register the Feedback model with custom admin settings
admin.site.register(Feedback, FeedbackAdmin)






@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'industry', 'department', 'created_at')
    list_filter = ('industry', 'department', 'company_size', 'website_type', 'app_type')
    search_fields = ('name', 'email', 'phone')





class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'resume', 'message', 'date_applied')
    search_fields = ('name', 'email', 'role')
    list_filter = ('role', 'created_at')  # Use created_at here
    ordering = ('-created_at',)  # Use created_at for ordering
    readonly_fields = ('resume',)

    def date_applied(self, obj):
        return obj.created_at  # Use created_at here
    date_applied.short_description = 'Date Applied'
