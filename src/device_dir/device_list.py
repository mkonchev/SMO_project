from src.device_dir.device import Device
from src.order_dir.order import Order


class DeviceList:
    device_list = list[Device]

    def __init__(self, num_of_devices: int, lambda_: float, mode_: bool):
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

    def manage_finished_devices(self, time: float) -> None:
        for device in sorted(self.device_list, key=lambda device_: device_.get_end_time()):
            if device.is_ready() == False and device.get_end_time() < time:
                device.end_handle_order()

    def are_all_available(self) -> bool:
        for device in self.device_list:
            if not device.is_ready():
                return False
        return True
