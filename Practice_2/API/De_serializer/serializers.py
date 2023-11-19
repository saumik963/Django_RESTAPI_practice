from rest_framework import serializers
from .models import Student

#Validators ___ Create custome validators

# def start_with_H(value):
#     if value[0].lower() !='h':
#         raise serializers.ValidationError("City should start with H")


# class StudentSerialzer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     roll=serializers.IntegerField()
#     city=serializers.CharField(max_length=100,validators=[start_with_H])


#     def create(self,validate_data):
#         return Student.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get("name",instance.name)
#         instance.roll=validated_data.get("roll",instance.roll)
#         instance.city=validated_data.get("city",instance.city)
#         instance.save()
#         return instance

#     #Field level validation
#     def validate_roll(self,value):
#         if value >= 200:
#             raise serializers.ValidationError("Sheet is full!")
#         return value
    
#     #Object level validation
#     def validate(self, data):
#         nm= data.get('name')
#         ct= data.get('city')
#         if nm.lower() == "john" and ct.lower() != 'Hogworts':
#             raise serializers.ValidationError("City must be Hogworts!")
#         return data
    

#_________________ Class based serializer __________________

class StudentSerialzer(serializers.ModelSerializer):
    # name= serializers.CharField(read_only=True)
    class Meta:
        model= Student
        fields= ['name','roll', 'city']
        # read_only_fields=['name','roll']
    

#     Field level validation

    # def validate_roll(self,value):
    #     if value >= 200:
    #         raise serializers.ValidationError("Sheet is full!")
    #     return value
    
    # def validate_name(self,value):
    #     if value == "rohit":
    #         raise serializers.ValidationError("You cant enter!")
    #     return value
    
#     Object level validation
    def validate(self, data):
        nm= data.get('name')
        ct= data.get('city')
        if nm.lower() == "john" and ct.lower() != 'hogworts':
            raise serializers.ValidationError("City must be Hogworts!")
        return data