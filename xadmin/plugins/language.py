
from django.conf import settings
from django.template import loader
from django.views.i18n import set_language
from xadmin.plugins.utils import get_context_dict
from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, CommAdminView, BaseAdminView


class SetLangNavPlugin(BaseAdminPlugin):

    def block_top_navmenu(self, context, nodes):
        context = get_context_dict(context)
        context['redirect_to'] = self.request.get_full_path()
        nodes.append(loader.render_to_string('xadmin/blocks/comm.top.setlang.html', context=context))

class SetLangView(BaseAdminView):

    def post(self, request, *args, **kwargs):
        if 'nav_menu' in request.session:
            del request.session['nav_menu']
        return set_language(request)


# if settings.LANGUAGES and 'django.middleware.locale.LocaleMiddleware' in settings.MIDDLEWARE_CLASSES:

# MIDDLEWARE = MIDDLEWARE_CLASSES
a = 1
b = 2
h = ""

h = a-b if a>b else a+b

import django

#Django 1.10 版本 更名为 MIDDLEWARE（单复同形），写法也有变化，详见 第四部分。
# 如果用 Django 1.10版本开发，部署时用 Django 1.9版本或更低版本，要特别小心此处。
MIDDLEWARE = settings.MIDDLEWARE_ClASSES if django.VERSION[0] ==1 and django.VERSION[1] <9 else settings.MIDDLEWARE
if settings.LANGUAGES and 'django.middleware.locale.LocaleMiddleware' in MIDDLEWARE:
    site.register_plugin(SetLangNavPlugin, CommAdminView)
    site.register_view(r'^i18n/setlang/$', SetLangView, 'set_language')
