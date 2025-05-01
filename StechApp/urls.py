# StechApp/urls.py
from django.urls import path
from . import views  # Import your views

urlpatterns = [
   path('home/', views.Home, name="home"), # Replace 'home' with your actual view function
   path('about/', views.About, name="about"), 
   path('Webdevelopment/', views.Web, name="web"), 
   path('Appdevelopment/', views.App, name="App"), 
   path('Desktop/', views.Desktop, name="Desktop"),
   path('WebMaintence/', views.Main, name="WebMain"),
   path('WebRedisgning/', views.WebRe, name="WebRe"),
   path('SEO Services/', views.SEO, name="SEo"),
   path('Digital/', views.Digital, name="Digital"),
   path('Testimonial/', views.Testimonial, name="Test"),
   path('Our Vision/', views.JoinVision, name="JoinVison"),
   path('Team/', views.Team, name="Team"),
   path('Project/', views.project_list, name="Project"),
   path('Our Client/', views.Clint, name="Clint"),
   path('Jobs/', views.jobs, name="Our Jobs"),
   path('Contact/', views.contact_us, name="Contact"),
   path('feedback/', views.feedback, name='feedback'),
   path('Login/', views.Login, name='Signin'),
   path('register/', views.register_view, name='register'),
   path('logout/', views.logout_view, name='Logout'),
  path('get-started/', views.start, name='get_started'),
  path('job-apply/', views.job_apply, name='job-apply'),
]






