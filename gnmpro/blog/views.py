from django.shortcuts import render, get_object_or_404
from .models import BlogPost



def blogHome(request):
    # Pata pinned post
    pinned_post = BlogPost.objects.filter(isPinned=True).first()

    # Kama hakuna pinned post, chukua latest post
    if not pinned_post:
        pinned_post = BlogPost.objects.order_by('-created_at').first()

    # All posts without the pinned one
    all_posts = BlogPost.objects.exclude(id=pinned_post.id) if pinned_post else BlogPost.objects.all()

    latest_posts = BlogPost.objects.order_by('-created_at')[:4]

    context = {
        'pinned_post': pinned_post,
        'all_posts': all_posts,
        'latest_posts': latest_posts
    }
    
    return render(request, "blog/blogHome.html", context)

def blog_detail(request, blogId):
    post = get_object_or_404(BlogPost, id=blogId)
    sections = post.sections.all()
    latest_posts = BlogPost.objects.order_by('-created_at')[:3]

    post.views +=1
    post.save()

    context= {
        "post": post,
        "sections": sections,
        'latest_posts': latest_posts
        }
    return render(request, "blog/blog-details.html", context)
