from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("Admin.html", views.Admin, name="Admin"),
	       path("AdminLogin", views.AdminLogin, name="AdminLogin"),
	       path("User.html", views.User, name="User"),
	       path("RegisterLand.html", views.RegisterLand, name="RegisterLand"),
	       path("RegisterLandAction.html", views.RegisterLandAction, name="RegisterLandAction"),
	       path("UserCheck.html", views.UserCheck, name="UserCheck"),
	       path("AdminLandSearch.html", views.AdminLandSearch, name="AdminLandSearch"),
]