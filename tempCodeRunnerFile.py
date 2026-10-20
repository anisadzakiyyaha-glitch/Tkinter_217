import tkinter as tk

top = tk.Tk()

def hasilPrediksi():
    var.set("Teknologi Informasi")

judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan")
judul.pack(pady=10)

labelframe = tk.LabelFrame(top, text="Input Nilai Mata Pelajaran")
labelframe.pack(padx=20, pady=5)

mapel = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia", "Biologi", "Sejarah", "Geografi", "Ekonomi", "Informatika"]

for i in range(10):
    L = tk.Label(labelframe, text=mapel[i])
    L.grid(row=i, column=0, sticky=tk.W, padx=10, pady=3)
    E = tk.Entry(labelframe, bd=5)
    E.grid(row=i, column=1, padx=10, pady=3)

B = tk.Button(top, text="Hasil Prediksi", command=hasilPrediksi)
B.pack(pady=10)

var = tk.StringVar()
hasil = tk.Label(top, textvariable=var, relief=tk.RAISED, width=30)
hasil.pack(pady=(0, 15))

top.mainloop()