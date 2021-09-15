from django.db import models

# Create your models here.
from django.db import models




class Record(models.Model):
    name_of_fellow = models.CharField('Full name of Fellow', max_length=5000, null=True)
    year_of_completion_of_ICOHRTA_feliowship_degree_programme = models.DateField('Year of Completion of ICOHRTA Feliowship Degree Programme', max_length=5000, null=True)
    year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution = models.CharField('Instituion where you did your ICOHRTA Feliowship Degree Programme', max_length=5000, null=True)
    position_s_held_since_completion_of_degree_programme1 = models.CharField(max_length=5000, null=True)
    position_held_since_completion_of_degree_programme_institution = models.CharField('Institution name where you are currently working', max_length=5000, null=True)
    current_position = models.CharField(max_length=5000, null=True)
    current_position_institution = models.CharField(max_length=5000, null=True)
    scientific_publications_1 = models.CharField(max_length=5000, null=True)
    grants_applied_for_1 = models.CharField(max_length=5000, null=True)
    award_number_or_sponsor_1 = models.CharField(max_length=5000, null=True)
    project_period_start_1  = models.CharField(max_length=5000, null=True)
    project_period_end_1  = models.CharField(max_length=5000, null=True)
    pd_or_pi_1= models.CharField(max_length=5000, null=True)
    number_of_trainees_supported_1 = models.IntegerField(null=True)
    mentors_1  = models.CharField(max_length=5000, null=True)
    mentees_1 = models.CharField(max_length=5000, null=True)
    any_other_relevant_information = models.CharField(max_length=5000, null=True)



# Create your models here.
class Nameinstitution(models.Model):
    name_of_fellow = models.CharField('Full name of Fellow', max_length=5000, null=True)
    year_of_completion_of_ICOHRTA_feliowship_degree_programme = models.DateField('Year of Completion of ICOHRTA Feliowship Degree Programme', max_length=5000, null=True)
    year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution = models.CharField('Instituion where you did your ICOHRTA Feliowship Degree Programme', max_length=5000, null=True)

    class Meta:
        db_table = 'nameinstitution'

    def __str__(self):
        return self.name_of_fellow

    def get_positionsheld(self):
        return ', '.join(self.positionsheld.all().values_list('name', flat=True))


    def get_currentpositions(self):
        return ', '.join(self.currentposition.all().values_list('name', flat=True))
    
    def get_achievements(self):
        return ', '.join(self.achievement.all().values_list('name', flat=True))

    def get_publications(self):
        return ', '.join(self.publication.all().values_list('name', flat=True))

    def get_grantsappliedfor(self):
        return ', '.join(self.grantsappliedfor.all().values_list('name', flat=True))

    def get_grantsawarded(self):
        return ', '.join(self.grantsawarded.all().values_list('name', flat=True))

    def get_mentor(self):
        return ', '.join(self.mentor.all().values_list('name', flat=True))

    def mentee(self):
        return ', '.join(self.mentee.all().values_list('name', flat=True))


class Positionsheld(models.Model):
    position_s_held_since_completion_of_degree_programme1 = models.CharField(max_length=5000, null=True)
    position_held_since_completion_of_degree_programme_institution = models.CharField('Institution name where you are currently working', max_length=5000, null=True)

class Currentposition(models.Model):
    current_position = models.CharField(max_length=5000, null=True)
    current_position_institution = models.CharField(max_length=5000, null=True)

# class Achievement(models.Model):
# 
#     achievements = models.CharField(max_length=5000, null=True)

class Publication(models.Model):
    scientific_publications_1 = models.CharField(max_length=5000, null=True)
  
class Grantsappliedfor(models.Model):

    grants_applied_for_1 = models.CharField(max_length=5000, null=True)

class Grantsawarded(models.Model):
    award_number_or_sponsor_1 = models.CharField(max_length=5000, null=True)

    project_period_start_1  = models.CharField(max_length=5000, null=True)

    project_period_end_1  = models.CharField(max_length=5000, null=True)

    pd_or_pi_1= models.CharField(max_length=5000, null=True)

    number_of_trainees_supported_1 = models.IntegerField(null=True)

class Mentor(models.Model):
    mentors_1  = models.CharField(max_length=5000, null=True)

class Mentee(models.Model):
    mentees_1 = models.CharField(max_length=5000, null=True)

class Relevant_information(models.Model):
    any_other_relevant_information = models.TextField(max_length=5000, null=True)


