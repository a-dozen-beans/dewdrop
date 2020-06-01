from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('recruitment/', include('recruitment.urls')),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Recruitment administration"
admin.site.site_title = "Recruitment administration panel"
admin.site.index_title = "Welcome to Recruitment administration panel"