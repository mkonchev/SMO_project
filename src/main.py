from math import log
from random import random

from src.buffer_dir.buffer import Buffer
from src.buffer_dir.buffer_item import BufferItem
from src.order_dir.order import Order
from src.source_dir.source_list import SourceList
from src.source_dir.source import Sourse
from src.device_dir.device_list import DeviceList
from src.processes import Processes

if __name__ == '__main__':
    num_of_orders = 1000
    num_of_devices = 3
    num_of_sources = 3
    buffer_capacity = 10
    lambda_ = 1.3  # Для экспоненциального распределения времени обслуживания
    a = 2  # для равномерного распределения источников
    b = 1.5  # для равномерного распределения источников
    mode = True  # True - пошаговый    False - автоматический

    # source_list = SourceList(num_of_sources, a, b)
    # device_list = DeviceList(num_of_devices, lambda_, mode)
    # buffer = Buffer(buffer_capacity)
    # order_list = [source.generate_order() for source in source_list]
    # gen_orders = 0
    # time = 0
    # mode = True

    model = Processes(num_of_orders,
                      num_of_devices,
                      num_of_sources,
                      buffer_capacity,
                      lambda_, a, b, mode)
    if mode:
        model.auto_sim()
    else:
        model.step_sim()

