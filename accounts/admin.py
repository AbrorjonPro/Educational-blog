from django.contrib import admin
from .models import  Profile, Contact, AdminContactPhones, AddressLink, Counter, Visitors
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_staff')
    fieldsets = (
        ('LOGIN INFO', {
            'fields':('username', 'password')
        },),
        ('TEACHER INFO', {
            'fields':(('first_name_uz', 'last_name_uz'), ('first_name_en', 'last_name_en'),('first_name_ru', 'last_name_ru'), )
        },),
        ('', {
            'fields':('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
            'classes':('collapse',)
        },),
    )
    filter_horizontal = ('user_permissions',)
    readonly_fields=('password','is_superuser', 'is_staff')

admin.site.unregister(User)

admin.site.register(User, UserAdmin)




class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Fakultet'), {
            'fields':('faculty_uz', 'faculty_ru', 'faculty_en')
        }),
        (_('Cafedra'), {
            'fields':('cafedra_uz', 'cafedra_ru', 'cafedra_en')
        }),
        (_('Level'), {
            'fields':('level_uz', 'level_ru', 'level_en')
        }),
        (_('FILES'), {
            'fields':(('biography', 'avatar'),)
        }),
        (_('Social links'), {
            'fields':(('telegram', 'facebook'), 'scopus')
        }),
        ('', {
            'fields':('bio','user')
        })
    )
    # inlines = (UserTabularInline,)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_sent', 'status', 'email', 'phone')
    list_filter = ('subject', 'status')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(AdminContactPhones)
admin.site.register(AddressLink)
admin.site.register(Counter)
admin.site.register(Visitors)

def switch_lang_code(path, language):
   
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]
    
    # Validate the inputs
    if path == '':
        raise Exception('URL path for language switch is empty')
    elif path[0] != '/':
        raise Exception('URL path for language switch does not start with "/"')
    elif language not in lang_codes:
        raise Exception('%s is not a supported language code' % language)
 
    # Split the parts of the path
    parts = path.split('/')
    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1]=language
    else:
        parts[0] = "/" + language

    # Return the full new path
    return '/'.join(parts)
