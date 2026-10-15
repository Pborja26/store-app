from django.conf import settings
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from person import models as person_models
from person import serializers as person_serializers

# Create your views here.
def set_refresh_cookie(response):
    """Tira o refresh do corpo da resposta e grava no cookie HttpOnly."""
    refresh = response.data.pop('refresh', None)
    if refresh:
        response.set_cookie(
            value=refresh,
            max_age=int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds()),
            **settings.REFRESH_COOKIE,
        )
    return response

def delete_refresh_cookie(response):
    cookie = settings.REFRESH_COOKIE
    response.delete_cookie(cookie['key'], path=cookie['path'], samesite=cookie['samesite'])
    return response

class RefreshFromCookieMixin:
    """Pega o refresh do cookie e entrega ao serializer como se tivesse vindo no body."""
    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data'].copy()
            data['refresh'] = self.request.COOKIES.get(settings.REFRESH_COOKIE['key'], '')
            kwargs['data'] = data
        return super().get_serializer(*args, **kwargs)

class CookieLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return set_refresh_cookie(response)

class CookieRefreshView(RefreshFromCookieMixin, TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return set_refresh_cookie(response)   # com a rotação ligada, vem um refresh novo

class CookieLogoutView(RefreshFromCookieMixin, TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return delete_refresh_cookie(response)

class RegisterView(generics.CreateAPIView):
    queryset = person_models.User.objects.all()
    serializer_class = person_serializers.RegisterSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
