from django.contrib import admin
from django.urls import path
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

router = routers.DefaultRouter()                      # add this
router.register(r'recipes', views.RecipeView, 'recipe')     # add this
router.register(r'users', views.UsersView, 'users')

urlpatterns = [
    path('admin/', admin.site.urls),         
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),               # add this
    # path('api/token/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)