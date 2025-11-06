from sitesetting.models import SiteTheme, SiteMainSettings
from contactus.models import SiteSocialHandle


def default(request):
    primary_color = ''
    secondary_color = ''
    
    try:
        theme = SiteTheme.objects.filter(is_default_theme=True).first()
        if theme:
            primary_color = theme.primarycolor
            secondary_color = theme.secondarycolor
        else:
            primary_color = ''
            secondary_color = ''
    except:
        primary_color = ''
        secondary_color = ''
        
    # Retrieve SiteMainSettings
    site_settings = SiteMainSettings.objects.first()
    social_handles = SiteSocialHandle.objects.filter(is_active=True)    

    

    context = {
        'primarycolor':primary_color,
        'secondarycolor':secondary_color,
        'social_handles': social_handles,
        'siteMainSettings':{
                'site_name': site_settings.site_name if site_settings else '',
                'another_name': site_settings.another_name if site_settings else '',
                'slogan': site_settings.slogan if site_settings else '',
                'logo_url': site_settings.logo.url if site_settings and site_settings.logo else '',
                'working_hours': site_settings.working_hours if site_settings else '',
                'main_location': site_settings.main_location if site_settings else '',
                'main_email': site_settings.main_email if site_settings else '',
                'main_contact': site_settings.main_contact if site_settings else '',
            },
    }
    
    print(' PPPPPPPPPPPPPP')
    
    return context