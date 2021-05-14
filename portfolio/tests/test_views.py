from django.test import TestCase, Client
from django.urls import reverse

from portfolio.models import Project, Techno


class PortfolioTestViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.techno = Techno('Django')
        self.project = Project.objects.create(
            title='project title',
            description='project description',
            detail='project detail',
            image='image.jpg',
            url_project='url',
            url_git='url',
        )

        self.portfolio_url = reverse('portfolio-hp')
        self.project_url = reverse('project-detail', args=[self.project.id])

    def test_homepage_view(self):
        """ Test that """
        response = self.client.get(self.portfolio_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/index.html')

    def test_project_page_view(self):
        """ """
        response = self.client.get(self.project_url, {'id': self.project.id})

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/project.html')
