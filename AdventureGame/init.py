 def __init__(self):
        self.player = Player() 
        self.game_active = True 
        self.locations = self.static()  
        self.student = Student()  
        self.classrooms = ["501", "502", "503", "504", "505", "506"]
        self.target_classroom = random.choice(self.classrooms)
        self.teacher_attempts = 3
        self.exam_special_artifacts = [
            Artifact("Шпаргалка", "📝", "Секрет успеха на экзамене", 50, True),
            Artifact("Конспект", "📒", "Все формулы в одном месте", 45, True),
            Artifact("Учебник", "📚", "Вся теория в одной книге", 60, True),
            Artifact("Калькулятор", "🧮", "Решает любые пределы и интегралы", 55, True),
        ]
        self.hallway_artifacts = [
            Artifact("Забытая тетрадь", "📓", "Чьи-то конспекты", 15, False),
        ]
        self.exam_tickets = list(range(1, 11))
        self.player.prepared_tickets = random.sample(self.exam_tickets, 3)
        self.special_in_hallway = random.randint(1, 2)
