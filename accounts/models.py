from multiprocessing.dummy import Array
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    faculty = models.CharField(_('faculty'), max_length=300, null=True, blank=True)
    cafedra = models.CharField(_('cafedra'), max_length=300, null=True, blank=True)
    level = models.CharField(_('level'), max_length=200, null=True, blank=True)
    avatar = models.ImageField(_('avatar'), default="profile_img.jpeg", upload_to="profile_pics")
    biography = models.FileField(upload_to='biography', null=True, blank=True)
    telegram = models.CharField(max_length=128, null=True, blank=True, help_text="Telegram username ni kiriting:")
    facebook = models.CharField(max_length=128, null=True, blank=True, help_text="Facebook username ni kiriting:")
    scopus = models.URLField(null=True, blank=True)
    bio = models.CharField(max_length=5000, null=True, blank=True)
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path) 

        if img.width>500 or img.height>500:
            output=(500, 500)
            img.thumbnail(output)
            img.save(self.avatar.path)

class Visitors(models.Model):
    visitors = models.IntegerField(default=0)


class Counter(models.Model):
    ip = models.CharField(max_length=20, unique=True)
    date_visited = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.ip}"


class Contact(models.Model):
    email = models.EmailField()
    phone = PhoneNumberField()
    subject = models.CharField(max_length=30)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages') 
    
    def __str__(self):
        return f'{self.subject}'

    

class AdminContactPhones(models.Model):
    phone = PhoneNumberField()
    class Meta:
        managed = True
        verbose_name = _('Contact Phone')
        verbose_name_plural = _('Contact Phones')
    
    def __str__(self):
        return f'{self.phone}'

class AddressLink(models.Model):
    name = models.CharField(_('name'), max_length=500)
    link = models.URLField(blank=False, null=False)

    class Meta:
        verbose_name = _('Address Link')
        verbose_name_plural = _('Address Links')

    def __str__(self):
        return self.name 