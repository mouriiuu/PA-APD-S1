import inquirer

def inquirer_login():
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print(f"{YELLOW}{'-'*50}{RESET}")
    print(f"{CYAN}{BOLD}")
    print("╔══════════════════════════════════════════════╗")
    print("║               MAPS TRAVEL APP                ║")
    print("╚══════════════════════════════════════════════╝")
    print("         📍 Jelajahi perjalananmu sekarang       ")
    print(RESET)
    print(f"{YELLOW}{'-'*50}{RESET}")

    login = [
        inquirer.List("list_login",
                    message="Pilih Menu Yang Tersedia...",
                    choices=[
                        "Login",
                        "Registrasi",
                        "Keluar"
                        ]
                    )
                        
    ]
    jawab = inquirer.prompt(login)
    return jawab
    
    

