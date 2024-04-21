# **Zadanie 2**

## Opis
- Program działa w następujący sposób
  - Zczytywany jest plik .txt jako dane wejściowe
  - za pomocą algorytmu Rabina-Karpa wyszukiwane są (podane w inpucie) błędne wyrazy
  - błędne wyrazy są zamieniane na poprawne
  - poprawiona opowieść-melodia jest kompresowana na ciąg znaków 0-1 za pomocą algorytmu Huffmana
  - przy użyciu zaimplementowanej funkcji dehuffman() możliwy jest powrót do normalnego tekstu
    
## Dane wejśćiowe (plik .txt)

- w pierwszej linijce pliku tekstowego są zawarte dwie liczby
  - pierwsza liczba to ilość linii w których zapisana jest opowieść-melodia
  - druga liczba oznacza ilość błędnych wyrazów lub ich fragmentów zawartych w opowieści-melodii
- przykład  
  3 2  
  przykladowy tekst  
  przykladowy tekst  
  przykladowy tekst  
  bledne_slowo poprawne_slowo  
  bledne_slowo poprawne_slowo  
  
