from rest_framework import serializers
from polls.models import Orders, Resturants, Votes, OrdersElements


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturants
        fields = "__all__"


class VotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votes
        fields = "__all__"


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersElements
        fields = "__all__"
