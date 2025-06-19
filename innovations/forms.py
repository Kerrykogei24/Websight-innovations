from django import forms
from .models import Image, ImageDetail, Subscriber,Testimonial


class ImageDetailForm(forms.ModelForm):
    class Meta:
        model = ImageDetail
        fields = ['title', 'detail_image']

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, label='Your Name')
#     email = forms.EmailField(label='Your Email')
#     phone = forms.CharField(label='Your Phone Number')
#     subject = forms.CharField(label= 'Your subject')
#     message = forms.CharField(widget=forms.Textarea, label='Your Message')



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']


# from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Firstname',
            'required': True,
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mobile Number',
            'required': True,
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your@gmail.com',
            'required': True,
        })
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
            'required': True,
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'What can we help you?',
        })
    )

#Testimonial
    
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'message', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your role or title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your feedback'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }