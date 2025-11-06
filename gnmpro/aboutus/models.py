from django.db import models


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=120, default="About Us")
    title = models.CharField(max_length=200, default="Driven by Trust. Powered by Innovation.")
    description = models.TextField(
        default="GNM Cargo commenced business in 2010 and has maintained a strong presence in China for over 15 years, expanding operations across East Africa—Kenya and Uganda—through strategic subsidiaries offering seamless logistics solutions."
    )
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    background_overlay = models.BooleanField(default=True, help_text="Show dark overlay on the image")

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title


class AboutFeature(models.Model):
    section = models.ForeignKey(
        AboutSection,
        on_delete=models.CASCADE,
        related_name="features"
    )
    icon_class = models.CharField(max_length=100, help_text="e.g. fas fa-ship")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]
        verbose_name = "About Feature"
        verbose_name_plural = "About Features"

    def __str__(self):
        return f"{self.title} ({self.section.subtitle})"



class AboutExperienceSection(models.Model):
    icon_class = models.CharField(
        max_length=100,
        default="fas fa-ship",
        help_text="FontAwesome icon class, e.g. fas fa-ship"
    )
    small_title = models.CharField(
        max_length=120,
        default="Experience",
        help_text="Small title above main heading"
    )
    heading = models.CharField(
        max_length=255,
        default="Experienced in East-Africa Logistic Services"
    )
    description = models.TextField(
        help_text="Main paragraph content about experience"
    )
    image = models.ImageField(
        upload_to="about_experience/",
        null=True,
        blank=True,
        help_text="Image shown on the right side"
    )

    class Meta:
        verbose_name = "About Experience Section"
        verbose_name_plural = "About Experience Section"

    def __str__(self):
        return self.heading


class AboutFeatureItem(models.Model):
    section = models.ForeignKey(
        AboutExperienceSection,
        on_delete=models.CASCADE,
        related_name="features"
    )
    icon_class = models.CharField(
        max_length=100,
        default="fas fa-check-circle",
        help_text="FontAwesome icon class"
    )
    text = models.CharField(max_length=120)

    def __str__(self):
        return self.text


class AboutTestimonial(models.Model):
    section = models.OneToOneField(
        AboutExperienceSection,
        on_delete=models.CASCADE,
        related_name="testimonial"
    )
    quote_icon = models.CharField(
        max_length=100,
        default="fas fa-quote-left",
        help_text="FontAwesome icon class for quote"
    )
    quote = models.TextField()
    author = models.CharField(max_length=120)

    def __str__(self):
        return f"Testimonial by {self.author}"
    
    


class ProfessionalismSection(models.Model):
    icon_class = models.CharField(
        max_length=100,
        default="fas fa-ship",
        help_text="FontAwesome icon class for the section"
    )
    small_title = models.CharField(
        max_length=120,
        default="Professionalism",
        help_text="Small title above main heading"
    )
    heading = models.CharField(
        max_length=255,
        default="Skillful and Professional Workers Doing The Job"
    )
    description = models.TextField(
        default="Here all the duties from receiving goods, baling, consolidation, de-consolidation, declaration to delivery by the ship is done with great care and expertise."
    )
    image = models.ImageField(
        upload_to="professionalism/",
        blank=True,
        null=True,
        help_text="Right side image"
    )

    class Meta:
        verbose_name = "Professionalism Section"
        verbose_name_plural = "Professionalism Section"

    def __str__(self):
        return self.heading


class ProfessionalSkill(models.Model):
    section = models.ForeignKey(
        ProfessionalismSection,
        on_delete=models.CASCADE,
        related_name="skills"
    )
    skill_title = models.CharField(max_length=120)
    skill_value = models.PositiveIntegerField(
        default=0,
        help_text="Skill percentage value (0-100)"
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.skill_title} - {self.skill_value}%"
    
    