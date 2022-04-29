from IrrigatsiyaUz.settings import LANGUAGES
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, AllowAny
from rest_framework.parsers import JSONParser,MultiPartParser, FormParser 
from django.http import FileResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action

class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

from .models import (
    Articles,
    Books, 
    Presentations,
    Projects,
    Subjects, 
    Videos,
    Fotos,
    Comments,
    VisibleComments,
    Warnings,
    # Documents,
    Subject_Files_Types, Subject_Files,
    )

from .serializers import (
    ArticlesSerializers,
    BooksSerializers,
    PresentationsSerializers,
    ProjectsSerializers,
    SubjectsSerializer,
    VideosSerializers,
    CommentSerializer,
    FotoSerializer,
    WarningSerializer,
    Subject_TypesSerializer, 
    Subject_FilesSerializer,
    ) 
# def error_404_view(request, exception):
#     return render(request,'404.html')

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return object.author == request.user
        return request.user.is_staff

class ArticlesViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [ IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]    
    queryset = Articles.objects.all().order_by('-date_updated')
    serializer_class = ArticlesSerializers
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Articles, slug=work)

    def list(self, request):
        serializer = ArticlesSerializers(Articles.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data)

 
    def create(self, request):
        try:
            serializer = ArticlesSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_articles.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))    
    
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
class BooksViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Books.objects.all().order_by('-date_updated')
    serializer_class = BooksSerializers
    parser_classes = (JSONParser, MultiPartParser, FormParser,)


    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Books, slug=work)

    def list(self, request):
        serializer = BooksSerializers(Books.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)
 
 
    def create(self, request):
        try:
            serializer = BooksSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_books.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class PresentationsViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Presentations.objects.all().order_by('-date_updated')
    serializer_class = PresentationsSerializers
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Presentations, slug=work)

    def list(self, request):
        serializer = PresentationsSerializers(Presentations.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        try:
            serializer = PresentationsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_presentations.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response

class ProjectsViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Projects.objects.all().order_by('-date_updated')
    serializer_class = ProjectsSerializers
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Projects, slug=work)

    def list(self, request):
        serializer = ProjectsSerializers(Projects.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data, status=200)
 
 
    def create(self, request):
        try:
            serializer = ProjectsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_projects.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))

    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response


class VideosViewList(viewsets.ModelViewSet, viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    queryset = Videos.objects.all().order_by('-date_updated')
    serializer_class = VideosSerializers
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
 
    def get_object(self, queryset=None, **kwargs):
        work = self.kwargs.get('pk')
        return get_object_or_404(Videos, slug=work)

    def list(self, request):
        serializer = VideosSerializers(Videos.objects.all().order_by('-date_updated'), many=True)
        return Response(serializer.data)
     
    def create(self, request):
        try:
            serializer = VideosSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            if e == 'UNIQUE constraint failed: my_works_videos.slug':
                return Response(_('This name is taken.Choose other one'))
            return Response(_('Some problems.Please, Try again.'))
    
    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download(self, *args, **kwargs):
        instance = self.get_object()

        # get an open file handle (I'm just using a file attached to the model for this example):
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name
        return response
    

class SubjectsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def list(self, request):
        queryset = Subjects.objects.all().order_by("-id")
        subject_types = Subject_Files_Types.objects.all()
        # subject_files = Subject_Files.objects.all()
        array = []
        for subject in queryset:
            data = {}
            data["id"] = subject.id
            data["name"] = subject.name
            for type in subject_types:
                objects = Subject_Files.objects.filter(document_type=type, subject=subject)
                data[f"{type.key}"] = Subject_FilesSerializer(objects, many=True).data
            array.append(data)
        return Response(array, status=200)


        # queryset = Subjects.objects.all().order_by("-id")
        # data = []
        # for object in queryset:
        #     serializer = {}
        #     serializer["id"] = object.id
        #     serializer["name"] = object.name
        #     serializer["books"] = BooksSerializers(Books.objects.filter(subject=object), many=True).data
        #     serializer["articles"] = ArticlesSerializers(Articles.objects.filter(subject=object), many=True).data
        #     serializer["projects"] = ProjectsSerializers(Projects.objects.filter(subject=object), many=True).data
        #     serializer["presentations"] = PresentationsSerializers(Presentations.objects.filter(subject=object), many=True).data
        #     serializer["videos"] = VideosSerializers(Videos.objects.filter(subject=object), many=True).data
        #     serializer["docs"] = DocumentsSerializer(Documents.objects.filter(subject=object), many=True).data
        #     data.append(serializer)
        # return Response(data, status=200)
        
    # def list(self, request):
    #     serializer = self.serializer_class(Subjects.objects.all().order_by('id'), many=True)
    #     return Response(serializer.data, status=200)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        
    def delete(self, request):
        object = self.get_object()
        if self.request.user.is_staff:
            object.delete()
            return Response({"detail":_("Succesfully deleted. ")})
        return Response({"detail":_("Error occured. ")})


class FotosView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
    queryset = Fotos.objects.all()
    serializer_class = FotoSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def list(self, request):
        serializer = self.serializer_class(Fotos.objects.all().order_by('-date_added'), many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



    def retrieve(self, request):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        
    def delete(self, request):
        object = self.get_object()
        if self.request.user.is_staff:
            object.delete()
            return Response({"detail":_("Succesfully deleted. ")})
        return Response({"detail":_("Error occured. ")})

class CommentsView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Comments.objects.all().order_by("-id")
    serializer_class = CommentSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    http_allowed_methods = ("GET", "POST","HEAD", "OPTIONS")

    def list(self, request):
        queryset_all_comments = Comments.objects.all()
        rating = 0
        summ_of_rating = 0
        for comment in queryset_all_comments:
            summ_of_rating += comment.rate
        print("queryset all comments: ", len(queryset_all_comments), "   ", summ_of_rating)
        rating = summ_of_rating/len(queryset_all_comments)
        length= len(queryset_all_comments)
        visible_queryset = VisibleComments.objects.filter(publicized=True).order_by('-id')
        query_result = []
        for object in visible_queryset:
            query_result.append(object.comment)
        data = {}
        serializer = self.serializer_class(query_result, many=True).data
        data["comments"]= serializer
        data["rating"]=round(float(rating), 2)
        return Response(data, status=200)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            rate=serializer.validated_data.get("rate")
            comment=serializer.validated_data.get("comment")
            object = Comments.objects.create(rate=rate, comment=comment)
            VisibleComments.objects.create(comment=object, publicized=True)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class WarningsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Warnings.objects.all()
    serializer_class = WarningSerializer
    parser_classes = (JSONParser, MultiPartParser, FormParser,)

    def list(self, request):
        serializer = self.serializer_class(Warnings.objects.all().order_by('-date_added'), many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



    def retrieve(self, request):
        object = self.get_object()
        serializer = self.serializer_class(object, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
        
    def delete(self, request):
        object = self.get_object()
        if self.request.user.is_staff:
            object.delete()
            return Response({"detail":_("Succesfully deleted. ")})
        return Response({"detail":_("Error occured. ")})



class AllWorksBySubject(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    http_allowed_methods = ("GET", "HEAD", "OPTIONS")
    permission_classes = (AllowAny, )
    parse_classes = (JSONParser, MultiPartParser, FormParser)

    def list(self, request, pk, *args, **kwargs):
        pass
    
