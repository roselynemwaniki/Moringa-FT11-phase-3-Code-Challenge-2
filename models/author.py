import sqlite3

class Author:
    def __init__(self, id=None, name=None):
        # Initialize an Author, create a new entry in the database if only a name is provided
        if name:
            self._name = name
            self._id = None
            # Add to the database and retrieve the newly created ID (mocked for this example)
            self._create_in_db(name)
        else:
            self._id = id
            self._name = None
            # Fetch name from the database using the provided ID (mocked)
            self._retrieve_from_db(id)

    def _create_in_db(self, name):
        # This method would interact with your database to insert the new Author.
        # Simulate the insertion process by assigning a mock ID.
        self._id = 1 # Mocked database-generated ID.
        print(f"New author '{self._name}' created with ID {self._id}.")

    def _retrieve_from_db(self, author_id):
        # Fetch the name from the database using the author's ID
        # Here we simulate it by setting a mock name.
        # You would query the database to fetch the name based on the provided `author_id`.
        
        self._name = "Mock Author Name"  # This should come from the DB
        print(f"Author with ID {self._id} retrieved from DB. Name: {self._name}")

    @property
    def id(self):
        # The id should be an integer and should be returned directly.
        if self._id is None:
            raise ValueError("Author not yet created in the database")
        return self._id

    @property
    def name(self):
        # The name is read-only after initialization, so only a getter.
        if not hasattr(self, '_name') or self._name is None:
            raise ValueError("Name has not been set for this author.")
        return self._name

    @name.setter
    def name(self, value):
        # Prevent changing the name after initialization.
        raise AttributeError("Name cannot be changed after initialization.")

    def articles(self):
        # Use a raw SQL query to get articles associated with the author using SQL JOIN
        # This assumes there is a table 'articles' and a foreign key 'authorId' in 'articles' pointing to 'authors'
        articles = self._execute_sql(
            'SELECT articles.* FROM articles '
            'JOIN authors ON articles.authorId = authors.id '
            'WHERE authors.id = :authorId', 
            {'authorId': self._id}
        )
        return articles

    def magazines(self):
        # Use a raw SQL query to get magazines associated with the author using SQL JOIN
        # This assumes there is a many-to-many relationship via 'AuthorMagazines' table
        magazines = self._execute_sql(
            'SELECT magazines.* FROM magazines '
            'JOIN AuthorMagazines ON magazines.id = AuthorMagazines.magazineId '
            'JOIN authors ON AuthorMagazines.authorId = authors.id '
            'WHERE authors.id = :authorId',
            {'authorId': self._id}
        )
        return magazines

    def _execute_sql(self, query, params):
        # This method would execute a SQL query (using raw SQL, an ORM like SQLAlchemy, or a database connection)
        # For now, we simulate database query execution by returning mock data.
        # This simulates fetching related articles and magazines from the database.
        print(f"Executing SQL: {query} with params {params}")
        return [{"title": "Mock Article Title", "id": 1}, {"title": "Another Article", "id": 2}]  # Mock data

# Example Usage
author = Author(name="John Doe")  # Creating a new author
print(f"Author ID: {author.id}, Author Name: {author.name}")

# Fetching articles associated with the author
articles = author.articles()
print("Articles:")
for article in articles:
    print(f"- {article['title']} (ID: {article['id']})")

# Fetching magazines associated with the author
magazines = author.magazines()
print("Magazines:")
for magazine in magazines:
    print(f"- {magazine['title']} (ID: {magazine['id']})")

# Trying to change the author's name (will raise an error)
try:
    author.name = "New Name"
except AttributeError as e:
    print(e)

# If you wanted to create an author using an existing ID
existing_author = Author(id=1)
print(f"Existing Author - ID: {existing_author.id}, Name: {existing_author.name}")
