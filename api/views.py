from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, RestaurantSerializer, VotesSerializer
from polls.models import Orders, Resturants, Votes
from rest_framework import status


@api_view(['GET'])
def get_orders_data(request):

    orders = Orders.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_restaurants_data(request):

    restaurants = Resturants.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def addData(request):
    print("POST method")
    seralizer = OrderSerializer(data=request.data)
    if seralizer.is_valid():
        seralizer.save()
    return Response(seralizer.data)


@api_view(['POST'])
def add_votes(request):

    seralizer = VotesSerializer(data=request.data)
    if seralizer.is_valid():
        seralizer.save()
        return Response(seralizer.data)
    else:
        return Response()


@api_view(['GET'])
def get_votes_data(request):

    votes = Votes.objects.all()
    serializer = VotesSerializer(votes, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def update_restaurant_vote(request):
    votes = Votes.objects.filter(user=request.data.get(
        'user'), restaurant=request.data.get('id'))
    if len(votes) == 0:
        restaurant = Resturants.objects.get(pk=request.data.get('id'))
        serializer = RestaurantSerializer(
            restaurant, data=request.data, partial=True)
        restaurant.current_vote += 1
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "vote already exists"})
