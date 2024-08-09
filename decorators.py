#task 4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Provide me your name & phone, please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "At least 1 argument (name) is required."

    return inner