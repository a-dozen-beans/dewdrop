from django.contrib import admin

from .models import Company, RecruitmentOffer, Category, Subcategory

admin.site.register(Company)
admin.site.register(RecruitmentOffer)
admin.site.register(Category)
admin.site.register(Subcategory)