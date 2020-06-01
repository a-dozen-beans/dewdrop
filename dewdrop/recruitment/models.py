from django.db import models


class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
    company_name = models.CharField(max_length=200)
    company_info = models.TextField()
    company_website = models.URLField()
    join_date = models.DateTimeField('Join date')

    def __str__(self):
        return self.company_name


class Category(models.Model):
    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"
    subcategory_name = models.CharField(max_length=200)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name   

class RecruitmentOffer(models.Model):
    class Meta:
        verbose_name = "Recruitment Offer"
        verbose_name_plural = "Recruitment Offers"
    recruiting_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,  null=True)
    recruitment_title = models.CharField(max_length=200)
    recruitment_info = models.TextField()
    recruitment_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.recruitment_title
