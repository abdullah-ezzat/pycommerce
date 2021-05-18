from abc import ABC, abstractmethod
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from api.resources import getHomeProductsResource
from PyCommerce.models import GetHomeProducts, ProductSpecifications, Categories
import math


class IGetHomeProducts(ABC):
    @abstractmethod
    def get_home_products():
        pass

    def get_searched_products():
        pass

    def get_max_page():
        pass


class getHomeProducts(IGetHomeProducts):
    def get_home_products(self, request, page=1, specValue='null', search='null', categoryId=0):
        if request.method == 'GET':
            homeProducts = GetHomeProducts.objects.all().order_by('StoreId')

            if search != 'null':
                homeProducts = homeProducts.filter(
                    ProductName__contains=search)

            if specValue != 'null':
                selectedValues = specValue.split(',')
                productIds = ProductSpecifications.objects.all().filter(
                    SpecificationValue__in=selectedValues)
                ids = [product.ProductId for product in productIds]
                homeProducts = homeProducts.filter(ProductId__in=ids)

            if categoryId != 0:
                homeProducts = homeProducts.filter(CategoryId=categoryId)

        maxPageNumber = len(homeProducts) / 8
        maxPageNumber = math.ceil(maxPageNumber) * 10

        paginator = Paginator(homeProducts, 8)
        pages = paginator.get_page(page)
        products = pages.object_list

        serializer = getHomeProductsResource(
            products, many=True)
        return JsonResponse(serializer.data, safe=False)

    def get_searched_products(self, request, search='null'):
        if request.method == 'GET':
            if search != 'null':
                products = GetHomeProducts.objects.all().filter(ProductName__contains=search)
                categoryIds = [product.CategoryId for product in products]
                categories = Categories.objects.all().filter(Id__in=categoryIds)

                productNames = [(product.CategoryId, product.ProductName)
                                for product in products]
                categoryNames = [(category.Id, category.NameL)
                                 for category in categories]
                List = []
                for p in set(productNames):
                    for c in set(categoryNames):
                        if p[0] == c[0]:
                            List.append(
                                {'ProductName': p[1], 'CategoryName': c[1]})

        return JsonResponse(List[:10], safe=False)

    def get_max_page(self, request, specValue='null', search='null', categoryId=0):
        if request.method == 'GET':
            homeProducts = GetHomeProducts.objects.all().order_by('StoreId')

            if search != 'null':
                homeProducts = homeProducts.filter(
                    ProductName__contains=search)

            if specValue != 'null':
                selectedValues = specValue.split(',')
                productIds = ProductSpecifications.objects.all().filter(
                    SpecificationValue__in=selectedValues)
                ids = [product.ProductId for product in productIds]
                homeProducts = homeProducts.filter(ProductId__in=ids)

            if categoryId != 0:
                homeProducts = homeProducts.filter(CategoryId=categoryId)

            maxPageNumber = len(homeProducts) / 8
            maxPageNumber = math.ceil(maxPageNumber)
            List = []
            for page in range(1, maxPageNumber + 1):
                List.append(page)

            return JsonResponse(List, safe=False)


get_home_products = getHomeProducts().get_home_products
get_searched_products = getHomeProducts().get_searched_products
get_max_page = getHomeProducts().get_max_page
