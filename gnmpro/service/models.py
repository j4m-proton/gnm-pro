from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class ServicesSection(models.Model):
    icon_class = models.CharField(
        max_length=50, 
        default="fas fa-ship",
        help_text="FontAwesome icon class, e.g., fas fa-ship"
    )
    small_title = models.CharField(
        max_length=120, 
        default="Our Services",
        help_text="Small heading above the main title"
    )
    main_title = models.CharField(
        max_length=200,
        default="We Provide The Best Logistic Services For Your Needs",
        help_text="Main heading displayed in bold"
    )
    description = models.TextField(
        default="We offer cargo consolidation and de-consolidation, Cargo Sourcing, Door-to-door cargo delivery services across East Africa and Southern Africa. "
                "We provide best and affordable services in clearing and forwarding, to both Full Container Shipping Services (FCL) and Loose Cargo Shipping Services (LCL) to our customers."
    )

    class Meta:
        verbose_name = "Services Section"
        verbose_name_plural = "Services Section"

    def __str__(self):
        return self.small_title


class ServiceCategory(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.CharField(max_length=200,blank=True)
    order = models.PositiveIntegerField(default=0)
    happy_client = models.PositiveIntegerField(default=0)
    complete_shipment = models.PositiveIntegerField(default=0)
    customer_reviews = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Service categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="services")
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    excerpt = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    icon_class = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="services/", null=True, blank=True)
    brochure = models.FileField(upload_to="brochures/", null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service_detail", args=[self.slug])
    
class ServiceDetail(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="details"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.service.title} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ServiceDetailSection(models.Model):
    service_detail = models.ForeignKey(
        ServiceDetail,
        on_delete=models.CASCADE,
        related_name="sections"
    )
    heading = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.service_detail.title} - {self.heading}"


class ServiceDetailMedia(models.Model):
    section = models.ForeignKey(
        ServiceDetailSection,
        on_delete=models.CASCADE,
        related_name="medias"
    )
    image = models.ImageField(upload_to="service_detail_media/images/", null=True, blank=True)
    video = models.FileField(upload_to="service_detail_media/videos/", null=True, blank=True)
    video_url = models.URLField(blank=True, help_text="YouTube or Vimeo link")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.section.heading} - Media {self.id}"    



class HardworkingSection(models.Model):
    icon_class = models.CharField(max_length=50, default="fas fa-ship")
    small_title = models.CharField(max_length=200, default="HARDWORKING INDIVIDUALS")
    main_title = models.CharField(max_length=300, default="Providing Excellent and Quality Customer Services")
    description = models.TextField(default="All activities and operations are performed with high commitment and integrity while putting customers’ needs forward. Teamwork, reliability, innovativeness and professionalism make us one of the best in the industry.")
    image = models.ImageField(upload_to="hardworking/", null=True, blank=True)

    class Meta:
        verbose_name = "Hardworking Section"
        verbose_name_plural = "Hardworking Sections"

    def __str__(self):
        return self.main_title


class HardworkingFeature(models.Model):
    section = models.ForeignKey(HardworkingSection, related_name="features", on_delete=models.CASCADE)
    icon_class = models.CharField(max_length=50, default="fas fa-people-carry")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Hardworking Feature"
        verbose_name_plural = "Hardworking Features"

    def __str__(self):
        return f"{self.title} ({self.section.small_title})"
    
    
class TestimonialSectionContent(models.Model):
    small_title = models.CharField(max_length=100, default="Client Testimonial", help_text="Small heading above the main title")
    main_title = models.CharField(max_length=200, default="More Than 40+ Satisfied Client Testimonial")
    description = models.TextField(default="Endorsements from more than 40 customers across East Africa and China vouching the quality and value of our services.")

    class Meta:
        verbose_name = "Testimonial Section Content"
        verbose_name_plural = "Testimonial Section Content"

    def __str__(self):
        return self.main_title    