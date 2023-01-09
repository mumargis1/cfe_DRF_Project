from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
        ):
    """
    get -> list -> Queryset
    get -> retrive -> Product instance Detail View
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
prodcut_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})
