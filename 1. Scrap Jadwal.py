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
        if data['code'] == 200:
            print('Data Diterima\n\n')
            print(data['data'])
        else:
            print('Terjadi Kesalahan Dalam Mengambil Data Jadwal, Silahkan Coba Kembali!')
    except requests.exceptions.RequestException as err:
        print("Error saat melakukan request:", err)
    except:
        print("Error saat melakukan request:", err)
    return
    

request_jadwal()