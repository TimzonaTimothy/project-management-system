from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.
class Project(models.Model):
    status = (
        ('Active', 'Active'),
        ('In-Progress', 'In-Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    name = models.CharField(max_length=80)
    project_id = models.CharField(max_length=8, verbose_name="Project ID",unique=True, null=True)
    slug = models.SlugField('shortcut', blank=True)
    assign = models.ManyToManyField(User)
    efforts = models.DurationField()
    status = models.CharField(max_length=30, choices=status, null=True, blank=True)
    dead_line = models.DateField()
    company = models.ForeignKey('register.Company', on_delete=models.CASCADE)
    complete_per = models.FloatField(max_length=2, validators = [MinValueValidator(0), MaxValueValidator(100)])
    description = models.TextField(blank=True)
    additional_information = models.TextField(blank=True)

    add_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return (self.name)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)
    

class Receipt(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    generated_date = models.DateTimeField(auto_now_add=True)