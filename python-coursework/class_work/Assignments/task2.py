def get_messages():
    messages = []
    num = int(input("Enter the number of messages: "))
    for _ in range(num):
        msg = input()
        messages.append(msg)
    return messages

def total_messages(messages):
    print(f"Total messages: {len(messages)}")

def unique_users(messages):
    users = {msg.split(":")[0].strip() for msg in messages}
    print(f"Unique users in the chat: {users}")

def total_words(messages):
    word_count = sum(len(msg.split(":")[1].split()) for msg in messages)
    print(f"Total words in the chat: {word_count}")

def average_words_per_message(messages):
    total = sum(len(msg.split(":")[1].split()) for msg in messages)
    avg = total / len(messages)
    print(f"Average words per message: {round(avg, 2)}")

def longest_message(messages):
    longest = max(messages, key=lambda msg: len(msg.split(":")[1]))
    print(f"Longest message: \"{longest}\"")

def most_active_user(messages):
    from collections import Counter
    user_counts = Counter(msg.split(":")[0] for msg in messages)
    user, count = user_counts.most_common(1)[0]
    print(f"Most active user: {user} ({count} messages)")

def message_count_for_user(messages):
    user = input("Enter user name: ")
    count = sum(1 for msg in messages if msg.startswith(user + ":"))
    print(f"Messages sent by {user}: {count}")

def most_used_word_by_user(messages):
    from collections import Counter
    user = input("Enter user name: ")
    words = []
    for msg in messages:
        if msg.startswith(user + ":"):
            content = msg.split(":")[1].lower()
            words.extend(content.split())
    if words:
        most_common = Counter(words).most_common(1)[0]
        print(f"Most frequent word used by {user}: \"{most_common[0]}\"")
    else:
        print(f"No messages by {user}")

def first_last_message_by_user(messages):
    user = input("Enter user name: ")
    user_msgs = [msg for msg in messages if msg.startswith(user + ":")]
    if user_msgs:
        print(f"First message by {user}: \"{user_msgs[0]}\"")
        print(f"Last message by {user}: \"{user_msgs[-1]}\"")
    else:
        print(f"No messages by {user}")

def check_user_presence(messages):
    user = input("Enter user name: ")
    if any(msg.startswith(user + ":") for msg in messages):
        print(f"User '{user}' found in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def repeated_words(messages):
    from collections import Counter
    all_words = []
    for msg in messages:
        words = msg.split(":")[1].lower().split()
        all_words.extend(words)
    word_counts = Counter(all_words)
    common = {word for word, count in word_counts.items() if count > 1}
    print(f"Common repeated words: {common}")

def longest_avg_message_user(messages):
    from collections import defaultdict
    user_word_counts = defaultdict(list)
    for msg in messages:
        user, content = msg.split(":")
        user_word_counts[user].append(len(content.strip().split()))
    avg_lengths = {user: sum(lengths)/len(lengths) for user, lengths in user_word_counts.items()}
    user = max(avg_lengths, key=avg_lengths.get)
    print(f"User with longest average message: {user} (avg {round(avg_lengths[user], 2)} words)")

def mention_count(messages):
    user = input("Enter user name to check mentions: ").lower()
    count = sum(1 for msg in messages if user in msg.lower().split(":")[1])
    print(f"Messages mentioning '{user}': {count}")

def remove_duplicates(messages):
    unique_msgs = list(set(messages))
    print(f"Unique messages count: {len(unique_msgs)}")
    for msg in unique_msgs:
        print(msg)

def sort_messages(messages):
    print("Sorted messages:")
    for msg in sorted(messages):
        print(msg)

def extract_questions(messages):
    print("Questions in the chat:")
    for msg in messages:
        if "?" in msg:
            print(msg)

def reply_ratio(messages):
    u1 = input("Enter first user: ")
    u2 = input("Enter second user: ")
    count = 0
    for i in range(1, len(messages)):
        if messages[i].startswith(u2 + ":") and messages[i-1].startswith(u1 + ":"):
            count += 1
    print(f"Reply ratio from {u2} to {u1}: {count} replies")

def check_deleted(messages):
    count = sum(1 for msg in messages if msg.lower().endswith("this message was deleted"))
    print(f"Deleted messages found: {count}")

def show_menu():
    print("""
Choose an analysis option:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user
9. Retrieve the first and last message sent by a user
10. Check if a user is present in the chat
11. Find commonly repeated words
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
""")

# Main program
messages = get_messages()

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        total_messages(messages)
    elif choice == '2':
        unique_users(messages)
    elif choice == '3':
        total_words(messages)
    elif choice == '4':
        average_words_per_message(messages)
    elif choice == '5':
        longest_message(messages)
    elif choice == '6':
        most_active_user(messages)
    elif choice == '7':
        message_count_for_user(messages)
    elif choice == '8':
        most_used_word_by_user(messages)
    elif choice == '9':
        first_last_message_by_user(messages)
    elif choice == '10':
        check_user_presence(messages)
    elif choice == '11':
        repeated_words(messages)
    elif choice == '13':
        longest_avg_message_user(messages)
    elif choice == '14':
        mention_count(messages)
    elif choice == '15':
        remove_duplicates(messages)
    elif choice == '16':
        sort_messages(messages)
    elif choice == '17':
        extract_questions(messages)
    elif choice == '18':
        reply_ratio(messages)
    elif choice == '19':
        check_deleted(messages)
    elif choice == '0':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")
