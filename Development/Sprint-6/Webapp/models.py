from django.db import models
from user_profile.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from .slugs import generate_unique_slug

# Create your models here.

class Category(models.Model):
    title = models.CharField(
        max_length = 150,
        unique = True
    )
    slug = models.SlugField(
        null = True,
        blank = True
    )
    created_date = models.DateField(
        auto_now_add = True
    )
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slag = slugify(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(
        max_length = 150
    )
    slug = models.SlugField(
        null = True,
        blank = True
    )
    created_date = models.DateField(
        auto_now_add = True
    )
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slag = slugify(self.title)
        super().save(*args, **kwargs)

class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'user_blogs',
        on_delete = models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name = 'category_blogs',
        on_delete = models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        related_name = 'tag_blogs',
        blank = True
    )
    title = models.CharField(
        max_length = 250,
    )
    amount = models.FloatField()
    balance = models.FloatField(
        default = 0
    )
    slug = models.SlugField(
        null = True,
        blank = True
    )
    banner = models.ImageField(
        upload_to = 'blog_banners',
        max_length = 500
    )
    description = models.TextField()
    created_date = models.DateField(
        auto_now_add = True
    )

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_unique_slug(self, self.title)
        super().save(*args, **kwargs)

    def donate(self, koto):
        self.balance = self.balance + koto
    
    def get_balance(self):
        return self.balance


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'user_comment',
        on_delete = models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name = 'blog_comments',
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateField(
        auto_now_add = True
    )

    def __str__(self) -> str:
        return self.text
    
class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name = 'user_replies',
        on_delete = models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name = 'comment_replies',
        on_delete = models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateField(
        auto_now_add = True
    )

    def __str__(self) -> str:
        return self.text