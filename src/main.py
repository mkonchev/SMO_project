from math import log
from random import random

from src.buffer_dir.buffer import Buffer
from src.buffer_dir.buffer_item import BufferItem
from src.order_dir.order import Order
from src.order_dir.order_list import OrderList


if __name__ == '__main__':
    num_of_orders = 1000
    num_of_devices = 3
    num_of_sources = 3
    buffer_capacity = 10
    lambda_ = 1.3  # Для экспоненциального распределения времени обслуживания
    a = 2  # для равномерного распределения источников
    b = 1.5  # для равномерного распределения источников
    mode = True  # True - пошаговый    False - автоматический



    # if mode == True:

