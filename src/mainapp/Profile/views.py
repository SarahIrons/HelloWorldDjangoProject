
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile

def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'profiles': profiles})


def admin_console(request):
    profiles = Profile.objects.all()
    return render(request, 'Profile/submitOrDeleteProfile.html', {'profiles': profiles})

def details(request, pk):
    pk = int(pk)
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'Profile/submitOrDeleteProfile.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    userName = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        userName.delete()
        return redirect('home')
    context = {"userName": userName}
    return render(request, "Profile/confirmDelete.html", context)

def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def createRecord(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'Profile/createProfile.html', context)