from django.contrib.admin.sites import AdminSite as BaseAdminSite


class AdminSite(BaseAdminSite):
    site_title = "FireLocs"
    site_header = "🔥 FireLocs"
