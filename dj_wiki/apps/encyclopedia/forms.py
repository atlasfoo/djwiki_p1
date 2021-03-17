from django import forms


class EntryForm(forms.Form):
    title = forms.CharField(label='Entry title', max_length='60',
                            required=True, widget=forms.TextInput(attrs={"class": "form-control"}),
                            error_messages={'required': 'Please write a entry title'})
    entry = forms.CharField(label='Entry body', widget=forms.Textarea(attrs={"class": "form-control"}), required=True,
                            error_messages={'required': 'Please write a entry body'})

