from django.shortcuts import render, reverse
from rest_framework.generics import get_object_or_404

from my_works.models import Articles, Presentations
from .models import Profile, Contact, AdminContactPhones, AddressLink, Counter, Visitors
from my_works.models import Books, Articles, Presentations, Projects, Videos

from django.contrib import messages
from datetime import datetime
from rest_framework.response import Response
from .serializers import (
    ContactSerializer, 
    ProfileSerializer, 
    User, 
    AddressLinkSerializer, 
    AdminContactPhonesSerializer,
    UserSerializer
)
from rest_framework import permissions, viewsets

from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def error_404_view(request, exception):
    data = {}
    return render(request,'404.html')

def error_500_view(exception):
    return render(exception, template_name='500.html')


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user == request.user

class ProfileView(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    http_allowed_methods = ("GET", "HEAD", "OPTION",)
    queryset = Profile.objects.all()

    def get_object(self, **kwargs):
        return Profile.objects.first() 

    def list(self, request, **kwargs):
        visitor, created = Visitors.objects.get_or_create(id=1)
        ip = get_client_ip(request)
        profile = self.get_object()
        try:
            counter = Counter.objects.get(ip=ip)
            if counter.date_visited.strftime("%d-%m-%Y") != datetime.now().strftime("%d-%m-%Y"):
                counter.date_visited = datetime.now()
                counter.save()
                visitor.visitors += 1
                visitor.save()
        except Exception as e:
            print(f"{e}")
            Counter.objects.create(ip=ip, date_visited=datetime.now())
            visitor.visitors += 1
            visitor.save()
        serializer = ProfileSerializer(profile)
        data = {}
        data["user"] = UserSerializer(profile.user).data
        data["faculty"] = profile.faculty
        data["cafedra"] = profile.cafedra
        data["level"] = profile.level
        data["avatar"] = profile.avatar.url
        try:
            data["biography"] = profile.biography.url
        except:
            data["biography"]=None
        data["bio"] = profile.bio    
        data["telegram"] = profile.telegram
        data["facebook"] = profile.facebook
        data["scopus"] = profile.scopus
        data["visitors"] = visitor.visitors
        #counting of books, articles, ...
        data['books'] = Books.objects.all().count()
        data['articles'] = Articles.objects.all().count()
        data['presentatitons'] = Presentations.objects.all().count()
        data['projects'] = Projects.objects.all().count()
        data['videos'] = Videos.objects.all().count()
        

        return Response(data)
    

    def put(self, request, *args, **kwargs):

        profile = self.get_object()
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = dict(serializer.validated_data.get('user'))
            updated_user = User.objects.get(id=1)
            updated_user.first_name = user['first_name']
            updated_user.first_name_ru = user['first_name_ru']
            updated_user.last_name = user['last_name']
            updated_user.last_name_ru = user['last_name_ru']
            updated_user.email = user['email']
            updated_user.save()
            serializer.save()

            return Response(serializer.data, status=200)
        return Response(serializer.errors)
class ContactAPIView(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSerializer
    http_allowed_methods = ['POST', 'HEAD', 'OPTIONS']

    def create(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            subject = serializer.validated_data.get('subject')
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            phone = serializer.validated_data.get('phone')
            recipient_list = ['mustafoali777@gmail.com']
            if subject and email and phone and message:
                try:
                    message_block = f'Hey Mr.\n {subject} has sent this email message lastly.\n This User\'s Message: \n {message}  \n \n \n For the Contact \n {phone} \n '
                    send_mail(subject, message_block, email, recipient_list)
                    contact_info = Contact.objects.create(email=email, subject=subject, phone=phone, message=message)
                    contact_info.save()
                except BadHeaderError:
                    return messages.warning(request, 'Please try again..')
                Response({'response':'E\'tiboringiz uchun rahmat!Tez orada siz bilan bog\'lanamiz..'})

        return Response({'response':'Xabar jo\'natildi.'})

class AdminContactView(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = AdminContactPhones.objects.all()
    serializer_class = AdminContactPhonesSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(AdminContactPhones.objects.all(), many=True)
        return Response(serializer.data, status=200)

class AddressLinkView(viewsets.ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = AddressLink.objects.all()
    serializer_class = AddressLinkSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(AddressLink.objects.all(), many=True)
        return Response(serializer.data, status=200)
