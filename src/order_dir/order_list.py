from src.order_dir.order import Order


class OrderList:
    """   Список заявок   """
    orders = list[Order]

    def __init__(self, capacity: int):
        self.items = [Order(i) for i in range(capacity)]

