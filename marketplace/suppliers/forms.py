from django import forms


class NewSupplierForm(forms.Form):
	agree = forms.BooleanField(label='Agree to Terms', widget=forms.CheckboxInput)


# add upload signed contract