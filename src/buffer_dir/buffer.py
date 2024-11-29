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

    def add_order_to_buffer(self, order: Order, mode: bool) -> None:  # Запись в буфер
        if self.has_empty_items():
            for item in self.items:
                if item.is_empty():
                    item.insert_order(order)
                    if mode:
                        print(
                            f'В буффер поступила заявка {order.get_id()},'
                            f' источником: {order.get_source_id()} в ячейку'
                            f' : {item.get_id()}')
                    return
        return

    def is_empty(self) -> bool:
        for buffer_item in self.items:
            if not buffer_item.is_empty():
                return False
        return True

    def remove_order(self):  # Выборка из буфера приоритет по номеру источника, по одной заявке
        min_source_id = sys.int_info.default_max_str_digits
        deleted_item: BufferItem = None
        for item in self.items:
            if not item.is_empty():
                order = item.get_order()
                order_source_id = order.get_source_id()
                if order_source_id < min_source_id:
                    min_source_id = order_source_id
                    deleted_item = item
        deleted_item.delete_order()
        return order
