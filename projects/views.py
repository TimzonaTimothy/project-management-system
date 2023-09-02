from django.shortcuts import render
from django.db.models import Avg
from register.models import *
from projects.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def projects(request):
    projects = Project.objects.all()
    active_projects = Project.objects.filter(status = 'Active')
    avg_projects = Project.objects.all().aggregate(Avg('complete_per'))['complete_per__avg']
    tasks = Task.objects.all()
    overdue_tasks = tasks.filter(due='2')
    context = {
        'active_projects':active_projects,
        'avg_projects' : avg_projects,
        'projects' : projects,
        'tasks' : tasks,
        'overdue_tasks' : overdue_tasks,
    }
    return render(request, 'projects/projects.html', context)

@login_required(login_url='/login')
def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_task.html', context)
        else:
            return render(request, 'projects/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_task.html', context)

@login_required(login_url='/login')
def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'projects/new_project.html', context)
        else:
            return render(request, 'projects/new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'projects/new_project.html', context)
    

#cancel a project view


# def generate_receipt(request, payment_id):
#     payment = Payment.objects.get(pk=payment_id)

#     # Create a receipt for the payment
#     receipt = Receipt(job=payment.job)
#     receipt.save()

#     # Render the receipt or invoice template with payment and receipt details
#     return render(request, 'generate_receipt.html', {'payment': payment, 'receipt': receipt})