    def play_again(self):
        while True:
            choice = input("\n Сыграть снова? (да/нет): ").lower().strip()

            if choice == "да":
                self.reset_game() 
                self.start() 
                break
            elif choice == "нет":
                print("Спасибо за игру! Удачи в учебе!")
                self.game_active = False 
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'")
