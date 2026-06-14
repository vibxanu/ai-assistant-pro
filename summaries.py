def summarize(text):
    if not text:
        return ""

    text = text.lower()

    if "ai" in text or "artificial intelligence" in text:
        return (
            "🧠 AI (Artificial Intelligence) is the technology that enables machines to think, learn, "
            "and make decisions like humans. It is used in chatbots, self-driving cars, and smart systems."
        )

    elif "python" in text:
        return (
            "🐍 Python is a programming language used for web development, AI, data science, and automation. "
            "It is simple, powerful, and beginner-friendly."
        )

    elif "ielts" in text:
        return (
            "📘 IELTS is an English language test used for study and immigration in English-speaking countries. "
            "It checks reading, writing, listening, and speaking skills."
        )

    else:
        return (
            f"📘 {text} is an important topic. It is used in real-world applications and helps in learning new concepts."
        )