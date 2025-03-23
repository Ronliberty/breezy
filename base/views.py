# views.py
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.core import serializers
from .forms import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

class HeroContentView(TemplateView):
    template_name = "base/hero.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hero'] = HeroContent.objects.get(is_active=True)
        return context


class ProjectsListView(ListView):
    model = Project
    template_name = "partials/projects.html"
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(is_featured=True).prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects_json'] = serializers.serialize('json', self.get_queryset())
        return context


class SkillsListView(ListView):
    model = SkillCategory
    template_name = "base/partials/skills.html"
    context_object_name = 'skill_categories'

    def get_queryset(self):
        return SkillCategory.objects.prefetch_related('skills')


class ContactInfoView(TemplateView):
    template_name = "base/partials/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        return context


class FooterContentView(TemplateView):
    template_name = "base/partials/footer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'social_links': SocialLink.objects.all(),
            'legal_links': LegalLink.objects.all()
        })
        return context


class HeroContentUpdateView(SuccessMessageMixin, UpdateView):
    model = HeroContent
    form_class = HeroContentForm
    template_name = 'base/partials/hero_form.html'
    success_message = "Hero content updated successfully"

    def get_success_url(self):
        return reverse_lazy('home')


class ProjectCreateView(SuccessMessageMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'partials/project_form.html'
    success_message = "Project created successfully"

    def get_success_url(self):
        return reverse_lazy('projects_list')


class SkillCategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = SkillCategory
    form_class = SkillCategoryForm
    template_name = 'partials/skill_category_form.html'
    success_message = "Skill category updated successfully"

    def get_success_url(self):
        return reverse_lazy('skills_list')


class ContactInfoUpdateView(SuccessMessageMixin, UpdateView):
    model = ContactInfo
    form_class = ContactInfoForm
    template_name = 'base/partials/contact_form.html'
    success_message = "Contact information updated successfully"

    def get_success_url(self):
        return reverse_lazy('contact_info')