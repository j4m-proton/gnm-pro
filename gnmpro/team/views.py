from django.shortcuts import render
from .models import HeadTeam,MidleTopTeam,TeamMember
def team(request):
    topTeam = HeadTeam.objects.all()
    middleTeam = MidleTopTeam.objects.all()
    teamAction = TeamMember.objects.all()

    context = {
        'title':'Our Team | GNM',
        'topTeam': topTeam,
        'middleTeam': middleTeam,
        'teamAction': teamAction
    }
    return render(request, "team/our-team.html",context)
