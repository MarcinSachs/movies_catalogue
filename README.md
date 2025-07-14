# Biblioteka Filmów

Prosta aplikacja webowa stworzona przy użyciu frameworka Flask, która prezentuje katalog filmów. Projekt został zrealizowany w celach edukacyjnych.

## Zrzut ekranu
![alt text](screen.png)

## Funkcjonalności

*   **Strona główna**: Wyświetla listę dostępnych filmów.
*   **O serwisie**: Podstrona z informacjami o projekcie.
*   **Kontakt**: Podstrona z formularzem kontaktowym.

## Użyte technologie

*   **Backend**: Python, Flask
*   **Frontend**: HTML, Bootstrap 4

## Struktura projektu

```
movies_catalogue/ 
├── static/ 
│ └── css/ 
│ └── main.css 
├── templates/ 
│ ├── index.html # Główny szablon strony 
│ ├── homepage.html # Widok strony głównej 
│ ├── movie_details.html # Widok szczegółów filmu 
│ ├── about.html # Widok podstrony "O serwisie" 
│ └── contact.html # Widok podstrony "Kontakt" 
├── .env # Plik konfiguracyjny (lokalny) 
├── .gitignore # Plik ignorowanych plików Git 
├── main.py # Główny plik aplikacji Flask 
├── tmdb_client.py # Klient do obsługi API TMDB 
├── requirements.txt # Lista zależności projektu 
└── README.md # Ten plik
```

## Instalacja i uruchomienie

1.  **Sklonuj repozytorium:**
    ```bash
    git clone <URL_repozytorium>
    cd movies_project
    ```

2.  **Stwórz i aktywuj wirtualne środowisko:**
    ```bash
    # Windows
    python -m venv movies_env
    movies_env\Scripts\activate
    ```

3.  **Zainstaluj wymagane pakiety:**
    (W tym projekcie jedyną zewnętrzną zależnością jest Flask. Warto stworzyć plik `requirements.txt`)
    ```bash
    pip install Flask
    ```

4.  **Uruchom aplikację:**
    ```bash
    cd movies_catalogue
    python main.py
    ```

5.  Otwórz przeglądarkę i przejdź pod adres `http://127.0.0.1:5000/`.