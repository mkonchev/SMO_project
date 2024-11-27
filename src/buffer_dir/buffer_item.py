from src.order_dir.order import Order


class BufferItem:
    """   Ячейка буфера   """
    id: int
    order: Order

    def __init__(self, id: int):
        self.id = id
        self.order = None

    def is_empty(self):
        return self.order is None

    def insert_order(self, order: Order):
        self.order = order

    def delete_order(self):
        deleted_order = self.order
        self.order = None
        return deleted_order

    def get_order(self):
        return self.order

    def get_id(self):
        return self.id
