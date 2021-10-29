def konv_dtk(x):
    hari = int(int(x) / 86400)
    sisa = int(int(x) % 86400)
    
    jam = int(sisa / 3600)
    sisa = int(sisa % 3600)
    
    menit = int(sisa / 60)
    sisa = int(sisa % 60)
    
    return print("Dari total " + x + " detik, diubah menjadi " + str(hari) + " hari " + str(jam) + " jam " + str(menit) + " menit " + str(sisa) + " detik.")