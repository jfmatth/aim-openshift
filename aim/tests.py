from django.test import TestCase

from aim.models import Holding, Portfolio, Symbol, Price
from users.models import User

import datetime

class AlertsTestCase(TestCase):
    
#    fixtures = ['test-portfolio.json', 'test-user.json', 'test-symbol.json', 'test-holding.json']
   
    def setUp(self):
        u = User.objects.create(email="testuser@test.com")
        p = Portfolio.objects.create(name="Test Portfolio",owner = u)
        
        s1 = Symbol.objects.create(name="ABC", description = "Company ABC")
        Price.objects.create(symbol = s1, date = datetime.date(2014,1,1), high=100,low=80, close=90, volume =1000 )
        
        s2 = Symbol.objects.create(name="XYZ", description = "Company XYZ")
        
        Holding.objects.create(portfolio = p, symbol = s1, reason = "Holding 1")
        Holding.objects.create(portfolio = p, symbol = s2, reason = "Holding 2")
        
    
        
    
        