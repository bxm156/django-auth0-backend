def permissions(strategy, details, user=None, *args, **kwargs):
    if not user:
        return
    claims = details.get('claims', {})

    groups = claims.get('groups', [])
    roles = claims.get('roles', [])
    permissions = claims.get('permissions', [])

    changed = False

    is_superuser = 'admin' in groups
    if user.is_superuser != is_superuser:
        user.is_superuser = is_superuser
        changed = True

    is_staff = 'staff' in groups
    if user.is_staff != is_staff:
        user.is_staff = is_staff
        changed = True

    if changed:
        strategy.storage.user.changed(user)
