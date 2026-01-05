class Location:
    def __init__(self, name: str, description: str, emoji: str = ""):
        self.name = name  
        self.description = description  
        self.emoji = emoji  
        self.visited = False 
        self.choices: Dict[str, str] = {} 
        self.artifacts: List[Artifact] = []  

    def visit(self):
        self.visited = True
        return f"{self.emoji}{self.description}{self.emoji}"
