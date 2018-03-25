from django.test import TestCase, Client

# Create your tests here.

def add(num1, num2):
    return num1 + num2

class Test(TestCase):
    
    def test(self):
        self.assertIs(add(2, 2), 4)