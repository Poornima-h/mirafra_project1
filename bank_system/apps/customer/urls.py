from django.urls import path
from .views import UserApi,BankApi

urlpatterns=[
          path('', UserApi.as_view({
           'post':'register',
          })),
          path('<int:id>', UserApi.as_view({
           'get' :'bank_details'
          })),
         path('withdraw/<int:id>/<int:amount>', BankApi.as_view({'get': 'withdraw'})),
         path('deposit/<int:id>/<int:amount>', BankApi.as_view({'get': 'deposit'})),
         path('check-balance/<int:id>', BankApi.as_view({'get': 'check_balance'}))

 ]