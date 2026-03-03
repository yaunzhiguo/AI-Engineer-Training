import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "students.json"

def load_students() -> dict[str, int]:
    if not DATA_PATH.exists():
        return {}
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        # 确保分数是 int
        return {k: int(v) for k, v in data.items()}
    except Exception:
        return {}

def save_students(students: dict[str, int]) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
