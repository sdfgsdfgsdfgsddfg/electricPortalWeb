from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from home.models import *
from .models import *
from datetime import *

# Create your views here.
def operations(request):
    context = {'lang':"ar"}
    if not request.user.is_authenticated:
        return redirect("/login")
    else:
        user = User.objects.get(pk=request.user.pk)
        userTable = UserTable.objects.get(main_user=user)
        context['user'] = userTable

    if request.method == "POST":
        ierr = ""
        errtitle = ""
        a = "work"
        now = datetime.now()
        if request.POST["formType"] == "emergencyForm":
            operationCreate = Operation.objects.create(
                operation_malfunctionNumber = request.POST["malfunctionNumber"],
                operation_malfunctionType   = request.POST["malfunctionType"],
                operation_contractor        = request.POST["contractor"],
                operation_date              = request.POST["date"],
                operation_materials         = request.POST["materials"],
                operation_consultantName    = request.POST["consultantName"],
                operation_type = "emergency",
                year = now.year,
                month = now.month,
                day = now.day,
                operation_user = userTable
            )
            operationCreate.save()
        elif request.POST["formType"] == "substitutionForm":
            operationCreate = Operation.objects.create(
                operation_workNumber = request.POST['workNumber'],
                operation_contractor = request.POST['contractor'],
                operation_employmentType = request.POST['employmentType'],
                operation_site = request.POST['location'],
                operation_date = request.POST['date'],
                operation_consultantName = request.POST['consultantName'],
                operation_type = "substitution",
                year = now.year,
                month = now.month,
                day = now.day,
                operation_user = userTable
            )
            operationCreate.save()
        elif request.POST["formType"] == "reinforcementForm":
            operationCreate = Operation.objects.create(
                operation_workNumber = request.POST['workNumber'],
                operation_contractor = request.POST['contractor'],
                operation_site = request.POST['location'],
                operation_date = request.POST['date'],
                operation_consultantName = request.POST['consultantName'],
                operation_type = "reinforcement",
                year = now.year,
                month = now.month,
                day = now.day,
                operation_user = userTable
            )
            operationCreate.save()
        elif request.POST["formType"] == "effortForm":
            operationCreate = Operation.objects.create(
                operation_workNumber = request.POST['workNumber'],
                operation_contractor = request.POST['contractor'],
                operation_site = request.POST['location'],
                operation_date = request.POST['date'],
                operation_type = "effort",
                year = now.year,
                month = now.month,
                day = now.day,
                operation_user = userTable
            )
            operationCreate.save()
        elif request.POST["formType"] == "violationsForm":
            operationCreate = Operation.objects.create(
                operation_type = "violations",
                year = now.year,
                month = now.month,
                day = now.day,
                operation_user = userTable
            )
            operationCreate.save()
        for file in request.FILES:
            operationFileCreate = OperationFile.objects.create(
                operation = operationCreate,
                file = request.FILES[file]
            )
            operationFileCreate.save()
        return JsonResponse({"ierr":ierr,"errtitle":errtitle})
    else:
        data = []
        dataFilter = Operation.objects.all()
        months = [1,2,3,4,5,6,7,8,9,10,11,12]
        for m in months:
            dataFilter = Operation.objects.filter(month=m)
            if m == 1:monthName = "يناير"
            if m == 2:monthName = "فبراير"
            if m == 3:monthName = "مارس"
            if m == 4:monthName = "إبريل"
            if m == 5:monthName = "مايو"
            if m == 6:monthName = "يونيو"
            if m == 7:monthName = "يوليو"
            if m == 8:monthName = "أغسطس"
            if m == 9:monthName = "سبتمبر"
            if m == 10:monthName = "أكتوبر"
            if m == 11:monthName = "نوفمبر"
            if m == 12:monthName = "ديسمبر"
            values = []
            for d in dataFilter:
                now = datetime(int(d.year),int(d.month),int(d.day))
                if now.strftime('%A') == 'Sunday':dayName = "الأحد"
                if now.strftime('%A') == 'Monday':dayName = "الإثنين"
                if now.strftime('%A') == 'Tuesday':dayName = "الثلاثاء"
                if now.strftime('%A') == 'Wednesday':dayName = "الأربعاء"
                if now.strftime('%A') == 'Thursday':dayName = "الخميس"
                if now.strftime('%A') == 'Friday':dayName = "الجمعة"
                if now.strftime('%A') == 'Saturday':dayName = "السبت"
                if d.operation_type == "emergency":operation_type = "طوارئ"
                if d.operation_type == "substitution":operation_type = "الإحلال"
                if d.operation_type == "reinforcement":operation_type = "التعزيز"
                if d.operation_type == "effort":operation_type = "الجهد المتوسط (المشاريع المركزية)"
                if d.operation_type == "violations":operation_type = "المخالفات"
                values.append([d.pk,f"{d.pk} "+operation_type,d.operation_user.consultant_name,f'{d.day} {dayName}'])
            if len(values) != 0:
                values = values[::-1]
                data.append([monthName,values])
        data = data[::-1]
        if "getData" in request.GET:
            return JsonResponse({"data":data})
        elif "getOperationData" in request.GET:
            data = []
            operationGet = Operation.objects.get(pk=request.GET["getOperationData"])
            data.append(operationGet.operation_type)
            if operationGet.operation_type == "emergency":operation_type = "طوارئ"
            if operationGet.operation_type == "substitution":operation_type = "الإحلال"
            if operationGet.operation_type == "reinforcement":operation_type = "التعزيز"
            if operationGet.operation_type == "effort":operation_type = "الجهد المتوسط (المشاريع المركزية)"
            if operationGet.operation_type == "violations":operation_type = "المخالفات"
            data.append(f'{operationGet.pk} '+operation_type)
            if operationGet.operation_type == "emergency":
                data.append(operationGet.operation_malfunctionNumber)
                data.append(operationGet.operation_malfunctionType)
                data.append(operationGet.operation_contractor)
                data.append(operationGet.operation_date)
                data.append(operationGet.operation_materials)
                data.append(operationGet.operation_consultantName)
            elif operationGet.operation_type == "substitution":
                data.append(operationGet.operation_workNumber)
                data.append(operationGet.operation_contractor)
                data.append(operationGet.operation_employmentType)
                data.append(operationGet.operation_site)
                data.append(operationGet.operation_date)
                data.append(operationGet.operation_consultantName)
            elif operationGet.operation_type == "reinforcement":
                data.append(operationGet.operation_workNumber)
                data.append(operationGet.operation_contractor)
                data.append(operationGet.operation_site)
                data.append(operationGet.operation_date)
                data.append(operationGet.operation_consultantName)
            elif operationGet.operation_type == "effort":
                data.append(operationGet.operation_workNumber)
                data.append(operationGet.operation_contractor)
                data.append(operationGet.operation_site)
                data.append(operationGet.operation_date)
            data.append(operationGet.operation_user.consultant_name)

            files = []
            fileGet = OperationFile.objects.filter(operation=operationGet)
            for fl in fileGet:
                files.append([fl.file.url,fl.file.name[10:]])
            data.append(files)
            return JsonResponse({"data":data})
    context['data']=data

    return render(request, 'operations.html', context)