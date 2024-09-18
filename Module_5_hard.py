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
        self.age = age  # возраст, число
        self.__password = hashlib.md5(password.encode()).hexdigest()  # в хэшированном виде, число

    def pass_check(self, password):
        if self.__password == hashlib.md5(password.encode()).hexdigest():
            return True
        else:
            return False


class Video:
    def __init__(self, title, duration, time_now=10, adult_mode=False):
        self.title = title  # заголовок, (строка),
        self.duration = duration  # продолжительность, секунды
        self.time_now = time_now  # секунда остановки (изначально 0)
        self.adult_mode = adult_mode  # ограничение по возрасту, bool (False по умолчанию)


class UrTube:
    __users = []  # список объектов User
    __videos = []  # список объектов Video
    current_user = None  # текущий пользователь, User

    def __get_user(cls, nickname):
        for item in cls.__users:
            if item.nickname == nickname:
                return item

        return None

    def log_in(self, nickname, password):
        user_obj = self.__get_user(nickname)

        if user_obj  == None:
            print(f"Пользователь {nickname} не существует !")
        elif user_obj.pass_check(password):
            self.current_user = user_obj
            print('Добро пожаловать!')
        else:
            print("Пользователь с такой парой Логин/Пароль не найден !")

    def register(self, nickname, password, age):
        user_obj = self.__get_user(nickname)
        if user_obj != None:
            print(f"Пользователь {nickname} уже существует !")
            return

        #password = hashlib.md5(password.encode()).hexdigest()
        cl_user = User(nickname, password, age)
        self.__users.append(cl_user)
        self.current_user = cl_user

        print('Регистрация прошла успешно!')
        return

    def log_out(self):
        self.current_user = None

    def __get_user(self, nickname):
        for item in self.__users:
            if item.nickname == nickname:
                return item

        return None

    def add(self, *cl_video):
        for item in cl_video:
            self.__videos.append(item)

    def get_videos(self, keywords):
        lst = []
        for item in self.__videos:
            keywords = keywords.upper()
            if item.title.upper().find(keywords) >= 0:
                lst.append(item.title)

        return lst

    def watch_video(self, keywords):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео !")
            return

        video = None
        keywords = keywords.upper()
        for item in self.__videos:
            if item.title.upper().find(keywords) >= 0:
                video = item
                break

        if video != None:
            if self.current_user.age <= 18 and item.adult_mode:
                print("Вам нет 18 лет, пожалуйста покиньте страницу !")
                return

            import time as t

            n = 0
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

def start():
    print("Приветствую!")

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
    print(ur.current_user.nickname)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')


if __name__ == '__main__':
    start()