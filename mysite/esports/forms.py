from django import forms

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
    
class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Name')
    contact_email = forms.EmailField(label='Email')
    content = forms.CharField(label='Comments', widget=forms.Textarea)