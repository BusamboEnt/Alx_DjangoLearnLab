# Django Permissions & Groups Setup

## Custom Permissions:
- `can_view`: Can view books.
- `can_create`: Can create books.
- `can_edit`: Can edit books.
- `can_delete`: Can delete books.

## Groups:
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Full access (view, create, edit, delete).

## How to Setup:
1. Run `python manage.py setup_groups` to create groups and assign permissions.
2. Assign users to groups via Django Admin (`/admin`).
3. Test user permissions by logging in with different roles.

## Enforced Views:
- **View Books**: `@permission_required('relationship_app.can_view')`
- **Create Book**: `@permission_required('relationship_app.can_create')`
- **Edit Book**: `@permission_required('relationship_app.can_edit')`
- **Delete Book**: `@permission_required('relationship_app.can_delete')`
