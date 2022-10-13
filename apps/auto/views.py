from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action
from apps.auto.serializers import AutoSerializer
from apps.mantenimiento.models import Mantenimiento

from apps.user.models import User
from apps.user.permissions import IsAdmin, IsCliente

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class MantenimientoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    ordering_fields = ['id', 'auto']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete',
                        'set_password']:
            permission_classes = (IsAuthenticated, IsAdmin)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated, IsAdmin, IsCliente)
        else:
            permission_classes = (IsAuthenticated)

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Mantenimiento.objects.all()
        user = self.request.user
        if user.type in [User.Type.CLIENTE]:
            queryset = queryset.filter(id=user.id)

        return queryset