from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForms
from operator import attrgetter
from .models import Blogs
from django.db.models import Q
# Create your views here.

#used  for complex q lookup not used as real views
def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Blogs.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(featuring__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))


def all_blogs(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q')
        context['query'] = str(query)

    blogposts = sorted(get_blog_queryset(query), key=attrgetter('time_valid'), reverse=True)
    context["all_blogs"] = blogposts
    # context = {
    #     "all_blogs": qs,
    # }

    return render(request, 'details/all_blogs.html', context)





def specified(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)

    blog_views = Blogs.objects.get(id=blog_id)
    blog_views.post_views += 1
    blog_views.save()

    context = {'views': blog_views, 'blog': blog}
    return render(request, 'details/detailed.html', context)
    

def postings(request):
    if request.method == "GET":
        context = {'form': BlogForms()}
        return render(request, 'details/postings.html', context)
    
    else:#i.e post
        try:
            form = BlogForms(request.POST)
            form.save()
            return redirect('home')
        
        except ValueError:
            context = {'form': BlogForms(), 'error': 'Hey! common fill the form completely'}
            return render(request, 'details/postings.html', context)
        else:
            pass#almost impossible to happen just abiding pep8 style of coding


