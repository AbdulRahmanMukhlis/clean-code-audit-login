# fungsi cek login
def cek(u, p):
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

# panggil fungsi
cek("admin", "123")