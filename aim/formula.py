from decimal import Decimal

class AimStandard(object):

    def __init__(self):
        self.started = False

        self.control = 0
        self.buymin =  500
        self.buysafe = 10 
        self.sellmin = 500
        self.sellsafe = 10


    def transaction(self, amount = 0):
        if amount > 0:
            if not self.started:
                # we can assume a control of 0 means its not started ?
                # if so, then start control at the total sale price.
                self.control += amount
            else:
                # otherwise we only add 1/2 to the control
                self.control += amount / 2

        self.started = True


    def BuyPrice(self, shares=0, value=0):
        if self.control <> 0:
            # JFM, 5/3/2010 - Just realized that the above formula is WRONG!  All these years!
            #
            # below is the new formula from the aim-users website (http://aim-users.com/aimbrief.htm)
            
            # JFM, account for the minimum amount field too.
            bm = value * (self.buysafe / Decimal(100) )
            
            # JFM, account for minimum amounts.
            bm = max(bm, self.buymin) 
            
            pc = Decimal(self.control)
            N  = Decimal(shares)
            bs = Decimal(self.buysafe) / Decimal(100)
                
            return (pc - bm) / (N * ( Decimal(1) + bs) )
                    
        else:
            return Decimal(0)


    def BuyAmount(self, value = 0):
        # Normal AIM formula for buy amount is
        #
        # PC - (Current Value + (Safe * Current value) )
        #
        amount = self.control - (value + (self.buysafe / Decimal(100) * value ) )
        if amount > 0:
            return abs(amount)
        else:
            return 0            


    def SellPrice(self, shares = 0, value = 0):
        if self.control <> 0 and shares > 0:
            # JFM, 6/17/10, account for minimums too.
            sm = value * (self.sellsafe / Decimal(100) )
            sm = max(sm, self.sellmin)
            
            pc = Decimal(self.control)
            N  = Decimal(shares)
            ss = Decimal(self.sellsafe / Decimal(100) )
            
            return (pc + sm) / (N * ( Decimal(1) - ss) )
        else:
            return Decimal(0)

                    
    def SellAmount(self, value = 0):
        # Normal AIM formula for sell amount is
        #
        #  PC + (Safe * Current value) - Current Value
        #
        amount = self.control + (self.sellsafe / Decimal(100) * value ) - value

        if amount < 0 :
            return abs(amount)
        else:
            return 0



class Holding(object):
    '''
    
    a = AimStandard()
    h = Holding(a)
    h.cash = 10000
    
    p0 = pricelist[0]
    h.buy(5000/p0)
    
    for p in pricelist:
        h.setprice(p)
    
    '''
    
    def __init__(self, aiminstance):
        self.shares = 0         # how many shares do we own.
        self.value = 0      # how much are we worth.
        self.price = 0      # current price of holding
        self.cash = 0

        self.aim =  aiminstance

    def buy(self, shares = 0, amount = 0):
        self.shares += shares
        self.value += amount
        
        self.aim.transaction(amount)
    
    def sell(self, shares = 0, amount = 0):
        self.shares -= shares
        self.value -= amount
        
    def setprice(self, price=0):
        self.price = price
        self.action()
    
    def action(self):
        # determine if there is any action to take
        
        # check buys
        if self.price <= self.aim.BuyPrice(self.shares, self.value) and self.aim.BuyAmount(self.value) > 0:
            # make sure we have enough cash too.
            print "Buy %s" % aim.BuyAmount(self.value)
            self.buy(self.aim.BuyAmount(self.value) / self.price, self.aim.BuyAmount(self.value) ) 
            return
        
        # check sell's
        if self.price >= self.aim.SellPrice(self.shares, self.value) and self.aim.SellAmount(self.value) > 0:
            print "Sell %s" % aim.SellAmount(self.value)
            self.sell(self.aim.SellAmount(self.value) / self.price, self.aim.SellAmount(self.value) )
            return


