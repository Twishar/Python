
"""

    __str__(self)
    Определяет поведение функции str(), вызванной для экземпляра вашего класса.

    __repr__(self)
    Определяет поведение функции repr(), вызыванной для экземпляра вашего класса.
    Главное отличие от str() в целевой аудитории.
    repr() больше предназначен для машинно-ориентированного вывода(более того, это часто должен быть валидный код на Питоне)
    , а str() предназначен для чтения людьми.

    __unicode__(self)
    Определяет поведение функции unicode(), вызыванной для экземпляра вашего класса. unicode() похож на str(),
    но возвращает строку в юникоде. Будте осторожны: если клиент вызывает str() на экземпляре вашего класса,
    а вы определили только __unicode__(), то это не будет работать.
    Постарайтесь всегда определять __str__() для случая, когда кто-то не имеет такой роскоши как юникод.

    __format__(self, formatstr)
    Определяет поведение, когда экземпляр вашего класса используется в форматировании строк нового стиля.
    Например, "Hello, {0:abc}!".format(a) приведёт к вызову a.__format__("abc").
    Это может быть полезно для определения ваших собственных числовых или строковых типов,
    которым вы можете захотеть предоставить какие-нибудь специальные опции форматирования.

    __hash__(self)
    Определяет поведение функции hash(), вызыванной для экземпляра вашего класса.
    Метод должен возвращать целочисленное значение, которое будет использоваться для быстрого сравнения ключей в словарях.
    Заметьте, что в таком случае обычно нужно определять и __eq__ тоже.
    Руководствуйтесь следующим правилом: a == b подразумевает hash(a) == hash(b).

    __nonzero__(self)
    Определяет поведение функции bool(), вызванной для экземпляра вашего класса.
    Должна вернуть True или False, в зависимости от того, когда вы считаете экземпляр соответствующим True или False.

    __dir__(self)
    Определяет поведение функции dir(), вызванной на экземпляре вашего класса.
    Этот метод должен возвращать пользователю список атрибутов.
    Обычно, определение __dir__ не требуется, но может быть жизненно важно для интерактивного использования вашего класса,
    если вы переопределили __getattr__ или __getattribute__ , или каким-либо другим образом динамически создаёте атрибуты.

    __sizeof__(self)
    Определяет поведение функции sys.getsizeof(), вызыванной на экземпляре вашего класса.
    Метод должен вернуть размер вашего объекта в байтах.
    Он главным образом полезен для классов, определённых в расширениях на C, но всё-равно полезно о нём знать.

"""