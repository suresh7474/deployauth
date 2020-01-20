from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import Sign_up
from django.http import HttpResponseRedirect
def home(request):
    return render(request,'home.html')
@login_required
def python_exam(request):
    return render(request,'python.html')
@login_required
def java_exam(request):
    return render(request,'java.html')
@login_required
def   c_exam(request):
    return render(request,'c.html')
# Create your views here.

def log_out(request):
    return render(request,'logout.html')

def sing_UP_view(request):
    form = Sign_up()
    if request.method == 'POST':
        form = Sign_up(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'signup.html', {'form': form})


