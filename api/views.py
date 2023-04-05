from .models import Customer,Product
from .serializers import ProductSerializer,CustomerSerializer
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser,FormParser
from datetime import datetime
from dateutil import relativedelta
from datetime import date,timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CustomerModelViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer


class ProductModelViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all().filter(status=True)
    serializer_class=ProductSerializer
    parser_classes=(MultiPartParser,FormParser)
    
    
class Listview(APIView):
    def get(self,request,format=None):
        object=Product.objects.all().filter(status=True)
        serializer=ProductSerializer(object,many=True)
        for obj in object:
            date_value=obj.created_date
            today_date=date.today()
            delta=relativedelta.relativedelta(today_date,date_value)
            res_month=delta.months+(delta.years * 12)
            if res_month > 2:
              obj.status=False
              serializer.save()
              return Response({'msg':'Some Product will be inactive','data':serializer.data})  
            else:
                return Response({'msg':'No Changes Occured'})
            
            