masalar = dict()
for i in range (10):
    masalar[i]=0
def hesapEkle():
    masaNo=int(input("Masa No:"))
    gecerli = masalar[masaNo]
    eklenecek= float(input("Eklenecek Ücret:"))
    toplam=gecerli+eklenecek
    masalar[masaNo]=toplam
def hesapSil():
    masaNo=int(input("Masa No:"))
    gecerli = masalar[masaNo]
    silinecek=int(input("Silinecek Tutar:"))
    Toplam = gecerli - silinecek
    masalar[masaNo] = Toplam
    


def main():
    while True:
        
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [Q] Çıkış
    
        """)

        secim=input("İşleminiz:")

        if secim == "1":
            
            for i in range(10):
                
                print("Masa {} için hesap: {}".format(i,masalar[i]))
            print("İşlem Tamamlandı ana menüye dönmek için enter e bas.")
            input()
        elif secim == "2":
            hesapEkle()
            print("İşlem Tamamlandı ana menüye dönmek için enter e bas.")
            input()
        elif secim == "3":
            hesapSil()
            print("İşlem Tamamlandı ana menüye dönmek için enter e bas.")
            input()
        elif secim == "q" or secim=="Q":
            print("Çıkış yapılıyor...")
            quit()
main()            
