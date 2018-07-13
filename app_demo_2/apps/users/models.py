from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    birthday = models.DateField(null=True, blank=True, verbose_name="birthday")
    gender = models.SmallIntegerField("gender",choices=((0, "male"), (1, "female")), default=0)
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="phone")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

from django.utils.translation import get_language,ugettext,ugettext_lazy as _

from mothertongue.models import MothertongueModelTranslate


from django.db import models
from django.conf import settings
from django.utils.translation import get_language, ugettext, ugettext_lazy as _

# import translation stuff
from mothertongue.models import MothertongueModelTranslate

# Create your models here.
class GenericPage(MothertongueModelTranslate):
    title = models.CharField(_('title'), max_length=200, help_text=_('Title for your page'))
    content = models.TextField(_('content'), blank=True, help_text=_('Copy for your page'))
    translations = models.ManyToManyField('GenericPageTranslation', blank=True, verbose_name=_('translations'))
    translation_set = 'genericpagetranslation_set'
    translated_fields = ['title','content',]

    def __unicode__(self):
        return u'%s' % self.title

# chunks translations model
class GenericPageTranslation(models.Model):
    generic_page_instance = models.ForeignKey('GenericPage', verbose_name=_('generic_page'))
    language = models.CharField(max_length=len(settings.LANGUAGES)-1, choices=settings.LANGUAGES[1:])
    title = models.CharField(_('title'), max_length=200, help_text=_('Title for your page'))
    content = models.TextField(_('content'), blank=True, help_text=_('Copy for your page'))

    class Meta(object):
        # ensures we can only have on translation for each language for each page
        unique_together = (('generic_page_instance', 'language'),)

    def __unicode__(self):
        return u'%s' % self.language


