from device import Device
from src.order_dir.order import Order


class DeviceList:
    device_list = list[Device]

    def __init__(self, num_of_devices: int, lambda_: int, mode_: bool):
        self.device_list = [Device(i, lambda_, mode_) for i in range(num_of_devices)]

    def has_device(self) -> bool:
        for device in self.device_list:
            if device.is_ready():
                return True
        return False

    def first_device(self) -> Device:
        for device in self.device_list:
            if device.is_ready():
                return device

    def order_to_device(self, order: Order, time: float):
        self.first_device().start_handle_order(order, time)

