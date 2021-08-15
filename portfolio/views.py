from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage
import os
import zipfile
import requests
from django.conf import settings
import glob
import shutil

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('Home')
    else:
        return render(request, "portfolio/portfolio.html")
    

def preview(request):
    if request.method == 'GET':
        temp = request.GET.get('temp')
        print(temp)
        return render(request, f'portfolio/{temp}')

def select(request):
    if request.method == 'GET':
        temp = request.GET.get('temp')
        print(temp)
        return render(request, f'portfolio/{temp}')

def imgHandler(request):
    if request.method == 'POST':
        print('\nFinally reached here\n')
        myfile = request.FILES['Image']
        print('\nMy file name is: ',myfile)
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        print(myfile.name, myfile)
        # return redirect(request. META['HTTP_REFERER'])  
        return JsonResponse({'error': False, 'responseValue':myfile.name })


def download(request):
    remove_files = [] 
    if request.method == 'POST':
        print('\nWe reached here\n')
        my_zip = zipfile.ZipFile('user.zip','w')
        my_zip.writestr('template/user.html', request.POST['html'])

        my_zip.write(f'media/{request.POST["homeImage"]}')
        os.remove(f'../myfolio/media/{request.POST["homeImage"]}')

        my_zip.write(f'media/{request.POST["aboutImage"]}')
        os.remove(f'../myfolio/media/{request.POST["aboutImage"]}')

        print(request.POST['homeImage'])
        for i in range(1,7):
            if request.POST[f'workImage{i}'] != '':
                my_zip.write(f'media/{request.POST[f"workImage{i}"]}')
                os.remove(f'../myfolio/media/{request.POST[f"workImage{i}"]}')

        #For Copying Static Images from Assets Folder to Media Folder
        num = int(request.POST["number"])  #Returns No of static Images in Template
        for i in range(num):
            fileName= request.POST[f"staticImage{i+1}"]  # Name of Static Image
            shutil.copyfile(f'assets/{fileName}', f'media/{fileName}')
            my_zip.write(f'media/{fileName}')
            os.remove(f'../myfolio/media/{fileName}')
        my_zip.close()
        
        os.replace('../myfolio/user.zip','../myfolio/media/user.zip')       
        return JsonResponse({'error': False})
    else:
        # needed_files=['user.zip','post','resume','profilePic','portfolio']
        # directory = '../myfolio/media'
        # for filename in os.listdir(directory):
        #     if filename not in needed_files:
        #          os.remove(directory+'/'+filename)

           
        # os.remove('C:/Users/Neelam/Desktop/TCET/SEMESTER 3/PBL/Django/myfolio/media/user.zip')
        # files = glob.glob('C:/Users/Neelam/Desktop/TCET/SEMESTER 3/PBL/Django/myfolio/media')
        # for f in files:
        #     os.remove(f)
        return redirect(request. META['HTTP_REFERER'])  
