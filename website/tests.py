from django.test import TestCase
from django.urls import reverse
class WebsiteTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Confidence in every")
        self.assertContains(response, "£112")
        self.assertContains(response, "£168")
        self.assertContains(response, "Impact resistance")
        self.assertContains(response, "+£31")
        self.assertContains(response, "+£51")
        self.assertContains(response, "EN ISO 12312-1:2022")
        self.assertContains(response, "ANSI Z80.3-2018")
    def test_contact_page(self):
        self.assertEqual(self.client.get(reverse("contact")).status_code, 200)
