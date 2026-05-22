
from django.contrib import admin
from django.urls import path
from ManageCash.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerpage/',registerpage,name='registerpage'),
    path('',loginpage,name='loginpage'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('dashboardpage/',dashboardpage,name='dashboardpage'),
    path('profilepage/',profilepage,name='profilepage'),
    path('profileupdate/',profileupdate,name='profileupdate'),
    
    path('AddCash/',AddCash,name='AddCash'),
    path('transactionpage/',transactionpage,name='transactionpage'),
    path('CashEdit<int:id>/',CashEdit,name='CashEdit'),
    path('CashDelete<int:id>/',CashDelete,name='CashDelete'),
    
    path('AddExpense/',AddExpense,name='AddExpense'),
    path('ExpenseEdit<int:id>/',ExpenseEdit,name='ExpenseEdit'),
    path('ExpenseDelete<int:id>/',ExpenseDelete,name='ExpenseDelete'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
