from django.shortcuts import render
from .models import Testimonial

# Create your views here.
def testimonial(request):
    testimonials=Testimonial.objects.all()
    return render(request, "testimonial/testimonial.html",{'listTestimonials':testimonials})