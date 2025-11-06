from django.db import models

# /////////////////////////////////////////////
class SiteMainSettings(models.Model):
    site_name = models.CharField(max_length=255)
    another_name = models.CharField(max_length=255, null=True, blank=True)
    slogan = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to='site_logos/', null=True, blank=True)
    
    working_hours = models.CharField(max_length=255, null=True, blank=True)
    main_location = models.CharField(max_length=255, null=True, blank=True)
    main_email = models.EmailField(max_length=255, null=True, blank=True)
    main_contact = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Site Main Settings"

    def __str__(self):
        return self.site_name

class SiteTheme(models.Model):
    name = models.CharField(max_length=200)
    primarycolor = models.CharField(max_length=200, default='#e41616')
    secondarycolor = models.CharField(max_length=200,default='#e41616') 
    is_default_theme = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        # If this theme is being set as the default
        if self.is_default_theme:
            # Set all other themes to not be the default
            SiteTheme.objects.filter(is_default_theme=True).update(is_default_theme=False)
        
        # Now save the current theme instance
        super(SiteTheme, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name
