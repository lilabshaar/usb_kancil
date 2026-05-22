## File: `boot.py`

```python
# boot.py - Konfigurasi USB HID untuk USB Kancil
import usb_hid
usb_hid.enable((usb_hid.Device.KEYBOARD,))
```
