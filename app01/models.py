from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateField()
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.IntegerField()
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    comment = models.CharField(max_length=20,null=True)
    hire_date = models.DateField()
    department = models.ForeignKey('Department')
    def __str__(self):
        return self.name


