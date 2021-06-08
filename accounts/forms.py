from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    # 별도의 widget 옵션을 사용하기 위해 password를 클래스 변수로 따로 지정
    password = forms.CharField(label='암호에옹', widget=forms.PasswordInput)
    password2 = forms.CharField(label='암호한번더', widget=forms.PasswordInput)

    # 기존의 모델 입력 폼을 쉽게 만들기 위한 클래스
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # password와 password2를 비교하기 위한 메서드
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('암호가 틀리데옹ㅋ')

        return cd['password2']