print("My introduction") 

def introduce_me():
    name = "Hazrat Bilal"
    field = "AI, Machine Learning, and Data Science"
    interests = ["Python Programming", "AI/ML Projects", "Data Analysis", "Git & GitHub"]
    goals = "To become a skilled AI & ML developer and contribute to real-world projects."

    print("Hello! My name is", name)
    print("I work in the field of", field)
    print("My main interests are:")
    for interest in interests:
        print("-", interest)
    print("My goal is:", goals)

# Call the function
introduce_me()
