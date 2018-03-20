def main():
    main_num = int(input("Sayi: "))

    # yüz=10^2 ve vigintilyon=10^63, ith element 10^3 times greater then (i-1)th.
    tp = [" yüz", " bin", "", "", " milyon", " milyar", " trilyon", " katrilyon", " kentilyon",
          " seksilyon", " septilyon", " oktilyon", " nonilyon", " desilyon", " undesilyon",
          " dodesilyon", " tredesilyon", " katordesilyon", " seksdesilyon", " septendesilyon",
          " oktodesilyon", " novemdesilyon", " vigintilyon"]

    # dec[]: every decimal digit,  ten[]: every tenth number
    dec = ["", " bir", " iki", " üç", " dört", " beş", " altı", " yedi", " sekiz", " dokuz"]
    ten = ["", " on", " yirmi", " otuz", " kırk", " elli", " altmış", " yetmiş", " seksen", " doksan"]

    text = ""

    # get length of main_num
    num = main_num
    leng = 0
    while num != 0:
        num = num // 10
        leng += 1

    if main_num == 0:
        text = "sıfır"

    # split main_num to (three digit) pieces and read them by mod 3.
    for i in range(leng, 0, -1):
        digit = int((main_num // (10 ** (i - 1))) % 10)

        if i % 3 == 0:
            if digit == 1:
                text += tp[0]
            else:
                text += dec[digit] + tp[0]
        elif i % 3 == 1:
            if i > 3:
                text += dec[digit] + tp[i - 3]
            else:
                text += dec[digit]
            if i>3:  # if you don't want commas, you can delete this if block.
                text += ","
        elif i % 3 == 2:
            text += ten[digit]


    print(text)


if __name__ == "__main__":
    main()
