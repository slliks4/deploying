from django.contrib import admin
from .models import My_applications
from .models import Admission_users,Personal_info,Course_listing,Staff_information
admin.site.register(My_applications)
admin.site.register(Admission_users)
admin.site.register(Personal_info)
admin.site.register(Course_listing)
admin.site.register(Staff_information)
