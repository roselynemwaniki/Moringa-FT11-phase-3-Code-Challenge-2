from .connection import get_db_connection


def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
        )
    ''')

    conn.commit()
    conn.close()




# import sqlite3  

# def setup_database():  
#     conn = sqlite3.connect('magazine.db')  
#     cursor = conn.cursor()  

#     # Create authors table  
#     cursor.execute('''  
#     CREATE TABLE IF NOT EXISTS authors (  
#         id INTEGER PRIMARY KEY AUTOINCREMENT,  
#         name TEXT NOT NULL  
#     )''')  

#     # Create magazines table  
#     cursor.execute('''  
#     CREATE TABLE IF NOT EXISTS magazines (  
#         id INTEGER PRIMARY KEY AUTOINCREMENT,  
#         name TEXT NOT NULL,  
#         category TEXT NOT NULL  
#     )''')  

#     # Create articles table  
#     cursor.execute('''  
#     CREATE TABLE IF NOT EXISTS articles (  
#         id INTEGER PRIMARY KEY AUTOINCREMENT,  
#         author_id INTEGER NOT NULL,  
#         magazine_id INTEGER NOT NULL,  
#         title TEXT NOT NULL,  
#         FOREIGN KEY (author_id) REFERENCES authors (id),  
#         FOREIGN KEY (magazine_id) REFERENCES magazines (id)  
#     )''')  

#     conn.commit()  
#     conn.close()  

# if __name__ == "__main__":  
#     setup_database()
