import time, sys, os


def teks_mulai():
    print("=" * 60)
    print("+" + "="*14 + "\tSelamat datang di GwehMauJalan!\t" + "="*11 + "+")
    print("+" + "=" * 58 + "+")
    print("+" + "="*14 + "\tSilahkan Login Terlebih Dahulu\t" + "="*11 + "+")
    print("=" * 60)
    
def detik3():
    for i in range(3, 0, -1):
        print(f"Anda dapat mencoba lagi dalam {i} detik...", end="\r")
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  
    
def detik5():
    for i in range(5, 0, -1):
        print(f"Tunggu {i} detik...", end="\r")
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
