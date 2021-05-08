from django.test import TestCase, Client
from django.urls import reverse


class PortfolioTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.portfolio_url = reverse('portfolio-hp')

    def test_homepage_view(self):
        """ Test that """
        response = self.client.get(self.portfolio_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')
