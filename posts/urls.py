from django.urls import path
from . import views
app_name='posts'



urlpatterns = [
    path('list/', views.p_list, name="list"),
    path('create/', views.p_create, name="create"),
    path('<int:post_id>/delete/', views.p_delete, name="delete"),
    path('<int:post_id>/update/', views.p_update, name="update"),
    path('<int:post_id>/datt/', views.p_datt, name="datt"),
    path('<int:post_id>/createdatt/', views.p_createdatt, name="createdatt"),
    path('<int:post_id>/datt/<int:datts_id>/deletedatt/', views.p_deletedatt, name="deletedatt"),
    path('<int:post_id>/datt/<int:datts_id>/updatedatt/', views.p_updatedatt, name="updatedatt"),

]