from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import RedirectView
from .models import SupplierAccount
from core.models import Activity
from django.shortcuts import get_object_or_404


from New.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from .mixins import (
	SupplierAccountMixin
	)

from .forms import NewSupplierForm

# Create your views here.
class SupplierActivityDetailRedirectView(RedirectView):
    permanent = True
    def get_redirect_url(self, *args, **kwargs):
        obj = get_object_or_404(Activity, pk=kwargs['pk'])
        return obj.get_absolute_url()




class SupplierDashboard(SupplierAccountMixin, FormMixin, View):
	form_class = NewSupplierForm
	success_url = "/supplier/"

	def post(self, request, *args, **kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get(self, request, *args, **kwargs):
		apply_form = self.get_form() 
		account = self.get_account()
		exists = account
		active = None
		context = {}
		if exists:
			active = account.active
		if not exists and not active:
			context["title"] = "Apply for Account"
			context["apply_form"] = apply_form
		elif exists and not active:
			context["title"] = "Account Pending"
		elif exists and active:
			context["title"] = "Supplier Dashboard"
			# activities = Activity.objects.filter(supplier=account)
			context["activities"] = self.get_activities()
		else:
			pass
		
		return render(request, "supplier/dashboard.html", context)

	def form_valid(self, form):
		valid_data = super(SupplierDashboard, self).form_valid(form)
		obj = SupplierAccount.objects.create(user=self.request.user)
		return valid_data

