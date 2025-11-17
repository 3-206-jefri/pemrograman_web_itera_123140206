Data_mahasiswa = [
    {
        "nama": "Jefri",
        "nim": "123140206",
        "nilai_tugas": 85,
        "nilai_uts": 90,
        "nilai_uas": 88
    },
    {
        "nama": "Siti",
        "nim": "123140137",
        "nilai_tugas": 78,
        "nilai_uts": 82,
        "nilai_uas": 80
    },
    {
        "nama": "Budi",
        "nim": "123140123",
        "nilai_tugas": 92,
        "nilai_uts": 88,
        "nilai_uas": 91
    },
    {
        "nama": "Ani",
        "nim": "123140105",
        "nilai_tugas": 70,
        "nilai_uts": 75,
        "nilai_uas": 72
    },
    {
        "nama": "Andi",
        "nim": "123140210",
        "nilai_tugas": 80,
        "nilai_uts": 85,
        "nilai_uas": 83
    }
]

def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    """Menghitung nilai akhir dengan bobot: 30% UTS, 40% UAS, 30% Tugas"""
    return 0.3 * nilai_uts + 0.40 * nilai_uas + 0.30 * nilai_tugas

def grade_nilai(nilai_akhir):
    """Menentukan grade berdasarkan nilai akhir"""
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 55:
        return 'C'
    elif nilai_akhir >= 40:
        return 'D'
    else:
        return 'E'

def input_data_mahasiswa():
    """Input data mahasiswa baru dengan validasi"""
    try:
        print("\n" + "="*50)
        print(" TAMBAH DATA MAHASISWA BARU")
        print("="*50)
        
        nama = input("Masukkan Nama Mahasiswa: ").strip()
        if not nama:
            print(" Nama tidak boleh kosong!")
            return
        
        nim = input("Masukkan NIM Mahasiswa: ").strip()
        if not nim:
            print(" NIM tidak boleh kosong!")
            return
        
        # Cek NIM duplikat
        for mahasiswa in Data_mahasiswa:
            if mahasiswa['nim'] == nim:
                print(f" NIM {nim} sudah terdaftar!")
                return
        
        nilai_tugas = int(input("Masukkan Nilai Tugas (0-100): "))
        nilai_uts = int(input("Masukkan Nilai UTS (0-100): "))
        nilai_uas = int(input("Masukkan Nilai UAS (0-100): "))
        
        # Validasi nilai
        if not (0 <= nilai_tugas <= 100 and 0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100):
            print(" Nilai harus berada di antara 0-100!")
            return
        
        mahasiswa_baru = {
            "nama": nama,
            "nim": nim,
            "nilai_tugas": nilai_tugas,
            "nilai_uts": nilai_uts,
            "nilai_uas": nilai_uas
        }
        
        Data_mahasiswa.append(mahasiswa_baru)
        print(f" Data mahasiswa {nama} berhasil ditambahkan!\n")
        
    except ValueError:
        print(" Input nilai tidak valid! Harus berupa angka.")

def filter_grade_mahasiswa(data_mahasiswa, grade):
    """Filter mahasiswa berdasarkan grade tertentu"""
    filtered_mahasiswa = []
    for mahasiswa in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(
            mahasiswa["nilai_tugas"], 
            mahasiswa["nilai_uts"], 
            mahasiswa["nilai_uas"]
        )
        if grade_nilai(nilai_akhir) == grade:
            filtered_mahasiswa.append(mahasiswa)
    
    # PERBAIKAN: Return list nama mahasiswa, bukan .nama
    return [mhs['nama'] for mhs in filtered_mahasiswa]

def rata_ratakelas(data_mahasiswa):
    """Menghitung rata-rata nilai akhir kelas"""
    if not data_mahasiswa:
        return 0
    
    total_nilai_akhir = 0
    for mahasiswa in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(
            mahasiswa["nilai_tugas"], 
            mahasiswa["nilai_uts"], 
            mahasiswa["nilai_uas"]
        )
        total_nilai_akhir += nilai_akhir
    
    rata_rata = total_nilai_akhir / len(data_mahasiswa)
    return round(rata_rata, 2)

def min_max(data_mahasiswa):
    """Mencari nilai tertinggi dan terendah beserta nama mahasiswanya"""
    if not data_mahasiswa:
        return None, None, None, None
    
    nilai_data = []
    for mahasiswa in data_mahasiswa:
        nilai = hitung_nilai_akhir(
            mahasiswa["nilai_tugas"], 
            mahasiswa["nilai_uts"], 
            mahasiswa["nilai_uas"]
        )
        nilai_data.append({
            'nama': mahasiswa['nama'],
            'nilai': nilai
        })
    
    # Cari nilai minimum dan maksimum
    min_data = min(nilai_data, key=lambda x: x['nilai'])
    max_data = max(nilai_data, key=lambda x: x['nilai'])
    
    return min_data['nama'], min_data['nilai'], max_data['nama'], max_data['nilai']

def tampilkan_data_mahasiswa(data_mahasiswa):
    """Menampilkan data mahasiswa dalam format tabel"""
    if not data_mahasiswa:
        print("\n Tidak ada data mahasiswa!")
        return
    
    print("\n" + "="*85)
    print("| No |     Nama     |    NIM     | Tugas |  UTS  |  UAS  | Akhir | Grade |")
    print("="*85)
    
    for index, mahasiswa in enumerate(data_mahasiswa, start=1):
        nilai_akhir = hitung_nilai_akhir(
            mahasiswa["nilai_tugas"], 
            mahasiswa["nilai_uts"], 
            mahasiswa["nilai_uas"]
        )
        grade = grade_nilai(nilai_akhir)
        print(f"| {index:2} | {mahasiswa['nama']:^12} | {mahasiswa['nim']:^10} | "
              f" {mahasiswa['nilai_tugas']:>3}   |  {mahasiswa['nilai_uts']:>3}  | "
              f" {mahasiswa['nilai_uas']:>3}   | {nilai_akhir:>5.2f} |   {grade:^3}   |")
    
    print("="*85)

def main():
    print(" SISTEM PENGELOLAAN DATA NILAI MAHASISWA")
    print("="*85)
    
    # Input data mahasiswa baru
    input_data_mahasiswa()
    
    # Tampilkan semua data mahasiswa
    tampilkan_data_mahasiswa(Data_mahasiswa)
    
    # Rata-rata nilai kelas
    rata_rata = rata_ratakelas(Data_mahasiswa)
    print(f"\n Rata-rata Nilai Kelas: {rata_rata}")
    
    # Filter mahasiswa dengan grade A
    mahasiswa_grade_a = filter_grade_mahasiswa(Data_mahasiswa, 'A')
    if mahasiswa_grade_a:
        print(f" Mahasiswa Dengan Grade A: {', '.join(mahasiswa_grade_a)}")
    else:
        print(" Mahasiswa Dengan Grade A: Tidak ada")
    
    # Nilai tertinggi dan terendah
    nama_min, nilai_min, nama_max, nilai_max = min_max(Data_mahasiswa)
    if nama_min and nama_max:
        print(f"\nNilai Terendah  : {nilai_min:.2f} ({nama_min})")
        print(f" Nilai Tertinggi : {nilai_max:.2f} ({nama_max})")
    
    print("\n" + "="*85)
    print(" Program selesai dijalankan!")

if __name__ == "__main__":
    main()