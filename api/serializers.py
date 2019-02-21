from rest_framework import serializers
from items.models import Item ,FavoriteItem
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class FavoriteItemSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['user',]

class ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    user_count = serializers.SerializerMethodField()
    added_by = UserSerializer()
    class Meta:
        model = Item
        fields = [
            'image',
            'name',
            'description',
            'added_by',
            'detail',
            'user_count'
            ]
    def get_user_count(self, obj):
        return obj.favorite.count() 
               
class ItemDetailSerializer(serializers.ModelSerializer):
    favorite = FavoriteItemSerializer(many=True)
    class Meta:
        model = Item
        fields = [
            'image',
            'name',
            'description',
            'added_by',
            'favorite',
            ]
