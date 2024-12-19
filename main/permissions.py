from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnly(BasePermission):
    """ Права доступа: только администраторы могут изменять данные, остальные пользователи имеют доступ только для чтения. """

    def has_permission(self, request, view):
        # Только администраторы могут выполнять запросы, отличные от GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff