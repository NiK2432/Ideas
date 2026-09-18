def show_ideas(ideas):
    print("\n=== Каталог идей для Python-проектов ===\n")
    for i, idea in enumerate(ideas):
        print(f"{i + 1}. {idea['name']}")
        print(f"Тема: {idea['topic']}")
        print(f"Сложность: {idea['difficulty']}\n")

def add_idea(ideas, name, topic, difficulty):
    new_idea = {
        'name': name,
        'topic': topic,
        'difficulty': difficulty
    }
    ideas.append(new_idea)
    print("\nИдея добавлена!\n")