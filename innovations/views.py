from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from .forms import ImageDetailForm,ContactForm,SubscribeForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponseNotFound
from itertools import zip_longest
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib import messages
from django.core.files import File
import os



# Create your views here.

from django.views.generic import ListView,DetailView
from .models import  Image,Contact,Products,Gallery



def group_testimonials(testimonials, n):
    """Group testimonials into chunks of n (4 in this case)."""
    args = [iter(testimonials)] * n
    return zip_longest(*args)


def home(request):
    images = Image.objects.all().order_by('title')
    
    

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)

            # If no image uploaded, assign a default avatar
            if not testimonial.image:
                default_image_path = os.path.join('static', 'images', 'avatar', 'default.jpg')
                with open(default_image_path, 'rb') as f:
                    testimonial.image.save('default.jpg', File(f), save=False)

            testimonial.save()
            messages.success(request, "Thank you for your testimonial! ")
            return redirect('homepage')  # or whatever your redirect target is
    else:
        form = TestimonialForm()

    # Context setup
    testimonials = Testimonial.objects.all()
    grouped_testimonials = list(group_testimonials(testimonials,1))


    return render (request, 'index.html',{'grouped_testimonials': grouped_testimonials  ,'form': form,'images': images})





def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
   

    return render(request, 'image_detail.html', {'image': image})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save the form data to the database
            contact_instance = Contact.objects.create(
                name=name, email=email, phone=phone, subject=subject, message=message
            )

            # Send email to yourself
            send_mail(
                f'Florance Rest House: {subject}',
                f'Name: {name}\n\nEmail: {email}\n\nPhone Number: {phone}\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Send confirmation email to the user
            client_message = render_to_string('email/client_message.txt', {'name': name})
            send_mail(
                'Thank you for contacting us!',
                strip_tags(client_message),
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=client_message,
                fail_silently=False,
            )

            # Send email to the specified email address from the .env file
            if settings.SPECIFIED_EMAIL:
                send_mail(
                    f'Kirimara Coffee Estate: {subject}',
                    f'Name: {name}\n\nEmail: {email}\n\nPhone Number: {phone}\n\nSubject: {subject}\n\nMessage:\n{message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.SPECIFIED_EMAIL],
                    fail_silently=False,
                )

            return redirect('success_page')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success( request):
    return render (request, 'success_page.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic here, such as sending a confirmation email
            return redirect('success_page')  # Redirect to a success page
    else:
        form = SubscribeForm()

    return render(request, 'footer.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html',{'images': images})


def services(request):
    images = Image.objects.all()
    return render (request, 'service.html',{'images': images})
   
def products(request):
    products = Products.objects.all()
    return render (request, 'products.html',{'products': products})

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)