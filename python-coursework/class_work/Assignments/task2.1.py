messages = []
num = int(input("Enter the number of messages: "))
for _ in range(num):
    msg = input()
    messages.append(msg)

while True:
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
    choice = input("Enter your choice: ")

    if choice == '1':
        count = 0
        for _ in messages:
            count += 1
        print(f"Total messages: {count}")

    elif choice == '2':
        users = []
        for msg in messages:
            user = msg.split(":")[0].strip()
            if user not in users:
                users.append(user)
        print(f"Unique users: {users}")

    elif choice == '3':
        total_words = 0
        for msg in messages:
            content = msg.split(":")[1]
            words = content.split()
            for _ in words:
                total_words += 1
        print(f"Total words: {total_words}")

    elif choice == '4':
        total_words = 0
        total_msgs = 0
        for msg in messages:
            words = msg.split(":")[1].split()
            for _ in words:
                total_words += 1
            total_msgs += 1
        print(f"Average words per message: {round(total_words / total_msgs, 2)}")

    elif choice == '5':
        longest = messages[0]
        for msg in messages:
            if len(msg.split(":")[1]) > len(longest.split(":")[1]):
                longest = msg
        print(f"Longest message: \"{longest}\"")

    elif choice == '6':
        user_counts = {}
        for msg in messages:
            user = msg.split(":")[0]
            if user in user_counts:
                user_counts[user] += 1
            else:
                user_counts[user] = 1
        max_user = ""
        max_count = 0
        for user in user_counts:
            if user_counts[user] > max_count:
                max_user = user
                max_count = user_counts[user]
        print(f"Most active user: {max_user} ({max_count} messages)")

    elif choice == '7':
        user = input("Enter user name: ")
        count = 0
        for msg in messages:
            if msg.startswith(user + ":"):
                count += 1
        print(f"Messages sent by {user}: {count}")

    elif choice == '8':
        user = input("Enter user name: ")
        word_counts = {}
        for msg in messages:
            if msg.startswith(user + ":"):
                content = msg.split(":")[1].lower()
                words = content.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        max_word = ""
        max_count = 0
        for word in word_counts:
            if word_counts[word] > max_count:
                max_word = word
                max_count = word_counts[word]
        if max_word:
            print(f"Most frequent word used by {user}: \"{max_word}\"")
        else:
            print("No words found.")

    elif choice == '9':
        user = input("Enter user name: ")
        first = ""
        last = ""
        found = False
        for msg in messages:
            if msg.startswith(user + ":"):
                if not found:
                    first = msg
                    found = True
                last = msg
        if found:
            print(f"First message by {user}: \"{first}\"")
            print(f"Last message by {user}: \"{last}\"")
        else:
            print("No messages found for user.")

    elif choice == '10':
        user = input("Enter user name: ")
        found = False
        for msg in messages:
            if msg.startswith(user + ":"):
                found = True
                break
        if found:
            print(f"User '{user}' is present in the chat.")
        else:
            print(f"User '{user}' not found.")

    elif choice == '11':
        word_counts = {}
        for msg in messages:
            words = msg.split(":")[1].lower().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        repeated = []
        for word in word_counts:
            if word_counts[word] > 1:
                repeated.append(word)
        print(f"Repeated words: {repeated}")

    elif choice == '13':
        user_lengths = {}
        user_counts = {}
        for msg in messages:
            user, content = msg.split(":")
            words = content.strip().split()
            length = 0
            for _ in words:
                length += 1
            if user in user_lengths:
                user_lengths[user] += length
                user_counts[user] += 1
            else:
                user_lengths[user] = length
                user_counts[user] = 1
        max_user = ""
        max_avg = 0
        for user in user_lengths:
            avg = user_lengths[user] / user_counts[user]
            if avg > max_avg:
                max_avg = avg
                max_user = user
        print(f"User with longest average message: {max_user} (avg {round(max_avg, 2)} words)")

    elif choice == '14':
        mention = input("Enter user to check mentions: ").lower()
        count = 0
        for msg in messages:
            if mention in msg.split(":")[1].lower():
                count += 1
        print(f"Mentions of '{mention}': {count}")

    elif choice == '15':
        seen = []
        for msg in messages:
            if msg not in seen:
                seen.append(msg)
        print(f"Unique messages count: {len(seen)}")
        for msg in seen:
            print(msg)

    elif choice == '16':
        sorted_msgs = messages[:]
        for i in range(len(sorted_msgs)):
            for j in range(i+1, len(sorted_msgs)):
                if sorted_msgs[i] > sorted_msgs[j]:
                    sorted_msgs[i], sorted_msgs[j] = sorted_msgs[j], sorted_msgs[i]
        print("Sorted messages:")
        for msg in sorted_msgs:
            print(msg)

    elif choice == '17':
        print("Questions in chat:")
        for msg in messages:
            if "?" in msg:
                print(msg)

    elif choice == '18':
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        count = 0
        for i in range(1, len(messages)):
            if messages[i].startswith(u2 + ":") and messages[i - 1].startswith(u1 + ":"):
                count += 1
        print(f"Reply ratio from {u2} to {u1}: {count}")

    elif choice == '19':
        count = 0
        for msg in messages:
            if msg.lower().endswith("this message was deleted"):
                count += 1
        print(f"Deleted messages: {count}")

    elif choice == '0':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

