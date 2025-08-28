from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserCreateAPIView, UserUpdateAPIView, ChangePasswordAPIView, \
    UserDeleteAPIView, WishlistCreateAPIView, WishlistDeleteAPIView, WishlistListAPIView, \
    WishlistRetrieveAPIView

# user
urlpatterns = [
    path('user-create', UserCreateAPIView.as_view()),
    path('user-update/<int:pk>', UserUpdateAPIView.as_view()),
    path('user-delete/<int:pk>', UserDeleteAPIView.as_view()),
    path('user-change-passwd/<int:pk>', ChangePasswordAPIView.as_view()),
]

# wishlist
urlpatterns += [
    path('wishlist-create', WishlistCreateAPIView.as_view()),
    path('wishlist-delete/<int:pk>', WishlistDeleteAPIView.as_view()),
    path('wishlist-detail/<int:pk>', WishlistRetrieveAPIView.as_view()),
    path('wishlists', WishlistListAPIView.as_view()),
]

# JWT
urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
