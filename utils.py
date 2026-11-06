
def hitung_huruf(teks):
    vokal = "aiueoAIUEO"
    jumlah_vokal = 0
    jumlah_konsonan = 0

    for huruf in teks:
        if huruf.isalpha():
            if huruf in vokal:
                jumlah_vokal += 1
            else:
                jumlah_konsonan += 1

    return jumlah_vokal, jumlah_konsonan


def buat_grafik(frekuensi, jumlah=5):
    hasil = []

    for kata, total in frekuensi.most_common(jumlah):
        grafik = "#" * total
        hasil.append(f"{kata:<15} {grafik} ({total})")

    return "\n".join(hasil)
