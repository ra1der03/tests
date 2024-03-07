import pytest

from unique_names import unique_names

mentors_ = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

expected_ = ['Адилет', 'Азамат', 'Александр', 'Алексей', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', 'Евгений', 'Елена', 'Иван', 'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', 'Сергей', 'Татьяна', 'Тимур', 'Филипп', 'Эдгар', 'Юрий']

@pytest.mark.parametrize(
    'mentors,expected',
    [(mentors_, expected_)])
def test_result(mentors, expected):
    result = unique_names(mentors)
    assert result == expected






