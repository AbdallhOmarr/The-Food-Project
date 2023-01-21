from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OrderSerializer, RestaurantSerializer, VotesSerializer, ElementSerializer
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
def create_new_order(request):
    print("POST method")
    seralizer = OrderSerializer(data=request.data)
    if seralizer.is_valid():
        seralizer.save()
        return Response(seralizer.data)
    else:
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_votes(request):
    serializer = VotesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        for field, errors in serializer.errors.items():
            for error in errors:
                print(f"{field}: {error}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_votes_data(request):

    votes = Votes.objects.all()
    serializer = VotesSerializer(votes, many=True)

    return Response(serializer.data)


@api_view(['PUT'])
def update_restaurant_vote(request):
    try:
        # Get the restaurant object
        restaurant = Resturants.objects.get(pk=request.data.get('id'))
        # Check if a vote already exists for the same user and restaurant
        votes = Votes.objects.filter(user=request.data.get(
            'user'), restaurant=request.data.get('id'))
        if len(votes) == 0:
            # If no vote exists, increment the restaurant's current vote by 1
            restaurant.current_vote += 1
            restaurant.save()
            # Serialize and return the updated restaurant object
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        else:
            # If a vote already exists, return a 400 Bad Request with an error message
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "vote already exists"})
    except Resturants.DoesNotExist:
        # If the restaurant does not exist, return a 404 Not Found
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "restaurant not found"})

# send and recieve any type of data


# this view fn to add a new element to my cart
# item should be have data about the element id ,user id, order no, and qty

@api_view(['POST'])
def addElement(request):
    # get request data
    data = request.data

    # example for the data
    # {
    #     "state": "Ongoing",
    #     "resturant": 6
    # }

    print(f"Data: {data}")
    # create serializer instance
    serializer = ElementSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
