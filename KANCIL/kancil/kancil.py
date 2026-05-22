## File: `kancil/kancil.py`

"""
Kancil - Parser Script Kancil untuk USB Kancil
Bahasa scripting HID injection berbahasa Indonesia
"""

import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import usb_hid


class Kancil:
    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayoutUS(self.kbd)
        self.tunda_bawaan = 0
        self.baris_terakhir = ""

        # Pemetaan tombol Script Kancil -> Keycode
        self.tombol = {
            "MASUK": Keycode.ENTER,
            "SPASI": Keycode.SPACE,
            "TAB": Keycode.TAB,
            "WIN": Keycode.GUI,
            "KENDALI": Keycode.CONTROL,
            "ALT": Keycode.ALT,
            "GESER": Keycode.SHIFT,
            "KELUAR": Keycode.ESCAPE,
            "ATAS": Keycode.UP_ARROW,
            "BAWAH": Keycode.DOWN_ARROW,
            "KIRI": Keycode.LEFT_ARROW,
            "KANAN": Keycode.RIGHT_ARROW,
            "HAPUS": Keycode.BACKSPACE,
            "HAPUS_KANAN": Keycode.DELETE,
            "F1": Keycode.F1, "F2": Keycode.F2, "F3": Keycode.F3,
            "F4": Keycode.F4, "F5": Keycode.F5, "F6": Keycode.F6,
            "F7": Keycode.F7, "F8": Keycode.F8, "F9": Keycode.F9,
            "F10": Keycode.F10, "F11": Keycode.F11, "F12": Keycode.F12,
        }

    def proses_baris(self, baris):
        baris = baris.strip()
        if not baris:
            return
        print(f"Sedang menjalankan: {baris}") 

        bagian = baris.split(" ", 1)
        perintah = bagian[0].upper()
        argumen = bagian[1] if len(bagian) > 1 else ""

        if perintah == "CATATAN":
            return  # Komentar, abaikan

        elif perintah == "TUNDA":
            time.sleep(int(argumen) / 1000)

        elif perintah == "TUNDA_BAWAAN":
            self.tunda_bawaan = int(argumen) / 1000

        elif perintah == "TEKS":
            self.layout.write(argumen)

        elif perintah == "TEKS_BARIS":
            self.layout.write(argumen)
            self.kbd.send(Keycode.ENTER)

        elif perintah == "ULANGI":
            for _ in range(int(argumen)):
                self.proses_baris(self.baris_terakhir)
            return  # Jangan simpan ULANGI sebagai baris terakhir

        else:
            # Kombinasi tombol: WIN r, KENDALI ALT HAPUS, dll
            kode_tombol = []
            for token in baris.split():
                token_atas = token.upper()
                if token_atas in self.tombol:
                    kode_tombol.append(self.tombol[token_atas])
                elif len(token) == 1:
                    # Karakter tunggal seperti 'r' di "WIN r"
                    kode_tombol.append(getattr(Keycode, token.upper(), None))

            kode_tombol = [k for k in kode_tombol if k is not None]
            if kode_tombol:
                self.kbd.send(*kode_tombol)

        if perintah != "TUNDA":
            time.sleep(self.tunda_bawaan)

        self.baris_terakhir = baris

    def jalankan_file(self, path):
        """Membaca dan menjalankan file Script Kancil (.kancil)"""
        with open(path, "r") as f:
            for baris in f:
                self.proses_baris(baris)
