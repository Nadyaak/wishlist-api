from items.models import Item
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .serializers import (
    ItemListSerializer,
    ItemDetailSerializer,
)
from rest_framework.permissions import AllowAny
from .permissions import IsAdded_by
from rest_framework.filters import OrderingFilter, SearchFilter


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [OrderingFilter, SearchFilter,]
    search_filed = ['name','description',]

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    permission_classes = [IsAdded_by]
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'

