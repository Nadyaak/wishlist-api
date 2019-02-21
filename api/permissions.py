from rest_framework.permissions import BasePermission

class IsAdded_by (BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or  request.user == obj.added_by:
            return True
        return False