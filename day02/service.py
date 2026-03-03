from .storage import load_students, save_students
from day02.logger import setup_logger


class StudentService:
    def __init__(self):
        self.students = load_students()
        self.logger = setup_logger()
        self.logger.info("Loaded %d students.", len(self.students))


    def add(self, name: str, score: int) -> bool:
        if name in self.students:
            return False
        self.students[name] = score
        save_students(self.students)
        self.logger.info("ADD name=%s score=%d", name, score)
        return True

    def delete(self, name: str) -> bool:
        if name not in self.students:
            return False
        del self.students[name]
        save_students(self.students)
        self.logger.info("DEL name=%s ", name)
        return True

    def query(self, name: str) -> int | None:
        return self.students.get(name)

    def update(self, name: str, score: int) -> bool:
        if name not in self.students:
            return False
        self.students[name] = score
        save_students(self.students)
        self.logger.info("UPD name=%s score=%d", name, score)
        return True

    def list_all(self) -> list[tuple[str, int]]:
        return sorted(self.students.items(), key=lambda x: x[1], reverse=True)

    
    def save(self) -> None:
        save_students(self.students)


