# urls.py
from django.urls import path
from .views import HeroContentView, ProjectsListView, SkillsListView, ContactInfoView, FooterContentView, ProjectCreateView, HeroContentUpdateView, SkillCategoryUpdateView, ContactInfoUpdateView, ProjectUpdateView
from ..custom.urls import app_name

app_name = 'base'
urlpatterns = [
    path('hero-content/', HeroContentView.as_view(), name='hero_content'),
    path('projects/', ProjectsListView.as_view(), name='projects_list'),
    path('skills/', SkillsListView.as_view(), name='skills_list'),
    path('contact/', ContactInfoView.as_view(), name='contact_info'),
    path('footer/', FooterContentView.as_view(), name='footer_content'),
    path('admin/hero/edit/<int:pk>/', HeroContentUpdateView.as_view(), name='hero_edit'),

    # Projects
    path('admin/projects/new/', ProjectCreateView.as_view(), name='project_create'),
    path('admin/projects/edit/<int:pk>/', ProjectUpdateView.as_view(), name='project_edit'),

    # Skills
    path('admin/skills/edit/<int:pk>/', SkillCategoryUpdateView.as_view(), name='skill_category_edit'),

    # Contact
    path('admin/contact/edit/<int:pk>/', ContactInfoUpdateView.as_view(), name='contact_edit'),
]