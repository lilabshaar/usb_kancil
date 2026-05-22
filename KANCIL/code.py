## File: `code.py`
# code.py - Program utama USB Kancil
import time
from kancil.kancil import Kancil

# Tunggu 2 detik agar komputer siap
time.sleep(2)

# Jalankan Script Kancil
kancil = Kancil()

kancil.jalankan_file("/skrip/skrip.kancil")

