from django.shortcuts import render
from rest_framework.response import Response
from .models import User,Bank
from .serializers import UserSerializer,BankSerializer
from rest_framework import viewsets,status
from abc import ABC,abstractmethod


class UserApi(viewsets.ViewSet):
      def register(self,request):
          data=request.data
          serializer=UserSerializer(data=data)
          if serializer.is_valid(raise_exception=True):
              serializer.save()
              user=User.objects.get(id=serializer.data['id'])
              account=Bank.objects.create(customer=user)
              account.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
          return Response('failed', status=status.HTTP_400_BAD_REQUEST)


      def bank_details(self,request,id):
          user=Bank.objects.get(id=id)
          context={
              'account_no':user.id,
              'customer_name': user.customer.name,
              'balance':user.balance
          }
          return Response(context,status=status.HTTP_200_OK)

class BankApi(viewsets.ViewSet):
      def withdraw(self,request,amount,id):
          account_no=Bank.objects.get(id=id)
          if account_no.balance>amount:
             account_no.balance=account_no.balance-amount
             context={
                 'withdraw_amount':amount,
                 'balance': account_no.balance
             }
             return Response(context,status=status.HTTP_200_OK)
          else:
              return Response('insuffient balance')

      def deposit(self,request,amount,id):
          account_no=Bank.objects.get(id=id)

          account_no.balance=account_no.balance+amount
          account_no.save()
          context={
                 'balance': account_no.balance
                 }
          return Response(context,status=status.HTTP_200_OK)

      def check_balance(self,request,id):
          account_no=Bank.objects.get(id=id)
          context={
                 'balance': account_no.balance
             }
          return Response(context,status=status.HTTP_200_OK)

