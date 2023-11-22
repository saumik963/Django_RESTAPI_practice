from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status

# Create your views here.


# @api_view()
# def hello_world(request):
#     return Response({'msg':"hello world"})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':"hello world"})


# @api_view(["POST"])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':"Requested posted!"})


# @api_view(["GET","POST"])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg':"Requested GET!"})
        
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':"Requested posted!", 'data':request.data})
    


# Function based API view

# @api_view(["GET","POST","PUT","DELETE"])
# def Student_api(request):

#     if request.method == "GET":
#         id=request.data.get("id")
#         if id is not None:
#             stu= Student.objects.get(id=id)
#             serializer= StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer= StudentSerializer(stu,many=True)
#         return Response(serializer.data)

        
#     if request.method == "POST":
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Inserted.'})
#         return Response(serializer.errors)
    
#     if request.method == "PUT":
#             id= request.data.get('id')
#             stu= Student.objects.get(pk=id)
#             serializer=StudentSerializer(stu,data=request.data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'msg':'Data Updated.'})
#             return Response(serializer.errors)
    
#     if request.method == "DELETE":
#             id= request.data.get('id')
#             stu= Student.objects.get(pk=id)
#             stu.delete()
#             return Response({'msg':'Data Deleted.'})
    



# Browseable API view

@api_view(["GET","POST","PUT","PATCH","DELETE"])
def Student_API(request,pk=None):

    if request.method == "GET":
        id=pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer= StudentSerializer(stu,many=True)
        return Response(serializer.data)

        
    if request.method == "POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted.'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    if request.method == "PUT":
            id=pk
            stu= Student.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated.'})
            return Response(serializer.errors)
    
    if request.method == "PATCH":
            id=pk
            stu= Student.objects.get(pk=id)
            serializer=StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Partial Data Updated.'})
            return Response(serializer.errors)
    
    if request.method == "DELETE":
            id=pk
            stu= Student.objects.get(pk=id)
            stu.delete()
            return Response({'msg':'Data Deleted.'})