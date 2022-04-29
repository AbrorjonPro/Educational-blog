from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from .views import (
    ArticlesViewList,
    BooksViewList,
    PresentationsViewList,
    ProjectsViewList,
    VideosViewList,
    SubjectsView,
    FotosView,
    CommentsView,
    WarningsView,
    AllWorksBySubject
    )
from rest_framework import routers
from django.conf.urls import handler404

router = routers.DefaultRouter()

router.register(r'articles', ArticlesViewList, basename='articles')
router.register(r'books', BooksViewList, basename='books')
router.register(r'presentations', PresentationsViewList, basename='presentations')
router.register(r'projects', ProjectsViewList, basename='projects')
router.register(r'videos', VideosViewList, basename='videos')
router.register(r'subjects', SubjectsView, basename='subjects')
router.register(r'fotos', FotosView, basename='fotos')
router.register(r'comments', CommentsView, basename='comments')
router.register(r'warnings', WarningsView, basename='warnings')
router.register(r'subject-works/<int:pk>', AllWorksBySubject, basename='all-works-by-subject-id')


urlpatterns = []

urlpatterns += router.urls
