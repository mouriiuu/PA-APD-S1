import json, inquirer, time

from pesan import *
from file_data.akun import *
from file_data.datajson import baca_data
from list_inquirer import *
from pack_admin.menu_admin import *

data = baca_data()

while True:
    teks_mulai() #<-- Ada di pesan.py
    jawab = inquirer_login() #<-- Ada di list_inquirer.py
    if jawab["list_login"] == "Login":
        role, id_akun = login_akun() #<-- Ada di akun.py
        if role == "admin":
            print("="*40) 
            print("👑 Selamat Datang, Admin! 👑") 
            print(f"ID Akun: {id_akun}") 
            print("Login Berhasil: ", time.strftime("%d %B %Y %H:%M:%S")) 
            print("="*40) 
            time.sleep(1.5)
            while True:
                jawab = menu_admin()  #<-- Ada di list_inquirer.py
                if jawab["menu_admin"][0]:
                    pass 
        elif role == "member":
            print(f"Selamat datang Member (ID: {id_akun})!")
            
    elif jawab["list_login"] == "Registrasi":
        registrasi()  #<-- Ada di akun.py
    
    elif jawab["list_login"] == "Keluar":
        print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
