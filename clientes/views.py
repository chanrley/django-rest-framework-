from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

# myapp/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from clientes.pagination import MyPagination
# from clientes.models import Cliente

# class MyAPIView(APIView):
#     pagination_class = MyPagination

#     def get(self, request):
#         queryset = Cliente.objects.all()
#         page = self.paginate_queryset(queryset)
#         serializer = Cliente(page, many=True)
#         return self.get_paginated_response(serializer.data)