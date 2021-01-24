# language: pl

Właściwość: Zarządzanie książkami

    Scenariusz: Użytkownik dodaje książke do bazy
        Mając Baze danych
        Oraz książke z poprawnym numerem isbn
        Wtedy książka sie dodaje

    Scenariusz: Użytkownik usuwa książke z bazy
        Mając Baze danych
        Jeśli dodamy książke
        Wtedy książka sie usuwa

    Scenariusz: Użytkownik pobiera nazwe autora książki
        Mając Baze danych
        Jeśli dodamy książke
        Wtedy autor książki może być odczytany
