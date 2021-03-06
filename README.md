# Зависимость между количеством ошибок и показателями сложности текста

Структура репозитория:
* Inspector
* R

## Inspector

В этой папке находятся все вспомогательные файлы Инспектора. Кроме того, здесь находится папка *exam*, в которой должна быть размещена версия REALEC'а, соотносимая с названиями эссе из исследуемого датасета.

В папке *table* находятся таблицы с исследуемыми эссе следующего вида:

| text_name     | errors |   |
|---------------|--------|---|
| .             |        |   |
| .             |        |   |
| .             |        |   |
| One Error     |        | x |
| Four and more |        | y |

Сам Инспектор запускается из файл *main.py*. Там есть несколько функций, которые отвечают за создание датасетов. Кроме того, здесь же находятся примеры полученных датасетов про синтаксис: *dataset_syntax.csv*, *dataset_syntax_1.csv*, *dataset_syntax_2.csv*.

UPD: ВАЖНО! для корректной работы Инспектора тебуется scikit-learn версии 0.21.2

## R

В папке находится директория *datasets*, в которую кладутся файлы, полученные из *main.py* в предыдущем пункте.

Сам код состоит из подключения пакетов, функции и её запуска.

Чтобы установить необходимые пакеты необходимо дописать строки следующего вида:

```R
install.packages("PACKAGE_NAME")
```

Функция работает следующим образом:

* считываем датасеты в датафреймы
* убираем столбец с именем (он нам не понадобится при обучении модели)
* обучаем модель
* получаем результаты с помощью функции `stargazer` из одноимённого пакета
* результаты записываются в файл *regression_results.html*
* также можно получить не HTML код таблицы, а код для вставки в Latex: для этого нужно удалить аргумент `type`. Сами авторы пакета предлагают копировать таблицы в `.docx` через срендеренный HTML, в целом удобно, но как-то костыльно, попробую потом сразу в Word писать

Примеры для R также есть в папке.
