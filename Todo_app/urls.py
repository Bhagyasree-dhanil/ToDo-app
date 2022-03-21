from django.urls import path
from . import views

urlpatterns=[
  # General home page
   path('', views.home,name="home"),
   path('signup/', views.signup_user,name="signup_user"),
   path('login/', views.login_user,name="login_user"),
   path('logout/', views.logout_user,name="logout_user"),


   # User pages
   path('home/', views.current_todo,name="current_todo"),
   path('completed/', views.completed_todo,name="completed_todo"),
   path('create/', views.create_todo,name="create_todo"),

   # indirect pages

   path('show/<int:todo_pk>', views.show_todo,name="show_todo"),
   path('show/<int:todo_pk>/complete/', views.complete_todo,name="complete_todo"),
   path('show/<int:todo_pk>/delete/', views.delete_todo,name="delete_todo"),

]
