    def reset_game(self):
        self.player = Player() 
        self.student = Student() 
        self.target_classroom = random.choice(self.classrooms) 
        self.teacher_attempts = 3 
        self.player.prepared_tickets = random.sample(list(range(1, 11)), 3)
        self.special_in_hallway = random.randint(1, 2) 
    
        for loc in self.locations.values():
            loc.visited = False
