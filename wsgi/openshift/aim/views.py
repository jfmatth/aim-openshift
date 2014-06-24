from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

from aim.forms import PortfolioForm, ControlForm, HoldingForm, TransactionForm

from aim.models import Portfolio, Holding, Symbol, Transaction, AimController

#===============================================================================
# MainView for /aim
#===============================================================================
class MainView(ListView):
    """
    This is the main screen a logged in user sees for all their holdings and portfolios.
    """
    template_name = "aim/MainView.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return Portfolio.objects.filter(owner=self.request.user)




#===============================================================================
# Portofolio's
#===============================================================================
class PortfolioUpdate(UpdateView):
    model = Portfolio
    success_url = "/aim/"
    form_class = PortfolioForm

    def get_queryset(self):
        # return only the records that we are allowed to see
        return Portfolio.objects.filter(owner = self.request.user)

class PortfolioCreate(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    
    success_url = "/aim/"

    def get_form(self, form_class):
        # Since we don't show the owner field, take it from the user
        # requesting to add this portfolio.
        form = super(PortfolioCreate,self).get_form(form_class)
        form.instance.owner = self.request.user
        return form



#===============================================================================
# Holding
#===============================================================================
class HoldingCreateView(CreateView):
    model = Holding
    form_class = HoldingForm
    success_url = "/aim/"
    template_name = "aim/HoldingView.html"

    portfolio = None

    def get_form(self, form_class):
        form = super(HoldingCreateView, self).get_form(form_class)
        
        portfolio = Portfolio.objects.get(pk=self.kwargs['portid'])
        if portfolio.owner != self.request.user:
            raise ObjectDoesNotExist
        
        form.instance.portfolio = portfolio 
       
#         # setup the available portfolios and the inital value if any for this holding
#         form.fields['portfolio'].queryset = Portfolio.objects.filter(owner=self.request.user)
#         form.fields['portfolio'].initial = self.kwargs.get("portid", None)
#         
        return form
    
    
class HoldingUpdateView(UpdateView):
    template_name = "aim/HoldingView.html"
    #form_class = HoldingForm
    model = Holding
    success_url = "/aim/"
    
        
    def get_initial(self):
        # setup the symbol, otherwise it will show the FK id instead.
        initial = super(HoldingUpdateView, self).get_initial()
        initial.update( {'symbol':self.object.symbol} )
        
        return initial

    def get_queryset(self):
        # return only the records that we are allowed to see
        return Holding.objects.filter(portfolio__owner = self.request.user)

    def get_form_kwargs(self):
        kwargs = super(HoldingUpdateView,self).get_form_kwargs()

        # if we are POSTing a control button, then return the control object, 
        # otherwise treat it as a holding object.        
        if "_control" in self.request.POST:
            kwargs.update({'instance': self.object.controller})
        else:
            kwargs.update({'instance': self.object})

        return kwargs

    def get_context_data(self, **kwargs):
        cd = super(HoldingUpdateView, self).get_context_data(**kwargs)
        
        cd['controlform'] = ControlForm(instance = self.object.controller)
        
        return cd
    
    def get_form_class(self):
        # this line is the same as specifying the form_class as a  
        # class variable.
        if self.request.method == "GET":
            return HoldingForm
        
        # if we are posting, figure out if we hit the submit button on the holding form
        # or the control form.
        if "_holding" in self.request.POST:
            return HoldingForm
        else:
            if "_control" in self.request.POST:
                return ControlForm
            else:
                return super(HoldingUpdateView,self).get_form_class()


#===============================================================================
# Transaction
#===============================================================================
class TransactionCreate(CreateView):
    model = Transaction
    form_class = TransactionForm
    success_url = "/aim/"

    type = None

#     def get_queryset(self):
#         return Transaction.objects.filter(holding__portfolio__owner = self.request.user)

    def get_form(self, form_class):
        form = super(TransactionCreate, self).get_form(form_class)
        holding = Holding.objects.get(pk=self.kwargs['holding_id'])

        if holding.portfolio.owner != self.request.user:
            raise

        form.instance.holding = holding

        return form

    def form_valid(self, form):
        form = super(TransactionCreate,self).form_valid(form)

        return form

    def get_initial(self):
        # we get the type of transaction from the URLconf as a named parameter.
        self.initial['type'] = self.type
        
        return super(TransactionCreate,self).get_initial()



class PriceView(TemplateView):
    template_name = "chartview.html"
    
    
    