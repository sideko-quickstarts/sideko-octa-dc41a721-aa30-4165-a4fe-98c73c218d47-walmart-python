from sideko_octa_api_64_py.core import AsyncBaseClient, SyncBaseClient
from sideko_octa_api_64_py.resources.v3.ca.orders import AsyncOrdersClient, OrdersClient


class CaClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.orders = OrdersClient(base_client=self._base_client)


class AsyncCaClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.orders = AsyncOrdersClient(base_client=self._base_client)
