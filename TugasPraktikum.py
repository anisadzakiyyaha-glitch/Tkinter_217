import tkinter as tk

top = tk.Tk()

def hasilPrediksi():
    var.set("Teknologi Informasi")

judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan")
judul.pack()

labelframe = tk.LabelFrame(top, text="Input Nilai Mata Pelajaran")
labelframe.pack()

for i in range(10):
    L = tk.Label(labelframe, text="Nilai Mata Pelajaran " + str(i + 1))
    L.grid(row=i, column=0)
    E = tk.Entry(labelframe, bd=5)
    E.grid(row=i, column=1)

B = tk.Button(top, text="Hasil Prediksi", command=hasilPrediksi)
B.pack()

var = tk.StringVar()
hasil = tk.Label(top, textvariable=var, relief=tk.RAISED)
hasil.pack()

top.mainloop()