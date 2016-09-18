from django import forms
from davyhome.models import Tyre, PriceRange


def brand_choices():
    choices = [('', 'Tyre Brand')] + list(set([(str(tyre.brand), str(tyre.brand)) for tyre in Tyre.objects.all()]))
    return choices


def price_choices():
    prices = [('', 'Price Range')] + list(set([('{}-{}'.format(price_range.min_price,
                                          price_range.max_price), '${} - ${}'.format(price_range.min_price,
                                          price_range.max_price)) for price_range in PriceRange.objects.all()]))
    return prices


def type_choices():
    choices = [('', 'Vehicle Type')] + list(set([(str(tyre.type), str(tyre.type)) for tyre in Tyre.objects.all()]))
    return choices


def category_choices():
    choices = [('', 'Tyre Category')] + list(set([(str(tyre.category),
                                                   str(tyre.category)) for tyre in Tyre.objects.all()]))
    return choices


class TyreForm(forms.Form):
    width = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tyre Width', 'class': 'tyre-form-text'}),
                            label='')
    profile = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tyre Profile', 'class': 'tyre-form-text'}),
                              label='')
    size = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tyre Size', 'class': 'tyre-form-text'}),
                           label='')
    speed = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tyre Speed', 'class': 'tyre-form-text'}),
                            label='')
    brand = forms.ChoiceField(widget=forms.Select(attrs={'class': 'tyre-form-select'}), choices=brand_choices(),
                              label='')
    type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'tyre-form-select'}), choices=type_choices(),
                             label='')
    price = forms.ChoiceField(widget=forms.Select(attrs={'class': 'tyre-form-select'}), choices=price_choices(),
                              label='')
    category = forms.ChoiceField(widget=forms.Select(attrs={'class': 'tyre-form-select'}), choices=category_choices(),
                                 label='')

    def submit(self):
        pass
        # Perform search
