from django.urls import path
from .views import taskList,taskCreate,taskUpdate,delete_repeat_task,alldelete_confirm,allDelete
urlpatterns = [
    path('list/',taskList.as_view(),name='list'),
    path('create/',taskCreate.as_view(),name='create'),
    path('update/<int:pk>',taskUpdate.as_view(),name='update'),
    path('delete/<int:pk>',delete_repeat_task,name='delete'),
    path('alldeleteconfirm/',alldelete_confirm.as_view(),name='alldeleteconfirm'),
    path('alldelete/',allDelete.as_view(),name='alldelete'),
]