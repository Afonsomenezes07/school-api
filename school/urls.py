from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet,
    SubjectViewSet,
    GradeViewSet
)

router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'grades', GradeViewSet)

urlpatterns = router.urls