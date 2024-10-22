import inspect


def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes_and_methods = dir(obj)
    methods = [attr for attr in attributes_and_methods if callable(getattr(obj, attr))]
    attributes = [attr for attr in attributes_and_methods if not callable(getattr(obj, attr))]

    module = inspect.getmodule(obj)
    module_name = module.__name__ if module else '__main__'

    other_properties = {}
    if hasattr(obj, '__doc__'):
        other_properties['doc'] = obj.__doc__
    if hasattr(obj, '__class__'):
        other_properties['class'] = obj.__class__.__name__
    if hasattr(obj, '__dict__'):
        other_properties['instance_variables'] = obj.__dict__
    if hasattr(obj, '__name__'):
        other_properties['name'] = obj.__name__
    if hasattr(obj, '__qualname__'):
        other_properties['qualname'] = obj.__qualname__

    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
        'other_properties': other_properties
    }

    return info


number_info = introspection_info(42)
print(number_info)

class_info = introspection_info(int)
print(class_info)

list_info = introspection_info([1, 2, 3])
print(list_info)
