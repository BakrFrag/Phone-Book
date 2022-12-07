from rest_framework import routers 
from contact.views import ContactViewsets

router = routers.DefaultRouter()
router.register("",ContactViewsets )

urlpatterns = router.urls