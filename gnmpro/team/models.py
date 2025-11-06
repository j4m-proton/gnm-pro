from django.db import models

class HeadTeam(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    order = models.PositiveIntegerField(default=0)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
    
class MidleTopTeam(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    order = models.PositiveIntegerField(default=0)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name   


class TeamMember(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="team/")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=40, blank=True)
    order = models.PositiveIntegerField(default=0)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
