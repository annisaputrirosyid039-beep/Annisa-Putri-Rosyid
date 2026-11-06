
from pathlib import Path
from analyzer import analisis_teks


def main():
    file_input = Path("input.txt")
    file_output = Path("report.txt")

    try:
        teks = file_input.read_text(encoding="utf-8")

        if not teks.strip():
            print("File input.txt masih kosong.")
            return

        laporan = analisis_teks(teks)

        file_output.write_text(laporan, encoding="utf-8")

        print("Analisis teks berhasil!")
        print("\n" + laporan)
        print(f"\nLaporan disimpan di: {file_output.resolve()}")

    except FileNotFoundError:
        print("File input.txt tidak ditemukan.")
        print("Pastikan input.txt berada di folder program.")

    except OSError as error:
        print(f"Terjadi kesalahan saat membaca/menulis file: {error}")


if __name__ == "__main__":
    main()
