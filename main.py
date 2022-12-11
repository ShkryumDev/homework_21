from exceptions import BaseError
from structure.courier import Courier
from structure.request import Request
from structure.shop import Shop
from structure.store import Store

shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 15
    }
)

store = Store(
    items={
        'печенька': 10,
        'ноутбук': 20
    }
)

storages = {
    'Магазин': shop,
    'Склад': store
}


def main():
    while True:

        for storage_name in storages:
            print(f'{storage_name} хранит: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печеньки из склада в магазин".\n'
            'Введите "stop" или "стоп", чтобы продолжить:\n'
        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)

            courier = Courier(request=request, storages=storages)
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
