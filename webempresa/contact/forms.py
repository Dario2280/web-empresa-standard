from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholde': 'Escribe tu nombre'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="email", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholde': 'Escribe tu email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="contenido", required=True, widget=forms.Textarea(
       attrs={'class': 'form-control', 'rows': 4, 'placeholde': 'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)


