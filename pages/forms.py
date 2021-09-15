from .models import *
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class NameinstitutionForm(forms.ModelForm):
    name_of_fellow = forms.CharField()
    year_of_completion_of_ICOHRTA_feliowship_degree_programme = forms.DateField(widget=DateInput(),input_formats=['%d/%m/%Y'],
    )
    year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(NameinstitutionForm, self).__init__(*args, **kwargs)


class PositionsheldForm(forms.Form):
    name = forms.CharField(
        label='uyhfgcgj',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })

    )

class PositionsheldModelForm(forms.ModelForm):
    position_s_held_since_completion_of_degree_programme1 = forms.CharField(label='Positions held since completion of degree programme', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Positions held since completion of degree programme'}))
    position_held_since_completion_of_degree_programme_institution = forms.CharField(label='Position (s) held since completion of degree programme instituion', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Position (s) held since completion of degree programme instituions'})
                        )
    
PositionsheldFormSet = formset_factory(PositionsheldForm)                
PositionsheldModelFormSet = modelformset_factory(Positionsheld, 
                    fields=('position_s_held_since_completion_of_degree_programme1', 'position_held_since_completion_of_degree_programme_institution'),
                           )

class CurrentpositionForm(forms.ModelForm):
    current_position = forms.CharField(label='Current Position', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Current Position'}))
    current_position_institution = forms.CharField(label='Institution name where you are currently working', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Institution name where you are currently working'}))
CurrentpositionFormSet = modelformset_factory(Positionsheld, 
                    fields=('position_s_held_since_completion_of_degree_programme1', 'position_held_since_completion_of_degree_programme_institution'),
                            )

# class AchievementForm(forms.ModelForm):
#     achievements = forms.CharField(label='Achievements', 
#                         widget=forms.TextInput(attrs={'class': 'form-control',
#                         'placeholder': 'Achievements'}))


class PublicationForm(forms.ModelForm):    
    scientific_publications_1 = forms.CharField(label='Scientific Publications', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Scientific Publications'}))
PublicationFormSet = modelformset_factory(Publication, 
                    fields=('scientific_publications_1',),
                            )
  
class GrantsappliedforForm(forms.ModelForm):
    grants_applied_for_1 = forms.CharField(label='Grants applied for', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Grants applied for'}))
GrantsappliedforFormSet = modelformset_factory(Grantsappliedfor, 
                    fields=('grants_applied_for_1',),
                            )
  

class GrantsawardedForm(forms.ModelForm):
    award_number_or_sponsor_1 = forms.CharField(label='Grants Awarded', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Grants Awarded'}))

    project_period_start_1  = forms.DateField(label='Project Period(start)', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Project Period(start)'}))

    project_period_end_1  = forms.DateField(label='Project Period(end)', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Project Period(end)'}))

    pd_or_pi_1= forms.CharField(label='PD/PI.', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'PD/PI'}))

    number_of_trainees_supported_1 = forms.IntegerField(label='Number of trainees supported', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Number of trainees supported'}))

GrantsawardedFormSet = modelformset_factory(Grantsawarded, 
                    fields=('award_number_or_sponsor_1', 'project_period_start_1', 'project_period_end_1',
                    'pd_or_pi_1', 'number_of_trainees_supported_1'),)

class MentorForm(forms.ModelForm):
    mentors_1  = forms.CharField(label='Mentors', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Mentors'}))
MentorFormSet = modelformset_factory(Mentor, 
                    fields=('mentors_1',),)

class MenteeForm(forms.ModelForm):
    mentees_1 = forms.CharField(label='Mentees', 
                        widget=forms.TextInput(attrs={'class': 'form-control',
                        'placeholder': 'Mentees'}))
MenteeFormSet = modelformset_factory(Mentee, 
                    fields=('mentees_1',),)
def __init__(self, *args, **kwargs):
        super(MenteeForm, self).__init__(*args, **kwargs)

class Relevant_informationForm(forms.ModelForm):
    any_other_relevant_information = forms.CharField(label='Any other relavant information', 
                        widget=forms.Textarea(attrs={"rows":3, "cols":50, 'class': 'form-control',
                        'placeholder': 'Any other relavant information'}))


