from django.shortcuts import render
from users.models import UserInfo
from django.views import View
from django.contrib.auth.models import User


class ParticipantHomeView(View):
    """
    View for participant home page
    """

    def get(self, request, *args, **kwargs):
        queryset = UserInfo.objects.filter(user__is_staff=False)

        participant_info = []
        for participant in queryset:
            participants = {
                'name': participant.user.first_name,
                'age': participant.age,
                'have_siblings': participant.have_siblings,
                'known_env_exposures': participant.known_env_exposures,
                'known_genetic_mutations': participant.known_genetic_mutations
            }
            participant_info.append(participants)

        return render(request, 'client/home.html', {'context': participant_info})
