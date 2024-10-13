import sureler
print("╔═════════════════════╗")
print("║    Sureler          ║")
print("║                     ║")
print("║  1-Araf             ║")  
print("║  2-Saffat           ║")
print("║  3-Cin              ║")
print("║  4-Bakara           ║")   
print("║  5-Kafirun          ║")
print("╚═════════════════════╝")

#en az 5 seçim olsun
# ana menüde en az 5 seçenek olsun

secim=input() #input ile string veri alır.
print(secim,"seçtiniz.")
if secim=="1":
    print("1 seçtiniz,toplama yapılacak.")
if secim =="2":    
 print("2seçtiniz,çarpma yapılacak.")