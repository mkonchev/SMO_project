class Sourse:
    """   Источник заявки   """
    id: int
    order_count: int
    gen_time: float

    def __init__(self, id: int, order_count: int):
        self.id = id
        self.order_count = order_count

    def get_source_id(self):
        return self.id

    def gen_order(self):
        self.order_count += 1

    def get_order_count(self):
        return self.order_count
