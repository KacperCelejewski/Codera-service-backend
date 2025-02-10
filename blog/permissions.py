from rest_framework.permissions import BasePermission


class IsInPostCreatorGroup(BasePermission):
    """
    Permission for users who belong to the 'PostCreator' group.
    """

    def has_permission(self, request, view):
        # Sprawdzenie, czy użytkownik jest zalogowany i należy do grupy 'PostCreator'
        return request.user and request.user.groups.filter(name="PostCreator").exists()
