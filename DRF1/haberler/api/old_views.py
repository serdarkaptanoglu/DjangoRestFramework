from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from haberler.models import Makale
from haberler.api.old_serializers import MakaleSerializer


@api_view(['GET', 'POST'])
def makale_list_create_api_view(request):
    if request.method == 'GET':
        makale_instance = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makale_instance, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def makale_detail_api_view(request, pk):
    try:
        makale_instance = Makale.objects.get(pk=pk)
    except Makale.DoesNotExist:
        return Response(
            {
                'errors': {
                    'code': 404,
                    'message': f'Böyle bir id ({pk}) ile ilgili makale bulunamadi'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = MakaleSerializer(makale_instance)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MakaleSerializer(makale_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        makale_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

