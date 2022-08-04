from django.shortcuts import render

# Create your views here.
import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.
from restaurant.models import Menu
from restaurant.permissions import IsRestaurant, IsSuperAdmin
from restaurant.serializers import MenuSerializer
from user.models import UserProfile
from user.serializers import UserSerializer, UserProfileSerializer
from user.permissions import IsOwnerOrAdmin


# RestaurantViewSet to handle Employee create,update,delete,list
class RestaurantViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['update']:
            self.permission_classes = [IsOwnerOrAdmin, ]
        elif self.action in ['destroy', 'list']:
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action in ['retrieve']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def create(self, request):
        serialized = UserSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save(userType="restaurant")

            return Response("Restaurant created successfully", status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = UserProfile.objects.filter(userType="restaurant")
        serializer_class = UserProfileSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# RestaurantProfileViewSet to store additional information like userType='restaurant'
class RestaurantProfileViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        if self.action in ['update']:
            self.permission_classes = [IsOwnerOrAdmin, ]
        elif self.action in ['destroy', 'list']:
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action in ['retrieve']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def list(self, request):
        queryset = UserProfile.objects.all(userType="restaurant")
        serializer_class = UserProfileSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(UserProfile, id=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(UserProfile, id=pk)
        serializer = UserProfileSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# checking if specific time between two times or not
def is_now_in_time_period(start_time, end_time, now_time):
    if start_time < end_time:
        return start_time <= now_time <= end_time
    else:
        # Over midnight:
        return now_time >= start_time or now_time <= end_time


# MenuViewSet to handle Menu create,update,delete,list
class MenuViewSet(viewsets.ViewSet):
    """
    Example empty viewset demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action in ['update']:
            self.permission_classes = [IsSuperAdmin, ]
        elif self.action in ['destroy']:
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action in ['retrieve', 'list']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['create']:
            self.permission_classes = [IsRestaurant]
        return super().get_permissions()

    def create(self, request):
        today = datetime.date.today()
        # checking if time is between 12AM - 11AM or not
        # between that time restaurants can create Menu
        if is_now_in_time_period(datetime.time(00, 00), datetime.time(11, 00), datetime.datetime.now().time()):
            try:
                # a restaurant can have a single menu for single day
                # if menu already created fetching that object
                menu = Menu.objects.get(created__date=today, restaurant=request.user)
                serializer = MenuSerializer(instance=menu, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'Success': "Menu Updated Successful", "menu_details": serializer.data},
                                status=status.HTTP_202_ACCEPTED)
            except Menu.DoesNotExist:
                # if not already created create one
                serialized = MenuSerializer(data=request.data)
                user = request.user
                if serialized.is_valid():
                    menu = serialized.save(restaurant=user)
                    menu = MenuSerializer(menu)
                    return Response({'Success': "Menu Create Successful", "menu_details": menu.data},
                                    status=status.HTTP_201_CREATED)
                else:
                    return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Lunch Time Finished, Try Between 12:00 AM - 11:00 AM",
                            status=status.HTTP_406_NOT_ACCEPTABLE)

    def list(self, request):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer(queryset, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        menu = get_object_or_404(Menu, id=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        today = datetime.date.today()
        # checking if time is between 12AM - 11AM or not
        # between that time restaurants can delete/update Menu
        if is_now_in_time_period(datetime.time(00, 00), datetime.time(11, 00), datetime.datetime.now().time()):
            menu = get_object_or_404(Menu, id=pk)
            menu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Time Finished to Edit/Delete",
                            status=status.HTTP_406_NOT_ACCEPTABLE)
