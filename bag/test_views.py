from django.test import TestCase
from django.urls import reverse
from products.models import Product


class TestBagViews(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            price=10
        )

    def test_view_bag_page(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_product_to_bag_no_size(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 2,
                'redirect_url': reverse('view_bag')
            }
        )

        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product.id)], 2)
        self.assertEqual(response.status_code, 302)

    def test_add_product_to_bag_with_size(self):
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.id]),
            {
                'quantity': 1,
                'product_size': 'm',
                'redirect_url': reverse('view_bag')
            }
        )

        bag = self.client.session['bag']
        self.assertEqual(
            bag[str(self.product.id)]['items_by_size']['m'], 1
        )

    def test_adjust_bag_quantity(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(
            reverse('adjust_bag', args=[self.product.id]),
            {'quantity': 3}
        )

        bag = self.client.session['bag']
        self.assertEqual(bag[str(self.product.id)], 3)

    def test_remove_from_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            str(self.product.id),
            self.client.session.get('bag', {})
        )
