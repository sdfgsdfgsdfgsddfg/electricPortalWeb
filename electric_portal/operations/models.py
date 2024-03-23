from django.db import models
from home.models import *

class Operation(models.Model):
    operation_malfunctionNumber = models.CharField(max_length=50, null = True, blank = True)
    operation_malfunctionType = models.CharField(max_length=50, null = True, blank = True)
    operation_workNumber = models.CharField(max_length=50, null = True, blank = True)
    operation_employmentType = models.CharField(max_length=50, null = True, blank = True)
    operation_contractor = models.CharField(max_length=50, null = True, blank = True)
    operation_date = models.CharField(max_length=50, null = True, blank = True)
    operation_site = models.CharField(max_length=50, null = True, blank = True)
    operation_materials = models.CharField(max_length=50, null = True, blank = True)
    operation_consultantName = models.CharField(max_length=50, null = True, blank = True)
    operation_type = models.CharField(max_length=50, null = True, blank = True)
    operation_user = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    year = models.CharField(max_length=5)
    month = models.CharField(max_length=5)
    day = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.operation_malfunctionNumber} {self.operation_workNumber}'

class OperationFile(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    file = models.FileField(upload_to="pdf-files")