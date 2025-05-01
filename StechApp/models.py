# StechApp/models.py
from django.db import models
from django.utils.html import format_html
from django.utils import timezone

class Project(models.Model):
    title        = models.CharField(max_length=200)
    image        = models.ImageField(upload_to='projects/')
    description  = models.TextField()
    link         = models.URLField(blank=True)
    created_at   = models.DateTimeField(auto_now_add=True, null=True)  # ← allow null

    def __str__(self):
        return self.title

    def profile_link(self):
        if self.link:
            return format_html('<a href="{}" target="_blank">View</a>', self.link)
        return "-"
    profile_link.short_description = 'Profile Link'




class OurClient(models.Model):
    name        = models.CharField("Client Name", max_length=150)
    image       = models.ImageField("Photo", upload_to='clients/')
    description = models.TextField("Project Description")
    location    = models.CharField("Location", max_length=200, blank=True)
    address     = models.TextField("Address", blank=True)
    email       = models.EmailField("Email Address", blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title       = models.CharField(max_length=200)
    location    = models.CharField(max_length=200, blank=True)
    salary      = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    posted_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    



from django.db import models

class ContactUs(models.Model):
    SERVICE_CHOICES = [
        ('consult', 'Consultant'),
        ('web_dev', 'Web Development'),
        ('app_dev', 'App Development'),
        ('seo', 'Digital Marketing / SEO'),
        ('maint', 'Website Maintenance'),
        ('redesign', 'Website Redesigning'),
    ]

    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    phone        = models.CharField(max_length=20, blank=True)
    service      = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message      = models.TextField(max_length=1500)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.get_service_display()}"





class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Your Name")
    email = models.EmailField(max_length=100, verbose_name="Your Email")
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Rating (1 to 5)")
    feedback = models.TextField(max_length=1500, verbose_name="Your Feedback")
    image = models.ImageField(upload_to='feedback_images/', null=True, blank=True, verbose_name="Feedback Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Feedback Date")

    def __str__(self):
        return f"Feedback from {self.name} - Rating: {self.rating}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"













class ServiceRequest(models.Model):
    INDUSTRY_CHOICES = [
        ('IT', 'IT'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Retail Ecommerce', 'Retail Ecommerce'),
        ('Manufacturing', 'Manufacturing'),
        ('Media & Communication', 'Media & Communication'),
        ('NEOS', 'NEOS'),
    ]

    DEPARTMENT_CHOICES = [
        ('Web Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Web Maintenance', 'Web Maintenance'),
        ('Web Redesigning', 'Web Redesigning'),
        ('SEO Marketing', 'SEO Marketing'),
    ]

    COMPANY_SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    PAGES_CHOICES = [
        ('1-3', '1-3 Pages'),
        ('1-5', '1-5 Pages'),
        ('1-7', '1-7 Pages'),
        ('7+', 'Up to 14 Pages'),
    ]

    WEBSITE_TYPE_CHOICES = [
        ('Static', 'Static Website'),
        ('Dynamic', 'Dynamic Website'),
        ('Ecommerce', 'Ecommerce Website'),
        ('None', 'None'),
    ]

    APP_TYPE_CHOICES = [
        ('Basic', 'Basic App'),
        ('Business', 'Business App'),
        ('Advanced', 'Advanced App'),
        ('None', 'None'),
    ]

    DESKTOP_APP_CHOICES = [
        ('Basic', 'Basic Desktop App'),
        ('Business', 'Business Desktop App'),
        ('Advanced', 'Advanced Desktop Solution'),
        ('None', 'None'),
    ]

    DIGITAL_MARKETING_CHOICES = [
        ('Starter', 'Starter Package'),
        ('Growth', 'Growth Package'),
        ('Premium', 'Premium Package'),
        ('None', 'None'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    company_size = models.CharField(max_length=10, choices=COMPANY_SIZE_CHOICES)
    page_range = models.CharField(max_length=10, choices=PAGES_CHOICES)
    product_services = models.CharField(max_length=500)
    website_type = models.CharField(max_length=20, choices=WEBSITE_TYPE_CHOICES, default='None')
    app_type = models.CharField(max_length=20, choices=APP_TYPE_CHOICES, default='None')
    desktop_package = models.CharField(max_length=20, choices=DESKTOP_APP_CHOICES, default='None')
    digital_package = models.CharField(max_length=20, choices=DIGITAL_MARKETING_CHOICES, default='None')
    message = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.name} ({self.email})"
    


from django.db import models

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/')
    created_at = models.DateTimeField(default=timezone.now)  # 
    def __str__(self):
        return f"Job application from {self.name}"
