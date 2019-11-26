from rest_framework.routers import DefaultRouter

from core import viewsets

router = DefaultRouter()
router.register('department', viewsets.DepartmentViewSet)
router.register('employee', viewsets.EmployeeViewSet)

urlpatterns = router.urls
