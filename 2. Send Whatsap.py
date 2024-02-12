import requests
import json
import datetime
from datetime import datetime

# buat fungsi baru
def pesan_sanitize():
    
    # Menjalankan Fungsi Utk inputan
    isipesan = input("Silahkan Input Pesan Whatsappnya : ")
    
    # Periksa inputan apakah kosong, atau pesannya kurang dari 5
    if isipesan == False or isipesan == '' or len(isipesan) < 5:
        print("Masukkan pesan yang valid")
        
        # kembalikan ke fungsinya lagi
        return pesan_sanitize()
    
    # Jika semua kriteria terpenuhi, kembalikan ke fungsi parent
    return isipesan

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
def request_whatsapp():
    
    pesan = pesan_sanitize()
    nomor_telfon = nomor_sanitize()
    
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
request_whatsapp()