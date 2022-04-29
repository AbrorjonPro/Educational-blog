from django.contrib import admin
from .models import (
    Articles,
    Books,
    # Documents,
    Fotos,
    Presentations,
    Projects,
    Subject_Files_Types,
    Subject_Files,
    Subjects,
    Comments,
    Videos,
    VisibleComments,
    Warnings,
)
from django.utils.translation import ugettext_lazy as _


class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name_uz','name_en', 'name_ru')}
    list_display = ('name', 'file', )


    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en',)
        }),
        ('FILE or FILE LINK', {
            'fields':('file', 'link', )
        }),
        ('SUBJECT', {
            'fields':('subject',)
        }),
        ('', {
            'fields':('slug', ),
            'classes':('collapse',)
        })
    )

admin.site.register(Articles, ArticlesAdmin)


class BooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_uz','name_en', 'name_ru')}
    list_display = ('name','file',)

    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en',)
        }),
        ('FILE or FILE LINK', {
            'fields':('file', 'link', )
        }),
        ('SUBJECT', {
            'fields':('subject',)
        }),
        ('', {
            'fields':('slug', ),
            'classes':('collapse',)
        })
    )

admin.site.register(Books, BooksAdmin)


class PresentationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_uz','name_en', 'name_ru')}
    list_display = ('name', 'file',)

    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en',)
        }),
        ('FILE or FILE LINK', {
            'fields':('file', 'link', )
        }),
        ('SUBJECT', {
            'fields':('subject',)
        }),
        ('', {
            'fields':('slug', ),
            'classes':('collapse',)
        })
    )

admin.site.register(Presentations, PresentationsAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_uz','name_en', 'name_ru')}
    list_display = ('name', 'file',)

    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en',)
        }),
        ('FILE or FILE LINK', {
            'fields':('file', 'link', )
        }),
        ('SUBJECT', {
            'fields':('subject',)
        }),
        ('', {
            'fields':('slug', ),
            'classes':('collapse',)
        })
    )

admin.site.register(Projects, ProjectsAdmin)


class VideosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_uz','name_en', 'name_ru')}
    list_display = ('name', 'file',)

    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en',)
        }),
        ('FILE or FILE LINK', {
            'fields':('file', 'link', )
        }),
        ('SUBJECT', {
            'fields':('subject',)
        }),
        ('', {
            'fields':('slug', ),
            'classes':('collapse',)
        })
    )

class CommentsAdmin(admin.ModelAdmin):
    list_display = ("subject", "rate", "comment", )


class VisibleCommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "publicized", )
    list_editable = ("publicized", )

admin.site.register(Videos, VideosAdmin)
 
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Subjects, SubjectsAdmin)
class FotosAdmin(admin.ModelAdmin):
    list_display = ("name", "image",)
    fieldsets = (
        ('IMAGE NAME', {
            'fields':('name_uz', 'name_ru', 'name_en'),
            'classes':('wide',),
        }),
        ('Rasmga biror satr qoldirishingiz mumkin', {
            'fields':('text_uz', 'text_ru', 'text_en'),
            # 'classes':('collapse',),
        }),
        (_('Image'), {
            'fields':('image',)
        })
    )


admin.site.register(Fotos, FotosAdmin)
admin.site.register(Comments, CommentsAdmin)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ("name",)
class WarningsAdmin(admin.ModelAdmin):
    list_display = ("name", "publicized",)
    list_editable = ("publicized",)

    fieldsets = (
        ('NAME', {
            'fields':('name_uz', 'name_ru', 'name_en')
        }),
        ('E\'LON MATNI', {
            'fields':('text_uz', 'text_ru', 'text_en',),
        }),
        ('', {
            'fields':(('image', 'publicized'),)
        }
        )
        )



admin.site.register(Warnings, WarningsAdmin)
# class DocumentsAdmin(admin.ModelAdmin):
#     list_display = ("name", "subject", "value", )
# admin.site.register(Documents, DocumentsAdmin)
admin.site.register(VisibleComments, VisibleCommentsAdmin)

class Subject_Files_TypesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )

    fieldsets = (
        ('', {
            'fields':('name',),
            'classes':('wide',)
        }),
        ('', {
            'fields':('slug', 'key'),
            'classes':('collapse',)
        }),
    )

class Subject_FilesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', "file", "link",)
    fieldsets = (
        ('NAME', {
            'fields':('name',('subject', 'document_type', ), ),
            'classes':('wide',)
        }),
        ('FILE or FILE LINK', {
            'fields':(('file','link', ),),
            'classes':('wide',)
        }),

        ('', {
            'fields':('slug',),
            'classes':('collapse',)
        }),
    )

admin.site.register(Subject_Files_Types, Subject_Files_TypesAdmin)
admin.site.register(Subject_Files, Subject_FilesAdmin)

