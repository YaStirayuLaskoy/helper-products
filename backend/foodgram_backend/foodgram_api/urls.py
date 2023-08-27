from rest_framework import routers
from django.urls import path, include

from .views import (CustomUserViewSet, TagViewSet,
                    RecipeViewSet, IngredientViewSet)


# http://localhost/api/docs/ - docks
# http://localhost - foodgram front
# https://www.figma.com/file/HHEJ68zF1bCa7Dx8ZsGxFh/ - figma


app_name = 'foodgram_api'

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
# router.register('recipes', RecipeViewSet)


urlpatterns = [
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
    # path('recipes/', RecipeApiList.as_view()),
    # path('recipes/<int:pk>', RecipeApiList.as_view()),
]


'''from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import TagViewSet, IngredientViewSet, RecipeViewSet


app_name = 'foodgram_api'

router = SimpleRouter() 
router.register('recipes', RecipeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]'''
