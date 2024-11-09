from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

# import class Task dari file todo/models.py
from django.contrib.auth.models import User, Group


class PenggunaForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(), required=True, label="Group"
    )
    first_name = forms.CharField(max_length=15, required=False)
    last_name = forms.CharField(max_length=15, required=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput, required=False, label="New Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput, required=False, label="Confirm New Password"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "role",
            "first_name",
            "last_name"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Mengatur widget dan label
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Jika password baru diisi, pastikan keduanya sama
        if password1 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data

    def as_div(self):
        """Metode ini digunakan untuk merender form dengan div."""
        output = []
        for field in self:
            # Mendapatkan label dan field
            output.append(f'<div class="form-group row mb-2">')
            output.append(
                f'<div class="col-sm-4"><label for="{field.id_for_label}">{field.label}</label></div>'
            )
            output.append(f'<div class="col-sm-8">{field}</div>')
            if field.errors:
                output.append('<div class="text-danger">')
                for error in field.errors:
                    output.append(f"<p>{error}</p>")
                output.append("</div>")
            output.append("</div>")
        return "\n".join(output)

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hanya set password jika password1 diisi
        password1 = self.cleaned_data.get("password1")
        if password1:
            user.set_password(password1)  # Set password baru jika diisi
        else:
            print(password1)
            # Jika password1 tidak diisi, jangan panggil set_password
            # Tidak melakukan apa-apa dengan password
        if commit:
            user.save()  # Simpan user tanpa mengubah password jika tidak ada update

            # Kosongkan grup yang ada
            user.groups.clear()
            group = self.cleaned_data.get("role")
            if group:
                user.groups.add(group)

        return user
