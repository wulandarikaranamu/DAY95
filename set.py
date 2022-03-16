#cara membuat set

data = {"merry",125,2.34}#hasil run random
print(data)

#konversi list kedalam set

data = set(["wulandari",1.63])#tidak dapat memiliki nilai yang sama
print(data)

#menjadikan immutable sebagai anggota
#karena bersifat immutable
keyboard = {
    (1,2,3),
    (4,5,6),
    (7,8,9),
    (0)
}
print(keyboard)

#tidak menerima nilai duplikat

hari = {"senin","senin","selasa","rabu"}
print(hari)
#hasilnya run hanya ada 3 nilai tidak 4

#mengahpus nilai dari set
data = {"merry",125,2.34}
data.remove("merry")
print(data)
