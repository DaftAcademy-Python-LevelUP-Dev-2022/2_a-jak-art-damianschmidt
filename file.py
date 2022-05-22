def greeter(func):
    def wrapper(*args):
        name = func(*args)
        greetings = f"Aloha {name.title()}"
        return greetings

    return wrapper


def sums_of_str_elements_are_equal(func):
    def wrapper(*args):
        num1, num2 = func(*args).split()
        sum_of_num1 = sum([int(char) for char in num1 if char != "-"])
        sum_of_num2 = sum([int(char) for char in num2 if char != "-"])

        if "-" in num1:
            sum_of_num1 *= -1
        if "-" in num2:
            sum_of_num2 *= -1

        sign = "==" if sum_of_num1 == sum_of_num2 else "!="
        return f"{sum_of_num1} {sign} {sum_of_num2}"

    return wrapper


def format_output(*required_keys):
    def decorator(func):
        def wrapper(*args):
            data = func(*args)
            formatted_dict = {}
            for keys in required_keys:
                try:
                    found_data = " ".join(
                        data[key] if data[key] else "Empty value" for key in
                        keys.split("__"))
                except KeyError:
                    raise ValueError
                formatted_dict[keys] = found_data
            return formatted_dict

        return wrapper

    return decorator


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args):
            return func()

        setattr(klass, func.__name__, wrapper)
        return wrapper

    return decorator
