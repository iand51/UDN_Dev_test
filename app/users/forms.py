from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo


class UserInfoRegisterForm(UserCreationForm):
    """
    Form for a user to register with
    """
    CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    age = forms.IntegerField(label="Age")
    have_siblings = forms.ChoiceField(label="Does the participant have any siblings?", choices=CHOICES)
    known_env_exposures = forms.CharField(label="Any known Enviormental Exposures?")
    known_genetic_mutations = forms.CharField(label="Any Known Genetic Mutations?")

    class Meta:
        model = User
        fields = ["username", "first_name", "age", "have_siblings", "known_env_exposures", "known_genetic_mutations"]
