    def exam_preparation(self):
        loc = self.locations["exam_preparation"]
        print(f"\n{loc.visit()}")
        self.player.visited_locations.append("Подготовка к экзамену")

        print("\n📖 Вы зашли в аудиторию. До экзамена еще 30 минут.")

        extra_tickets = 0
        if self.player.special_artifact("Конспект мечты"):
            print("📒 Конспект мечты помогает быстрее усваивать материал!")
            extra_tickets += 1
        if self.player.special_artifact("Учебник гения"):
            print("📚 Учебник гения содержит ответы на сложные вопросы!")
            extra_tickets += 1
        if extra_tickets > 0:
            remaining_tickets = [t for t in self.exam_tickets if t not in self.player.prepared_tickets]
            if remaining_tickets:
                additional = min(extra_tickets, len(remaining_tickets))
                additional_tickets = random.sample(remaining_tickets, additional)
                self.player.prepared_tickets.extend(additional_tickets)
                print(f"🎯 Благодаря артефактам вы подготовились к дополнительным {additional} билетам!")

        print(f"📊 Вы подготовились к {len(self.player.prepared_tickets)} билетам из 10.")
        print(f"📋 Подготовленные билеты: {', '.join(map(str, sorted(self.player.prepared_tickets)))}")
        if self.player.special_artifact("Шпаргалка"):
            print("📝 У вас есть шпаргалка! Она может помочь при списывании.")

        print("\n⏰ Время вышло! Заходит преподаватель и выкладывает билеты...")
        self.exam_begin()
