from django.test import TestCase
from django.urls import reverse

from .models import Product

# Create your tests here.
class ProductListView(TestCase):

    def test_should_return_200(self):
        url = reverse('list_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 0)

    def test_should_return_200_with_products(self):
        url = reverse('list_product')
        Product.objects.create(
            name="test",
            description="test_description",
            price="5",
            available=True,
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products'].count(), 1)



# -----breakpoint()
#Esta es una funcion incorporada de que se utiliza para 
#pausar la ejecución del programa y abrir un depuracdor interactivo

# def suma(a, b):
#     resultado = a + b
#     breakpoint()
#     return resultado

# x = suma(3, 2)
# print(x)