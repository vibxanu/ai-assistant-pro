def generate_quiz(text):
    return [
        {
            "q": f"What is {text} mainly about?",
            "options": ["Core concept", "Random idea", "Nothing", "Confusion"],
            "ans": "Core concept"
        },
        {
            "q": f"Where is {text} used?",
            "options": ["Real life", "Never", "Books only", "Unknown"],
            "ans": "Real life"
        },
        {
            "q": f"{text} helps in?",
            "options": ["Learning", "Harming", "Confusion", "Nothing"],
            "ans": "Learning"
        }
    ]