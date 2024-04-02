from django import forms


class SendEmailMessageForm(forms.Form):
    name = forms.CharField(max_length=256, label="Имя", widget=forms.TextInput(
        attrs={"class": "form-control bg-transparent border-0 border-bottom"}))
    email = forms.EmailField(label="Почта",
                             widget=forms.EmailInput(
                                 attrs={"class": "form-control bg-transparent border-0 border-bottom"}))
    message = forms.CharField(label="Текст сообщения",
                              widget=forms.Textarea(
                                  attrs={"class": "form-control bg-transparent border-0 border-bottom"}))


class UpdatePostsForm(forms.Form):
    pass
