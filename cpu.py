import os


def get_cpu() -> str:
    s = "cpu count = {}".format(cpu_count())
    return s


def cpu_count() -> int:
    return os.cpu_count()
