from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from django_app.models import Company
from django_app.serializers import CompanySerializer


@api_view(['GET', 'POST'])
def get_company_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_company_detail(request, pk):
    """
        Retrieve, update or delete a code snippet.
        """
    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return JsonResponse(data={"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse(data={"message": "Success"}, status=status.HTTP_204_NO_CONTENT)

