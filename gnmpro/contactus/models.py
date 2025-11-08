from django.db import models


class ContactInfo(models.Model):
    # General info
    title = models.CharField(max_length=100, default="We are Here for You")
    description = models.TextField(
        default="We would love to hear from you! Use the contact information below to get to us and we’ll be in touch and reach out to you as soon as possible."
    )
    image = models.ImageField(upload_to='contact/', null=True, blank=True)
    
    # Contact details
    opening_hours = models.CharField(max_length=255, default="Mon - Fri: 8:30 AM - 4:30 PM, Sat: 9:00 AM - 3:00 PM")
    
    def __str__(self):
        return "Contact Information"

class SiteSocialHandle(models.Model):
    SOCIAL_MEDIA_CHOICES = [
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('pinterest', 'Pinterest'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        # Add other social media platforms if needed
    ]

    platform = models.CharField(max_length=50, choices=SOCIAL_MEDIA_CHOICES)
    url = models.URLField(max_length=255)
    is_active = models.BooleanField(default=True)

    def get_icon_path(self):
        """Returns the path to the social media icon based on the platform."""
        icon_paths = {
            'facebook': 'assets/imgs/theme/icons/icon-facebook-white.svg',
            'twitter': 'assets/imgs/theme/icons/icon-twitter-white.svg',
            'instagram': 'assets/imgs/theme/icons/icon-instagram-white.svg',
            'pinterest': 'assets/imgs/theme/icons/icon-pinterest-white.svg',
            'youtube': 'assets/imgs/theme/icons/icon-youtube-white.svg',
            'tiktok': 'assets/imgs/theme/icons/tiktok-svgrepo-com.svg'
            # Add paths for other platforms if needed
        }
        
        return icon_paths.get(self.platform, 'assets/imgs/theme/icons/icon-facebook-white.svg')

    def __str__(self):
        return self.platform.capitalize()


class OfficeLocation(models.Model):
    location_type = models.CharField(max_length=100, choices=[('Office', 'Office'), ('Studio', 'Studio'), ('Shop', 'Shop'),('Store', 'Shore')])
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)
    isHQ = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.location_type} - {self.address}"

class SiteSupportContact(models.Model):
    contact_name = models.CharField(max_length=200, blank=True, null=True)
    normal_call = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.contact_name or "Unnamed Contact"
