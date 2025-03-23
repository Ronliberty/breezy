from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import itertools


class HeroContent(models.Model):
    name = models.CharField(max_length=255)  # Main heading (John Doe)
    subtitle = models.CharField(max_length=255)  # (Full Stack Developer & UI Designer)
    cta_text = models.CharField(max_length=100)  # Call-to-action button text (View My Work)
    cta_link = models.URLField()                # Button link
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hero',
        default=1
    )

    def __str__(self):
        return self.name  # Changed from title to name

    class Meta:
        verbose_name = "Hero Content"
        verbose_name_plural = "Hero Contents"
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_hero_content'
            )
        ]


class ProjectTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(ProjectTag)
    image = models.ImageField(upload_to='projects/')
    date = models.DateField()
    views = models.PositiveIntegerField(default=0)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.TextField(help_text="SVG path data or icon class")

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Percentage value (0-100)")

    def __str__(self):
        return f"{self.name} ({self.category})"


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_contact_info'
            )
        ]

    def __str__(self):
        return "Contact Information"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('other', 'Other'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.TextField(help_text="SVG path data or icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.get_platform_display()} Profile"


class LegalLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


# HeroContent model from previous step (included for completeness)
class HeroContent(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=100)
    cta_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hero',
        default=1
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hero Content"
        verbose_name_plural = "Hero Contents"
        constraints = [
            models.UniqueConstraint(
                fields=['is_active'],
                condition=models.Q(is_active=True),
                name='unique_active_hero_content'
            )
        ]