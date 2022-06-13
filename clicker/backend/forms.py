from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    username = forms.CharField(
        max_length=20,
        label='Кодовое имя гуля:',
        widget=forms.TextInput(attrs={'placeholder': 'Сколопендра'}),
    )
    password = forms.CharField(
        min_length=3,
        max_length=20,
        label='ID гуля в Кокурии:',
        widget=forms.PasswordInput(attrs={'placeholder': '240'}),
    )
    password_confirm = forms.CharField(
        min_length=3,
        max_length=20,
        label='Подтвердите ID:',
        widget=forms.PasswordInput(attrs={'placeholder': '240'}),
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Пароли разные!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user