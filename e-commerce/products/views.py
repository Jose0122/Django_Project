from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Products_details
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ModelViewSet):
    queryset = Products_details.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]



# class ProductList(ListCreateAPIView):
#     queryset = Products_details.objects.all()
#     serializer_class = ProductSerializers


# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = Products_details.objects.all()
#     serializer_class = ProductSerializers


# class ProductList(APIView):

#     def get(self,request):
#         products = Products_details.objects.all()
#         serializing = ProductSerializers(products, many=True)
#         return Response(serializing.data)
#     def post(self,request):
#         if request.method == "POST":
#             serializing = ProductSerializers(data = request.data)
#             if serializing.is_valid():
#                 serializing.save()
#                 return Response(serializing.data)
#             else:
#                 return Response(serializing.errors)

# class ProductDetails(APIView):
        
#     def get(self,request,id):
#         try:
#             product = Products_details.objects.get(id = id)
#             serializer = ProductSerializers(product)
#             return Response(serializer.data)
#         except:
#             Products_details.DoesNotExist()
#             return Response({"error":"Product not found"},status=400)

#     def put(self,request,id):
#         product = Products_details.objects.get(id = id)
#         serializing = ProductSerializers(product,data = request.data)
#         serializing.is_valid(raise_exception=True)
#         serializing.save()
#         return Response(serializing.data)
#     def patch(self,request,id):
#         product = Products_details.objects.get(id = id)
#         serializing = ProductSerializers(product,data = request.data,partial = True)
#         serializing.is_valid(raise_exception=True)
#         serializing.save()
#         return Response(serializing.data)
#     def delete(self,request,id):
#         product = Products_details.objects.get(id = id)
#         product.delete()
#         return Response(status=204)


# @api_view(["GET"])
# def get_products(request):
#     if request.method == "GET":
#         products = Products_details.objects.all()
#         serializing = ProductSerializers(products, many=True)
#         return Response(serializing.data)

# @api_view(["POST"])
# def create_products(request):
#     if request.method == "POST":
#         serializing = ProductSerializers(data = request.data)
#         if serializing.is_valid():
#             serializing.save()
#             return Response(serializing.data)
#         else:
#             return Response(serializing.errors)   


# @api_view(["GET","PUT","PATCH","DELETE"])
# def all_products(request,id):

#     try:
#         product = Products_details.objects.get(id = id)
#     except:
#         Products_details.DoesNotExist
#         return Response({"error":"Product not found"},status=400)
    
#     if request.method == "GET":
#         serializer = ProductSerializers(product)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializing = ProductSerializers(product,data = request.data)
#         serializing.is_valid(raise_exception=True)
#         serializing.save()
#         return Response(serializing.data)
    
#     elif request.method == "PATCH":
#         serializing = ProductSerializers(product,data = request.data,partial = True)
#         serializing.is_valid(raise_exception=True)
#         serializing.save()
#         return Response(serializing.data)
    
#     elif request.method == "DELETE":
#         product.delete()
#         return Response(status=204)


