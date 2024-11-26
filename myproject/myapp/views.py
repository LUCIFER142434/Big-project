from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


def index(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    
    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()
    
    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()
    
    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        
        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,
        
        'main_two_left':main_two_left,
        'main_two_right':main_two_right
    }
    return render(request,'index.html',obj)


def admin(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    
    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()
    
    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()
    
    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        
        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,
        
        'main_two_left':main_two_left,
        'main_two_right':main_two_right
    }
    return render(request,'admin.html',obj)




def meetings(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    
    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()
    
    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()
    
    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        
        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,
        
        'main_two_left':main_two_left,
        'main_two_right':main_two_right
    }
    return render(request,'meetings.html',obj)




def meeting_details(request):
    header_top = models.HeaderTop.objects.all()
    header_center = models.HeaderCenter.objects.all()
    header_end = models.HeaderEnd.objects.all()
    
    main_one_top = models.MainOneTop.objects.all()
    main_one_left = models.MainOneLeft.objects.all()
    main_one_right = models.MainOneRight.objects.all()
    
    main_two_left = models.MainTwoLeft.objects.all()
    main_two_right = models.MainTwoRight.objects.all()
    
    obj = {
        'header_top':header_top,
        'header_center':header_center,
        'header_end':header_end,
        
        'main_one_top':main_one_top,
        'main_one_left':main_one_left,
        'main_one_right':main_one_right,
        
        'main_two_left':main_two_left,
        'main_two_right':main_two_right
    }
    return render(request,'meeting_details.html',obj)



# Header CRUD start

def creat_header_top(request):
    if request.method == 'POST':
        form = forms.HeaderTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderTopForm()
    return render(request,'form.html',{'form':form})

def update_header_top(request,head_id):
    head = get_object_or_404(models.HeaderTop,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_top(request,head_id):
    head = get_object_or_404(models.HeaderTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_header_center(request):
    if request.method == 'POST':
        form = forms.HeaderCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderCenterForm()
    return render(request,'form.html',{'form':form})

def update_header_center(request,head_id):
    head = get_object_or_404(models.HeaderCenter,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderCenterForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderCenterForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_center(request,head_id):
    head = get_object_or_404(models.HeaderCenter,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



def creat_header_end(request):
    if request.method == 'POST':
        form = forms.HeaderEndForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderEndForm()
    return render(request,'form.html',{'form':form})

def update_header_end(request,head_id):
    head = get_object_or_404(models.HeaderEnd,id=head_id)
    if request.method == 'POST':
        form = forms.HeaderEndForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.HeaderEndForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_header_end(request,head_id):
    head = get_object_or_404(models.HeaderEnd,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



# Header end

# Main one start



def creat_main_one_top(request):
    if request.method == 'POST':
        form = forms.MainOneTopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneTopForm()
    return render(request,'form.html',{'form':form})

def update_main_one_top(request,head_id):
    head = get_object_or_404(models.MainOneTop,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneTopForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneTopForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_top(request,head_id):
    head = get_object_or_404(models.MainOneTop,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_one_left(request):
    if request.method == 'POST':
        form = forms.MainOneLeftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneLeftForm()
    return render(request,'form.html',{'form':form})

def update_main_one_left(request,head_id):
    head = get_object_or_404(models.MainOneLeft,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneLeftForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneLeftForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_left(request,head_id):
    head = get_object_or_404(models.MainOneLeft,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_one_right(request):
    if request.method == 'POST':
        form = forms.MainOneRightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneRightForm()
    return render(request,'form.html',{'form':form})

def update_main_one_right(request,head_id):
    head = get_object_or_404(models.MainOneRight,id=head_id)
    if request.method == 'POST':
        form = forms.MainOneRightForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainOneRightForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_one_right(request,head_id):
    head = get_object_or_404(models.MainOneRight,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})



# Main one end


# Main two start




def creat_main_two_left(request):
    if request.method == 'POST':
        form = forms.MainTwoLeftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoLeftForm()
    return render(request,'form.html',{'form':form})

def update_main_two_left(request,head_id):
    head = get_object_or_404(models.MainTwoLeft,id=head_id)
    if request.method == 'POST':
        form = forms.MainTwoLeftForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoLeftForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_two_left(request,head_id):
    head = get_object_or_404(models.MainTwoLeft,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})


def creat_main_two_right(request):
    if request.method == 'POST':
        form = forms.MainTwoRightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoRightForm()
    return render(request,'form.html',{'form':form})

def update_main_two_right(request,head_id):
    head = get_object_or_404(models.MainTwoRight,id=head_id)
    if request.method == 'POST':
        form = forms.MainTwoRightForm(request.POST,instance=head)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = forms.MainTwoRightForm(instance=head)
    return render(request,'form.html',{'form':form})

def delete_main_two_right(request,head_id):
    head = get_object_or_404(models.MainTwoRight,id=head_id)
    if request.method == 'POST':
        head.delete()
        return redirect('admin')
    return render(request,'delete.html',{'head':head})
