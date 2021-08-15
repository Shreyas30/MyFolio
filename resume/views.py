from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

# Create your views here.

# @login_required(login_url='/')
def index(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('Home')
    else:
        return render(request, "resume/resume.html")

    

@login_required(login_url='/')
def inputData(request):
    if request.method == 'GET':
        template_name = request.GET.get('template_name', ' ')
        params = {'template_name': template_name}
        print("The resume template name is ", template_name)
        return render(request, 'resume/getData.html', params)
    if request.method == 'POST':
        print("Get data is clicked")
        template_name = request.POST.get('template_name', ' ')

        # Personal Details
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        dob = request.POST.get('dob', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        pincode = request.POST.get('pincode', '')
        phone = request.POST.get('phone', '')
        image = request.POST.get('image', '')
        about = request.POST.get('about', '')

        # Academic Details
        ten_board = request.POST.get('ten-board', ' ')
        ten_marks = request.POST.get('ten-marks', ' ')
        twelve_board = request.POST.get('twelve-board', ' ')
        twelve_marks = request.POST.get('twelve-marks', ' ')
        degree = request.POST.get('degree', ' ')
        institute = request.POST.get('institute', ' ')
        cgpa = request.POST.get('cgpa', ' ')
        exam = {}
        certificate = {}

        i = 1
        no_of_exam = int(request.POST.get('no-of-exam'))
        # no_of_exam = int(no_of_exam)
        while(no_of_exam > 0):
            exam_name = request.POST.get(f'exam{i}')
            rank = request.POST.get(f'rank{i}')
            if(exam_name != None):
                exam[exam_name] = rank
            i = i+1
            no_of_exam = no_of_exam-1

        i = 1
        no_of_course = int(request.POST.get('no-of-course'))
        while(no_of_course > 0):
            course = request.POST.get(f'course{i}')
            duration = request.POST.get(f'duration{i}')
            if(course != None):
                certificate[course] = duration
            i = i+1
            no_of_course = no_of_course-1

        for x, y in exam.items():
            print(f'Exam: {x} Rank: {y}')
        for x, y in certificate.items():
            print(f'Course: {x} Duration: {y}')

        # WORK Experience
        experience_status = request.POST.get('experience-status')
        exp = {}
        print(experience_status)
        print(type(experience_status))
        if(experience_status == 'fresher'):
            # do nothing as exp is already
            exp = {}
        elif(experience_status == 'experienced'):
            i = 1
            no_of_company = int(request.POST.get('no-of-company'))
            while(no_of_company > 0):
                company_name = request.POST.get(f'company-name{i}')
                job_title = request.POST.get(f'job-title{i}')
                experience = request.POST.get(f'experience{i}')
                if(company_name != None):
                    exp[company_name] = [job_title, experience]
                i = i+1
                no_of_company = no_of_company-1
        for x, y in exp.items():
            print(f'Company: {x} Job-title: {y[0]} Experience: {y[1]}')

        # PROJECT Details
        project_status = request.POST.get('project-status')
        project = {}
        print(project_status)
        print(type(project_status))
        if(project_status == 'noProject'):
            # do nothing as exp is already
            project = {}
        elif(project_status == 'doneProject'):
            i = 1
            no_of_project = int(request.POST.get('no-of-project'))
            print(no_of_project)
            while(no_of_project > 0):
                project_title = request.POST.get(f'project-title{i}')
                print(project_title)
                project_description = request.POST.get(
                    f'project-description{i}')
                skills_used = request.POST.get(f'skills-used{i}')
                if(project_title != None):
                    project[project_title] = [project_description, skills_used]
                i = i+1
                no_of_project = no_of_project-1
        for x, y in project.items():
            print(
                f'Project: {x} Project-Description: {y[0]} Skills Used: {y[1]}')

        # INTERNSHIP Details
        internship_status = request.POST.get('internship-status')
        internship = {}
        print(internship_status)
        print(type(internship_status))
        if(internship_status == 'noInternship'):
            # do nothing as exp is already
            internship = {}
        elif(internship_status == 'doneInternship'):
            i = 1
            no_of_internship = int(request.POST.get('no-of-internship'))
            print(no_of_internship)
            while(no_of_internship > 0):
                internship_title = request.POST.get(f'internship-title{i}')
                internship_duration = request.POST.get(
                    f'internship-duration{i}')
                internship_description = request.POST.get(
                    f'internship-description{i}')
                internship_skills_used = request.POST.get(
                    f'internship-skills-used{i}')
                if(internship_title != None):
                    internship[internship_title] = [
                        internship_description, internship_duration, internship_skills_used]
                i = i+1
                no_of_internship = no_of_internship-1
        for x, y in internship.items():
            print(
                f'Internship: {x} Internship-Description: {y[0]} Internship-Description: {y[1]} Internship-Skills Used: {y[2]}')

        # SKILLS and Abilities
        skills = []
        i = 1
        no_of_skill = int(request.POST.get('no-of-skill'))
        print(no_of_skill)
        while(no_of_skill > 0):
            skill_possesed = request.POST.get(f'skill{i}')
            if(skill_possesed != None):
                skills.append(skill_possesed)
            i = i+1
            no_of_skill = no_of_skill-1
        print(skills)

        # Now enter or pass all this data in template_name below, and then insert these values in template their
        params = {
            # Personal
            'fname': fname,
            'lname': lname,
            'email': email,
            'dob': dob,
            'state': state,
            'city': city,
            'pincode': pincode,
            'phone': phone,
            'image': image,
            'about' : about,

            # Academic
            'ten_board' : ten_board,
            'ten_marks' : ten_marks,
            'twelve_board': twelve_board,
            'twelve_marks': twelve_marks,
            'degree' : degree,
            'institute' : institute,
            'cgpa' : cgpa,
            'exam' : exam,
            'certificate' :certificate,

            #Work,
            'work_experience' : exp,

            #Project,
            'project' : project,

            #Internship,
            'internship':internship,

            #Skills,
            'skills':skills,

        }
        return render(request, f'resume/{template_name}', params)
    # return HttpResponse(template_name)
