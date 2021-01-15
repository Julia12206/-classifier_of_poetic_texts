from rest_framework.serializers import ModelSerializer

from .models import Texts, TextsModel


class ClassSerializer(ModelSerializer):
    """Cериализатор мля модели TextsModel"""
    class Meta:
        model = TextsModel
        fields = ['klaccName', 'klacc']

class TextSerializer(ModelSerializer):
    """Cериализатор мля модели Texts"""
    klacc = ClassSerializer('klacc', required=False)
    class Meta:
        model = Texts
        fields = ['stih', 'author', 'nazvanie']
