# Дополнительное практическое задание по модулю: "Классы и объекты."
# ***************************************************************************************
#   Задание "Свой YouTube":
#  Всего будет 3 класса: UrTube, Video, User.
#
# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы
# добавления видео, авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты:
#   - nickname(имя пользователя, строка),
#   - password(в хэшированном виде, число),
#   - age(возраст, число)
#
# Каждый объект класса Video должен обладать следующими атрибутами и методами:
#   Атриубуты:
#   - title(заголовок, строка),
#   - duration(продолжительность, секунды),
#   - time_now(секунда остановки (изначально 0)),
#   - adult_mode(ограничение по возрасту, bool (False по умолчанию))
#
# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#   Атриубты:
#   - users(список объектов User),
#   - videos(список объектов Video),
#   - current_user(текущий пользователь, User)
#
#   - Метод log_in, который принимает на вход аргументы:
#       nickname, password и пытается найти пользователя в users с такими же логином и паролем.
#       Если такой пользователь существует, то current_user меняется на найденного.
#       Помните, что password передаётся в виде строки, а сравнивается по хэшу.
#   - Метод register, который принимает три аргумента:
#       nickname, password, age, и добавляет пользователя в список, если пользователя не существует
#       (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже существует".
#       После регистрации, вход выполняется автоматически.
#   - Метод log_out для сброса текущего пользователя на None.
#   - Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
#       если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
#   - Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
#       содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
#       'Urban the best' (не учитывать регистр).
#   - Метод watch_video, который принимает название фильма, если не находит точного совпадения
#       (вплоть до пробела), то ничего не воспроизводится, если же находит - ведётся отчёт в консоль
#       на какой секунде ведётся просмотр. После текущее время просмотра данного видео сбрасывается.
#       Для метода watch_video так же учитывайте следующие особенности:
#           - Для паузы между выводами секунд воспроизведения можно использовать функцию sleep
#            из модуля time.
#           - Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
#            В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
#           - Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре,
#            т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет,
#            пожалуйста покиньте страницу"
#       После воспроизведения нужно выводить: "Конец видео"
#
# ***************************************************************************************
import hashlib


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя, строка
        self.password = password  # в хэшированном виде, число
        self.age = age  # возраст, число


class Video:
    def __init__(self, title, duration, time_now, adult_mode=False):
        self.title = title  # заголовок, (строка),
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)


class UrTube:
    __instance = None
    __current_user = None  # текущий пользователь, User
    __users = []  # список объектов User
    __videos = []  # список объектов Video

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        if len(self.__videos) == 0:
            cl_video = Video("Три поросенка", 1800, 10, True)
            self.add(cl_video)

            cl_video = Video("Бриллиантовая рука", 5960, 12)
            self.add(cl_video)

    def log_in(self, nickname, password):
        for item in self.__users:
            if item.nickname == nickname:
                if item.password == hashlib.sha256(password.encode()).hexdigest():
                    self.__current_user = item
                    print('Добро пожаловать!')
                    self.dialog()

        if self.__current_user == None:
            print("Пользователь с такой парой Логин/Пароль не найден !")
            return
        else:
            self.dialog()

    def register(self, nickname, password, age):
        password == hashlib.sha256(password.encode()).hexdigest()
        cl_user = User(nickname, password, age)
        self.__users.append(cl_user)
        self.__current_user = cl_user

        print('Регистрация прошла успешно!')
        self.dialog()

    def log_out(self):
        __current_user = None

    def add(self, *cl_video):
        for item in cl_video:
            self.__videos.append(item)

    def get_videos(self, keywords):
        lst = []
        for item in self.__videos:
            if item.title.upper().find(keywords) >= 0:
                lst.append(item.title)

        return lst

    def watch_video(self, keywords):
        video = None
        for item in self.__videos:
            if item.title.upper().find(keywords) >= 0:
                video = item
                break

        if video != None:
            if self.__current_user.age <= 18 and item.adult_mode:
                print("Вам нет 18 лет, пожалуйста покиньте страницу !")
                return

            import time as t

            n = 0
            print(n)
            while n <= item.time_now:
                t.sleep(1)
                n = n + 1
                print(n)

            print("Конец видео")

        else:
            #print("По вашему запросу ничего не найдено !")
            pass

    def get_users(self):
        return self.__users

    def dialog(self):
        while True:
            choice = int(input(
                "Выберите действие: \n1 - Доступные видео \n2 - Найти видео  \n3 - Смотреть видео \n4 - Добавить видео \n0 - Завершить сеанс \n>> "))

            if choice == 0:
                self.log_out()
                break

            elif choice == 1:
                lst = []
                for item in self.__videos:
                    lst.append(item.title)
                print(lst)

            elif choice == 2:
                print('Введите строку/название видео для поиска:')
                keywords = input()
                videos = self.get_videos(keywords.upper())

                if len(videos) == 0:
                    print("По вашему запросу ничего не найдено !")
                else:
                    print(videos)

            elif choice == 3:
                print('Введите название для поиска:')
                keywords = input()
                self.watch_video(keywords.upper())

            elif choice == 4:
                print('Введите название видео:')
                title = input()

                cl_video = Video(title, 1200, 10)
                self.add(cl_video)

def start():
    print("Приветствую!")
    while True:
        # UrTube_ = None
        choice = int(input("Выберите действие: \n1 - Вход \n2 - Регистрация \n0 - Завершение работы \n>> "))

        if choice == 0:
            print("Будем рады видеть Вас снова !")
            break

        if choice == 1:
            print('Введите логин:')
            login = input()

            print('Введите пароль:')
            nickname = input()

            UrTube_ = UrTube()
            UrTube_.log_in(login, nickname)

        if choice == 2:
            UrTube_ = UrTube()

            while True:
                print('Введите логин:')
                login = input()

                result = True
                for item in UrTube_.get_users():
                    if item.nickname == nickname:
                        print('Пользователь с таким логином уже существует')
                        result = False
                        break

                if result:
                    break

            while True:
                print('Введите пароль:')
                password = input()

                print('Повторите пароль:')
                password_repeat = input()

                if password != password_repeat:
                    print('Пароли не совпадают!')
                else:
                    break

            print('Введите Ваш возраст:')
            age = int(input())

            UrTube_.register(login, password, age)

    # Удаление объектов
    # del h2
    # del h3


if __name__ == '__main__':
    start()