def add_title(title):
    ...


class UserInterface:
    @add_title('Ввод пользовательских данных')
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действие со статьями:")
        print("1 - создание статьи"
              "\n2 - просмотр статей"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title('Создание стать:')
    def add_user_article(self):
        dict_articles = {
            "название": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        # print(" Создание статьи ".center(50, "="))
        for key in dict_articles:
            dict_articles[key] = input(f"Введите {key} статьи: ")
        # print("=" * 50)
        return dict_articles

    @add_title('Список статей:')
    def show_all_articles(self, articles):
        # print(" Список статей: ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)
