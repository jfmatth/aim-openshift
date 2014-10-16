from django.test import TestCase
from django.contrib.auth.models import User
 
from datetime import datetime

from aim.models import Portfolio, Symbol, Price

"""
Tests to be created:
- Portfolio Form - check for duplicates
- Holding Form - Check for valid symbols.


"""




class VTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

class CreateRecordsTests(TestCase):
    
    def setUp(self):
        self.s = Symbol(name="ABC", description="ABC Company")
        self.s.save()
        
        self.u1 = User(username="testuser1")
        self.u1.save()
    
    def tearDown(self):
        self.u1.delete()
    
    def test_create_price(self):
        # each price needs a symbol
        p = Price(symbol=self.s)
        p.volume = 100
        p.date = datetime(2010,10,14)
        p.high = 100
        p.low = 90
        p.close = 95  
        p.save()
        self.assertEquals(p.jsdate(), 1287014400000)

    def test_create_holding(self): 
        pass

    def test_create_portfolio(self):
        port1 = Portfolio()
        port1.name = "Test Portfolio 1"
        port1.owner = self.u1
        port1.permission = None 

