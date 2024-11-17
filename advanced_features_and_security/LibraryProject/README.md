### Permissions and Groups in the Application

1. **Groups**:

   - Editors: Can create and edit posts.
   - Viewers: Can view posts.
   - Admins: Can view, create, edit, and delete posts.

2. **Custom Permissions**:

   - `can_view`: View posts.
   - `can_create`: Create posts.
   - `can_edit`: Edit posts.
   - `can_delete`: Delete posts.

3. **Testing**:

   - Assign users to groups in Django admin.
   - Log in with different users to test permissions.

4. **Code Notes**:
   - Permissions are checked in views using `@permission_required`.
   - Permissions are defined in the `Post` model's `Meta` class.
