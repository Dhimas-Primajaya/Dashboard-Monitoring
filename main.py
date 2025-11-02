"""
Aplikasi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""


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
    hasil = dict()
    hasil["tanggal"] = "02 Nov 2025"
    hasil["waktu"] = "13:47:31 WIB"
    hasil["magnitudo"] = 2.9
    hasil["kedalaman"] = "17 Km"
    hasil["lokasi"] = {"ls": 4.02, "bt": -121.83}
    hasil["pusat"] = "pusat gempa berada di darat 10 km barat daya Kolaka Timur"
    hasil["dirasakan"] = "Dirasakan (Skala MMI): II-III Kolaka Timur"

    return hasil

def tampilkan_data(result):
    print("Gempa Terkini berdasarkan BMKG")
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print("Aplikasi Utama:")
    result = ekstraksi_data()
    tampilkan_data(result)