from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *


class ProductsView(APIView):

    def get(self, request):
        all_products = Products.objects.all()

        products_data = []

        for product in all_products:

            single_product = {
                'id': product.id,
                'product_name': product.product_name,
                'code': product.code,
                'price': product.price,
            }
            products_data.append(single_product)
        return Response(products_data)

    def post(self, request):
        new_product = Products(product_name= request.data["product_name"], code = request.data["code"], price = request.data["price"])
        new_product.save()
        return Response("Data Saved") 

class ProductsViewById(APIView):

    def get(self, request, id):
        product = Products.objects.get(id = id)
        

        single_product = {
            'id': product.id,
            'product_name': product.product_name,
            'code': product.code,
            'price': product.price,
        }
        return Response(single_product)
    
    def patch(self, request, id):
        product = Products.objects.filter(id = id)
        
        product.update(product_name= request.data["product_name"], code = request.data["code"], price = request.data["price"])
        return Response("Updated")
    
    def delete(self, request, id):
        product = Products.objects.get(id = id)
        product.delete()
        return Response("Deleted")