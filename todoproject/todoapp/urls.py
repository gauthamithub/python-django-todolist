from.import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

    #Class based Generic Views
    path('listview/',views.TaskListView.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.TaskDetailView.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.TaskUpdateView.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.TaskDeleteView.as_view(),name='deleteview')
]