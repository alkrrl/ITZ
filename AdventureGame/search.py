 def search_hallway(self):
        print("\n🔍 Пока вы стоите в коридоре, решаете осмотреться,чтобы найти полезные вещи перед экзаменом...")
        found_artifacts = []
        special_to_find = random.sample(self.exam_special_artifacts, self.special_in_hallway)
        for artifact in special_to_find:
            found_artifacts.append(artifact)
            self.player.add_artifact(artifact)
            print(f"✨ Вы нашли: {artifact}! {artifact.description}")
        normal_count = random.randint(0, 1)
        if normal_count > 0:
            normal_to_find = random.sample(self.hallway_artifacts, normal_count)
            for artifact in normal_to_find:
                found_artifacts.append(artifact)
                self.player.add_artifact(artifact)
                print(f" Вы нашли: {artifact}")

        if not found_artifacts:
            print("К сожалению, вы ничего не нашли. Коридор пуст.")
        else:
            print(f"🎒 Теперь у вас {len(found_artifacts)} предметов!")

        self.hallway()
