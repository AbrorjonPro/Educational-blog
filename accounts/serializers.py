from rest_framework import serializers
from .models import Profile, Contact, AddressLink, AdminContactPhones
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import User 
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        extra_kwargs = {
			'username':{
				'validators':[UnicodeUsernameValidator()]
			},
		}
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.first_name_ru = validated_data.get('first_name_ru', instance.first_name_ru)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.last_name_ru = validated_data.get('last_name_ru', instance.last_name_ru)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = "__all__"
        related_object = 'user'
        depth = 1

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        instance.user = validated_data.get('user', instance.user)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        instance.faculty_uz = validated_data.get('faculty_uz', instance.faculty_uz)
        instance.faculty_ru = validated_data.get('faculty_ru', instance.faculty_ru)
        instance.faculty_en = validated_data.get('faculty_en', instance.faculty_en)

        instance.cafedra = validated_data.get('cafedra', instance.cafedra)
        instance.cafedra_uz = validated_data.get('cafedra_uz', instance.cafedra_uz)
        instance.cafedra_ru = validated_data.get('cafedra_ru', instance.cafedra_ru)
        instance.cafedra_en = validated_data.get('cafedra_en', instance.cafedra_en)
        
        instance.biography = validated_data.get('biography', instance.biography)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.scopus = validated_data.get('scopus', instance.scopus)

        instance.level = validated_data.get('level', instance.level)
        instance.level_uz = validated_data.get('level_uz', instance.level_uz)
        instance.level_ru = validated_data.get('level_ru', instance.level_ru)
        instance.level_en = validated_data.get('level_en', instance.level_en)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
 

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('subject', 'email', 'phone', 'message')

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

class AdminContactPhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContactPhones
        fields = ('phone',)

class AddressLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressLink
        fields = ('name', 'link',)