# 
# class AimBase(models.Model):
#     holding   = models.OneToOneField(Holding, related_name="controller")
# 
#     started   = models.BooleanField(default=False)                   # is the program started?
#     control   = models.IntegerField(default=0)           # Portfolio Control
#     sellsafe  = models.IntegerField(default=10)          # SAFE for sales, a percentage value
#     buysafe   = models.IntegerField(default=10)          # SAFE for buys
#     buymin    = models.IntegerField(default=500)         # Minimum to buy
#     sellmin   = models.IntegerField(default=500)         # Minimum to sell in a transaction
#             
#     # Holy Shit! I just figure out the forumla I've been using hasn't been right, and missed these figures
#     # they are the percentage of value to buy / sell each time, instead of the fixed values above (buyin/sellmin).
#     # Crap!
#     buyperc    = models.IntegerField(default=10)          # how much percent of value to buy
#     sellperc   = models.IntegerField(default=10)          # how much percent of value to sell 
#     
#     def __unicode__(self):
#         return "Base class for Aim"
#     
#     def BuyPrice(self):
#         return Decimal(0)
#     def SellPrice(self):
#         return Decimal(0)
# 
#     def BuyAmount(self):
#         return Decimal(0)
#     def SellAmount(self):
#         return Decimal(0)
#             
#     def transaction(self, transaction=None):
#         return Decimal(0)
#         
#     class Meta:
#         abstract = True
#     
# 
# 
# 
# class AimController(AimBase):
#     def BuyPrice(self):
#         if self.control <> 0:
#             # JFM, 5/3/2010 - Just realized that the above formula is WRONG!  All these years!
#             #
#             # below is the new formula from the aim-users website (http://aim-users.com/aimbrief.htm)
#             
#             # JFM, account for the minimum amount field too.
#             bm = self.holding.value() * (self.buyperc / Decimal(100) )
#             # JFM, account for minimum amounts.
#             bm = max(bm, self.buymin) 
#             
#             pc = Decimal(self.control)
#             N  = Decimal(self.holding.shares())
# #             ss = Decimal(self.sellsafe) / Decimal(100)
#             bs = Decimal(self.buysafe) / Decimal(100)
#                 
#             return (pc - bm) / (N * ( Decimal(1) + bs) )
#                     
#         else:
#             return Decimal(0)
# 
#     def BuyAmount(self):
#         # Normal AIM formula for buy amount is
#         #
#         # PC - (Current Value + (Safe * Current value) )
#         #
#         amount = self.control - (self.holding.value() + (self.buysafe / Decimal(100) * self.holding.value()) )
#         if amount > 0:
#             return abs(amount)
#         else:
#             return 0            
#                     
#     def SellPrice(self):                
#         if self.control <> 0:
#             # JFM, 6/17/10, account for minimums too.
#             sm = self.holding.value() * (self.sellperc / Decimal(100) )
#             sm = max(sm, self.sellmin)
#             
#             pc = Decimal(self.control)
#             N  = Decimal(self.holding.shares() )
#             ss = Decimal(self.sellsafe) / Decimal(100)
# #             bs = Decimal(self.buysafe) / Decimal(100)
#             
#             return (pc + sm) / (N * ( Decimal(1) - ss) )
#         else:
#             return Decimal(0)
#                     
#     def SellAmount(self):
#         # Normal AIM formula for sell amount is
#         #
#         #  PC + (Safe * Current value) - Current Value
#         #
#         amount = self.control + (self.sellsafe / Decimal(100) * self.holding.value() ) - self.holding.value()
#         if amount < 0 :
#             return abs(amount)
#         else:
#             return 0
# 
# 
#     def transaction(self, transaction=None):
#         if transaction.total_sale() > 0:
#             if not self.started:
#                     # we can assume a control of 0 means its not started ?
#                     # if so, then start control at the total sale price.
#                     self.control += transaction.total_sale()
#             else:
#                     # otherwise we only add 1/2 to the control
#                     self.control += transaction.total_sale() / 2
#                     
#             self.started = True
#             self.save(from_trans=True)
#         
#             # now add a holding alert for the new transaction.
#         HoldingAlert(holding=self.holding, date=transaction.date).save()
# 
# 
#     def save(self, force_insert=False, force_update=False, from_trans=False):
#         if not from_trans and not self.id==None:
#             # if we are editing the controller settings, we should make a new alert, 
#             # and set the date to today.
#             HoldingAlert(holding=self.holding, date=datetime.datetime.today() ).save()
# 
#         super(AimController, self).save(force_insert, force_update)
#         
# 
#     def __unicode__(self):
#         return "%s (%s)" % (self.holding, self.control)
