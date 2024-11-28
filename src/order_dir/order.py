class Order:
    """   Заявка   """
    id: int
    source_id: int
    time: float

    def __init__(self, order_id: int, source_id: int, time: float):
        self.id = order_id
        self.source_id = source_id
        self.time = time

    def get_order_id(self) -> int:
        return self.id

    def get_source_id(self) -> int:
        return self.source_id

    def get_time(self) -> float:
        return self.time