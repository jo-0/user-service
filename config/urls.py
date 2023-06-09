from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/login"), name="login_redirect"),
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
]
