from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripcion")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible")
    photo = forms.ImageField(label="Foto", required=False)


#self hace referencia a la instancia de la clase

    def save(self): #save se trata de un metodo de una clase de Django personalizada para un formulario
        Product.objects.create( #Aqui se esta creando un objeto de la base de datos usando el modelo products
            name=self.cleaned_data["name"], #Self.clean es un diccionario
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"]
        )

