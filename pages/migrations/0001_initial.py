# Generated by Django 3.2.6 on 2021-09-06 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nameinstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_fellow', models.CharField(default='Full name of Fellow', max_length=5000, null=True, verbose_name='Full name of Fellow')),
                ('year_of_completion_of_ICOHRTA_feliowship_degree_programme', models.CharField(max_length=5000, null=True, verbose_name='Year of Completion of ICOHRTA Feliowship Degree Programme')),
                ('year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution', models.CharField(max_length=5000, null=True, verbose_name='Instituion where you did your ICOHRTA Feliowship Degree Programme')),
            ],
            options={
                'db_table': 'nameinstitution',
            },
        ),
        migrations.CreateModel(
            name='Relevant_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('any_other_relevant_information', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scientific_publications_1', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Positionsheld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_s_held_since_completion_of_degree_programme1', models.CharField(max_length=5000, null=True)),
                ('position_held_since_completion_of_degree_programme_institution', models.CharField(max_length=5000, null=True, verbose_name='Institution name where you are currently working')),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentors_1', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentees_1', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Grantsawarded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_number_or_sponsor_1', models.CharField(max_length=5000, null=True)),
                ('project_period_start_1', models.CharField(max_length=5000, null=True)),
                ('project_period_end_1', models.CharField(max_length=5000, null=True)),
                ('pd_or_pi_1', models.CharField(max_length=5000, null=True)),
                ('number_of_trainees_supported_1', models.IntegerField(null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Grantsappliedfor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grants_applied_for_1', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
        migrations.CreateModel(
            name='Currentposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_position', models.CharField(max_length=5000, null=True)),
                ('current_position_institution', models.CharField(max_length=5000, null=True)),
                ('name_of_fellow', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.nameinstitution')),
            ],
        ),
    ]