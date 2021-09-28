from rest_framework import permissions

class StoreOwnerWritePermission(permissions.BasePermission):
  message = "Editar uma loja é restrita ao somente dono."
  def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS:
        return True

      return obj.owner == request.user

  def has_permission(self, request, view):
      return super().has_permission(request, view)
