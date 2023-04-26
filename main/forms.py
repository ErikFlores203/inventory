from django import forms
from django.core import validators
from .models import Brand, Department, Product

class FormBrand(forms.Form):
    name = forms.CharField(
        label="Nombre de la marca",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Barcel',
                'class':'form-control'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El Nombre es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññb  ]*$', 'El Nombre tiene caracteres invalidos','invlaid_name')
        ]
    )

class FormDepartment(forms.Form):
    name = forms.CharField(
    label="Nombre del departamento",
    max_length=150,
    widget=forms.TextInput(
        attrs={
            'placeholder':'Higiene y Hogar',
            'class':'form-control'
        }
    ),
    validators=[
        validators.MinLengthValidator(4,'El Nombre es demasiado corto'),
        validators.RegexValidator('^[A-Za-z0-9Ññb  ]*$', 'El Nombre tiene caracteres invalidos','invlaid_name')
    ]
)

# class FormProduct(forms.Form):   
#     name = forms.CharField(
#         label="Nombre del producto",
#         max_length=150,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder':'Jabon Ajax',
#                 'class':'form-control'
#             }
#         ),
#         validators=[
#             validators.MinLengthValidator(4,'El titulo es demasiado corto'),
#             validators.RegexValidator('^[A-Za-z0-9Ññb  ]*$', 'El Nombre tiene caracteres invalidos','invlaid_name')
#         ]
#     )
#     amount = forms.DecimalField(
#         label="Cantidad de articulos",
#         widget=forms.NumberInput(attrs={'class':'form-control'})
#     )

#     brand = forms.ModelChoiceField(
#         label="¿Que marca es el producto?",
#         queryset=Brand.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )

#     department = forms.ModelChoiceField(
#         label="¿A que departamento pertenece?",
#         queryset=Department.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-select'})
#     )

#     visible_choices=[
#         (1,'Si'),
#         (0,'No')
#     ]
    
#     visible = forms.TypedChoiceField(
#         label="¿Visible?",
#         choices= visible_choices,
#         widget=forms.RadioSelect(),
#     )
class FormProduct(forms.ModelForm):
    visible = forms.BooleanField(required=False, initial=True, widget=forms.RadioSelect(choices=((True,'Visible'),(False,'Oculto'))))
    name = forms.CharField(
        label="Nombre del producto",
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Jabon Ajax',
            'class': 'form-control'
        }),
        validators=[
            validators.MinLengthValidator(3,'El Nombre es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9Ññb  ]*$', 'El Nombre tiene caracteres invalidos','invlaid_name')
        ]
    )
    class Meta:
        model = Product
        fields = ['name','amount','brand','department','visible']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'brand': forms.Select(attrs={
                'class': 'form-select'
            }),
            'department': forms.Select(attrs={
                'class': 'form-select'
            }),
            'visible': forms.RadioSelect(),
        }

        



