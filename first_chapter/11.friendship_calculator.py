def friendshhip_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2) 
    vowels = set('aeiou')
    score += len(shared_letters) * 5
    score += len(shared_letters & vowels) * 10
    return min(score, 100)

def run_friendship_calculator():
    name1 = input("Enter the first person's name: ")
    name2 = input("Enter the second person's name: ")
    score = friendshhip_score(name1, name2)
    print(f"The friendship score between {name1} and {name2} is: {score}%")

run_friendship_calculator()