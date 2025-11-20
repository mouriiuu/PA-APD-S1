import inquirer
import os
from review import review

def menu_login() -> None:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(f"User: {user_login}")
        print("=" * 60)
        
        pertanyaan = [
            inquirer.List('pertanyaan',
                         message="apakah anda ingin memberikan review?",
                         choices=[
                             'iya, saya ingin memberikan review',
                             'tidak'
                         ],
                         ),
        ]
        
        jawaban = inquirer.prompt(pertanyaan)
          
        if jawaban['pertanyaan'] == 'iya, saya ingin memberikan review':
            review()
        elif jawaban['pertanyaan'] == 'tidak':
            if Menu_utama():
                break

   


if __name__ == "__main__":
    Menu_utama()