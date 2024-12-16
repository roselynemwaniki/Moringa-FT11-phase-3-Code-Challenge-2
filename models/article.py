import sqlite3    
class Article:  
    def __init__(self, author, magazine, title):  
        # Assuming author and magazine are instances of Author and Magazine respectively  
        
        # Validate title  
        if not isinstance(title, str):  
            raise ValueError('Title must be a string')  
        if not (5 <= len(title) <= 50):  
            raise ValueError('Title must be between 5 and 50 characters inclusive')  

        # Assign values to the instance  
        self._title = title  
        self._author_id = author.id  # assuming `id` is the primary key in Author  
        self._magazine_id = magazine.id  # assuming `id` is the primary key in Magazine  

        # Call method to persist Article to the database  
        self._create_article_entry()  

    @property  
    def title(self):  
        return self._title  

    def _create_article_entry(self):  
        # Placeholder for database insertion logic  
        # e.g., INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)  
        # Be sure to handle exceptions for database operations accordingly  
        print(f"Creating article entry in the database: Author ID = {self._author_id}, Magazine ID = {self._magazine_id}, Title = '{self._title}'")  

# Example Author and Magazine classes for context  
class Author:  
    def __init__(self, id):  
        self.id = id  

class Magazine:  
    def __init__(self, id):  
        self.id = id  

# Example usage  
if __name__ == "__main__":  
    author = Author(1)  
    magazine = Magazine(2)  
    article = Article(author, magazine, "A Valid Title")  
    print(article.title)  # Accessing the title