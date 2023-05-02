from django.core import paginator
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.utils.text import slugify

from user_profile.models import User
from .models import (
    Blog,
    Category,
    Reply,
    Tag,
    Comment
)

from .forms import TextForm, AddBlogForm, DonationForm

# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    context = {
        "blogs": blogs,
        "tags": tags
    }
    return render(request, 'home.html', context)

def blogs(request):
    queryset = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)

    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    
    context = {
        "blogs": blogs,
        "tags": tags,
        "paginator":paginator
    }
    return render(request, 'blog.html', context)

def category_blogs(request, slug):
    all_blogs = Blog.objects.order_by('-created_date')
    category = get_object_or_404(Category, slug=slug)
    queryset = category.category_blogs.all()
    tags = Tag.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    context = {
        "blogs": blogs,
        "tags": tags,
        "all_blogs": all_blogs
    }
    return render(request, 'category_blogs.html', context)

def tag_blogs(request, slug):
    all_blogs = Blog.objects.order_by('-created_date')
    tag = get_object_or_404(Tag, slug=slug)
    queryset = tag.tag_blogs.all()
    tags = Tag.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)
    
    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    context = {
        "blogs": blogs,
        "tags": tags,
        "all_blogs": all_blogs
    }
    return render(request, 'tag_blogs.html', context)

def blog_details(request, slug):
    form = TextForm()
    blog = get_object_or_404(Blog, slug=slug)
    category = Category.objects.get(id = blog.category.id)
    related_blogs = category.category_blogs.all()
    tags = Tag.objects.order_by('-created_date')
    if request.method == "POST" and request.user.is_authenticated:
        form = TextForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                blog = blog,
                text = form.cleaned_data.get('text')
            )
            return redirect('blog_details', slug = slug)
    context = {
        "blog": blog,
        "related_blogs": related_blogs,
        "tags": tags,
        "form": form
    }
    return render(request, 'blog_details.html', context)

@login_required(login_url='/')
def add_reply(request, blog_id, comment_id):
    blog = get_object_or_404(Blog, id = blog_id)
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            comment = get_object_or_404(Comment, id = comment_id)
            Reply.objects.create(
                user = request.user,
                comment = comment,
                text = form.cleaned_data.get('text')
            )
    return redirect('blog_details', slug=blog.slug)

def search_blogs(request):
    search_key = request.GET.get('search', None)
    recent_blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    if search_key:
        blogs = Blog.objects.filter(
            Q(title__icontains = search_key) |
            Q(category__title__icontains = search_key)|
            Q(user__username__icontains = search_key) |
            Q(tags__title__icontains = search_key)
        ).distinct()
        context = {
            "blogs": blogs,
            "recent_blogs": recent_blogs,
            "tags":tags,
            "search_key":search_key
        }
        return render(request, 'search.html', context)
    else:
        blogs = Blog.objects.order_by('-created_date')
        return render('home')
    
def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def my_blogs(request):
    queryset = request.user.user_blogs.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 6)
    delete = request.GET.get('delete', None)

    if delete:
        blog = get_object_or_404(Blog, pk=delete)
        
        if request.user.pk != blog.user.pk:
            return redirect('home')

        blog.delete()
        messages.success(request, "Your blog has been deleted!")
        return redirect('my_blogs')

    try:
        blogs = paginator.page(page)
    except EmptyPage:
        blogs = paginator.page(1)
    except PageNotAnInteger:
        blogs = paginator.page(1)
        return redirect('blogs')

    context = {
        "blogs": blogs,
        "paginator": paginator
    }
    
    return render(request, 'my_blogs.html', context)
    

@login_required(login_url='login')
def add_blog(request):
    form = AddBlogForm()

    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            tags = request.POST['tags'].split(',')
            user = get_object_or_404(User, pk=request.user.pk)
            amount = request.POST.get('amount')
            category = get_object_or_404(Category, pk=request.POST['category'])
            blog = form.save(commit=False)
            blog.user = user
            blog.amount = amount
            blog.category = category
            blog.save()

            for tag in tags:
                tag_input = Tag.objects.filter(
                    title__iexact = tag.strip(),
                    slug = slugify(tag.strip())
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)
                else:
                    if tag != '':
                        new_tag = Tag.objects.create(
                            title=tag.strip(),
                            slug = slugify(tag.strip())
                        )
                        blog.tags.add(new_tag)

            messages.success(request, "Blog added successfully")
            return redirect('blog_details', slug = blog.slug)
        else:
            print(form.errors)

    context = {
        "form": form
    }
    return render(request, 'add_blog.html', context)

@login_required(login_url='login')
def update_blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = AddBlogForm(instance=blog)

    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES, instance=blog)
        
        if form.is_valid():
            
            if request.user.pk != blog.user.pk:
                return redirect('Home')

            tags = request.POST['tags'].split(',')
            user = get_object_or_404(User, pk=request.user.pk)
            amount = request.POST.get('amount')
            category = get_object_or_404(Category, pk=request.POST['category'])
            blog = form.save(commit = False)
            blog.user = user
            blog.amount = amount
            blog.category = category
            blog.save()

            for tag in tags:
                tag_input = Tag.objects.filter(
                    title__iexact=tag.strip(),
                    slug=slugify(tag.strip())
                )
                if tag_input.exists():
                    t = tag_input.first()
                    blog.tags.add(t)

                else:
                    if tag != '':
                        new_tag = Tag.objects.create(
                            title=tag.strip(),
                            slug=slugify(tag.strip())
                        )
                        blog.tags.add(new_tag)

            messages.success(request, "Blog updated successfully")
            return redirect('blog_details', slug=blog.slug)
        else:
            print(form.errors)


    context = {
        "form": form,
        "blog": blog
    }
    return render(request, 'update_blog.html', context)

@login_required(login_url='login')
def donation(request, slug):
    blog = get_object_or_404(Blog, slug = slug)
    if request.method == "POST":
        amount = request.POST.get('amount')
        amount = float(amount)
        if amount > 0:
            blog.donate(amount)
            blog.save()
            messages.success(request, "Donation Received Successfully")
        else:
            messages.error(request, "Amount Should Be Greater Than 0")
    return redirect('blog_details', blog.slug)