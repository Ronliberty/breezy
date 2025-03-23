from django import forms
from .models import *
from django.utils.html import escape

class HeroContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = '__all__'
        widgets = {
            'cta_text': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'cta_link': forms.URLInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full', 'rows': 3}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-multiselect mt-1 block w-full'}),
        }

class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = '__all__'
        widgets = {
            'icon': forms.Textarea(attrs={'class': 'form-textarea font-mono text-sm', 'rows': 4}),
        }
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'proficiency']
        widgets = {
            'category': forms.Select(attrs={'class': 'border p-2 rounded w-full'}),
            'name': forms.TextInput(attrs={'class': 'border p-2 rounded w-full'}),
            'proficiency': forms.NumberInput(attrs={'class': 'border p-2 rounded w-full', 'min': 0, 'max': 100}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'phone': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }
class SocialLinkForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'icon', 'order']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']

    def clean(self):
        cleaned_data = super().clean()
        # Escape all user input
        cleaned_data['name'] = escape(cleaned_data.get('name', ''))
        cleaned_data['message'] = escape(cleaned_data.get('message', ''))
        return cleaned_data
