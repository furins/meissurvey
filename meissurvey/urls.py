"""meissurvey URL Configuration"""

from django.contrib import admin
from django.urls import include, path, re_path
from survey import views
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

urlpatterns = i18n_patterns(
    path('welcome/', views.intro, name='intro'),
    path('newsletter/', views.iscrizione, name='iscrizione'),
    path('subscribed/', views.ringraziamento_iscrizione, name='ringraziamento'),
    path('thank-you/', views.conclusione, name='conclusione'),
    path('q/<slug:slug_questionario>/', views.questionario, name="questionario"),
    re_path(r'^rosetta/', include('rosetta.urls')),
)+[
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", RedirectView.as_view(url=f'/{settings.LANGUAGE_CODE}/q/qa/', permanent=False), name='home'),
]
