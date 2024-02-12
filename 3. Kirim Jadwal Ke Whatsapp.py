import requests
import json
import datetime
from datetime import datetime

# buat fungsi baru
def sanitize():
    # Tampung inputan didalam sebuah var
    inputan = input("Silahkan Input Tanggalnya dengan ( DD-MM-YYY ), jika hari ini maka kosongkan saja : ")
    
    # Periksa inputan apakah kosong, untuk selanjutnya diproses fungsi utama
    if inputan == False or inputan == '':
        return False
    # Terapkan blok try catch untuk menghandle apabila terjadi sebuah error
    try:
        # Pecah string dalam inputan agar bisa di parsing ke dalam gunsi date nantinya
        splitted = inputan.split("-")
        # Masukkian string yang sudah di pecah ke dalam fungsi date, apabila berhasil berarti formatnya sesuai, apabila gagal berarti format tidak sesuai
        datetime_obj = datetime.date(int(splitted[2]), int(splitted[1]), int(splitted[0]))
        # Kembalikan nilai inputannaya apabila berhasil
        return inputan

    except:
        # kembalikan string format untuk selanjutnya diproses fungsi utama
        return "format"

# Buat fungsi baru
def request_jadwal():
    
    # Menjalankan Fungsi Utk inputan
    tanggal = sanitize()
    nomor = nomor_sanitize()
    try:
        # Tampung URL untuk merequest API
        url = "https://mapi.tachyon.net.id:2443/api/coolyeah/jadwalkuliah"

        # Tampung Headersnya untuk merequest API
        headers = {
            'Content-Type': 'application/json'
        }
        
        # buat kondisi untuk pengecekkan apakah ada nilainya atau tidak dari hasil fungsi sanitasi
        if tanggal:
            
            # buat kondisi untuk pengecekkan apakah format valid atau tidak dari hasil fungsi sanitasi
            if tanggal == 'format':
                print("Format Tanggal Tidak Sesuai")
                # keluar dari fungsi, lalu mulai dari awal lagi fungsinya
                return request_jadwal()
                
            # Buat variabel baru ketika sesuai
            payload = f"tanggal={tanggal}"
            print('Sedang Mengambil Data Jadwal...')
            
            # Request ke api ketika sesuai
            response = requests.request("POST", url, headers=headers, data=payload)
        else:
            print('Sedang Mengambil Data Jadwal...')
            # Request ke api ketika sesuai
            response = requests.request("POST", url, headers=headers)
            
        # Ubah data hasil request json api agar bisa dibaca
        data = response.json()
        # Periksa responnya apakah error
        if data['code'] == 200:
            print('Data Diterima\n\n')
            # tampilkan data dari responnya
            return request_whatsapp(isi=data['data'], not_telp=nomor)
        else:
            print('Terjadi Kesalahan Dalam Mengambil Data Jadwal, Silahkan Coba Kembali!')
    # Blok except untuk menghandle ketika terjadi error pada saat request
    except requests.exceptions.RequestException as err:
        print("Error saat melakukan request:", err)
    except:
        print("Error saat melakukan request:", err)
    return


def nomor_sanitize():
    
    # Menjalankan Fungsi Utk inputan
    input_nomor = input("Masukkan nomor whatsapp (contoh: 628123456789) : ")
    
    # Memeriksa panjang input
    if len(input_nomor) <= 12:
        print('Panjang Nomor Minimal 12\n\n')
        return nomor_sanitize()
    
    # Memeriksa awalan nomor telepon
    if not input_nomor.startswith('62'):
        print('Format nomor menggunakan 62xxxxxxxxx\n\n')
        return nomor_sanitize()
    
    # Memeriksa apakah input hanya mengandung angka
    if not input_nomor.isdigit():
        print('Hanya Boleh Input Nomor\n\n')
        return nomor_sanitize()
    
    # Jika semua kriteria terpenuhi, kembalikan ke fungsi parent
    return input_nomor

# Buat fungsi baru
def request_whatsapp(isi=False, no_telp=False):
    
    pesan = isi
    nomor_telfon = no_telp
    
    try:
        
        # Tampung URL untuk merequest API
        url = "http://mid.tachyon.net.id:5001/send-message"

        # Tampung Headersnya untuk merequest API
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        
        # Buat variabel untuk tampung data request nanti
        payload = f'session=otp&to={nomor_telfon}&text={pesan}'
        
        # lakukan request untuk mengirim whatsapp
        print('Mengirim Pesan...\n\n')
        response = requests.request("POST", url, headers=headers, data=payload)
            
        # Ubah data hasil request json api agar bisa dibaca
        data = response.json()
        # Periksa responnya apakah error
        if data['data']['status'] == 1:
            print('Pesan Whatsapp Terkirim\n\n')
            
            # tampilkan data dari responnya
            print(data['data'])
            return
        else:
            print('Terjadi Kesalahan Dalam Mengirim Pesan, Silahkan Coba Kembali!\n\n')
            return
            
    # Blok except untuk menghandle ketika terjadi error pada saat request
    except requests.exceptions.RequestException as err:
        print(f"Error saat melakukan request: {err}")
        return
    except:
        print(f"Error saat melakukan request: {err}")
        return

# Panggil Fungsi utamanya
request_jadwal()