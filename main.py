from ideas import show_ideas, add_idea

my_ideas = [
    {
        'name': 'Трекер привычек',
        'topic': 'Консольное приложение',
        'difficulty': 'Средняя'
    },
    {
        'name': 'Космическая викторина',
        'topic': 'Игра',
        'difficulty': 'Лёгкая'
    },
    {
        'name': 'Планировщик задач',
        'topic': 'Организация времени',
        'difficulty': 'Средняя'
    }
]

show_ideas(my_ideas)

user_choice = input("Добавить новую идею? ").lower()

if user_choice == 'да':
    name_input = input("Название: ")
    topic_input = input("Тема: ")
    difficulty_input = input("Сложность: ")

    add_idea(my_ideas, name_input, topic_input, difficulty_input)

    show_ideas(my_ideas)
