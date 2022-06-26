from django.shortcuts import render,HttpResponse
from rest_framework import  serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Words, Admins,Users
import datetime
# Create your views here.
class give_product(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'

class give_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Words.objects.all()
        serlized_agent = give_product(all_agent, many=True)
        return Response(serlized_agent.data)

class admin_product(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'

class admin_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Admins.objects.all()
        serlized_agent = admin_product(all_agent, many=True)
        return Response(serlized_agent.data)

def users(req,tg_id,xabar,soz,f_name,kanal):
    get , cr = Users.objects.get_or_create(telegram_id=tg_id,
                                           full_name=f_name,
                                           kanal=kanal,
                                           xabar=xabar,
                                           soz=soz)
    get.save()
    return HttpResponse('sdad')