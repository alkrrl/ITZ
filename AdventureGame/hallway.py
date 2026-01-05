    def hallway(self):
        loc = self.locations["hallway"]
        print(f"\n{loc.visit()}")
        self.player.visited_locations.append(loc.name)
        while True:
            choice = input("Введите 'налево' или 'направо': ").lower().strip()

            if choice == "налево":
                self.cafeteria()
                break
            elif choice == "направо":
                self.exam_preparation()
                break
            else:
                print("Пожалуйста, введите 'налево' или 'направо'")
