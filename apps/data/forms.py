from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from ..models import m_data


# membuat class TaskForm untuk membuat task
class DataForm(ModelForm):
    class Meta:
        # merelasikan form dengan model
        model = m_data
        # mengeset field apa saja yang akan ditampilkan pada form
        fields = ('ekspor','jumlah','periode')
        # mengatur teks label untuk setiap field
        
        # mengatur teks pesan error untuk setiap validasi fieldnya
        error_messages = {
            'nama_media': {
                'required': _("Nama Media harus diisi."),
            }
        }
