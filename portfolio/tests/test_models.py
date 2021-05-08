from django.test import TestCase

from portfolio.models import Project, Techno


class PortfolioModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            title='Projet test',
            description='Description du projet qui peut prendre pas mal de mots, en tout cas plus que 255 caractères.',
            image='path/image.jpg',
            url_project='http://',
            url_git='http://',
        )
        # créer une création de tag

    def test_title_label_and_max_length(self):
        '''
        I test if the nama label and the max length are correct
        '''
        project = Project.objects.get(title='Projet test')

        field_label = project._meta.get_field('title').verbose_name
        max_length = project._meta.get_field('title').max_length

        self.assertEquals(field_label, 'title')
        self.assertEquals(max_length, 250)
