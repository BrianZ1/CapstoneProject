from django import forms
from django.forms import ModelForm

from .models import Comment

GAME_CHOICE = [
    ('', 'Select Game'),
    ('league of legends', 'Leauge of Legends'),
        ]

class PlayerSearchForm(forms.Form):
    player_name = forms.CharField(label='Player Name', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Player Name...'}))
    
    game = forms.ChoiceField(label='Game Type', choices=GAME_CHOICE)
    
    num_bullet = forms.IntegerField(label='Summary Length', 
                                widget=forms.TextInput(attrs={'placeholder': 'Enter a Number...'}))

class EventSearchForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Event Name...'}))
    game = forms.ChoiceField(label='Game Type', choices=GAME_CHOICE)
    
class ContactForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']

        widgets = {
						'name':forms.TextInput(attrs={'placeholder': 'Enter Your Name...'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Your Email... (Not Required)'}),
						'comment': forms.Textarea(attrs={'placeholder': 'Enter Your Comment...', 'rows':4, 'cols':15}),
        }