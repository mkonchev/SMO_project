from src.buffer_dir.buffer_item import BufferItem
from src.order_dir.order import Order


class Buffer:
    """   Буфер   """
    items: list[BufferItem]
    capacity: int

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = [BufferItem(i) for i in range(capacity)]

    def has_empty_items(self) -> bool:
        for item in self.items:
            if item.is_empty():
                return True
        return False

    def add_order(self, order: Order) -> None:
        for item in self.items:
            if item.is_empty():
                item.insert_order(order)

