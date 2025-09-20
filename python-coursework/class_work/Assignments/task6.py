import os
import re

# ---------- Predefined Positive & Negative Words ----------
positive_words = {"good", "great", "excellent", "happy", "joy", "love", "wonderful", "amazing"}
negative_words = {"bad", "terrible", "sad", "angry", "hate", "poor", "awful", "worst"}

NOTES_DIR = "usernotes"

def list_notes():
    """Return a list of all .txt files in the notes directory."""
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
    return files

def analyze_note(filename):
    """Analyze sentiment of a single note."""
    try:
        with open(os.path.join(NOTES_DIR, filename), "r", encoding="utf-8") as f:
            content = f.read().lower()

        # Use regex to find all words
        words = re.findall(r"\b\w+\b", content)
        pos_count = sum(word in positive_words for word in words)
        neg_count = sum(word in negative_words for word in words)

        if pos_count > neg_count:
            sentiment = "Positive 😊"
        elif neg_count > pos_count:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        print(f"\n--- Analysis of {filename} ---")
        print(f"Positive words: {pos_count}, Negative words: {neg_count}")
        print(f"Overall Sentiment: {sentiment}\n")

    except FileNotFoundError:
        print("File not found. Please try again.")
    except Exception as e:
        print(f"Error reading file: {e}")

def analyze_all_notes():
    files = list_notes()
    if not files:
        print("No notes available.")
        return
    for f in files:
        analyze_note(f)

def create_note():
    filename = input("Enter new note name (without extension): ").strip() + ".txt"
    content = input("Enter your note content:\n")
    try:
        with open(os.path.join(NOTES_DIR, filename), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Note '{filename}' created successfully!\n")
    except Exception as e:
        print(f"Error creating note: {e}")

def modify_note():
    files = list_notes()
    if not files:
        print("No notes to modify.")
        return
    print("Available notes:")
    for idx, f in enumerate(files, 1):
        print(f"{idx}. {f}")

    choice = input("Enter the number of the note to edit: ").strip()
    if not choice.isdigit() or int(choice) not in range(1, len(files) + 1):
        print("Invalid choice.")
        return

    filename = files[int(choice) - 1]
    try:
        with open(os.path.join(NOTES_DIR, filename), "a", encoding="utf-8") as f:
            new_text = input("Enter text to append:\n")
            f.write("\n" + new_text)
        print(f"Note '{filename}' updated successfully!\n")
    except Exception as e:
        print(f"Error modifying note: {e}")

def main():
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

    while True:
        print("\n===== Intelligent Notes Management System =====")
        print("1. Analyze a specific note")
        print("2. Analyze all notes")
        print("3. Create a new note")
        print("4. Modify an existing note")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            filename = input("Enter the filename (with .txt): ").strip()
            analyze_note(filename)
        elif choice == "2":
            analyze_all_notes()
        elif choice == "3":
            create_note()
        elif choice == "4":
            modify_note()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
