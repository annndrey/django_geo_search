from New.mixins import (
	LoginRequiredMixin
	)
from core.models import Activity

from .models import SupplierAccount



class SupplierAccountMixin(LoginRequiredMixin, object):
	account = None
	activities = []

	def get_account(self):
		user = self.request.user
		accounts = SupplierAccount.objects.filter(user=user)
		if accounts.exists() and accounts.count() == 1:
			self.account = accounts.first()
			return accounts.first()
		return None

	def get_activities(self):
		account = self.get_account()
		activities = Activity.objects.filter(supplier=account)
		self.activities = activities
		return activities

	# def get_transactions(self):
	# 	products = self.get_products()
	# 	transactions = Transaction.objects.filter(product__in=products)
	# 	return transactions
