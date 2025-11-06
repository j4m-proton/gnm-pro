# appBlog/models.py
from django.db import models

from django.utils.text import slugify

from django.contrib.auth import get_user_model

# Use get_user_model() to fetch the custom user model
User = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='based on your basiness you offer eg .shipping, wharehouse')
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    category = models.ForeignKey(BlogCategory, related_name="posts", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    cover_image = models.ImageField(upload_to="blog_covers/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    time_to_read = models.PositiveIntegerField(default=7, help_text='how long it take to finish read')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    isPinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class BlogSection(models.Model):
    blog = models.ForeignKey(BlogPost, related_name="sections", on_delete=models.CASCADE)
    heading = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="blog_sections/", blank=True, null=True)
    video = models.FileField(upload_to="blog_videos/", blank=True, null=True)  # au unaweza kutumia video URL
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.blog.title} - {self.heading or 'Section'}"