class Artifact:
    name: str 
    emoji: str 
    description: str  
    power: int = 0  
    special_for_exam: bool = False 

    def __str__(self):
        return f"{self.emoji} {self.name}"
