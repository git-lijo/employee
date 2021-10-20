
from django.urls import path, include
from .views import HomeView, PostDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home", ),
    path('employeedata/<int:pk>', PostDetailView.as_view(), name="post_detail", ),
    path('addemployee/', AddPostView.as_view(), name="add_post", ),
]

