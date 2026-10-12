from django import forms


class LoginForm(forms.Form):
    # MySQL의 -- 주석 뒤 공백을 포함해 실습 입력을 그대로 보존한다.
    account = forms.CharField(label="Account:", required=False, strip=False)
    password = forms.CharField(label="Password:", required=False, strip=False)
