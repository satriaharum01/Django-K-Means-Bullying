from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

# Decorator untuk memastikan pengguna dalam grup Admin
def admin_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and user.groups.filter(name='Admin').exists(),
        login_url='/guru/dashboard'  # Arahkan ke halaman login jika tidak memenuhi syarat
    )(view_func)
    return decorated_view_func

# Decorator untuk memastikan pengguna dalam grup Guru BK
def guru_bk_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and user.groups.filter(name='Guru BK').exists(),
        login_url='/siswa/dashboard'
    )(view_func)
    return decorated_view_func

# Decorator untuk memastikan pengguna dalam grup Siswa
def siswa_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and user.groups.filter(name='Siswa').exists(),
        login_url='/pusat/dashboard'
    )(view_func)
    return decorated_view_func
