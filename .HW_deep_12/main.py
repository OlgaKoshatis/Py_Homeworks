# Создайте класс студента
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра.
# - Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). Тут тоже добавить дескрипторы.
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета,
# и по оценкам всех предметов вместе взятых.

from student import Student
from lesson import Lesson

# Создаём класс студента
jon = Student('Jon', 'Bobrov', 'Nikolaevich')

# Создаём класс предмета существующего в файле CSV
math = Lesson('Math')
history = Lesson('History')

# Добавляем в студенту предмет в список его предметов
jon.append_lesson(math)
jon.append_lesson(history)

# Добавляем оценки и баллы за его учёбу
math.append_estimation(4)
math.append_estimation(3)
math.append_estimation(2)
math.append_estimation_ball(60)
math.append_estimation_ball(40)
math.append_estimation_ball(80)

history.append_estimation(5)
history.append_estimation(5)
history.append_estimation(5)
history.append_estimation_ball(30)
history.append_estimation_ball(60)
history.append_estimation_ball(60)

# Выводим средние баллы и оценки за его учёбу
jon.print_list_lesson()
