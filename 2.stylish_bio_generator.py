import textwrap

name=input("What is your name? ").strip()
profession=input("What is your profession? ").strip()
passion=input("What is your passion? ").strip()
emoji=input("What is your favorite emoji? ").strip()
website=input("What is your website? ").strip()

print("\n Choose your style: ")
print("1. Simple lines")
print("2. Vertical flair")
print("3. Emoji sandwich")

style_choice=input("Enter the number of your preferred style: ").strip()

def generate_bio(name, profession, passion, emoji, website, style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n 💡 {passion} \n  {website}" 
    elif style == "2":
        return f" {emoji} {name}\n {profession}🔥\n {passion}\n {website}🧑‍💻"
    elif style == "3":
        return f"{emoji*3} \n {name} - {profession} \n {passion} - {website} \n {emoji*3}"
    else:
        return "Invalid style choice."

bio = generate_bio(name, profession, passion, emoji, website, style_choice)

print("\nYour Stylish Bio:\n")
print("-" * 40)
print(textwrap.dedent(bio))
print("-" * 40)

save = input("Do you want to save this bio to a file? (y/n) ").strip().lower()
if save == 'y':
    filename = f"{name.replace(' ', '_')}_bio.txt"
    with open(filename, 'w') as file:
        file.write(bio)
    print(f"Bio saved to {filename}")
else:
    print("Bio not saved.")  