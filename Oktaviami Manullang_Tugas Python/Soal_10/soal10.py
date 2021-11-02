# Nama	: Oktaviami Manullang
# NPM	: 1194062
# Kelas : D4 Teknik Informatika 3B
# 1194062 mod 8 = 6 -> membangun trapesium, dan angka 2 terakhir npm = 6, jadi membangun 6 trapesium

import shapefile

w=shapefile.Writer('soal0',shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")


w.record("ngek","satu")
w.record("ngok","dua")
w.record("brat","tiga")
w.record("brot","empat")
w.record("cret","lima")
w.record("crot","enam")



w.poly([[[2,1],[6,1], [1,4],[7,4], [2,1]]])
w.poly([[[9,1],[13,1], [8,4],[14,4], [9,1]]])
w.poly([[[16,1],[20,1], [15,4],[21,4], [16,1]]])

w.poly([[[2,6],[6,6], [1,9],[7,9], [2,6]]])
w.poly([[[9,6],[13,6], [8,9],[14,9], [9,6]]])
w.poly([[[16,6],[20,6], [15,9],[21,9], [16,6]]])

w.close()