from django.conf import settings
from consumer.views.consumer_viewset import FeatureCollectionViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("", FeatureCollectionViewSet)

urlpatterns = router.urls
