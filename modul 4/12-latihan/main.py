# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    # Menghitung BMI dengan rumus BMI = berat (kg) / (tinggi (m) ^ 2)
    bmi = berat / (tinggi ** 2)
    return bmi

# Meminta input dari pengguna
tinggi = float(input("Masukkan tinggi badan Anda (dalam meter): "))
berat = float(input("Masukkan berat badan Anda (dalam kg): "))

# Menghitung BMI
bmi = hitung_bmi(berat, tinggi)

# Mencetak hasil dengan format string
print(f"Skor BMI Anda adalah: {bmi:.1f}")