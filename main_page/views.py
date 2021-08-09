from django.shortcuts import render, redirect
from .models import BlogPost, HistoricalEvent, ArmyExam, NavyExam, AirforceExam, ArmySyllabus, NavySyllabus, AirforceSyllabus
from sign_up_page.models import Account

from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.id:
        name=request.user.fullname.split()[0]
        exam=ArmyExam.objects.get(id=1)
        context={
            'name':name,
            'exam':exam,
        }
        return render(request,'main_page.html',context)
    return render(request,'main_page.html')

def about_us(request):
    return render(request,'about_us.html')

def sources(request):
    return render(request,'sources.html')

def privacy_policy(request):
    return render(request,'privacy_policy_page.html')

def contactus(request):
    return render(request,'contact_us.html')

def newsfeed(request):
    BlogPosts=BlogPost.objects.all()
    context={
        'BlogPosts':BlogPosts,
    }
    return render(request,'newsfeed.html',context)

def exams(request):
    ArmyExams=ArmyExam.objects.all()
    context={
        'ArmyExams':ArmyExams,
    }
    return render(request,'exam_main_page.html',context)

def exams_army(request):
    ArmyExams=ArmyExam.objects.all()
    context={
        'ArmyExams':ArmyExams,
    }
    return render(request,'exam_main_page.html',context)

def exams_navy(request):
    NavyExams=NavyExam.objects.all()
    context={
        'NavyExams':NavyExams,
    }
    return render(request,'exam_navy_main_page.html',context)

def exams_airforce(request):
    AirforceExams=AirforceExam.objects.all()
    context={
        'AirforceExams':AirforceExams,
    }
    return render(request,'exam_airforce_main_page.html',context)

def exam_sub_army(request,pk):
    exam=ArmyExam.objects.get(id=pk)
    syllabus=ArmySyllabus.objects.get(id=pk)

    subjects=ArmySyllabus._meta.get_field('subjects')
    subjects = subjects.value_from_object(syllabus).split('$')

    syllabus_data=ArmySyllabus._meta.get_field('syllabus')
    syllabus_data = syllabus_data.value_from_object(syllabus).split('$')

    dictionary = dict(zip(subjects, syllabus_data))

    eligibility_nationality = ArmyExam._meta.get_field('eligibility_nationality')
    eligibility_nationality = eligibility_nationality.value_from_object(exam).split('$')

    eligibility_educational = ArmyExam._meta.get_field('eligibility_educational')
    eligibility_educational = eligibility_educational.value_from_object(exam).split('$')

    eligibility_age = ArmyExam._meta.get_field('eligibility_age')
    eligibility_age = eligibility_age.value_from_object(exam).split('$')
    context={
        'exam':exam,
        'syllabus':syllabus,
        'dictionary':dictionary,
        'eligibility_nationality':eligibility_nationality,
        'eligibility_educational':eligibility_educational,
        'eligibility_age':eligibility_age,
    }
    return render(request,'exam_subpage.html',context)

def exam_sub_navy(request,pk):
    exam=NavyExam.objects.get(id=pk)
    syllabus=NavySyllabus.objects.get(id=pk)

    subjects=NavySyllabus._meta.get_field('subjects')
    subjects = subjects.value_from_object(syllabus).split('$')

    syllabus_data=NavySyllabus._meta.get_field('syllabus')
    syllabus_data = syllabus_data.value_from_object(syllabus).split('$')

    dictionary = dict(zip(subjects, syllabus_data))

    eligibility_nationality = NavyExam._meta.get_field('eligibility_nationality')
    eligibility_nationality = eligibility_nationality.value_from_object(exam).split('$')

    eligibility_educational = NavyExam._meta.get_field('eligibility_educational')
    eligibility_educational = eligibility_educational.value_from_object(exam).split('$')

    eligibility_age = NavyExam._meta.get_field('eligibility_age')
    eligibility_age = eligibility_age.value_from_object(exam).split('$')
    context={
        'exam':exam,
        'syllabus':syllabus,
        'dictionary':dictionary,
        'eligibility_nationality':eligibility_nationality,
        'eligibility_educational':eligibility_educational,
        'eligibility_age':eligibility_age,
    }
    return render(request,'exam_subpage.html',context)
def exam_sub_airforce(request,pk):
    exam=AirforceExam.objects.get(id=pk)
    syllabus=AirforceSyllabus.objects.get(id=pk)

    subjects=AirforceSyllabus._meta.get_field('subjects')
    subjects = subjects.value_from_object(syllabus).split('$')

    syllabus_data=AirforceSyllabus._meta.get_field('syllabus')
    syllabus_data = syllabus_data.value_from_object(syllabus).split('$')

    dictionary = dict(zip(subjects, syllabus_data))

    eligibility_nationality = AirforceExam._meta.get_field('eligibility_nationality')
    eligibility_nationality = eligibility_nationality.value_from_object(exam).split('$')

    eligibility_educational = AirforceExam._meta.get_field('eligibility_educational')
    eligibility_educational = eligibility_educational.value_from_object(exam).split('$')

    eligibility_age = AirforceExam._meta.get_field('eligibility_age')
    eligibility_age = eligibility_age.value_from_object(exam).split('$')
    context={
        'exam':exam,
        'syllabus':syllabus,
        'dictionary':dictionary,
        'eligibility_nationality':eligibility_nationality,
        'eligibility_educational':eligibility_educational,
        'eligibility_age':eligibility_age,
    }
    return render(request,'exam_subpage.html',context)

def hof_army(request):
    return render(request,'hof_army.html')

def hof_navy(request):
    return render(request,'hof_navy.html')

def hof_airforce(request):
    return render(request,'hof_airforce.html')

def he(request):
    HisEvents=HistoricalEvent.objects.all()
    context={
        'HisEvents':HisEvents,
    }
    return render(request,'he.html',context)

def donations(request):
    return render(request,'donation_page.html')

def settings(request):
    return render(request,'settings.html')

def settings_edit(request):
    if request.method == 'POST':
        userid=request.user.id
        Account.objects.get(pk=userid).delete()
        fullname=request.POST['fname_test']
        username=request.POST['uname_test']
        dob=request.POST['date_test']
        gender=request.POST['btn']
        email=request.POST['email_test']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode_test']
        password1=request.POST['pass_test1']
        password2=request.POST['pass_test2']
        if password1==password2:
            if Account.objects.filter(email=email).exists() and email!='':
                messages.info(request, 'Email already used. Use another email id.')
                return redirect('settings_edit')
            elif Account.objects.filter(username=username).exists():
                messages.info(request, 'Username not available. Use another username')
                return redirect('settings_edit')
            else:
                user=Account.objects.create_user(fullname=fullname,username=username, dob=dob, gender=gender, email=email, state=state,city=city, pincode=pincode, password=password1)
                user.save()
                messages.info(request, 'Account details updated.')
                user = auth.authenticate(username=username,password=password1)
                auth.login(request,user)

                return redirect('settings')
        else:
            messages.info(request, 'Make sure your passwords match.')
            return redirect('settins_edit')
    else:
        return render(request,'settings_edit_account.html')