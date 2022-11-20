import random

num = random.randint(1,100)

print("halo namaku laptop saya punya angka antara 1-100. apakah kamu bisa menebaknya")

while True :
    bil= int(input("masukan angka: "))
    
    if(bil < num):
        print("maaf, angka terlalu rendah")
    elif(bil >  num):
        print("maaf, angka terlalu tinggi")
    elif(bil == num):
        print("yapp, angka yang ditebak ",num," benar, selamat!")
        break   
        
        
