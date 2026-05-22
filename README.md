# USB Kancil

USB Kancil adalah proyek sederhana untuk menjalankan skrip bahasa Indonesia sebagai input keyboard HID melalui CircuitPython.

## Deskripsi

Proyek ini membaca file skrip `.kancil` dan mengubah perintah bahasa Indonesia menjadi aksi keyboard USB HID. Tujuannya adalah membuat sebuah perangkat USB yang dapat menjalankan rangkaian perintah keyboard secara otomatis.

## Struktur Proyek

- `KANCIL/boot.py` - Konfigurasi USB HID untuk board CircuitPython.
- `KANCIL/code.py` - Program utama yang memulai eksekusi skrip.
- `KANCIL/kancil/kancil.py` - Parser dan logika utama untuk menjalankan perintah skrip.
- `KANCIL/lib/adafruit_hid/` - Library HID Adafruit untuk keyboard dan keycode.
- `KANCIL/skrip/skrip.kancil` - Contoh skrip Kancil.
- `KANCIL/settings.toml` - File konfigurasi (kosong saat ini).

## Perintah Dasar Script Kancil

Parser saat ini mendukung beberapa perintah utama seperti:

- `CATATAN` - komentar
- `TUNDA <ms>` - jeda dalam milidetik
- `TUNDA_BAWAAN <ms>` - pengaturan jeda default
- `TEKS <teks>` - mengetik teks
- `TEKS_BARIS <teks>` - mengetik teks lalu enter
- `ULANGI <n>` - ulangi baris terakhir sebanyak n kali

Selain itu, parser menerjemahkan nama tombol Indonesia menjadi `Keycode` HID, seperti `MASUK`, `SPASI`, `TAB`, `WIN`, `KENDALI`, `ALT`, `GESER`, `KELUAR`, `HAPUS`, `F1`–`F12`, dan panah arah.

## Cara Menggunakan

1. Salin semua isi folder `KANCIL/` ke root drive CircuitPython pada perangkat USB.
2. Pastikan board CircuitPython terhubung dan dikenali oleh komputer.
3. Jalankan board sehingga `code.py` dieksekusi secara otomatis.
4. `code.py` akan memuat dan menjalankan skrip dari `/skrip/skrip.kancil`.

## Contoh Skrip

Contoh sederhana dapat ditemukan di `KANCIL/skrip/skrip.kancil`.

## Catatan

- Pastikan file skrip berada di jalur yang benar.
- Timer default diatur oleh perintah `TUNDA_BAWAAN`.
- Jika ada perintah baru, tambahkan logika parser di `KANCIL/kancil/kancil.py`.
