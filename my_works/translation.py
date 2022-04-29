from modeltranslation.translator import translator, TranslationOptions
from .models import *

class ArticleTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Articles, ArticleTranslation)

class BookTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Books, BookTranslation)

class PresentationsTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Presentations, PresentationsTranslation)

class ProjectsTranslation(TranslationOptions):
    fields = ('name',)
 
translator.register(Projects, ProjectsTranslation)

class SubjectsTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Subjects, SubjectsTranslation)

class VideosTranslation(TranslationOptions):
    fields = ('name',)

translator.register(Videos, VideosTranslation)

class WarningsTranslation(TranslationOptions):
    fields = ('name','text')

translator.register(Warnings, WarningsTranslation)

class FotosTranslation(TranslationOptions):
    fields = ('name', 'text',)

translator.register(Fotos, FotosTranslation)