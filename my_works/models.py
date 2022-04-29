from cloudinary_storage.validators import validate_video
from cloudinary_storage.storage import VideoMediaCloudinaryStorage, MediaCloudinaryStorage
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .validators import validate_file_extension
from django.utils.translation import gettext_lazy as _


class Subjects(models.Model):
    name = models.CharField(_('name'), max_length=500, blank=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, verbose_name=_('Author'), null=True, blank=True)

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    def __str__(self):
        return self.name


class Articles(models.Model):
    name = models.CharField(_('name'), null=True, blank=True, max_length=500)
    file = models.FileField(_('File'), blank=True,
                            null=True, upload_to='articles')
    link = models.URLField(_('Link'), blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False,
                            null=False, unique=True, max_length=500)
    subject = models.ForeignKey(
        Subjects, null=True, blank=True, max_length=500, on_delete=models.CASCADE,
        help_text=_('Is this article related to any subject  (Optional.)'))

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Articles, self).save(*args, **kwargs)


class Books(models.Model):
    name = models.CharField(_('Name'), max_length=500, null=True, blank=True)
    file = models.FileField(_('File'), blank=True,
                            null=True, upload_to='books')
    link = models.URLField(_('Link'), blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False,
                            null=False, unique=True, max_length=500)
    subject = models.ForeignKey(
        Subjects, null=True, blank=True, max_length=500, on_delete=models.CASCADE,
        help_text=_('Is this book related to any subject  (Optional.)'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Books, self).save(*args, **kwargs)


class Presentations(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True, null=True)
    file = models.FileField(_('File'), blank=True,
                            null=True, upload_to='presentations')
    link = models.URLField(_('Link'), blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False,
                            null=False, unique=True, max_length=500)
    subject = models.ForeignKey(
        Subjects, null=True, blank=True, max_length=500, on_delete=models.CASCADE,
        help_text=_('Is this presentation related to any subject  (Optional.)'))

    class Meta:
        verbose_name = _('Presentation')
        verbose_name_plural = _('Presentations')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Presentations, self).save(*args, **kwargs)


class Projects(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True, null=True)
    file = models.FileField(_('File'), blank=True,
                            null=True, upload_to='projects')
    link = models.URLField(_('Link'), blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(_('Slug'), blank=False,
                            null=False, unique=True, max_length=500)
    subject = models.ForeignKey(
        Subjects, null=True, blank=True, max_length=500, on_delete=models.CASCADE,
        help_text=_('Is this project related to any subject  (Optional.)')
        )

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Projects, self).save(*args, **kwargs)


class Videos(models.Model):
    name = models.CharField(_('Name'), max_length=500, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='videolar',
                            storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    link = models.URLField(_('Link'), blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(
        _('Slug'), blank=False, null=False, unique=True, max_length=500)
    subject = models.ForeignKey( Subjects, null=True, blank=True, max_length=500, on_delete=models.CASCADE,
        help_text=_('Is this video related to any subject  (Optional.)'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __str__(self):
        return f'{self.name}'

    def link_management(self):
        if self.link:
            #	    link =''
            parts = []
            parts = self.link.split('/')
            if parts[2] == 'youtu.be':
                parts[2] = 'youtube.com'
                link = parts[0] + '//' + parts[2] + '/embed/' + parts[-1]
            elif parts[2] == 'mover.uz':
                parts[3] = 'video'
                link = parts[0] + '//' + parts[2] + '/video/embed/' + parts[-1]
                print(parts)
            else:
                link = self.link
            return link

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.link = self.link_management()
        return super(Videos, self).save(*args, **kwargs)


class Comments(models.Model):
    subject = models.ForeignKey(
        Subjects, on_delete=models.CASCADE, null=True, blank=True)
    rate = models.IntegerField(_("Rate"), null=True, blank=True)
    comment = models.TextField()
    date_added = models.DateField(_("Date_Added"), auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"{self.comment}  {self.date_added.strftime('%Y-%m-%d %H:%M:%S')}"


class VisibleComments(models.Model):
    comment = models.OneToOneField(Comments, on_delete=models.CASCADE)
    publicized =  models.BooleanField(
        verbose_name=_("visible"), default=True, null=True, blank=True
    )
    class Meta:
        verbose_name = _("Visible Comment")
        verbose_name_plural = _("Visible Comments")

    def __str__(self):
        return f"{self.comment.rate}:  {self.comment.comment}  {self.comment.date_added}"


class Fotos(models.Model):
    name = models.CharField(_("name"), max_length=100, null=True, blank=True)
    text = models.CharField(_("text"), max_length=5000, null=True, blank=True)
    image = models.ImageField(
        upload_to="Images", storage=MediaCloudinaryStorage,
        help_text=_('Bu yerga faqat rasm yuklang'))
    date_added = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, verbose_name=_('Author'), null=True, blank=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __str__(self):
        return f"{self.image.url}"


class Warnings(models.Model):
    name = models.CharField(_("name"), max_length=100, null=True, blank=True)
    text = models.TextField(_("text"), null=True, blank=True)
    image = models.ImageField(
        default="default.jpg", upload_to="warnings", storage=MediaCloudinaryStorage, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    publicized = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Warning")
        verbose_name_plural = _("Warnings")

    def __str__(self) -> str:
        return f"{self.name} : {self.publicized}"



class Subject_Files_Types(models.Model):
    name = models.CharField(max_length=100, verbose_name="Hujjat turi")
    slug = models.SlugField(max_length=100)
    key = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Subject File_Types")
        verbose_name_plural = _("Subject Files Types")    

    def save(self, *args, **kwargs):        
        self.slug = slugify(self.name)
        self.key = ''.join(self.slug.replace('-', '_'))
        return super(Subject_Files_Types, self).save(*args, **kwargs)

class Subject_Files(models.Model):
    document_type = models.ForeignKey(Subject_Files_Types, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(_('File'), blank=True, null=True, upload_to='jobdocs')
    link = models.URLField(_('Link'), blank=True, null=True)
    slug = models.SlugField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    class Meta:
        verbose_name = _("Subject File")
        verbose_name_plural = _("Subject Files")

    def __str__(self):
        return self.name




