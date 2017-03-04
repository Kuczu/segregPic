#SegregPic

SegregPic powstał jako 'hello word' dla pythona. Początkowo miał być małym skryptem, nauką pythona do czegoś więcej niż krótkie skrypty ad-hoc, lecz z czasem się trochę rozrósł.

SegregPic napisany został w celu wyselekcjonowania zdjęć/tapet spełniających wymaganą rozdzielczość.

Program testowany był na Windows 10 oraz wymaga Pythona 3 (v3.5.2+). **Ponadto do działania wymaga PIL oraz colorama.**

W programie podaje się ścieżkę w której program ma segregować pliki. Działa tak, że w każdym wykrytym folderze, i rekurencyjnie w jego podfolderach, segreguje obrazy przenosząc je do zadeklarowanych folderów.

Program udostępnia szereg opcji które można zmienić następującymi komendami - można je podać jako komendy wywoływane wsadowe lub już bezpośrednio w programie:

**Opcje główne programu:**
+ **-w wartość(int)**:
	Zmienia szerokość graniczną obrazka, obrazy z większą bądź równą szerokością będą brane jako spełniające warunek.
+ **-h wartość(int)**:
	Zmienia wysokość graniczną obrazka, obrazy z większą bądź równą wysokością będą brane jako spełniające warunek.
+ **-p ścieżka(string)**:
	Zmienia ścieżkę do posegregowania relatywnie do SegregPic.py.
+ **-pa ścieżka(string)**:
	Zmienia całą ścieżkę do posegregowania.
+ **-g nazwa_folderu**:
	Zmienia nazwę folderu dla pasujących obrazów.
+ **-b nazwa_folderu**:
	Zmienia nazwę folderu dla nie pasujących obrazów.
+ **-u nazwa_folderu**:
	Zmienia nazwę folderu dla plików które nie są plikami graficznymi
	
	### **UWAGA: przed uruchomieniem należy zmienić domyślną ścieżkę!**
	
**Opcje wypisywania:**
+ **-info boolean**:
	Zmienia pozwolenie na wypisywanie informacji takich jak: aktualnie przetwarzany folder, gdzie skopiowano akutalnie przetwarzany plik itp.
	
	Odpowiednio **-info t** aktywuje wypisywanie informacji natomiast **-info f** wyłącza tą opcję.
+ **-warn boolean**:
	Zmienia pozwolenie na wypisywanie ostrzeżeń takich jak: nierozpoznany plik, o istniejących już folderach które próbuje utworzyć itp.
	
	Odpowiednio **-warn t** aktywuje wypisywanie ostrzeżeń natomiast **-warn f** wyłącza tą opcję.

	*Błędy są wypisywane zawsze.*
	
**Opcje dla pliku z podsumowaniem:**
+ **-infof boolean**:
	Zmienia pozwolenie na zapis informacji takich jak: aktualnie przetwarzany folder, gdzie skopiowano akutalnie przetwarzany plik itp do pliku z podsumowaniem.
	
	Odpowiednio **-infof t** aktywuje zapisywania ostrzeżeń natomiast **-infof f** wyłącza tą opcję.
+ **-succf  boolean**:
	Zmienia pozwolenie na zapis informacji o powodzeniu do pliku z podsumowaniem - opcja jeszcze niewykorzystana!
	
	Odpowiednio **-succf t** aktywuje zapis natomiast **-succf f** wyłącza tą opcję.
+ **-warnf boolean**:
	Zmienia pozwolenie na zapis ostrzeżeń do pliku z podsumowaniem takich jak: nierozpoznany plik, o istniejących już folderach które próbuje utworzyć itp.
	
	Odpowiednio **-warnf t** aktywuje zapis ostrzeżeń natomiast **-warnf f** wyłącza tą opcję.
+ **-errf  boolean**:
	Zmienia pozwolenie na zapis błędów do pliku z podsumowaniem takich jak: brak uprawnień do pliku, błąd kopiowania itp.
	
	Odpowiednio **-errf t** aktywuje zapis błędów natomiast **-errf f** wyłącza tą opcję.
	
	*Jeśli wszystkie 4 opcje będą wyłączone to plik nie zostanie utworzony.*
	
+ **-statf boolean**:
	Zmienia pozwolenie na utworzenie pliku z podsumowaniem w każdym folderze  w którym dokonano segregowania.
	
	Odpowiednio **-statf t** aktywuje zapis ostrzeżeń natomiast **-statf f** wyłącza tą opcję.
	
**Komendy sterujące programem:**
+ **help**:
	Wyświetla opis komend.
+ **config**:
	Wyświetla aktualną konfigurację.
+ **start**:
	Startuje segregowanie.
+ **q**:
	Wyłącza program.
	
Jeśli istnieje konflikt nazw - np. 2 pliki o takie samej nazwie, program generuje pod folder o unikalnej nazwie i tam umieszcza kolejne pliki z tą samą nazwą.
