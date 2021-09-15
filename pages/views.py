from django.shortcuts import render, redirect
from django.forms import formsets, modelformset_factory
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def home(request):

    name_of_fellow = ''
    year_of_completion_of_ICOHRTA_feliowship_degree_programme = ''
    year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution = ''

    position_s_held_since_completion_of_degree_programme1 = ''
    position_held_since_completion_of_degree_programme_institution = ''
    current_position = ''
    current_position_institution = ''

    scientific_publications_1 = ''
    grants_applied_for_1 = ''
    award_number_or_sponsor_1 = ''
    project_period_start_1  = ''
    project_period_end_1  = ''
    pd_or_pi_1= ''

    number_of_trainees_supported_1 = 0
    mentors_1  = ''
    mentees_1 = ''
    any_other_relevant_information = ''


    if request.method == 'POST':
        NameinstitutionForm = modelformset_factory(Nameinstitution, fields=('name_of_fellow','year_of_completion_of_ICOHRTA_feliowship_degree_programme',
        'year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution',))

        form = NameinstitutionForm(request.POST)
        
        if form.is_valid():
            name_of_fellow=form[0].cleaned_data.get('name_of_fellow')
            year_of_completion_of_ICOHRTA_feliowship_degree_programme=form[0].cleaned_data.get('year_of_completion_of_ICOHRTA_feliowship_degree_programme')
            year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution=form[0].cleaned_data.get('year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution')

            form.save()
        else:
            print(form.errors)

        CurrentpositionFormSet = modelformset_factory(Currentposition, fields=('current_position', 'current_position_institution'))
        formset = CurrentpositionFormSet(request.POST)

        if formset.is_valid():
            for form in formset:

                current_position += form.cleaned_data.get('current_position') + '; '
                current_position_institution += form.cleaned_data.get('current_position_institution') + '; '

            formset.save()
        else:
            print(formset.errors)


        PositionsheldFormSet = modelformset_factory(Positionsheld, fields=('position_s_held_since_completion_of_degree_programme1',
        'position_held_since_completion_of_degree_programme_institution'))
        formset1=PositionsheldFormSet(request.POST)
        if formset1.is_valid():
            for form in formset1:
                position_s_held_since_completion_of_degree_programme1+=form.cleaned_data.get('position_s_held_since_completion_of_degree_programme1') + '; '
                position_held_since_completion_of_degree_programme_institution+=form.cleaned_data.get('position_held_since_completion_of_degree_programme_institution') + '; '
            formset1.save()
        else:
            print(formset1.errors)



        PublicationFormSet = modelformset_factory( Publication, fields=('scientific_publications_1',
        ))
        formset3=PublicationFormSet(request.POST)
        if formset3.is_valid():
            for form in formset3:
                scientific_publications_1 += form.cleaned_data.get('scientific_publications_1') + '; '
                formset3.save()
        else:
            print(formset3.errors)



        GrantsappliedforFormSet = modelformset_factory( Grantsappliedfor, fields=('grants_applied_for_1',
        ))
        formset4=GrantsappliedforFormSet(request.POST)
        if formset4.is_valid():
            for form in formset4:
                grants_applied_for_1 += form.cleaned_data.get('grants_applied_for_1') + '; '
            formset4.save()
        else:
            print(formset4.errors)

        GrantsawardedFormSet = modelformset_factory( Grantsawarded, fields=('award_number_or_sponsor_1','pd_or_pi_1','project_period_start_1',
            'number_of_trainees_supported_1','project_period_end_1'))
        formset5=GrantsawardedFormSet(request.POST)
        if formset5.is_valid():
            for form in formset5:
                award_number_or_sponsor_1 += form.cleaned_data.get('award_number_or_sponsor_1') + '; '
                project_period_start_1  += form.cleaned_data.get('project_period_start_1') + '; '
                project_period_end_1  += form.cleaned_data.get('project_period_end_1') + '; '
                pd_or_pi_1+= form.cleaned_data.get('pd_or_pi_1') + '; '
                number_of_trainees_supported_1 += form.cleaned_data.get('number_of_trainees_supported_1') 
            formset5.save()
        else:
            print(formset5.errors)

        MentorFormSet = modelformset_factory( Mentor, fields=('mentors_1',))
        formset6=MentorFormSet(request.POST)
        if formset6.is_valid():
            for form in formset6:
                mentors_1+=form.cleaned_data.get('mentors_1') + '; '
                formset6.save()
        else:
            print(formset6.errors)

        MenteeFormSet = modelformset_factory( Mentee, fields=('mentees_1',))
        formset7=MenteeFormSet(request.POST)
        if formset7.is_valid():
            for form in formset7:
                mentees_1+=form.cleaned_data.get('mentees_1') + '; '
                formset7.save()
        else:
            print(formset7.errors)

        Relevant_informationForm = modelformset_factory(Relevant_information, fields=('any_other_relevant_information',))
        form8=Relevant_informationForm(request.POST)
        if form8.is_valid():
                any_other_relevant_information+=form8[0].cleaned_data.get('any_other_relevant_information') + '; '
                form8.save()
        else:
            print(form8.errors)

        context={'formset': formset, 'formset1':formset1, 'form':form,
                'formset3':formset3, 'formset4':formset4, 'formset5':formset5,
                'formset6':formset6, 'formset7':formset7, 'form8':form8,}

        record = Record(any_other_relevant_information=any_other_relevant_information,
        mentees_1=mentees_1,
        mentors_1=mentors_1,
        award_number_or_sponsor_1=award_number_or_sponsor_1,
        project_period_start_1=project_period_start_1,
        project_period_end_1=project_period_end_1,
        pd_or_pi_1=pd_or_pi_1,
        grants_applied_for_1=grants_applied_for_1,
        scientific_publications_1=scientific_publications_1,
        position_held_since_completion_of_degree_programme_institution=position_held_since_completion_of_degree_programme_institution,
        position_s_held_since_completion_of_degree_programme1=position_s_held_since_completion_of_degree_programme1,
        current_position_institution=current_position_institution,
        current_position=current_position,
        year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution=year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution,
        year_of_completion_of_ICOHRTA_feliowship_degree_programme=year_of_completion_of_ICOHRTA_feliowship_degree_programme,
        name_of_fellow=name_of_fellow,
        number_of_trainees_supported_1=number_of_trainees_supported_1
        
        )
        record.save()

        return render(request, 'index.html', context)

    NameinstitutionForm = modelformset_factory(Nameinstitution, fields=('name_of_fellow','year_of_completion_of_ICOHRTA_feliowship_degree_programme',
        'year_of_completion_of_ICOHRTA_feliowship_degree_programme_institution',))   
    form = NameinstitutionForm(queryset=Nameinstitution.objects.none())

            
    CurrentpositionFormSet = modelformset_factory(Currentposition, fields=('current_position', 'current_position_institution'))
    formset = CurrentpositionFormSet(queryset=Currentposition.objects.none())

    PositionsheldFormSet = modelformset_factory(Positionsheld, fields=('position_s_held_since_completion_of_degree_programme1',
        'position_held_since_completion_of_degree_programme_institution'))
    formset1=PositionsheldFormSet(queryset=Positionsheld.objects.none())

    PublicationFormSet = modelformset_factory( Publication, fields=('scientific_publications_1',
        ))
    formset3=PublicationFormSet(queryset=Publication.objects.none())

    GrantsappliedforFormSet = modelformset_factory( Grantsappliedfor, fields=('grants_applied_for_1',
        ))
    formset4=GrantsappliedforFormSet(queryset=Grantsappliedfor.objects.none())

    GrantsawardedFormSet = modelformset_factory( Grantsawarded, fields=('award_number_or_sponsor_1','pd_or_pi_1','project_period_start_1',
            'number_of_trainees_supported_1','project_period_end_1'))
    formset5=GrantsawardedFormSet(queryset=Grantsawarded.objects.none())

    MentorFormSet = modelformset_factory( Mentor, fields=('mentors_1',))
    formset6=MentorFormSet(queryset=Mentor.objects.none())

    MenteeFormSet = modelformset_factory( Mentee, fields=('mentees_1',))
    formset7=MenteeFormSet(queryset=Mentee.objects.none())

    Relevant_informationForm = modelformset_factory(Relevant_information, fields=('any_other_relevant_information',))
    form8=Relevant_informationForm(queryset=Relevant_information.objects.none())

    context={'formset': formset, 'formset1':formset1, 'form':form,
                'formset3':formset3, 'formset4':formset4, 'formset5':formset5,
                'formset6':formset6, 'formset7':formset7, 'form8':form8,}

    return render(request, 'index.html', context)