from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import (
    Articles,
    Books,
    Fotos,
    Presentations,
    Projects,
    Videos,
    Subjects,
    Comments,
    Fotos,
    # Documents,
    Warnings,
    Subject_Files,
    Subject_Files_Types,
)
import re


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ("id", "name", )


class ArticlesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = ('slug', 'name',
                  'file', 'link', 'date_published', 'date_updated', 'subject')
        extra_kwargs = {
            'date_published': {'read_only': True},
            'slug': {'read_only': True},
        }

    def create(self, validated_data):
        return Articles.objects.create(**validated_data, author_id=1)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.date_published = validated_data.get('date_published', instance.date_published)
    #     instance.date_updated = validated_data.get('date_updated', instance.date_updated)
    #     instance.save()
    #     return instance


class BooksSerializers(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('slug', 'name',
                  'file', 'link',
                  'date_published', 'date_updated', 'subject')
        extra_kwargs = {
            'date_published': {'read_only': True},
            'slug': {'read_only': True},

        }

    def create(self, validated_data):
        return Books.objects.create(**validated_data, author_id=1)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.date_published = validated_data.get('date_published', instance.date_published)
    #     instance.date_updated = validated_data.get('date_updated', instance.date_updated)
    #     instance.save()
    #     return instance


class PresentationsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Presentations
        fields = ('slug', 'name',
                  'file', 'link',
                  'date_published', 'date_updated', 'subject')
        extra_kwargs = {
            'date_published': {'read_only': True},
            'slug': {'read_only': True},
            'author': {'read_only': True},
        }

    def create(self, validated_data):
        return Presentations.objects.create(**validated_data, author_id=1)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.date_published = validated_data.get('date_published', instance.date_published)
    #     instance.date_updated = validated_data.get('date_updated', instance.date_updated)
    #     instance.save()
    #     return instance


class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ('slug', 'name', 'file', 'link',
                  'date_published', 'date_updated', 'subject')
        extra_kwargs = {
            'date_published': {'read_only': True},
            'slug': {'read_only': True},

        }

    def create(self, validated_data):
        return Projects.objects.create(**validated_data, author_id=1)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.link = validated_data.get('link', instance.link)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.date_published = validated_data.get('date_published', instance.date_published)
    #     instance.date_updated = validated_data.get('date_updated', instance.date_updated)
    #     instance.save()
    #     return instance


class VideosSerializers(serializers.ModelSerializer):

    class Meta:
        model = Videos
        fields = ('slug', 'name', 'file', 'link',
                  'date_published', 'date_updated', 'subject')
        extra_kwargs = {
            'date_published': {'read_only': True},
            'slug': {'read_only': True},
        }

    def link_management(self, validated_data):
        link = validated_data.get('link')

        if link:
            if not link.find('https://youtube.com/embed/'):
                return link
            elif link.find('youtu.be'):
                res = link.find('youtu.be/')
                result = link[:res] + 'youtube.com/embed/' + link[(res+9):]
                link = result
                return link

    def create(self, validated_data):
        name = validated_data.get('name')
        file = validated_data.get('file')
        name_en = validated_data.get('name_en')
        name_uz = validated_data.get('name_uz')
        name_ru = validated_data.get('name_ru')
#        file_en = validated_data.get('file_en')
 #       file_uz = validated_data.get('file_uz')
  #      file_ru = validated_data.get('file_ru')
        subject = validated_data.get('subject')
        return Videos.objects.create(name=name, name_en=name_en, name_uz=name_uz, name_ru=name_ru, file=file, subject=subject, link=self.link_management(validated_data=validated_data), author_id=1)

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.file = validated_data.get('file', instance.file)
        #instance.file_uz = validated_data.get('file_uz', instance.file_uz)
        #instance.file_ru = validated_data.get('file_ru', instance.file_ru)
        #instance.file_en = validated_data.get('file_en', instance.file_en)
        instance.link = self.link_management(validated_data=validated_data)
        instance.author = validated_data.get('author', instance.author)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.date_published = validated_data.get(
            'date_published', instance.date_published)
        instance.date_updated = validated_data.get(
            'date_updated', instance.date_updated)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("rate", "comment", "date_added")


class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ("name", "text", "image")


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warnings
        fields = ("name", "text", "image", "date_added",)


# class DocumentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = "__all__"


class Subject_FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Files
        fields = ("name", "file", "link", "slug", 'date_added',)


class Subject_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Files_Types
        fields = ("name", "slug", "date_added",  "key", )
