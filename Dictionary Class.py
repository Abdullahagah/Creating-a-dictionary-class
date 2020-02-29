class MapSınıfı():

    def __init__(self, isim,__sözlük = []):
        self.isim = isim
        self.__sözlük = []
        print("Örnek Oluşturuldu")

    def sözlük_bastır(self):
        print(self.__sözlük)

    def sözlük_ekle(self, __anahtar, __değer):
        self.__sözlük.append(__anahtar)
        self.__sözlük.append(__değer)
        print("Anahtar ve Değeri eklendi")

    def değer_bastır(self,__anahtar):
        self.__anahtar = __anahtar
        try:
            print(self.__sözlük[self.__sözlük.index(__anahtar)+1])
        except IndexError:
            print(None)

    def anahtar_bastır(self, __değer):
        self.__değer = __değer
        print(self.__sözlük[self.__sözlük.index(__değer)-1])

    def sözlükten_çıkart_anahtar(self,__anahtar):
        self.__anahtar = __anahtar
        self.__anahtar_index = self.__sözlük.index(self.__anahtar)
        self.__sözlük.pop(self.__anahtar_index+1)
        self.__sözlük.remove(__anahtar)
        print("Anahtar ile çıkartıldı")

    def sözlükten_çıkart_değer(self,__değer):
        self.__değer = __değer
        self.__değer_index = self.__sözlük.index(self.__değer)
        self.__sözlük.remove(__değer)
        self.__sözlük.pop(self.__değer_index-1)
        print("Değer ile çıkartıldı.")

    def sözlük_birleştir(self, __Sınıf1, __Sınıf2):
        self.__Sınıf1 = __Sınıf1
        self.__Sınıf2 = __Sınıf2
        for i in self.__Sınıf2.__sözlük:
            self.__Sınıf1.__sözlük.append(i)
        print("Sözlük Birleştirildi.")

