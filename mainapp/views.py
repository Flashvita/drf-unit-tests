from mainapp import serializers
from rest_framework import generics, viewsets, status
from mainapp.models import Company
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = serializers.CompanySerializer

    def list(self, request, *args, **kwargs):
        """End-point для получение списка компаний
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """End-point для создания компании
            request data: id: id компании(int)
        """
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """End-point для удаления компании
        """
        return super().destroy(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        """End-point для редактирования данных компании
        """
        company = Company.objects.get(id=self.kwargs.get('pk'))
        serializer = self.serializer_class(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.partial_update(request, *args, **kwargs)

        return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)


   



