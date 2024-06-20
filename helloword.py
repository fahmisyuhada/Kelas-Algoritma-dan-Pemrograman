def main():
    print("update data uang di database")
    x =0
    hasil = 0
    try:
        # printah yang ada kemungkinan error
        hasil = 8/x
        # Sebagai programmer harus teliti disini untuk m
    except ZeroDivisionError:
        print("kamu bagi bilangan dengan nol mass. ganti dia")
    except :
        # alternatif perintah jika errro terjadi
        print("Ada terjadi error mass...")
    finally:
        print("Keluarkan uang")
    print(hasil)
    

if __name__=="__main__":
    main()
    