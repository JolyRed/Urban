class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

def generate_exception(arg):
    if arg == 1:
        raise InvalidDataException("Неверные данные")
    elif arg == 2:
        raise ProcessingException("Ошибка обработки")
    else:
        return "Успешно"

def handle_exception(arg):
    try:
        result = generate_exception(arg)
    except InvalidDataException:
        print("Обработка исключения InvalidDataException")
        raise  
    except ProcessingException:
        print("Обработка исключения ProcessingException")
        raise  
    else:
        print(f"Результат: {result}")

def main():
    try:
        handle_exception(1)
        handle_exception(2)
        handle_exception(3)
    except InvalidDataException:
        print("Исключение InvalidDataException передано в main")
    except ProcessingException:
        print("Исключение ProcessingException передано в main")
    finally:
        print("Блок finally всегда выполняется, вне зависимости от исключений")

if __name__ == "__main__":
    main()
