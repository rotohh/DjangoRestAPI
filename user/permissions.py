from rest_framework import permissions

from user.models import UserProfile


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_superuser


class IsVendor(permissions.BasePermission):
    def has_permission(self, request, view):
        return UserProfile.objects.get(user=request.user).userType == "vendor" or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user or request.user.is_superuser