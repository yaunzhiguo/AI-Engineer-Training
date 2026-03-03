def input_non_empty(prompt: str) -> str:
    s = input(prompt).strip()
    if not s:
        print("Input cannot be empty.")
        return ""
    return s

def input_score(prompt: str = "Enter score (0-100): ") -> int | None:
    s = input(prompt).strip()
    try:
        score = int(s)
    except ValueError:
        print("Score must be an integer.")
        return None
    if not (0 <= score <= 100):
        print("Score must be in [0, 100].")
        return None
    return score
