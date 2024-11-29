from src.source_dir.source_list import SourceList
from src.source_dir.source import Sourse
from src.device_dir.device_list import DeviceList
from src.buffer_dir.buffer import Buffer
from src.buffer_dir.buffer_item import BufferItem
from src.table import Table
from math import log
from random import random


class Processes:
    def __init__(self, num_of_orders: int,
                 num_of_devices: int,
                 num_of_sources: int,
                 buffer_capacity: int,
                 lambda_: float,
                 a: int, b: int, mode: bool):
        self.stats = Table(num_of_sources, mode)
        self.source_list = SourceList(num_of_sources, a, b)
        self.device_list = DeviceList(num_of_devices, lambda_, mode)
        self.buffer = Buffer(buffer_capacity)
        self.order_list = [source.order_generate() for source in self.source_list.source_list]
        self.num_of_orders = num_of_orders
        self.gen_orders = 0
        self.time = 0
        self.lambda_ = lambda_
        self.a = a
        self.b = b
        self.mode = True

    def auto_sim(self):
        while self.gen_orders < self.num_of_orders:
            self.order_proc()

        while not self.device_list.are_all_available() or not self.buffer.is_empty():
            self.time = (-1 / self.lambda_ * log(random()))
            self.device_list.manage_finished_devices(self.time + 0.5)
            while not self.buffer.is_empty() and self.device_list.has_device():
                first_order_in_buffer = self.buffer.remove_order()
                self.device_list.order_to_device(first_order_in_buffer, self.time)
                self.stats.add_order_waiting_time(first_order_in_buffer, self.time)

    def order_proc(self):
        print('Календарь событий')
        for order in self.order_list:
            print(
                f"Генерация заявки: источник {order.get_source_id()},"
                f" заявка №{order.get_id()}, время генерации {order.get_time():.2f}"
            )
        for device in self.device_list.device_list:
            print(
                f'Прибор номер: {device.get_device_id()}, работоспособность: {device.is_ready()}'
            )
        for buffer in self.buffer.items:
            print(
                f'Номер ячейки буфера: {buffer.id}, состояние: {buffer.is_empty()}'
            )
        earliest_order = self.order_list.pop(self.order_list.index(min(self.order_list, key=lambda x: x.time)))
        self.stats.add_generated_order(earliest_order)
        self.gen_orders += 1
        self.time = earliest_order.get_time()

        source_id = earliest_order.get_source_id()
        order_number = self.gen_orders
        gen_time = earliest_order.get_time()

        if self.stats.mode:
            print('Заявка с наименьшим временем:')
            print(f"Генерация заявки: источник {source_id}, заявка №{order_number}, время генерации {gen_time:.2f}")

        self.device_list.manage_finished_devices(self.time)

        if self.buffer.is_empty() and self.device_list.has_device():
            self.device_list.order_to_device(earliest_order, self.time)
        elif not self.device_list.has_device():
            self.buffer.add_order_to_buffer(earliest_order, self.time)
        else:
            while not self.buffer.is_empty() and self.device_list.has_device():
                first_order_in_buffer = self.buffer.remove_order()
                self.device_list.order_to_device(first_order_in_buffer, self.time)
                self.stats.add_order_waiting_time(first_order_in_buffer, self.time)
            if self.device_list.has_device():
                self.device_list.order_to_device(earliest_order, self.time)
            else:
                self.buffer.add_order_to_buffer(earliest_order, self.time)
        self.order_list.append(self.source_list.get_source_by_id(earliest_order.get_source_id()).order_generate())
