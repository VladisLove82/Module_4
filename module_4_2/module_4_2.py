def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return test_function()


inner_function() # Ошибка возникает из за того, что наша функция inner_function() не определена
