from django import forms
from .models import Tweet

MAX_LENGTH = 240

class TweetForm(forms.ModelForm):
    # content = forms.CharField()
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("This tweet is too long !")
        return content

