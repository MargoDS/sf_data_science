# Проект 3. Разведывательный анализ данных и проектирование признаков для построения модели машинного обучения
На примере базы данных отзывов с сайта 
[Booking.com](https://www.booking.com/)

[к проекту](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/Project_3_Kravchenko_v.final.ipynb):arrow_right:

## Оглавление
[1.Описание проекта](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Описание-проекта)

[2.Какой кейс решаем?](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Какой-кейс-решаем)

[3.Краткая информация о данных](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Краткая-информация-о-данных)

[4.Этапы работы над проектом](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Этапы-работы-над-проектом)

[5.Результат](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Результат)

### Описание проекта
Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

Вам поставлена задача создать такую модель.

### Какой кейс решаем?
Необходимо обработать датасет, в котором содержатся сведения о 515 000 отзывов на отели Европы. 
Модель, которую нужно будете обучать, должна предсказывать рейтинг отеля по данным сайта Booking на основе имеющихся в датасете данных. 

Необходимо обосновать и применить инструменты разведывательного анализа данных (EDA), обработки имеющихся и создания новых признаков.

### Краткая информация о данных:
Ссылка страницу с данными: https://www.kaggle.com/competitions/sf-booking/data
В своей работе я использовала только файл hotels_train.csv
Это датасет размером около 400 тыс. строк с информацией об отзывах, рецензентах и отелях, на которые предоставлены отзывы. 

### Этапы работы над проектом:
1) Базовый анализ структуры данных
2) Разведывательный анализ данных. 
На этом этапе я исследовала каждый признак и выдвигала гипотезы о его возможной важности при построении модели предсказания целевого признака. 
3) Создание новых признаков. 
Параллельно с предыдущим этапом, по мере анализа существующих признаков, происходило формирование новых.
4) Анализ полученных признаков на мультиколлинеарность и оценка значимости.
5) Построения модели предсказания целевой переменной и оценка итоговых метрик.

### Результат
В результате работы над проектом удалось реализовать и оценить значимость для модели различных методов обработки и конструирования признаков. 
Попробовать разные подходы к обработке одних и тех же данных и выбрать наиболее эффективные.

:arrow_up:[к оглавлению](https://github.com/MargaritaKr/sf_data_science/blob/main/project_3_EDA/README.md#Оглавление)
