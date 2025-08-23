import requests
import os

while True:
    print("\n--- Basit DirBuster ---")
    print("Çıkmak için 'x' yazın.")

    ip = input("Hedef IP adresini girin: ").strip()
    if ip.lower() == 'x':
        break

    base_url = f"http://{ip}"

    wordlist_path = input("Wordlist dosya yolunu girin: ").strip()
    if wordlist_path.lower() == 'x':
        break

    if not os.path.exists(wordlist_path):
        print(" Wordlist dosyası bulunamadı. Lütfen geçerli bir yol girin.")
        continue

    with open(wordlist_path, 'r') as f:
        paths = f.read().splitlines()

    for path in paths:
        url = base_url + '/' + path
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f" Bulundu: {url}")
            else:
                print(f" Bulunamadı: {url} - Kod: {response.status_code}")
        except requests.RequestException as e:
            print(f" Hata oluştu: {e}")
