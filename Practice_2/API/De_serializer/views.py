from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerialzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.


# ___________________   Function based  _____________________


@csrf_exempt
def student_create(request):
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        # print(pydata)
        serializer= StudentSerialzer(data=pydata)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data inserted.'}

            json_data=JSONRenderer().render(res)
        
            return HttpResponse(json_data,content_type='application/json')
    
        json_data=JSONParser().render(serializer.errors)



@csrf_exempt
def student_api(request):
    if request.method =="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer= StudentSerialzer(stu)
            json_data=JSONRenderer().render(serializer.data)

            return HttpResponse(json_data,content_type='application/json')
        
        stu=Student.objects.all()
        serializer=StudentSerialzer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == "POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        serializer= StudentSerialzer(data=pydata)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data inserted.'}

            json_data=JSONRenderer().render(res)
        
            return HttpResponse(json_data,content_type='application/json')
    
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    if request.method =="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id= pydata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerialzer(stu,data=pydata)
        # serializer=StudentSerialzer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    

    if request.method == "DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted!'}
        return JsonResponse(res,safe=False)
    


# ___________________   Class based  _____________________


@method_decorator(csrf_exempt,name='dispatch')
class StudentAPI(View):

    def get(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer= StudentSerialzer(stu)
            json_data=JSONRenderer().render(serializer.data)

            return HttpResponse(json_data,content_type='application/json')
        
        stu=Student.objects.all()
        serializer=StudentSerialzer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        serializer= StudentSerialzer(data=pydata)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data inserted.'}

            json_data=JSONRenderer().render(res)
        
            return HttpResponse(json_data,content_type='application/json')
    
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


    def put(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id= pydata.get('id')
        stu=Student.objects.get(id=id)
        # serializer=StudentSerialzer(stu,data=pydata)   # Require all field data
        serializer=StudentSerialzer(stu,data=pydata,partial=True)   # Require partial field data only
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Updated!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    

    def delete(self,request,*args, **kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Data Deleted!'}
        return JsonResponse(res,safe=False)