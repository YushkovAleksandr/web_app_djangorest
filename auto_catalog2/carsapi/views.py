from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Car
from .serializers import CarListSerializer, CarPopularSerializer, \
                         CarCreateSerializer, CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('id')
    serializer_class = CarSerializer


class CarPopularViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('rating')
    serializer_class = CarPopularSerializer


class CarListView(APIView):

    def get(request):
        cars = Car.objects.all().order_by('id')
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data)


class CarPopularView(APIView):

    def get(request):
        popular = Car.objects.all().order_by('rating')
        serializer = CarPopularSerializer(popular, many=True)
        return Response(serializer.data)


class CarCreateView(APIView):
    def post(request):
        post_car = CarCreateSerializer(data=request.data)
        if post_car.is_valid():
            post_car.save()
        return Response(status=201)
