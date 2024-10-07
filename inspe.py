import inspect

def introspection_info(obj):
    # Тип объекта
    obj_type = type(obj).__name__

    # Атрибуты и методы объекта
    attributes_and_methods = dir(obj)
    methods = [attr for attr in attributes_and_methods if callable(getattr(obj, attr))]

    # Модуль, к которому объект принадлежит
    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else '__main__'

    # Другие интересные свойства объекта
    other_properties = {}
    if hasattr(obj, '__doc__'):
        other_properties['doc'] = obj.__doc__
    if hasattr(obj, '__class__'):
        other_properties['class'] = obj.__class__.__name__

    # Собираем все данные в словарь
    info = {
        'type': obj_type,
        'attributes': attributes_and_methods,
        'methods': methods,
        'module': module_name,
        'other_properties': other_properties
    }

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)

class_info = introspection_info(int)
print(class_info)

list_info = introspection_info([1, 2, 3])
print(list_info)