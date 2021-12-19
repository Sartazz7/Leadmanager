from rest_framework import routers, urlpatterns

from leads.models import Lead
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')

urlpatterns = router.urls