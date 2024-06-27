from rest_framework import serializers
from crud.models import Classroom, Student


# Serializers are the feature provided by DRF to serialize and deserialize the objects in APIs
# Serialization is the process of changing the python objects to JSON
# Desearialization is the process of validation of the JSON data provided by Frontend / Postman


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    section = serializers.CharField()


class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "name", "section"]


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField()
    # classroom = serializers.IntegerField()


class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    class Meta:
        model = Student
        fields = ["id", "name", "age", "email", "address", "classroom"]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request.method and request.method == "GET":
            fields["classroom"] = ClassRoomModelSerializer()
        return fields
