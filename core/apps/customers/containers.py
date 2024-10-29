from functools import lru_cache

import punq

from core.apps.customers.services.auth import BaseAuthServices, AuthService
from core.apps.customers.services.codes import BaseCodeServices, DjangoCacheCodeServices
from core.apps.customers.services.customers import BaseCustomerServices, ORMCustomerServices
from core.apps.customers.services.senders import BaseSendersServices, DummySenderServices
from core.apps.products.services.products import ORMProductServices, BaseProductServices


def _initialize_container():
    container = punq.Container()

    #initial products
    container.register(BaseProductServices, ORMProductServices)

    #initialize customers
    container.register(BaseCustomerServices, ORMCustomerServices)
    container.register(BaseSendersServices, DummySenderServices)
    container.register(BaseCodeServices, DjangoCacheCodeServices)
    container.register(BaseAuthServices, AuthService)

    return container

@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()