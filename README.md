# Конфигурационное управление

## Домашнее задание №4

**Вариант №5**

Разработать ассемблер и интерпретатор для учебной виртуальной машины (УВМ). Система команд УВМ представлена далее.

Для ассемблера необходимо разработать читаемое представление команд УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к которой задается из командной строки.

Результатом работы ассемблера является бинарный файл в виде последовательности байт, путь к которому задается из командной строки.

Дополнительный ключ командной строки задает путь к файлу-логу, в котором хранятся ассемблированные инструкции в духе списков “ключ=значение”, как в приведенных далее тестах.

Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон также указывается из командной строки.

Форматом для файла-лога и файла-результата является csv.

Необходимо реализовать приведенные тесты для всех команд, а также написать и отладить тестовую программу.

**Загрузка константы**

| A | B | C |
|---|---|---|
| Биты 0—7 | Биты 8—12 | Биты 13—31 |
| 201 | Адрес | Константа |

Размер команды: 4 байт. Операнд: поле C. Результат: регистр по адресу, которым является поле B.

Тест (A=201, B=22, C=836):

0xC9, 0x96, 0x68, 0x00


**Чтение значения из памяти**

| A | B | C |
|---|---|---|
| Биты 0—7 | Биты 8—12 | Биты 13—17 |
| 57 | Адрес | Адрес |

Размер команды: 3 байт. Операнд: значение в памяти по адресу, которым является регистр по адресу, которым является поле C. Результат: регистр по адресу, которым является поле B.

Тест (A=57, B=8, C=30):

0x39, 0xC8, 0x03


**Запись значения в память**

| A | B | C |
|---|---|---|
| Биты 0—7 | Биты 8—12 | Биты 13—17 |
| 27 | Адрес | Адрес |

Размер команды: 3 байт. Операнд: регистр по адресу, которым является поле C. Результат: значение в памяти по адресу, которым является регистр по адресу,которым является поле B.

Тест (A=27, B=9, C=23):

0x1B, 0xE9, 0x02


**Бинарная операция: побитовый логический сдвиг вправо**

| A | B | C | D |
|---|---|---|---|
| Биты 0—7 | Биты 8—21 | Биты 22—26 | Биты 27—31 |
| 113 | Адрес | Адрес | Адрес |

Размер команды: 4 байт. Первый операнд: регистр по адресу, которым является поле D. Второй операнд: регистр по адресу, которым является поле C. Результат: значение в памяти по адресу, которым является поле B.

Тест (A=113, B=387, C=6, D=12):

0x71, 0x83, 0x81, 0x61

Тестовая программа: Выполнить поэлементно операцию побитовый логический сдвиг вправо над двумя векторами длины 8. Результат записать в новый вектор.


## Описание работы программы программы

Данная программа реализует ассемблер и интерпретатор для учебной виртуальной машины. В ассемблер подаётся программа на обработку и на выходе программы создаётся файл логов и бинарное представление программы. В интерпретаторе производится обработка программы в бинарном представлении и на выходе создаётся файл в формате CSV.


## Запуск программы

Запуск программы осуществляется из командной строки:
```
python ass.py program.txt program.bin program_log.csv
python interpreter.py program.bin result.csv 0-31
```
где:
* program.txt - файл с программой для обработки
* program.bin - файл с бинарным представлением программы
* program_log.csv - файл логов работы программы-ассемблера
* result.csv - файл результата работы программы в CSV формате
* 0-31 - байты, используемые для интерпретации бинарного файла

Для запуска юнит-тестов в коммандной строке необходимо написать:
```
python -m unittest test_assembler.py test_interpreter.py
```


## Результат юнит-тестов программы

![img.png](images/tests.png)

## Результат работы программы

![img.png](images/ass.png)

![img.png](images/interpreter.png)
