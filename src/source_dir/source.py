import random as rnd

from src.order_dir.order import Order


class Sourse:
    """   Источник заявки   """
    id: int
    order_count: int = 0
    a: int
    b: int
    prev_gen_time: float

    def __init__(self, id_: int, a_: int, b_: int):
        self.id = id_
        self.a = a_
        self.b = b_
        self.prev_gen_time = 0.0

    def get_id(self):
        return self.id

    def gen_order_count(self):
        self.order_count += 1

    def get_gen_order_count(self):
        return self.order_count

    def order_generate(self) -> Order:
        self.prev_gen_time = (self.b - self.a) * rnd.random() + self.a
        order = Order(self.order_count, self.id, self.prev_gen_time)
        self.order_count = self.order_count+1
        return order
