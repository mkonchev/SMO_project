from src.order_dir.order import Order
from random import random
from math import log


class Device:
    """   Прибор   """
    id: int
    lambda_: int
    start_time: float
    end_time: float
    total_time: float
    order: Order
    total_orders: int
    ready: bool
    mode: bool

    def __init__(self, id_: int, lambda_: int, mode_: bool):
        self.id = id_
        self.lambda_ = lambda_
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.order = None
        self.total_orders = 0
        self.ready = True
        self.mode = mode_

    def get_device_id(self):
        return self.id

    def get_total_orders(self):
        return self.total_orders

    def is_ready(self):
        return self.ready

    def get_total_time(self):
        return self.total_time

    def get_end_time(self):
        return self.end_time

    def start_handle_order(self, order: Order, time: float):
        self.order = order
        self.start_time = time
        total_time_ = (-1 / self.lambda_) * log(random())
        self.end_time = time + self.total_time
        self.total_time += total_time_
        self.ready = False
        if self.mode:
            print(f'Заявка {order.get_full_id()} направлена на прибор {self.id} '
                  f'в {time}, прибор обработает заявку в {self.end_time}')

    def end_handle_order(self):
        if self.mode:
            print(f'Заявка {self.order.get_full_id()} обработана в {self.get_end_time()}'
                  f' прибором {self.get_device_id()}')
        self.total_time =

