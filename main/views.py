from django.shortcuts import render, redirect
from .forms import ContactForm, ReviewForm
from .models import Contact, Testimonials, AboutUs
from details.models import Blogs
# Create your views here.

def home(request):
    
    total_blogs = Blogs.objects.all()
    contacted = Contact.objects.all()
    context = {"all_blogs": total_blogs, "contact": contacted}
    return render(request, 'main/home.html', context)

def contact(request):
    
    if request.method == "GET":
        
        context = {'form': ContactForm()}
        return render(request, 'main/contact.html', context)
    else:#if POST
        try:
            form = ContactForm(request.POST)
            form.save()
            return redirect('home')
        except ValueError:
            context = {'form': ContactForm(), 'error': "Hey look up the form..... you didn't make the cut"}
            return render(request, 'main/contact.html', context)


def about(request):
    about = AboutUs.objects.all()
    context = {"about": about}
    return render(request, 'main/about.html', context)


def review(request):
    if request.method=="GET":
        context={'form': ReviewForm()}
        return render(request, 'main/review.html', context)
    
    else:#i.e POST
        try:
            forms = ReviewForm(request.POST)
            forms.save()
            return redirect('reviewreaders')
        except ValueError:
            context={'error':'hey Buddy! your form did not make the cut, Please Try Again', 'forms': ReviewForm()}
            return render(request, 'main/review.html', context)
        else:#impossible to transpire
            pass


def reviewreaders(request):
    reviews = Testimonials.objects.order_by('-time')
    context={"reviews": reviews}
    return render(request, 'main/review_reader.html', context)

def charity(request):
    context = {}
    return render(request, 'main/charity.html', context)