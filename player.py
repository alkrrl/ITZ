class Player:
    def __init__(self):
        self.artifacts: List[Artifact] = []  
        self.visited_locations: List[str] = []  
        self.has_pen = False 
        self.prepared_tickets = []  
        self.special_artifacts_found = 0  

    def add_artifact(self, artifact: Artifact):
        self.artifacts.append(artifact)
        if artifact.special_for_exam:
            self.special_artifacts_found += 1

    def get_artifact_names(self) -> str:
        if not self.artifacts:
            return "Ничего"
        return ", ".join(str(artifact) for artifact in self.artifacts)

    def special_artifact(self, artifact_name: str) -> bool:
        return any(artifact.name == artifact_name for artifact in self.artifacts)
