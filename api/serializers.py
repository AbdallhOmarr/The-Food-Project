from rest_framework import serializers
from polls.models import Orders, Resturants, Votes


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
