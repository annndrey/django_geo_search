from django.http import Http404
from Accounts.models import User

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from suppliers.mixins import (
	SupplierAccountMixin
	)



class ProductManagerMixin(SupplierAccountMixin, object):
	def get_object(self, *args, **kwargs):
		supplier = self.get_account()
		obj = super(ProductManagerMixin, self).get_object(*args, **kwargs)
		try:
			obj.supplier  == supplier
		except:
			raise Http404

		if obj.supplier == supplier:
			return obj
		else:
			raise Http404

