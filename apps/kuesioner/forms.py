from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from ..models import m_kuesioner


class DivWidget(forms.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Membuat div pembungkus untuk widget
        attrs = attrs or {}
        div_start = '<div class="col-sm-8">'
        div_end = "</div>"
        # Memanggil super untuk mendapatkan HTML dari field
        input_html = super().render(name, value, attrs=attrs, renderer=renderer)

        # Mengembalikan HTML yang diinginkan
        return f"{div_start}{input_html}{div_end}"

class KuesionerForm(ModelForm):
    class Meta:
        model = m_kuesioner
        fields = ["question_text", "question_type"]
        labels = {
            "question_text": _("Kusioner:"),
            "question_type": _("Kategori Bullying:"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mengatur widget dan label
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

            self.fields[field].widget.attrs.update(
                {"data-label": self.fields[field].label}
            )

    def as_div(self):
        """Metode ini digunakan untuk merender form dengan div."""
        output = []
        for field in self:
            # Mendapatkan label dan field
            label = field.label_tag()  # Mendapatkan label sebagai HTML
            output.append(
                f'<div class="form-group row mb-2"><div class="col-sm-4">{label}</div><div class="col-sm-8">{field}</div></div>'
            )
        return "\n".join(output)

    # Menambahkan label dan widget untuk memformat input
    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    # Mengatur widget dan label
    #    for field in self.fields:
    #        self.fields[field].widget.attrs.update({'class': 'form-control'})


#
#        # Membuat label dengan struktur div
#        self.fields[field].label = f'<div class="col-sm-4">{self.fields[field].label}</div>'
#        self.fields[field].widget.attrs.update({'data-label': self.fields[field].label})
#
#    #self.fields['question_text'].widget = DivWidget(attrs={
#    #    'class': 'form-control',
#    #    'required': True,
#    #})
#    #self.fields['question_type'].widget = DivWidget(attrs={
#    #    'class': 'form-control',
#    #    'required': True,
#    #})
#
#    #self.fields['question_text'].labels = f'<div class="col-sm-4">{self.fields[question_text].label}</div>'
#    #self.fields['question_type'].labels = f'<div class="col-sm-4">{self.fields[question_type].label}</div>'
#
# def as_div(self):
#    """Metode ini digunakan untuk merender form dengan div."""
#    output = []
#    for field in self:
#        # Mendapatkan label dan field
#        label = field.label_tag()  # Mendapatkan label sebagai HTML
#        output.append(f'<div class="form-group row mb-2">{label}<div class="col-sm-8">{field}</div></div>')
#    return '\n'.join(output)
