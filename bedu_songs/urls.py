"""Project URL Configuration"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

# Views
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path(
        route='change-language/',
        view=TemplateView.as_view(template_name='change-language.html'),
        name='change_language'
    ),
    path('', include('users.urls', namespace='users')),
    path('songs/', include('songs.urls', namespace='songs')),
]

# GraphQL

urlpatterns += [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]


if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
