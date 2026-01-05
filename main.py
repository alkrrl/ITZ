def main():
    print("-" * 20)
    print("Игра:СТУДЕНЧЕСКАЯ ЖИЗНЬ")

    print("Соберите особые артефакты в коридоре!")

    while True:
        start_choice = input("\n Хотите сыграть? (да/нет): ").lower().strip()

        if start_choice == "да":
            game = AdventureGame()
            game.start()

            if not game.game_active:
                break
        elif start_choice == "нет":
            print("\n До свидания! Удачи на сессии!")
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")


if __name__ == "__main__":
    main()
