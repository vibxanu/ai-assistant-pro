def generate_plan(text):
    text = text.lower()

    if "python" in text:
        return [
            "Day 1: Learn Python basics",
            "Day 2: Variables and data types",
            "Day 3: Loops and functions",
            "Day 4: Practice coding",
            "Day 5: Build small project"
        ]

    elif "ielts" in text:
        return [
            "Day 1: Learn English basics",
            "Day 2: Reading practice",
            "Day 3: Listening practice",
            "Day 4: Writing practice",
            "Day 5: Mock test"
        ]

    else:
        return [
            f"Day 1: Understand {text}",
            f"Day 2: Learn basics of {text}",
            f"Day 3: Study examples",
            f"Day 4: Practice",
            f"Day 5: Revise"
        ]