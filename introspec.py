def introspection_info(obj):
    info = {}

    info['type'] = str(type(obj)).split("'")[1]

    info['attributes'] = dir(obj)

    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]

    info['module'] = getattr(obj, '__module__', 'builtins')

    # Другие интересные свойства объекта
    if isinstance(obj, (list, tuple, set)):
        info['size'] = len(obj)
    elif isinstance(obj, dict):
        info['size'] = len(obj)
        info['keys'] = list(obj.keys())
    
    # Добавляем строковое представление, если оно существует
    if hasattr(obj, '__str__'):
        info['string_representation'] = str(obj)

    return info

# Пример использования
if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
