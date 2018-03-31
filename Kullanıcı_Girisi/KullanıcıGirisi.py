
print("""
***********************
    Kullanıcı Girişi
***********************   
""")
sys_kullanıcı_adı="Oğuzhan" #Varolan kullanıcı adı
sys_parola="123456"         ##Varolan parola
kullanıcı_adı=input("Kullanıcı Adı:")
parola=input("Parola:")

if sys_kullanıcı_adı==kullanıcı_adı and sys_parola!=parola:
    print("Parola hatalı!")
elif sys_kullanıcı_adı!=kullanıcı_adı and sys_parola==parola:
    print("Kullanıcı adı hatalı!")
elif sys_kullanıcı_adı!=kullanıcı_adı and sys_parola!=parola:
    print("Kullanıcı adı ve parola hatalı!")
else :
    print("Sisteme başarıyla giriş yapıldı..")



