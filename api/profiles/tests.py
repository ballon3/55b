from django.test import TestCase
from profiles.models import MyUser
# Create your tests here.

class MyUserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        MyUser.objects.create(first='jake', last='beep')
    
    def tearDown(self):
        pass

    def test_first_name(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('first').verbose_name
        self.assertEquals(field_label, 'first')
    
    def test_last_name(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('last').verbose_name
        self.assertEquals(field_label, 'last')
    
    def test_headline(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('headline').verbose_name
        self.assertEquals(field_label, 'headline')
    
    def test_country(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('country').verbose_name
        self.assertEquals(field_label, 'country')
    
    def test_zipcode(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('zipcode').verbose_name
        self.assertEquals(field_label, 'zipcode')

    def test_industry(self):
        myuser = MyUser.objects.get(id=1)
        field_label = myuser._meta.get_field('industry').verbose_name
        self.assertEquals(field_label, 'industry')
   

          


