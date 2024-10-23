import random
with open ('questions.txt', 'r',encoding='utf-8') as file:
    questions= file.readlines()

    with open ('response.txt ', 'r',encoding='utf-8') as file:
        response=file.readlines()

        random_questions= random.choice(questions).strip()
        random_response= random.choice(response).strip()
        print(f"Ваш вопрос:{random_questions}")
        print(f"Ответ:{random_response}")
        