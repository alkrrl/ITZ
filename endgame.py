    def end_game(self):
        print("\n" + "-" * 20)
        print(" ИГРА ЗАВЕРШЕНА")
        print("-" * 20)

        unique_locations = []
        for loc in self.player.visited_locations:
            if loc not in unique_locations:
                unique_locations.append(loc)
        print(f"📍 Посещенные локации: {', '.join(unique_locations)}")
        print(f" Ваши предметы: {self.player.get_artifact_names()}")
        print(f"✨ Найдено особых артефактов: {self.player.special_artifacts_found}")

        self.play_again()
