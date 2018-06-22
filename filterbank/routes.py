
from rest_framework import routers

from drawing.views import RoiViewSet, SampleViewSet
from filterbank.views import FilterViewSet, ParsingRequestViewSet, RepresentationViewSet
from social.views import UserViewSet, CommentsViewSet

router = routers.SimpleRouter()
router.register(r"filters", FilterViewSet)
router.register(r"parsing", ParsingRequestViewSet)
router.register(r"representations", RepresentationViewSet)