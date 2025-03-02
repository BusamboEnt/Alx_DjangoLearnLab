from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Book

class Command(BaseCommand):
    help = "Setup user groups and permissions"

    def handle(self, *args, **kwargs):
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_create", "can_edit"],
            "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
        }

        for group_name, perm_codes in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perm_codes:
                permission = Permission.objects.get(codename=perm_code)
                group.permissions.add(permission)
            
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' configured."))
