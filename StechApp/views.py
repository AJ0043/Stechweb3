from django.shortcuts import render , redirect
from .models import Project,OurClient,Job,Feedback ,ServiceRequest
from django.conf import settings
from django.contrib import messages
from .models import ContactUs
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout 
from django.contrib.auth.models import User
import re
from django.utils import timezone
import requests
from .models import JobApplication
import urllib.parse
import webbrowser
from xhtml2pdf import pisa
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    return render(request,"index.html")


def About(request):
    return render(request,"About.html")

def Web(request):
    return render(request,"webd.html")


def App(request):
    return render(request,"App.html")

def Desktop(request):
    return render(request,"Desktop.html")

def Main(request):
    return render(request,"WebMain.html")

def WebRe(request):
    return render(request,"WebRe.html")

def SEO(request):
    return render(request,"SEO.html")

def Digital(request):
    return render(request,"Digital.html")

def Testimonial(request):
    # Fetch all feedback records from the database
    feedbacks = Feedback.objects.all().order_by('-created_at')  # You can order them by date or rating as needed
    return render(request, "Testimonial.html", {'feedbacks': feedbacks})

def JoinVision(request):
    return render(request,"Join.html")


def Team(request):
    return render(request,"Team.html")


def project_list(request):
    projects = Project.objects.all()   # ← returns a QuerySet, not a single object
    return render(request, 'Project.html', {
        'projects': projects
    })




def Clint(request):
    """
    Display a list of all OurClient entries.
    """
    clients = OurClient.objects.all().order_by('name')
    return render(request, "Client.html", {
        "clients": clients,
    })

def jobs(request):
    all_jobs = Job.objects.order_by("-posted_at")
    return render(request, "jobs.html", {"jobs": all_jobs})


from django.shortcuts import redirect
@login_required
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message_text = request.POST.get('message')

        # WhatsApp Message create karna
        whatsapp_message = (
            f"New Contact Inquiry%0A"
            f"Name: {name}%0A"
            f"Email: {email}%0A"
            f"Phone: {phone}%0A"
            f"Service: {service}%0A"
            f"Message: {message_text}"
        )

        # Tumhara WhatsApp number
        whatsapp_number = "918949167574"  # 91 + 8949167574

        # WhatsApp Link banana
        whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"

        # Django success message
        messages.success(request, 'Thanks for contacting us, we will contact you soon.')

        # WhatsApp par redirect karna
        return HttpResponseRedirect(whatsapp_link)

    return render(request, 'contact.html')


@login_required
def feedback(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        feedback_text = request.POST.get('feedback')
        image = request.FILES.get('image')  # Make sure this matches the model's image field

        # Save the feedback data into the model
        feedback = Feedback(
            name=name,
            email=email,
            rating=rating,
            feedback=feedback_text,
            image=image
        )
        feedback.save()

        # Show success message
        messages.success(request, 'Thank you for your feedback!')
        return redirect('feedback')  # Redirect back to feedback page

    return render(request, 'feedback.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your actual home view name
        else:
            messages.error(request, "Invalid username or password.")  # Error shown when wrong input
    
    return render(request, 'Login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Password length check (between 6 to 8 characters)
        if len(password1) < 6 or len(password1) > 8:
            messages.error(request, "Password must be between 6 to 8 characters long!")
            return redirect('register')

        # Check if password has both letters and numbers
        if not re.search(r'[A-Za-z]', password1) or not re.search(r'[0-9]', password1):
            messages.error(request, "Password must contain both letters and numbers!")
            return redirect('register')

        # Username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already registered. Please try another username.")
            return redirect('register')

        # Email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered. Please try another email.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('Signin')
    
    return render(request, 'Ragister.html')

def logout_view(request):
    logout(request)
    return redirect('home')



from .models import ServiceRequest

@login_required
def start(request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        industry = request.POST.get('industry')
        department = request.POST.get('department')
        company_size = request.POST.get('company_size')
        page_range = request.POST.get('page_range')
        product_services = request.POST.get('product_services')
        website_type = request.POST.get('website_type')
        app_type = request.POST.get('app_type')
        desktop_package = request.POST.get('desktop_package')
        digital_package = request.POST.get('digital_package')
        price_negotiation = request.POST.get('price_negotiation')
        message = request.POST.get('text_message')

        # Save to DB
        new_request = ServiceRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            industry=industry,
            department=department,
            company_size=company_size,
            page_range=page_range,
            product_services=product_services,
            website_type=website_type,
            app_type=app_type,
            desktop_package=desktop_package,
            digital_package=digital_package,
            message=message,
            created_at=timezone.now()
        )

        # Generate PDF
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'industry': industry,
            'department': department,
            'company_size': company_size,
            'page_range': page_range,
            'product_services': product_services,
            'website_type': website_type,
            'app_type': app_type,
            'desktop_package': desktop_package,
            'digital_package': digital_package,
            'price_negotiation': price_negotiation,
            'message': message
        }

        pdf_file = generate_pdf(context)
        filename = f"{name.replace(' ', '_')}_request.pdf"

        if pdf_file:
            fs = FileSystemStorage()
            filepath = fs.save(f"pdfs/{filename}", pdf_file)
            pdf_url = request.build_absolute_uri(fs.url(filepath))
        else:
            pdf_url = "PDF generation failed."

        # WhatsApp redirect
        whatsapp_message = (
            f"New Request from {name}%0A"
            f"Email: {email}%0A"
            f"Phone: {phone}%0A"
            f"PDF Link: {pdf_url}"
        )
        whatsapp_number = "918949167574"
        whatsapp_link = f"https://wa.me/{whatsapp_number}?text={whatsapp_message}"

        messages.success(request, "Thank you! Redirecting you to WhatsApp with your request.")
        return HttpResponseRedirect(whatsapp_link)

    return render(request, 'Start.html')





def generate_pdf(context):
    template = get_template('pdf_template.html')
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result
    return None









from django.utils import timezone
@login_required
def job_apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        message = request.POST.get('message')
        resume = request.FILES.get('resume')

        # Save to database, including created_at manually
        job_application = JobApplication.objects.create(
            name=name,
            email=email,
            phone=phone,
            role=role,
            message=message,
            resume=resume,
            created_at=timezone.now()  # Manually set the created_at field
        )

        # WhatsApp Notification (same as before)
        whatsapp_number = "918949167574"  # Your WhatsApp number here
        whatsapp_message = f"📩 New Job Application Received:\nName: {name}\nEmail: {email}\nPhone: {phone}\nRole: {role}\nMessage: {message}\nPlease check your email for the resume."

        # URL-encode the message
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={urllib.parse.quote(whatsapp_message)}"
        
        # Open WhatsApp Web with the pre-filled message
        webbrowser.open(whatsapp_url)

        # Show success message to the user
        messages.success(request, 'Your application has been submitted successfully! A notification has been sent to the team.')

        return redirect('job-apply')  # Redirect back to the form after submission
    
    return render(request, 'jobFrom.html')  # Show the form if the request is GET
