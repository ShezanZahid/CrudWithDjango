from django.urls import path
from . import views
from . import datatable

urlpatterns=[
    path('',views.index,name='index'),
    path('details/<int:item_id>',views.details,name='details'),
    path('allindex',views.allindex,name='allindex'),
    path('selfindex',views.selfindex,name='selfindex'),
    path('post_approval_list',views.post_approval_list,name='post_approval_list'),
    path('post_approved_list',views.post_approved_list,name='post_approved_list'),
    path('post_rejected_list',views.post_rejected_list,name='post_rejected_list'),
    path('create',views.create,name='create'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('approve_post/<int:id>',views.approve_post,name='approve_post'),
    path('reject_post/<int:id>',views.reject_post,name='reject_post'),
    
]