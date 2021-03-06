# Задача об инвесторе

Данный проект решает задачу об инвесторе с помощью динамического 
программирования.

## Постановка задачи
На фондовом рынке запланированы первичные размещения облигаций с номиналом 1000
условных единиц, по которым каждый день выплачивается купон размером 1 уе.
Погашение номинала облигации (то есть выплата 1000 условных единиц) происходит в
конце срока.

Каждая облигация на рынке характеризуется названием (некая строка) и ценой, цена
выражается в виде процентов от номинала, то есть цена 98.5 соответствует цене
98,5% * 1000 = 985 условных единиц.

У некоего инвестора есть информация о том, какие предложения по облигациям будут
размещаться на рынке в ближайшие N дней. По каждому дню он знает, какие лоты
будут размещены на бирже: название облигации, цену и количество в штуках. Каждый
день на рынке может быть от 0 до M лотов. Инвестор располагает суммой денежных
средств в количестве S.

Необходимо определить какие лоты в какие дни нужно купить, чтобы получить
максимальный доход с учетом следующих условий:

1. Инвестор может только покупать облигации. Купленные облигации не продаются.
2. Инвестор может купить только весь лот целиком при наличии доступных
денежных средств.
3. Выплаченные купоны по купленным облигациям не реинвестируются, то есть не
Выходные данные
Мегатрейдер
увеличивают сумму доступных денежных средств.
4. Все купленные облигации будут погашены в день N+30.
5. Доход рассчитывается на день N+30, то есть после погашения облигаций.


Входные данные:

На первой строке будут даны числа N, M и S. Далее будет идти k строк вида “<день>
<название облигации в виде строки без пробелов> <цена> <количество>”. Ввод будет
завершен пустой строкой.

2 2 8000
1 alfa-05 100.2 2
2 alfa-05 101.5 5
2 gazprom-17 100.0 2

Выходные данные:

В первой строке необходимо указать сумму дохода, полученного трейдером на день
N+30. В последующих строках привести купленные лоты в таком же формате,
который используется во входных данных. Последняя строка должна быть пустой.

135
2 alfa-05 101.5 5
2 gazprom-17 100.0 2


Дополнительно необходимо указать:
1. оценку необходимой памяти для его выполнения (можно экспериментально измерить)
2. ограничения на размер входных параметров, при которых алгоритм будет
выполняться разумное время (до 5 секунд, например)
3. (если есть) использованные сторонние пакеты для оптимизированной версии (requirements.txt).

Опционально: сравнить неоптимизированную (чистый Python) и оптимизированную реализацию.


## Рассмотренные подходы к оптимизации
1. Использование типов `NumPy` - для хранения данных 
используются типы `numpy.int32` и `numpy.float32`. Данный
подход работает медленнее, чем встроенные типы.  Это связано
с тем, что динамическое программирование предполагает
последовательное решение подзадач на предыдущих шагах,
т.е. возникает зависимость по данным в предшествующие
моменты времени, из чего следует невозможность
использования быстрых векторизованных операций `numpy` над
всем скопом данных сразу.
2. Попытка использования `numba` не увенчалась успехом, 
потому что она "стремно" работает с классами, а переписывать
по 10 раз один и тот же код как-то не круто.
3. Так как задача динамического программирования — это
рекурсивная задача, то можно написать код для ее решения
в виде рекурсии и использовать `кэширование` рекурсивных
вызовов.

В итоге сравнение производиться между обычным алгоритмом
(не рекурсивным) и рекурсивным с использованием кэширования.

## Структура проекта
* [interfaces](interfaces)- директория, содержащая
абстрактные классы для инвестора и облигаций.
* [pure_python](pure_python) - содержит файлы для работы с инвестором
и облигациями, используюя только встроенные типы данных 
python.
* [with_numpy_types](with_numpy_types) - аналогично
`pure_python`, только с типами `numpy`.
* [test_files](test_files) - тестовые входные данные.
* [optimization_algorithms.py](optimization_algorithms.py) -
файл, который содержит описанные алгоритмы динамического
программирования.
* [main.py](main.py) - основной файл, который обрабатывает
данные.

## Запуск
`Обязательные` параметры запуска:
* `-i` - путь к `.txt` файлу, которые содержит входные данные.
* `-o` - путь к `директории`, в которую будет сохранен
файл с результатами.

`Не обязательные` параметры запуска:
* `-a` - текущий тип алгоритма:
    * `base` - не рекурсивный алгоритм
    * `base_recursive` - рекурсивный алгоритм без кэширования
    (работает медленнее, чем `base`)
    * `opt` - рекурсивный алгоритм с кэшированием
* `-use_numpy_types` - использование типов `numpy`:
    * `0` - не использовать
    * `1` - использовать
    
Пример командной строки:
```bash
python main.py -a opt -i test_files\random_data_small.txt -o C:\study\script_languages -use_numpy_types 0
```
