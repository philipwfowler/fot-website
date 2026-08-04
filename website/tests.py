from django.test import TestCase
from django.urls import reverse
class WebsiteTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Confidence in every")
    def test_contact_page(self):
        self.assertEqual(self.client.get(reverse("contact")).status_code, 200)
