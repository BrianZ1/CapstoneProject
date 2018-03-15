from django import forms
from django.forms import ModelForm

from .models import Comment

GAME_CHOICE = [
    ('', 'Game'),
    ('league of legends', 'Leauge of Legends'),
        ]

class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Player Name...'}))
    
    game = forms.ChoiceField(label='', choices=GAME_CHOICE)
    
    num_bullet = forms.IntegerField(label='', 
                                widget=forms.TextInput(attrs={'placeholder': 'Summary Length'}))

class EventSearchForm(forms.Form):
    event_name = forms.CharField(label='', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Event...'}))
    game = forms.ChoiceField(label='', choices=GAME_CHOICE)
    
class ContactForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']

        widgets = {
						'name':forms.TextInput(attrs={'placeholder': 'Your Name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Your Email... (Not Required)'}),
						'comment': forms.Textarea(attrs={'placeholder': 'Your Comment...', 'rows':4, 'cols':15}),
        }