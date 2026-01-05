USD_RATE = 12700
EUR_RATE = 13500
RUB_RATE = 140

def usd_uzs(miqdor):
    return miqdor * USD_RATE

def eur_uzs(miqdor):
    return miqdor * EUR_RATE

def rub_uzs(miqdor):
    return miqdor * RUB_RATE
