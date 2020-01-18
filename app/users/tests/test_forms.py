from django.test import TestCase
from users.forms import UserInfoRegisterForm

class TestParticipantForm(TestCase):
    """
    Tests for Form
    """
    def setUp(self):
        self.correct_payload = {
            'username': 'iand51',
            'first_name':'Ian',
            'age':20,
            'have_siblings':"No",
            'known_env_exposures':"Yes",
            'known_genetic_mutations':"No",
            'password1':'Nauset123',
            'password2':'Nauset123',
        }

        self.incorrect_payload = {
            'username': 'iand51',
            'first_name':'Ian',
            'age':'20',
            'have_siblings':"",
            'known_env_exposures':"Yes",
            'known_genetic_mutations':"No",
            'password1':'Nauset123',
            'password2':'Nauset123',
        }
    def test_correct_inputs(self):
        form = UserInfoRegisterForm(data=self.correct_payload)
        self.assertTrue(form.is_valid())

    def test_incorrect_payload(self):
        form = UserInfoRegisterForm(data=self.incorrect_payload)
        self.assertFalse(form.is_valid())
