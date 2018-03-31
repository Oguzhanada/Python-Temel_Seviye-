print("""********************************
HESAP MAKİNESİ PROGRAMI

İŞLEMLER;

1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi


********************************
""")

a=int(input("Birinci sayı:"))
b=int(input("İkinci sayı:"))

islem=int(input("İşlem giriniz"))

if islem==1 :
    print("{} ile {} toplamı: 124{}".format(a,b,a+b))
elif islem == 2:
    print("{} ile {} çıkarma işlemi: {}".format(a, b, a - b))
elif islem == 3:
     print("{} ile {} çarpma işlemi:{}".format(a, b, a * b))
elif islem == 4:
 print("{} ile {} bölme işlemi:{}".format(a, b, a / b))
else:
    print("Hatalı işlem girdiniz!\nTekrar deneyin!")
