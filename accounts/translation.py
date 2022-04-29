from modeltranslation.translator import translator, TranslationOptions
from .models import *
from accounts.models import AddressLink, Profile, User

class AddressLinkTranslation(TranslationOptions):
    fields = ('name',)

translator.register(AddressLink, AddressLinkTranslation)


class UserTranslation(TranslationOptions):
    fields = ('first_name','last_name')

translator.register(User, UserTranslation)
class ProfileTranslation(TranslationOptions):
    fields = ('faculty', 'cafedra', 'level')

translator.register(Profile, ProfileTranslation)