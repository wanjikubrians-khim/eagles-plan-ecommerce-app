from decimal import Decimal
from django.conf import settings
from ecommerce_app.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            product_id = str(product.id)
            cart_item = cart[product_id]
            cart_item['product'] = product
            cart_item['total_price'] = Decimal(product.price) * cart_item['quantity']
            yield cart_item

    def get_total_price(self):
        return sum(
            Decimal(item['product'].price) * item['quantity'] for item in self
        )

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
