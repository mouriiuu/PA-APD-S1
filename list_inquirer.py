import inquirer

def inquirer_login():
    login = [
        inquirer.List("list_login",
                    message="Pilih menu",
                    choices=[
                        "Login",
                        "Registrasi",
                        "Keluar"
                        ]
                    )
                        
    ]
    jawab = inquirer.prompt(login)
    return jawab
    
    
def menu_admin():
    menu_awal = [
        inquirer.List("admin_menu",
                      message = "Pilih Salah Satu Menu Yang Tersedia",
                      choices = [
                          "1. Membuat Rute Perjalanan Baru",
                          "2. Melihat Semua Rute Perjalanan",
                          "3. Menghapus Rute Perjalanan",
                          "4. Melihat dan Menangani Laporan Pengguna Tentng Rute",
                          "5. Melihat dan Menghapus Review Pengguna",
                          "6. Mengelola Akun Pengguna",
                          "7. Logout"
                      ]
                    )   
    ]
    jawab =inquirer.prompt(menu_awal)