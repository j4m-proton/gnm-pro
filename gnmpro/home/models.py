from django.db import models
from service.models import Service

class HeroSlide(models.Model):
    headline = models.CharField(max_length=140)
    subheadline = models.CharField(max_length=200, blank=True)
    cta_text = models.CharField(max_length=40, blank=True)
    cta_url = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="hero/")
    overlay_opacity = models.FloatField(default=0.5)
    order = models.PositiveIntegerField(default=0)
    isImageForPC = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.headline


class AboutFeature(models.Model):
    icon_class = models.CharField(max_length=64, help_text="FontAwesome icon class, e.g. fa-globe")
    title = models.CharField(max_length=120)
    description = models.TextField()
    background_image = models.ImageField(upload_to="Home-about/", null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    heading = models.CharField(max_length=120)
    subheading = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="Explore More")
    button_url = models.URLField(blank=True)
    features = models.ManyToManyField(AboutFeature, related_name="sections", blank=True)
    background_image = models.ImageField(upload_to="about/", null=True, blank=True)

    def __str__(self):
        return self.heading
    
    
class FactSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.TextField(blank=True)
    call_text = models.CharField(max_length=200, default="Call for any query!")
    overlay_color = models.CharField(max_length=20, blank=True, default="#000000")  # optional overlay

    def __str__(self):
        return self.heading


class FactItem(models.Model):
    section = models.ForeignKey(FactSection, on_delete=models.CASCADE, related_name="facts")
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class, e.g., fa-users")
    number = models.PositiveIntegerField()
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label} ({self.number})"
    

class HomeFeatureSection(models.Model):
    heading = models.CharField(max_length=200, default="We Are Trusted Logistics Company Since 2010")
    subheading = models.CharField(max_length=200, default="Our Features")
    background_image = models.ImageField(upload_to="features_bg/", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.heading
    
    @property
    def embed_url(self):
        if not self.video_url:
            return None

        url = self.video_url.strip()

        # youtu.be short links
        if "youtu.be/" in url:
            return url.replace("https://youtu.be/", "https://www.youtube.com/embed/")
        # normal YouTube links
        elif "watch?v=" in url:
            return url.replace("watch?v=", "embed/")
        # shorts format
        elif "/shorts/" in url:
            return url.replace("/shorts/", "/embed/")
        # already embed link
        elif "/embed/" in url:
            return url

        return None


    
class HomeFeature(models.Model):
    section = models.ForeignKey(HomeFeatureSection, related_name="homefeatures", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title          
    
    
    
class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="why_choose_us/", null=True, blank=True)

    def __str__(self):
        return self.title


class WhyChooseUsFeature(models.Model):
    section = models.ForeignKey(
        WhyChooseUs,
        on_delete=models.CASCADE,
        related_name="features"
    )
    icon_class = models.CharField(max_length=100, help_text="e.g. fas fa-ship")
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} ({self.section.title})"    
    
    

class Partner(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="partners/")
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
    

class QuoteSection(models.Model):
    heading_top = models.CharField(
        max_length=200,
        default="Get A Quote",
        help_text="Small heading above the main title"
    )
    heading_main = models.CharField(
        max_length=200,
        default="Request A Free Quote!",
        help_text="Main heading displayed in bold"
    )
    description = models.TextField(
        help_text="Brief paragraph under the heading"
    )
    
    call_text = models.CharField(
        max_length=200,
        default="Call for any query!",
        help_text="Small caption above the phone number"
    )
    background_image = models.ImageField(
        upload_to="quote_section/",
        blank=True,
        null=True,
        help_text="Optional background image for the quote section"
    )

    class Meta:
        verbose_name = "Quote Section"
        verbose_name_plural = "Quote Section"

    def __str__(self):
        return self.heading_main
    

class Quote(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name="quotes")
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"


class Testimonial(models.Model):
    name = models.CharField(max_length=80)
    role = models.CharField(max_length=80, blank=True)
    company = models.CharField(max_length=80, blank=True)
    rating = models.PositiveSmallIntegerField(default=5)
    quote = models.TextField()
    avatar = models.ImageField(upload_to="testimonials/", null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} – {self.company or 'Client'}"    