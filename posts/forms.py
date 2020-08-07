# forms.py == modelform에 대한 class를 정의해주기 위한 파일

from django import forms
from posts.models import Post, Datt

class PostForm(forms.ModelForm): #이렇게 반드시해야한다.
    class Meta:
        model = Post
        fields = ['author','contents'] #실제 입력할 것이 무엇인가.

class DattForm(forms.ModelForm): #이렇게 반드시해야한다.
    class Meta:
        model = Datt
        fields = ['author','contents'] #실제 입력할 것이 무엇인가.