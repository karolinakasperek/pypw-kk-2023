from pathlib import Path


def save_file(fn):
    def wrapper(*args, **kwargs):
        path = Path("arguments.txt")
        if path.exists():
            f = open("arguments.txt", "r")
            text = f.read()
            f.close()
        data = [fn.__name__, (args, tuple(kwargs.items()))]
        text_to_save = [text, data]
        h = open("arguments.txt", "w")
        h.writelines(text_to_save)
        h.close()
    return wrapper

