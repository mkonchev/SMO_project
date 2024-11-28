import sys

from src.buffer_dir.buffer_item import BufferItem
from src.order_dir.order import Order


class Buffer:
    """   Буфер   """
    items: list[BufferItem]
    capacity: int
    mode: bool

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items = [BufferItem(i) for i in range(capacity)]

    def has_empty_items(self) -> bool:
        for item in self.items:
            if item.is_empty():
                return True
        return False

    def add_order(self, order: Order) -> None:  # Запись в буфер
        for item in self.items:
            if item.is_empty():
                item.insert_order(order)

    def remove_order(self):  # Выборка из буфера приоритет по номеру источника, по одной заявке
        order: Order = None
        min_source_id = sys.int_info.default_max_str_digits
        deleted_item: BufferItem = None
        for item in self.items:
            if not item.is_empty():
                order_source_id = order.get_source_id()
                if order_source_id < min_source_id:
                    min_source_id = order_source_id
                    order = item.get_order()
                    deleted_item = item
        deleted_item.delete_order()
        return order
