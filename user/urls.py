from django.urls import path
from .views import CustomerSignUpView, OwnerSignUpView, UserDeleteView, UserDetailView, UserUpdateView, index, UserLoginView, UserListView, UserLogoutView


app_name = 'user'

urlpatterns = [
    path('customer/signup/', CustomerSignUpView.as_view(), name='customer_signup'),
    path('owner/signup/', OwnerSignUpView.as_view(), name='owner_signup'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('userlist/', UserListView.as_view(), name="userlist"),
    path('<int:pk>/userupdate/', UserUpdateView.as_view(), name='userupdate'),
    path('<int:pk>/userdelete/', UserDeleteView.as_view(), name="userdelete"),
    path('<int:pk>/userdetail/', UserDetailView.as_view(), name="userdetail"),
    path('', index, name='index'),
]