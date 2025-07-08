def chat_create_cat(name):
    return {"name": name, "type": "cat"}

def chat_meow(cat):
    return f"{cat['name']} says Meow!"

def chat_eat(cat):
    return f"{cat['name']} is eating."


# Je dis que ce code ne s'exécutera uniquement si le fichier est exécuté directement.
if __name__ == "__main__":
    # Example usage
    cat = chat_create_cat("Mittens")
    print(chat_meow(cat))
    print(chat_eat(cat))

print("FILENAME : ", __name__)