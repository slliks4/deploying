from django.db import models
from django.contrib.auth.models import User

class My_applications(models.Model):
    application=models.CharField(max_length=200)
    class Meta:
        verbose_name_plural='My_applications'

class Admission_users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100, null=True)


RELEASE_OF_INFORMATION=[
    ('YES','Yes'),
    ('NO','No')
]

DECLARATION_AUTHORIZATION=[
    ('YES','Yes'),
    ('NO','No')
]

AGREEMENT=[
    ('YES','Yes'),
    ('NO','No')
]
class Personal_info(models.Model):
    Agreement=models.CharField(max_length=100, null=True, choices=AGREEMENT)
    Entry_term=models.CharField(max_length=200, null=True)
    Campus=models.CharField(max_length=200, null=True)
    Student_type=models.CharField(max_length=200, null=True)
    Admission_category=models.CharField(max_length=200, null=True)
    Area_of_interest=models.CharField(max_length=200, null=True)
    Academic_program=models.CharField(max_length=200, null=True)
    Student_id=models.CharField(max_length=200, null=True)
    Given_name=models.CharField(max_length=100,null=True)
    Middle_name=models.CharField(max_length=100,null=True)
    Family_name=models.CharField(max_length=100,null=True)
    Preffered_first_name=models.CharField(max_length=100,null=True)
    Preffered_family_name=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=100,null=True)
    Phone=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Gender=models.CharField(max_length=50, null=True)
    Birthday=models.DateField(null=True)
    First_language=models.CharField(max_length=200,null=True)
    Country_of_residence=models.CharField(max_length=200,null=True)
    Kin_given_name=models.CharField(max_length=100, null=True)
    Kin_middle_name=models.CharField(max_length=100, null=True)
    Kin_family_name=models.CharField(max_length=100, null=True)
    Kin_address=models.CharField(max_length=200, null=True)
    Kin_city=models.CharField(max_length=100, null=True)
    Kin_information_authorization=models.CharField(max_length=100, null=True, choices=RELEASE_OF_INFORMATION)
    School_name=models.CharField(max_length=200, null=True)
    School_city=models.CharField(max_length=100, null=True)
    Declaration_authorization=models.CharField(max_length=100, null=True, choices=DECLARATION_AUTHORIZATION)
    Signature=models.CharField(max_length=300, null=True)
    Signature_date=models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural='Personal_info'

    def __str__(self) -> str:
        return f'{self.Given_name} {self.Middle_name}'



class Course_listing(models.Model):
    course_name=models.CharField(max_length=200)
    course_description=models.TextField()

    def __str__(self) -> str:
        return f'{self.course_name}'

class Staff_information(models.Model):
    name=models.CharField(max_length=50)