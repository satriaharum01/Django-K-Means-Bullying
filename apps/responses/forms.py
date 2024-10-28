from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from ..models import m_response

class ResponsesForm(ModelForm):
    class Meta:
        model = m_response
        fields = ["kuesioner", "answer"]
        labels = {
            "kuesioner": _("Kusioner:"),
            "answer": _("Jawaban:"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mengatur widget dan label
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control",'required':True})

            self.fields[field].widget.attrs.update(
                {"data-label": self.fields[field].label}
            )
        
        self.fields['kuesioner'].widget.attrs.update({"class": "form-control", 'required':True,'readonly':True})

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
