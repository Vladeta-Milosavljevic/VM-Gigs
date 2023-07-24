from django import forms
from .models import Job, Tag


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        labels = {
            "user": "",
            "custom_tags": "Custom tags - please separate tags with a comma",
            "tags": "Tags - please select standard tags",
            "logo": "Please add your logo",
        }

        widgets = {
            "user": forms.HiddenInput(),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "logo": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-control"
                }
            ),
            "custom_tags": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "company": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "website": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }


class TagForm (forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        labels = {
            "name": "Name of the tag",

        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        tag = Tag.objects.filter(name__exact=name).all()
        if len(tag) > 0:
            raise forms.ValidationError('Tag is present in the database.')
        return name


class ApplyForm(forms.Form):
    job_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'readonly': 'readonly', 'type': 'hidden'}))
    job_email = forms.CharField(label='', widget=forms.TextInput(
        attrs={'readonly': 'readonly', 'type': 'hidden'}))
    name = forms.CharField(label='Your name', min_length=5, max_length=75,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    intro = forms.CharField(label='Tell us about yourself.', min_length=20,
                            max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    files = forms.FileField(label='Your files,(CV, cover letter, etc.)', widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'class': 'form-control'}))



