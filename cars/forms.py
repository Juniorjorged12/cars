from django import forms
from cars.models import Car, Brand

class CarForm(forms.Form):
        name = forms.CharField(max_length=100)
        brand = forms.ModelChoiceField(queryset=Brand.objects.all())
        year = forms.IntegerField(required=False)
        model_year = forms.IntegerField(required=False)
        price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
        plate = forms.CharField(max_length=20, required=False)
        photo = forms.ImageField(required=False)
        bio = forms.CharField(widget=forms.Textarea, required=False)

        def save(self):
                car = Car(
                        name=self.cleaned_data['name'],
                        brand=self.cleaned_data['brand'],
                        year=self.cleaned_data.get('year'),
                        model_year=self.cleaned_data.get('model_year'),
                        price=self.cleaned_data.get('price'),
                        plate=self.cleaned_data.get('plate'),
                        photo=self.cleaned_data.get('photo'),
                        bio=self.cleaned_data.get('bio')
                )
                car.save()
                return car


class CarModelForm(forms.ModelForm):
        class Meta:
                model = Car
                fields = ['name', 'brand', 'year', 'model_year', 'price', 'plate', 'photo', 'bio']

        def clean_price(self):
                price = self.cleaned_data.get('price')
                if price is not None and price < 0:
                        raise forms.ValidationError("O valor nao pode ser negativo.")
                return price

        def clean_year(self):
                year = self.cleaned_data.get('year')
                if year is not None and (year < 2000 or year > 2100):
                        raise forms.ValidationError("Ano invalido.")
                return year

