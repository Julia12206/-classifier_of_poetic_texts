from.models import Texts, TextsModel
from django.forms import ModelForm, TextInput, Textarea
from django import forms


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
                'placeholder': 'Введите текст'

            })
        }


class TextsForm(ModelForm):
    class Meta:
        model = Texts
        fields = ["nazvanie", "stih", "author", 'klaccName']
        widgets = {

            "klaccName": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите категорию(хокку, стихи-пирожки, стихи-порошки, лимерики, стихи)'
            }),
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
        #form_class = PostForm
        model = TextsModel
        fields = ['klacc', 'klaccName']



    # CHOISES = (
    #     ('1', 'хокку'),
    #     ('2', 'стихи-порошки'),
    #     ('3', 'стихи-пирожки'),
    #     ('4', 'лимерики'),
    #     ('5','стихи'),
    #     )
    # filter_by = forms.ChoiceField(choices=CHOISES)