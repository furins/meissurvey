"""meissurvey URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from survey import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('q/<slug:slug_questionario>/', views.questionario),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", RedirectView.as_view(url='/q/qa/', permanent=False)),
]
