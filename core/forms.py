from django.contrib.auth.forms import UserCreationForm

from core.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
