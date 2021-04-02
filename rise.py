import random


berabere = 0

oyuncu_win = 0

bilgisayar_win = 0


while True:

    seçenek = ["taş","kağıt","makas"]

    bilgisayar = random.choice(seçenek).lower()

    oyuncu = None

    oyuncu = input("\nTaş Kağıt Makas : ")
    if oyuncu not in seçenek:
        print(48*"*")   
        print("Lütfen üç seçenekten birini doğru giriniz.")
    print(48*"*")

    while  oyuncu in seçenek:
        
        print("Oyuncu : ",oyuncu)
        print("Bilgisayar : ",bilgisayar)

        if oyuncu == bilgisayar:
            berabere += 1
            print("Berabere !")
            print(48*"*")

        elif oyuncu == "taş":

            if bilgisayar == "kağıt":
                bilgisayar_win += 1
                print("Bilgisayar Kazandı !")
                print(48*"*")

            if bilgisayar == "makas":
                oyuncu_win += 1
                print("Oyuncu Kazandı !")
                print(48*"*")

        elif oyuncu == "kağıt":

            if bilgisayar == "taş":
                oyuncu_win += 1
                print("Oyuncu Kazandı !")
                print(48*"*")

            if bilgisayar == "makas":
                bilgisayar_win += 1
                print("Bilgisayar Kazandı !")
                print(48*"*")

        elif oyuncu == "makas":

            if bilgisayar == "taş":
                bilgisayar_win += 1
                print("Bilgisayar Kazandı !")
                print(48*"*")

            if bilgisayar == "kağıt":
                oyuncu_win += 1
                print("Oyuncu Kazandı !")
                print(48*"*")

        break

    print("\nBilgisayar Kazanma Sayısı : ",bilgisayar_win)
    print("Oyuncu Kazanma Sayısı : ",oyuncu_win)
    print("Berabere Sayısı : ",berabere)
    
