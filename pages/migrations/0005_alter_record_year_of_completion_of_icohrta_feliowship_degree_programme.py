# Generated by Django 3.2.6 on 2021-09-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_nameinstitution_year_of_completion_of_icohrta_feliowship_degree_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='year_of_completion_of_ICOHRTA_feliowship_degree_programme',
            field=models.DateField(max_length=5000, null=True, verbose_name='Year of Completion of ICOHRTA Feliowship Degree Programme'),
        ),
    ]
