from snacks.models import Snack
from django.test import TestCase

from django.urls import reverse


class SnacksTest(TestCase):
    def test_list_page_status(self):
        #Arrange
        url = reverse('snack_list')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status(self):
        #Arrange
        url = reverse('snack_detail')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertEqual(response.status_code, 200)

    def test_list_page_templete(self):
        #Arrange
        url = reverse('snack_list')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_templete(self):
        #Arrange
        url = reverse('snack_detail')
        #Act
        response = self.client.get(url)
        #Assert
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')



