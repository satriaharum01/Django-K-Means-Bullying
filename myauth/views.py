from django.views import View
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Template login yang digunakan
    redirect_authenticated_user = True  # Arahkan pengguna yang sudah login

    def form_valid(self, form):
        # Proses login pengguna
        user = form.get_user()
        login(self.request, user)

        # Pengalihan berdasarkan grup
        if user.groups.filter(name='Admin').exists():
            return redirect('pusat/dashboard')  # Ubah sesuai URL name dashboard admin
        elif user.groups.filter(name='Guru BK').exists():
            return redirect('guru/dashboard')  # Ubah sesuai URL name dashboard guru BK
        elif user.groups.filter(name='Siswa').exists():
            return redirect('siswa/dashboard')  # Ubah sesuai URL name dashboard siswa
        
        # Jika tidak ada grup yang sesuai
        return redirect('pusat/dashboard')  # Ubah sesuai URL name dashboard default
 
class HomeView(View):
    template_name = 'accounts/home.html'

    def get(self, request):
        return render(request, self.template_name)
    
    
class CustomLogoutView(LogoutView):
    template_name = 'accounts/login.html'
    next_page = 'login'
