import webview
import threading
import os
import sys
import signal
import time


# Flag untuk menghentikan thread
stop_thread = False

# Fungsi untuk menjalankan Django server
def run_django(stop_thread):
    while True:
        os.system("python manage.py runserver")
        print('thread running')
        if stop_thread():
            break


# Fungsi untuk menghentikan Django server
def stop_django():
    print("WebView ditutup, menghentikan server Django...")
    print("exit")
    os.kill(os.getpid(), signal.SIGBREAK)


# Menjalankan server Django di thread terpisah
django_thread = threading.Thread(target=run_django, args=(lambda: stop_thread,))
django_thread.start()

print("My PID is:", os.getpid())
window = webview.create_window("PT.BBN", "http://127.0.0.1:8000/", confirm_close=True)
# Mulai WebView
window.events.closed += stop_django

webview.start()
