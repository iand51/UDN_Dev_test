from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserInfoRegisterForm
from .models import UserInfo
from django.contrib.auth.models import User


class ParticipantFormView(View):
    """
    View for Participant Form
    """
    participant_form = UserInfoRegisterForm

    def get(self, request):
        form = self.participant_form
        return render(request, 'users/participant_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.participant_form(request.POST)
        if form.is_valid():
            user=form.save()


            participant = UserInfo.objects.create(
                        user=user,
                        age = form.cleaned_data.get('age'),
                        have_siblings = form.cleaned_data.get('have_siblings'),
                        known_env_exposures = form.cleaned_data.get('known_env_exposures'),
                        known_genetic_mutations = form.cleaned_data.get('known_genetic_mutations'))

            participant.save()
            user.refresh_from_db()
            return redirect('participant_home')

        else:
            messages.error(request, f'Invalid Data')
            return render(request, 'users/participant_form.html', {'form': form})
