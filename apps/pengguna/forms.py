from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from django.contrib.auth.models import User,Group

class PenggunaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ModelChoiceField(queryset=Group.objects.all(),required=True,label="Group")
    first_name = forms.CharField(max_length=15, required=False)
    last_name = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'first_name', 'last_name', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mengatur widget dan label
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control",'required':True})

    def as_div(self):
        """Metode ini digunakan untuk merender form dengan div."""
        output = []
        for field in self:
            # Mendapatkan label dan field
            output.append(f'<div class="form-group row mb-2">')
            output.append(f'<div class="col-sm-4"><label for="{field.id_for_label}">{field.label}</label></div>')
            output.append(f'<div class="col-sm-8">{field}</div>')
            if field.errors:
                output.append('<div class="text-danger">')
                for error in field.errors:
                    output.append(f'<p>{error}</p>')
                output.append('</div>')
            output.append('</div>')
        return "\n".join(output)
    
    def save(self, commit=True):
        # Simpan user tanpa grup terlebih dahulu
        user = super().save(commit=False)
        #user.set_unusable_password()  # atau setel password, jika perlu
        if commit:
            user.save()
            # Tambahkan user ke grup yang dipilih
            group = self.cleaned_data.get('role')
            if group:
                user.groups.add(group)
        return user
    