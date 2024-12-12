from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.generics import get_object_or_404

from haberler.api.serializers import MakaleSerializer, GazeteciSerializer
from haberler.models import Makale, Gazeteci


class GazeteciListCreateAPIView(APIView):
    def get(self, request):
        yazarlar = Gazeteci.objects.all()
        serializer = GazeteciSerializer(yazarlar, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = GazeteciSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MakaleListCreateAPIView(APIView):
    def get(self, request):
        makale_instance = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makale_instance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MakaleDetailAPIView(APIView):
    def get_object(self, pk):
        makale = get_object_or_404(Makale, pk=pk)
        return makale

    def get(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale)
        return Response(serializer.data)

    def put(self, request, pk):
        makale = self.get_object(pk=pk)
        serializer = MakaleSerializer(makale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        makale = self.get_object(pk=pk)
        makale.delete()
        return Response({
            'errors': {
                'code': 204,
                'message': f'{pk} id li makale silinmiştir'
            }
        }, status=status.HTTP_204_NO_CONTENT)
