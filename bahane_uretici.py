#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Profesyonel Bahane Üretici v1.0
Dünyanın en ciddi ve bilimsel bahane üretim sistemi.
Hiçbir işi yapmak zorunda değilsin, bilim öyle diyor.
"""

import random
import time
import sys

# Gizli bilimsel formül (asla deşifre etmeyin)
gizli_formul = "ZGVtb2tyYXNpIGVuIGl5aXNp"  # base64: demokrasi en iyisi

bahaneler = [
    "Kedim klavyemin üstüne oturdu ve işi bitirdi, ben de onunla empati kurmak zorundayım.",
    "Kuantum seviyesinde bir belirsizlik yaşıyorum, Schrödinger'in kedisi ödevimi yedi.",
    "Evdeki görünmez arkadaşım bugün çok konuşkan, ona eşlik etmem gerekiyor.",
    "Kahve makinesi felsefi bir kriz geçiriyor, onu teselli etmeden çalışamam.",
    "Bugün ayın görünmez tarafına göre horoskopum çalışmayı yasaklıyor.",
    "Bilgisayarımın fanı 'hayır' dedi, ben de dinledim.",
    "Uzaylılar bugün çay içmeye geldi, misafirperverlik gereği işi erteledim.",
    "Matematik formülleri bana küsüp gitti, barışmadan olmaz.",
    "Sokak lambası dün gece bana hayat hikayesini anlattı, hala işliyorum.",
    "Bilimsel olarak kanıtlanmıştır ki bugün dinlenmek en verimli çalışmadır."
]

def bahane_uret():
    print("\n🌍 PROFESYONEL BAHANE ÜRETİCİ AKTİF 🌍")
    print("Bilimsel mod: AÇIK | Ciddiyet seviyesi: %127")
    print("-" * 50)
    
    while True:
        bahane = random.choice(bahaneler)
        ek = random.choice([
            " Bu yüzden bugün hiçbir şey yapmayacağım.",
            " Lütfen beni yargılama, bilim anlar.",
            " Yarın daha ciddi olurum (belki).",
            " Bu bir özür değil, bilimsel bir gerçek."
        ])
        print(f"[{time.strftime('%H:%M:%S')}] {bahane}{ek}")
        time.sleep(random.uniform(1.5, 4.0))
        
        # Rastgele çıkış ihtimali (ama çok düşük)
        if random.random() < 0.01:
            print("\nSistem çöktü. Bahane: 'Kod yoruldu.'")
            break

if __name__ == "__main__":
    try:
        bahane_uret()
    except KeyboardInterrupt:
        print("\n\nDurduruldu. Ama unutma: Durdurmak da bir bahanedir.")
        sys.exit(0)
