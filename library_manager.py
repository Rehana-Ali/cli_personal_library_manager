import json

# File to store library data
LIBRARY_FILE = "book_data.json"

def load_library():
    """Load library data from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    """Save library data to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)  # Save after adding
    print("Book added successfully!")

def remove_book(library):
    """Remove a book from the library."""
    title = input("Enter the title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)  # Save after removal
            print("Book removed successfully!")
            return
    print("Book not found!")

def search_book(library):
    """Search for a book by title or author."""
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter the search term: ")
    
    results = [
        book for book in library 
        if (choice == "1" and query.lower() in book["title"].lower()) or
           (choice == "2" and query.lower() in book["author"].lower())
    ]
    
    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display total books and percentage read."""
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}\nPercentage read: {percentage_read:.2f}%")

def main():
    """Main function to run the program."""
    library = load_library()
    
    while True:
        print("""
Welcome to your Personal Library Manager!  
1. Add a book  
2. Remove a book  
3. Search for a book  
4. Display all books  
5. Display statistics  
6. Exit  
        """)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


























































































































































































































