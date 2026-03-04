
import datetime

entry = input("What did you learn today? ").strip()
rating = input("Rate your productivity today (1-5, optional) ").strip()

now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n {date_str}\nEntry: {entry}\nProductivity Rating: {rating if rating else 'N/A'}\n{'-'*40}"

with open("daily_learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)

print("Your learning journal entry has been saved!")