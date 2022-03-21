from django import forms
from .models import UserInfo

class LoginForm(forms.Form):
    userid = forms.CharField(error_messages={
        "required": "아이디를 입력해주세요."
    }, max_length=30, label="아이디")
    password = forms.CharField(error_messages={
        "required": "비밀번호를 입력해주세요."
    }, widget= forms.PasswordInput, max_length=50, label="비밀번호")

