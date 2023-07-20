
roma = [
    ' ', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
    ' ', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC',
    ' ', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM',
    ' ', 'M', 'MM', 'MMM','MV̄'
]

# Roma rakami dizimizi olusturuyoruz. 0 girildiginde 0 sonucunu elde etmek
# icin 9 dan sonra 10'a gecmiyoruz her basamagin 0 alacagi ihtimalini dusunuyoruz
# ornegin 1000 icin soldan saga 4. basamaktan sonraki hanelere 0 basabilmek icin

while True:
    basamak = [0, 0, 0, 0, 0]  # basamak degeri ve sonuc icin
    sonuc = ' '

    sayi = int(input("ceviri yapmak istediginiz sayiyi giriniz (MAX 4999) : "))
    if sayi > 4999:
        print(" Max 4999 a kadar yazilabilir. ")
    else:
        basamak[0] = sayi % 10  # birler basamagini buluyoruz
        basamak[1] = ((sayi // 10) % 10) + 10  # onlar basamagini buluyoruz
        basamak[2] = ((sayi // 100) % 10) + 20  # yuzler basamagini buluyoruz
        basamak[3] = ((sayi // 1000) % 10) + 30  # binler basamagini buluyoruz
        for i in range(0, 35, 1):  # dizimiz 34 adet elemanli oldugu icin
            for r in range(0, 4, 1):  # basamak degerlerini bulmak icin
                if basamak[r] == i:
                    sonuc = roma[i] + ' ' + sonuc
        print("Sayinin Roma Rakami karsiligi : ", sonuc)

