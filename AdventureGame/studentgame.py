    def student_game(self):
        loc = self.locations["student_game"]
        print(f"\n{loc.visit()}")
        self.player.visited_locations.append("Игра с голодными студентами")
        player_wins = 0  
        student_wins = 0 

        print("\n Игра 'камень/ножницы/бумага' (3 раунда)")
        for round_num in range(1, 4):
            print(f"\n РАУНД {round_num}/3")
            print(f"🏆 Счет: Вы {player_wins} - {student_wins} Студенты")
            while True:
                player_choice = input("Ваш выбор (камень/ножницы/бумага): ").lower().strip()
                if player_choice not in ["камень", "ножницы", "бумага"]:
                    print("Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'")
                    continue
                student_choice = random.choice(self.student.choices)
                print(f"Студент выбрал: {student_choice}")
                if player_choice == student_choice:
                    print("🤝 Ничья! Переигрываем этот раунд.")
                    continue  # При ничьей переигрываем раунд
                elif (player_choice == "камень" and student_choice == "ножницы") or \
                        (player_choice == "ножницы" and student_choice == "бумага") or \
                        (player_choice == "бумага" and student_choice == "камень"):
                    print("✅ Вы выиграли раунд!")
                    player_wins += 1
                else:
                    print("❌ Студент выиграл раунд!")
                    student_wins += 1

                break  

     def tiebreaker_round(self):
        print("\n Финальный раунд!")

        while True:
            player_choice = input("Ваш выбор (камень/ножницы/бумага): ").lower().strip()

            if player_choice not in ["камень", "ножницы", "бумага"]:
                print("Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'")
                continue

            student_choice = random.choice(self.student.choices)
            print(f" Студент выбрал: {student_choice}")
            if player_choice == student_choice:
                print("🤝 Опять ничья! Продолжаем...")
                continue  
            elif (player_choice == "камень" and student_choice == "ножницы") or \
                    (player_choice == "ножницы" and student_choice == "бумага") or \
                    (player_choice == "бумага" and student_choice == "камень"):
                print("🏆 ПОБЕДА! Вы выиграли решающий раунд!")
                self.choose_food()  
            else:
                print("ПОРАЖЕНИЕ! Студенты выиграли решающий раунд.")
                print("⏰ Вам придется вернуться в начало очереди и вы опоздаете на экзамен.")
                self.end_game() 

            break
        print("ИТОГИ 3 РАУНДОВ")
        print(f"Вы: {player_wins}    и     {student_wins} :Студенты")
        if player_wins > student_wins:
            print(" ПОБЕДА! Вы обогнали голодных студентов!")
            self.choose_food() 
        elif player_wins < student_wins:
            print("ПОРАЖЕНИЕ! Придется вернуться в начало очереди.")
            print("Вы опоздали на экзамен и вас отчислили. 💀")
            self.end_game()  
        else:
            print("🤝 НИЧЬЯ! Нужен дополнительный раунд...")
            self.tiebreaker_round() 
