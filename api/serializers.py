from rest_framework import serializers


# Serializers are the feature provided by DRF to serialize and deserialize the objects in APIs
# Serialization is the process of changing the python objects to JSON
# Desearialization is the process of validation of the JSON data provided by Frontend / Postman


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    section = serializers.CharField()


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField()
    # classroom = serializers.IntegerField()
