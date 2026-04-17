# fungsi cek login
def cek():
    u = input("Masukan nama: ")
    p = input("Masukan pass: ")
    
    if u == "admin":
        if p == "12345":
            print("Login Berhasil!")
            return True
        else:
            print("Password Salah!")
            return False
    else:
        print("User Tidak Ada!")
        return False

cek()