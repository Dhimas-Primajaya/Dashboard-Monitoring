import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def ekstraksi_data():
    """
    Tanggal: 02 Nov 2025
    Waktu: 13:47:31 WIB
    Magnitudo: 2,9
    Kedalaman: 17 Km
    Lokasi: 4,02 LS-121,83 BT
    Pusat Gempa: Berada di darat 10 km barat daya Kolaka Timur
    Dirasakan (Skala MMI): II-III Kolaka Timur
    :return:
    """

    # Inisialisasi variabel untuk menghindari NameError jika parsing gagal
    global koordinat

    try:
        content = requests.get("https://bmkg.go.id")
    except RequestException:
        return None
    # print(content) #Menampilkan Response Status Code dari Server
    # print(content.text)

    if content.status_code == 200:
        hasil = dict()

        soup = BeautifulSoup(content.text, "html.parser")
        title = soup.find("title")
        print(title.text)

        # --- 1. Ambil Tanggal & Waktu & Pusat (Tetap) ---
        result = soup.find("p", {"class": "mt-2 text-sm leading-[22px] font-medium text-gray-primary"})
        result = result.text.split(", ")
        tanggal = result[0]
        waktu = result[1]
        pusat = soup.find("p", {"class": "mt-4 text-xl lg:text-2xl font-bold text-black-primary"})
        pusat = pusat.text

        # --- 2. Ambil Magnitudo, Kedalaman, Lokasi (Index) ---
        semua_nilai_span = soup.find_all("span", {"class": "text-base lg:text-lg font-bold text-black-primary"})

        if len(semua_nilai_span) > 1:
            # Jika list memiliki lebih 1 elemen (Magnitudo dan Kedalaman ada)
            magnitudo = semua_nilai_span[0].text.strip()
            kedalaman = semua_nilai_span[1].text.strip()
            koordinat = semua_nilai_span[2].text.strip()
        else:
            # Jika list kosong (0 elemen)
            magnitudo = "N/A"
            kedalaman = "N/A"
            koordinat = "N/A"

        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = koordinat
        hasil["pusat"] = pusat
        # hasil["dirasakan"] = "Dirasakan (Skala MMI): II-III Kolaka Timur"
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return None
    print("Gempa Terkini berdasarkan BMKG")
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Koordinat: {result['koordinat']}")
    print(f"Pusat: {result['pusat']}")
    return None
    # print(f"Dirasakan: {result['dirasakan']}")

#Code dibawah tidak akan dijalankan karena nama filenya bukan main
if __name__ == "__main__":
    print("Ini adalah package gempaterkini")

#Code dibawah ini akan dijalankan karena tidak didalam if __name__ == "__main__":
# print("Ini adalah package gempaterkini")