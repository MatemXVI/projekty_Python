def meeus(year):
    a = year % 19
    b = int(year / 100)
    c = year % 100
    d = int(b / 4)
    e = b % 4
    f = int((b + 8) / 25)
    g = int((b - f + 1) / 3)
    h = (19 * a + b - d - g + 15) % 30
    i = int(c / 4)
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = int((a + 11 * h + 22 * l) / 451)
    p = (h + l - 7 * m + 114) % 31
    day = p + 1
    month = int((h + l - 7 * m + 114) / 31)
    if month == 3:
        print("W kalendarzu gregoriańskim Wielkanoc wypada:", day, "marca")
    elif month == 4:
        print("W kalendarzu gregoriańskim Wielkanoc wypada:", day, "kwietnia")


def meeus_gregorian(year):
    a = year % 4
    b = year % 7
    c = year % 19
    d = (19 * c + 15) % 30
    e = (2 * a + 4 * b - d + 34) % 7
    day = ((d + e + 114) % 31) + 1
    month = int((d + e + 114) / 31)
    if month == 3:
        print("W kalendarzu juliańskim Wielkanoc wypada:", day, "marca")
    elif month == 4:
        print("W kalendarzu juliańskim Wielkanoc wypada:", day, "marca")


year = int(input("Podaj rok: "))
if 0 < year < 33:
    print("Chrystus żył, ale jeszcze nie zmartwychwstał!")
elif year < 0:
    print("W tym roku jeszcze nie narodził się Chrystus!")
else:
    meeus(year)
    meeus_gregorian(year)
