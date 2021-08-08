from django.urls import path
from . import views
from . import datatable

urlpatterns=[
    path('',views.index,name='index'),
    path('details/<int:item_id>',views.details,name='details'),
    path('allindex',views.allindex,name='allindex'),
    path('selfindex',views.selfindex,name='selfindex'),
    path('create',views.create,name='create'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    
]