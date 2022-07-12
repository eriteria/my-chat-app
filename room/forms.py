from django import forms
from .models import Room


class CreateRoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'slug', 'visibility')


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('creator',)
