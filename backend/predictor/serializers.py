from rest_framework import serializers

class CoffeeRoastSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeRoast
        fields = '__all__'
