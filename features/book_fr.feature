# language: fr

Fonctionnalité: Managing books
    Scénario: User adds a book to the database
        Etant donné Database
        Et a book with a correct IBNS number
        Alors the book can be added

    Scénario: User deletes a book from database
        Etant donné Database
        Quand we add a book
        Alors the book can be deleted

    Scénario: User gets a books title from database
        Etant donné Database
        Quand we add a book
        Alors the books author can be retrieved
