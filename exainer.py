def explain(text):
    if not text:
        return ""

    return (
        "📘 Simple Explanation:\n\n"
        f"{text[:200]}...\n\n"
        "👉 This is a simplified version of the topic. "
        "For deep understanding, break it into smaller concepts."
    )