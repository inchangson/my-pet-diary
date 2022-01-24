from .models import BulletinFeed
from django import forms

class BulletinFeedForm(forms.ModelForm):
    class Meta:
        model = BulletinFeed
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            }
        labels = {'title': '제목','content': '내용',}