from.models import Texts, TextsModel
from django.forms import ModelForm, TextInput, Textarea


class TextsModelForm(ModelForm):
    class Meta:
        model = TextsModel
        fields = ["klaccName"]
        widgets = {
            "klaccName":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название категории (хокку, стихи-пирожки, стихи-порожки, лиммерики)'

            })
        }


class TextsFormSecond(ModelForm):
    class Meta:
        model = Texts
        fields = ["stih"]
        widgets = {
            "stih": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст на русском языке'

            })
        }


class TextsForm(ModelForm):
    class Meta:
        model = Texts
        fields = ["nazvanie", "stih", "author","klacc"]
        widgets = {
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя автора'
            }),
            "nazvanie" : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),

            "stih": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            })

        }

class VipSp(ModelForm):
    class Meta:
        model = Texts
        fields = ['klacc']

class FiltCat(ModelForm):
    class Meta:

        model = TextsModel
        fields = ['klacc', 'klaccName']

