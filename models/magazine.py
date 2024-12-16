import sqlite3

class Database:  
    """Simulated Database for demonstration purposes."""  
    magazines = []  
    articles = []  
    authors = []  
    article_authors = []  # Stores tuples of (article_id, author_id)  

    @classmethod  
    def add_magazine(cls, magazine):  
        cls.magazines.append(magazine)  

    @classmethod  
    def add_article(cls, article):  
        cls.articles.append(article)  

    @classmethod  
    def add_author(cls, author):  
        cls.authors.append(author)  

    @classmethod  
    def add_article_author(cls, article_id, author_id):  
        cls.article_authors.append((article_id, author_id))  


class Article:  
    def __init__(self, id: int, title: str, magazine_id: int):  
        self.id = id  
        self.title = title  
        self.magazine_id = magazine_id  
        Database.add_article(self)  


class Author:  
    def __init__(self, id: int, name: str):  
        self.id = id  
        self.name = name  
        Database.add_author(self)  


class Magazine:  
    def __init__(self, id: int, name: str, category: str):  
        self._id = id  
        self._name = None  
        self._category = None  
        
        # Set name and category using their respective setters  
        self.name = name  
        self.category = category  
        
        # Add the magazine entry to the simulated database  
        Database.add_magazine(self)  

    @property  
    def id(self) -> int:  
        return self._id  

    @property  
    def name(self) -> str:  
        return self._name  

    @name.setter  
    def name(self, value: str):  
        if not isinstance(value, str):  
            raise ValueError("Name must be a string.")  
        if not (2 <= len(value) <= 16):  
            raise ValueError("Name must be between 2 and 16 characters.")  
        self._name = value  

    @property  
    def category(self) -> str:  
        return self._category  

    @category.setter  
    def category(self, value: str):  
        if not isinstance(value, str):  
            raise ValueError("Category must be a string.")  
        if len(value) == 0:  
            raise ValueError("Category must be longer than 0 characters.")  
        self._category = value  

    def articles(self):  
        """Return all articles associated with this magazine."""  
        return [article for article in Database.articles if article.magazine_id == self.id]  

    def article_titles(self):  
        """  
        Return a list of titles of all articles for this magazine.  
        Return None if there are no articles.  
        """  
        article_list = self.articles()  
        return [article.title for article in article_list] if article_list else None  

    def contributors(self):  
        """Return all authors associated with articles in this magazine."""  
        article_ids = [article.id for article in self.articles()]  
        
        author_ids = set()  
        for article_id in article_ids:  
            for entry in Database.article_authors:  
                if entry[0] == article_id:  
                    author_ids.add(entry[1])  
        
        return [author for author in Database.authors if author.id in author_ids]  

    def contributing_authors(self):  
        """  
        Return a list of authors who have written more than 2 articles for this magazine.  
        Return None if there are no such authors.  
        """  
        # Count articles per author  
        author_article_count = {}  
        
        for article in self.articles():  
            for entry in Database.article_authors:  
                if entry[0] == article.id:  
                    author_id = entry[1]  
                    author_article_count[author_id] = author_article_count.get(author_id, 0) + 1  
        
        # Find authors with more than 2 articles  
        contributors = [author for author in Database.authors if author.id in author_article_count and author_article_count[author.id] > 2]  

        return contributors if contributors else None  


# Example setup for testing  
magazine1 = Magazine(1, "Techie", "Technology")  
author1 = Author(1, "Alice Smith")  
author2 = Author(2, "Bob Johnson")  
author3 = Author(3, "Charlie Brown")  

# Create articles  
article1 = Article(1, "Latest Tech Trends", magazine1.id)  
article2 = Article(2, "AI in the Future", magazine1.id)  
article3 = Article(3, "The Rise of Quantum Computing", magazine1.id)  
article4 = Article(4, "Gadgets of Tomorrow", magazine1.id)  
article5 = Article(5, "Innovations in Robotics", magazine1.id)  

# Link articles with authors  
Database.add_article_author(article1.id, author1.id)  
Database.add_article_author(article2.id, author1.id)  
Database.add_article_author(article3.id, author1.id)  # Alice Smith has 3 articles  
Database.add_article_author(article4.id, author2.id)   # Bob Johnson has 1 article  
Database.add_article_author(article5.id, author2.id)   # Bob Johnson has 2 articles  

# Testing article_titles method  
print("Article Titles in magazine:")  
titles = magazine1.article_titles()  
print(titles if titles else "No articles found.")  

# Testing contributing_authors method  
print("\nContributing Authors for magazine:")  
contributing_authors = magazine1.contributing_authors()  
if contributing_authors:  
    for author in contributing_authors:  
        print(author.name)  
else:  
    print("No authors with more than 2 articles found.")
    
