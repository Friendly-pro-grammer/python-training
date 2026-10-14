from django.db import models
from django.conf import settings
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
            return self.name
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT="draft","Draft"
        PUBLISHED = "published","Published"
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
        null=True,
        blank=True
    )
    published_at = models.DateTimeField(
        null=True,
        blank=True
    )
    class Meta:
        indexes = [
            models.Index(
                fields=['status','-created_at']
            ),
        ]
    def __str__(self):
        return self.title
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    body = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"