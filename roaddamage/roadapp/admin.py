from django.contrib import admin

from roadapp.models import AlertTable, AssignWorkTable, AuthorityTable, ComplaintTable, ContactTable, FeedBackTable, IssueTable, LoginTable, MapViewTable, ReportTable, UserTable

# Register your models here.
admin.site.register(LoginTable),
admin.site.register(UserTable),
admin.site.register(AuthorityTable),
admin.site.register(AlertTable),
admin.site.register(ReportTable),
admin.site.register(MapViewTable),
admin.site.register(ContactTable),
admin.site.register(FeedBackTable),
admin.site.register(ComplaintTable),
admin.site.register(AssignWorkTable),
admin.site.register(IssueTable)