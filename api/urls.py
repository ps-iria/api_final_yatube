from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

from . import views

router = DefaultRouter()
router.register(
    r'posts',
    views.PostViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
router.register(
    'follow',
    views.FollowViewSet,
    basename='followers'
)
router.register(
    'group',
    views.GroupViewSet,
    basename='group'
)

urlpatterns = [
        path('', include(router.urls)),
        path('api-token-auth/', auth_views.obtain_auth_token),
        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
