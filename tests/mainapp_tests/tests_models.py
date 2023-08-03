from mainapp.models import Company
from django.urls import reverse
from rest_framework import status
from  django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class CompanyTest(APITestCase):

    def setUp(self):
        user_1 = User.objects.create(
            username='AdminTest',
            password='123456789test',
            is_superuser=True,
            is_staff=True)# Cоздаём пользователя
        self.user_1_token = Token.objects.create(user=user_1)# Cоздаём токен для пользователя
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)# Принудительно авторизируем пользователя
        self.company_test_1 = Company.objects.create(
            title='Test 123',
            phones =[89004667790],
            start_date="2022-05-30T10:13:35+03:00",
            end_date="2022-05-30T12:15:35+03:00"
        )
        self.update = {
            'title':'Company for update',
            'phones':[89111111111, 8978901111, 89004567892],
        }
        self.data = {
            'title':'TestCopmany1',
            'phones':[89004667788],
            'start_date': "2022-10-30T10:23:55+03:00",
            'end_date': "2022-10-31T10:23:55+03:00" 
        }
        
    def test_company_list(self):
        #Тест на получении списка компаний
        response = self.client.get(reverse('company'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)

    def test_company_create(self):
        #Тест на создание компании
        response = self.client.post(reverse('company'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_company_create_invalid(self):
        #Тест на проверку доступа к созданию компании
        self.client.credentials()# Отправляем пустое значение токена
        response = self.client.post(reverse('company'), self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_company_detail(self):
        #Тест на получении детализации компании 
        response = self.client.get(reverse('company_detail', kwargs={'pk': self.company_test_1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_detail_invalid(self):
        #Тест на проверку отсутствия компании(404)
        response = self.client.get(reverse('company_detail', kwargs= {'pk': 15}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_company_delete(self):
        #Тест на удаление компании 
        response = self.client.delete(reverse('company_detail', kwargs={'pk': self.company_test_1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_company_update(self):
        #Тест на ре редактирования данных о компании 
        response = self.client.patch(reverse('company_detail', kwargs={'pk': self.company_test_1.id}), self.update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    
    
    