import tkinter as tk

def create_lps_table(pattern):
    """
    Membuat tabel presufiks (lps) untuk pola yang diberikan.
    """
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Melakukan pencarian menggunakan algoritma KMP.
    """
    m = len(pattern)
    n = len(text)

    lps = create_lps_table(pattern)
    i = j = 0
    positions = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


def search_word():
    """
    Fungsi untuk menangani pencarian kata pada teks ketika tombol "Cari" ditekan.
    """
    text = text_entry.get("1.0", tk.END).strip()
    pattern = pattern_entry.get().strip()

    positions = kmp_search(text, pattern)

    if len(positions) > 0:
        result_label.config(text="Kata ditemukan pada posisi: " + str(positions))
    else:
        result_label.config(text="Kata tidak ditemukan dalam teks.")


# Membangun UI
window = tk.Tk()
window.title("Aplikasi Pencarian Pola")
window.geometry("400x200")

# Label dan entry untuk memasukkan teks
text_label = tk.Label(window, text="Teks:")
text_label.pack()

text_entry = tk.Text(window, height=4, width=30)
text_entry.pack()

# Label dan entry untuk memasukkan pola yang ingin dicari
pattern_label = tk.Label(window, text="Pola:")
pattern_label.pack()

pattern_entry = tk.Entry(window)
pattern_entry.pack()

# Tombol untuk melakukan pencarian
search_button = tk.Button(window, text="Cari", command=search_word)
search_button.pack()

# Label untuk menampilkan hasil pencarian
result_label = tk.Label(window)
result_label.pack()

window.mainloop()
