import os


def say_cpu_count() -> str:
    ss = CpuInfo()
    return ss.cpu_count()


class CpuInfo:
    def cpu_count(self):
        return "cpu count = {}".format(os.cpu_count())
