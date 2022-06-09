# Model uczenia maszynowego do wykrywania wybranych anomalii sieciowych

Aplikacja ta pozwala wykrywać cyberataki na podstawie zebranych pakietów do pliku typu `*.pcap`. Jest to projekt zaliczeniowy z przedmiotu Inżynieria Cyberbezpieczeństwa.

## Struktura plików

W folderze `aplikacja` znajduje się kod aplikacji okienkowej oraz przykładowe pliki do przetestowania działania aplikacji.

W folderze `trenowanie_modelu` znajduje się notanik Jupyter wraz z kodem do wytrenowania modelu.

Aplikacja zawiera kod aplikacji CICflowmeter ze strony: https://gitlab.com/hieulw/cicflowmeter

W każdym z folderów znajduje się plik `requirements.txt`, który zawiera listę wymaganych bibliotek. Aby stworzyć wirtualne środwisko, wystarczy wywołać skrypt znajdujący się w pliku `create_environment`.

Z powodu ograniczonego miejsca na GitHubie, w plikach programu nie znajduje się wytrenowany model. Oryginalnie, po wytrenowaniu i zapisaniu modelu przy pomocy biblioteki `pickle`, plik z modelem został przeniesiony do folderu `./aplikacja/model_files/`.

## Uruchomienie aplikacji okienkowej

Aplikacja okienkowa została przetestowana i działa poprawnie na systemie Ubuntu.

Trzeba przejść do folderu `aplikacja` i w konsoli wpisać polecenie `python3 gui_app.py`.

## Trenowanie modelu

Zbiór danych użyty do trenowania modelu pochodzi ze strony: https://ieee-dataport.org/open-access/iot-network-intrusion-dataset. Plik ten oryginalnie był umieszczony w folderze `./trenowanie_modelu/idea_3_iot/` 
