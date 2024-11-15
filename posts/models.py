from django.db import models
import uuid


class HashTag(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    content_id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    type = [
        ("facebook", "페이스북"),
        ("X", "X"),
        ("instagram", "인스타"),
        ("threads", "스레드"),
    ]
    # type = TYPE_CHOICES, verbose_name="SNS종류"
    title = models.CharField(max_length=50)
    content = models.TextField()
    hashtags = models.ManyToManyField(
        HashTag, related_name="hash_products"
    )
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title