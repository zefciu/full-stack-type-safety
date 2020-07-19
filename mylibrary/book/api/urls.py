from rest_framework.routers import DefaultRouter

from book.api.views import BookViewSet, PublisherViewSet, AuthorViewSet

router = DefaultRouter()
router.register('book', BookViewSet)
router.register('author', AuthorViewSet)
router.register('publisher', PublisherViewSet)
urlpatterns = router.urls