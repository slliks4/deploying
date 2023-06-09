# Generated by Django 4.1.3 on 2022-12-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_portal', '0011_personal_info_academic_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('course_description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='Signature_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
