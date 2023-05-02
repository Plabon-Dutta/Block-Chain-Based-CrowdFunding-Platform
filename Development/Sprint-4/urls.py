from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'Home'),
    path('blogs/', blogs, name = 'Blogs'),
    path('about_us/', about_us, name = 'about_us'),
    path('contact_us/', contact_us, name = 'contact_us'),
    path('category_blogs/<str:slug>/', category_blogs, name = 'category_blogs'),
    path('tag_blogs/<str:slug>/', tag_blogs, name = 'tag_blogs'),
    path('blog/<str:slug>/', blog_details, name = 'blog_details'),
    path('add_reply/<int:blog_id>/<int:comment_id>', add_reply, name = 'add_reply'),
    path('search_blogs/', search_blogs, name = 'search_blogs'),
    path('my_blogs/', my_blogs, name='my_blogs'),
    path('add_blog/', add_blog, name='add_blog'),
    path('update_blog/<str:slug>/', update_blog, name='update_blog'),
    path('donate/<str:slug>/', donation, name='donation'),
]