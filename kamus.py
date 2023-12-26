import time

meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY":"menakutkan, tidak menyenangkan",
            "AGGRO": "Untuk menjadi agresif/marah"
            }

for i in range(6):
    time.sleep(1)   
    print("Halo:)!")
    time.sleep(1)
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!)  : ")
    time.sleep(1)
    if word in meme_dict.keys():
        print("Artinya:")
        time.sleep(1)
        print(meme_dict[word])
        
    else:
        time.sleep(1)
        print('Maaf aku tidak tau arti kata itu:(')
    print("    ")
