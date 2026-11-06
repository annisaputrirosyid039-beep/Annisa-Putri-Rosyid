
import re
from collections import Counter
from utils import hitung_huruf, buat_grafik


def analisis_teks(teks):
    # Menghitung jumlah baris yang berisi teks
    baris = teks.splitlines()
    jumlah_baris = sum(1 for b in baris if b.strip())

    # Mengambil kata dan mengabaikan tanda baca
    kata_list = re.findall(r"\b\w+\b", teks.lower())
    jumlah_kata = len(kata_list)

    # Menghitung frekuensi setiap kata
    frekuensi = Counter(kata_list)

    # Menghitung huruf vokal dan konsonan
    vokal, konsonan = hitung_huruf(teks)

    # Menyusun laporan
    laporan = [
        "========================================",
        "       LAPORAN ANALISIS TEKS",
        "========================================",
        f"Jumlah baris       : {jumlah_baris}",
        f"Jumlah kata        : {jumlah_kata}",
        f"Jumlah huruf vokal : {vokal}",
        f"Jumlah konsonan    : {konsonan}",
        "",
        "5 KATA PALING SERING MUNCUL",
        "----------------------------------------",
    ]

    for kata, total in frekuensi.most_common(5):
        laporan.append(f"{kata:<15} : {total} kali")

    laporan.extend([
        "",
        "GRAFIK FREKUENSI KATA",
        "----------------------------------------",
        buat_grafik(frekuensi),
        "========================================",
    ])

    return "\n".join(laporan)
