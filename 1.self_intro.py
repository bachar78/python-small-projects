import datetime

name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Where do you live? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favorite hobby? ").strip()


intro_message = (f"Hello! My name is {name}. I am {age} years old and I live in {city}.\n"
                 f"I work as a {profession} and in my free time, I enjoy {hobby}. \n"
                 f"Nice to meet you!")

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}."

border = "=" * 15
final_output = f"{border}\n{intro_message}\n{border}"
print(final_output)