from django.http import JsonResponse
from django.views.generic import View

from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request) -> JsonResponse:
        return JsonResponse({1: "Hello World"})


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        print(users)
