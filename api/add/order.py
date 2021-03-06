from PyCommerce.models import cartTransactions, inventoryDetails, orderMasters, orders
from api.update.checkBalance import check_inv_balance
from api.update.invBalance import update_inv_balance
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http.response import JsonResponse
from api.resources import cartResource
from abc import ABC, abstractmethod
import datetime
import json


class IAddOrder(ABC):
    @abstractmethod
    def add_order():
        pass


class AddOrder():
    @csrf_exempt
    def add_order(self, request, cartId, userId):
        order = False
        if request.method == 'POST':
            items = cartTransactions.objects.filter(
                MasterId=cartId, IsOrdered=False)
            Serializer = cartResource(items, many=True)
            Data = json.loads(JSONRenderer().render(Serializer.data))
            if items.count() > 0:
                master = orderMasters.objects.create(
                    cartId_id=cartId, DateCreated=datetime.datetime.now(), UserId_id=userId, OrderStatusId_id=0)
                for data in Data:
                    check_balance = check_inv_balance(
                        data['ProductId'], data['StoreId'], data['Quantity'])
                    if check_balance == True:
                        order = orders.objects.create(
                            MasterId_id=master.id, cartId_id=cartId,
                            ProductId_id=data['ProductId'], StoreId_id=data['StoreId'],
                            ShippingAgentId_id=data['ShippingAgentId'], UserId_id=userId,
                            UnitPrice=data['TotalPricePerItem'], Quantity=data['Quantity'],
                            TotalPrice=data['TotalPricePerItem'] *
                            data['Quantity'],
                            Latitude=data['Latitude'], Longitude=data['Longitude'],
                            isDelivered=False, DeliveredByUserId_id=None)

                        inventoryDetails.objects.create(
                            ProductId_id=data['ProductId'], StoreId_id=data['StoreId'], Quantity=data['Quantity'], TransType_id=2)
                        data['StoreId_id'] = data['StoreId']
                        data['ProductId_id'] = data['ProductId']
                        update_inv_balance(data)
                order = master.id
        return JsonResponse(order, safe=False)


add_order = AddOrder().add_order
