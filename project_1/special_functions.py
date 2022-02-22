# функция обработки столбца с данными о вакансиях:
def get_profession(data_str):
    """Selection of a profession
       Args:
           data_string (str): A string of data
       Returns:
           (str): Profession
           :param data_str:
       """

    data_s = data_str.lower()
    data_s = data_s.replace('c', 'с')

    junior_list = ['младший специалист', 'стажер', 'помощник', 'начинающий', 'junior']
    if True in list(map(lambda x: x in data_s, junior_list)):
        return 'Начинающий специалист'

    manager_list = ['начальник', 'директор', 'руководитель', 'менеджер проект', 'manager', 'главный специалист',
                    'администратор проектов', 'менеджер it-проектов', 'координатор', 'ведущий специалист',
                    'менеджер по управлен', 'проектный менеджер', 'региональный менеджер',
                    'менеджер по развитию бизнеса']
    if True in list(map(lambda x: x in data_s, manager_list)):
        return 'Руководитель'

    if ('менеджер' in data_s and ('продаж' in data_s or 'магазин' in data_s)) or data_s == 'менеджер' \
            or 'продавец' in data_s or data_s == 'региональный представитель' or data_s == 'специалист по продажам':
        return 'Менеджер по продажам'

    if 'системный администратор' in data_s or 'сетевой администратор' in data_s or data_str == 'Администратор':
        return 'Системный администратор'

    if 'тестир' in data_s:
        return 'Тестировщик'

    if 'программист' in data_s or 'разработчик' in data_s or 'developer' in data_s:
        return 'Программист'

    if 'инженер' in data_s or 'engineer' in data_s:
        return 'Инженер'

    if 'верстальщик' in data_s:
        return 'Верстальщик'

    if 'data' in data_s or 'аналитик дан' in data_s:
        return 'Data scientist'

    if 'дизайн' in data_s or 'худож' in data_s or 'design' in data_s:
        return 'Дизайнер'

    if 'аналитик' in data_s:
        return 'Аналитик'

    if 'оператор' in data_s or data_s == 'специалист по вводу данных':
        return 'Оператор'

    if ('специалист' in data_s and 'поддержк' in data_s) or ('сопровожден' in data_s and 'клиент' in data_s) or\
            'helpdesk' in data_s:
        return 'Специалист технической поддержки'

    if ('специалист' in data_s and ('it' in data_s or 'ит' in data_s)) or ('специалист' in data_s and 'техн' in data_s)\
            or data_s == 'специалист' or 'техник' in data_s or 'мастер' in data_s or 'механик' in data_s \
            or 'монтаж' in data_s or 'монтер' in data_s:
        return 'Технический специалист'

    if ('интернет' in data_s and 'маркет' in data_s) or 'seo' in data_s or 'трафик' in data_s:
        return 'SEO-специалист'

    if 'работ' in data_s and 'клиент' in data_s:
        return 'Специалист по работе с клиентами'

    if data_s == 'веб-дизайнер' or data_s == 'web-дизайнер':
        return 'Web-дизайнер'

    if 'модератор' in data_s or data_s == 'стратор сайт':
        return 'Модератор'

    if 'контент' in data_s or 'аккаунт' in data_s or 'редактор' in data_s:
        return 'Контент-менеджер'

    data_ls = data_str.split(' / ')
    return data_ls[0]
