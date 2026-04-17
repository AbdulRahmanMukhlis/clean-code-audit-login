# Konstanta untuk kredensial
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

def is_login_authorized(username, password):
    """Fungsi murni untuk validasi logika (tanpa print/input)."""
    if username != VALID_USERNAME:
        return False, "User tidak ditemukan!"
    
    if password != VALID_PASSWORD:
        return False, "Password salah!"
        
    return True, "Selamat datang, Login berhasil!"

def main():
    """Fungsi utama untuk menangani Input dan Output (I/O)."""
    print("=== Sistem Login Keamanan ===")
    
    # Mengambil input dari pengguna
    username_input = input("Username: ")
    password_input = input("Password: ")
    
    # Memanggil fungsi validasi
    is_success, message = is_login_authorized(username_input, password_input)
    
    print(message)

if __name__ == "__main__":
    main()