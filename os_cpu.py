import os


def os_cpu() -> str:
    s = "cpu count = {}".format(os.cpu_count())
    return s
