from sideko_octa_api_64_py.core import AsyncBaseClient, SyncBaseClient
from sideko_octa_api_64_py.resources.v3.ca import AsyncCaClient, CaClient


class V3Client:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.ca = CaClient(base_client=self._base_client)


class AsyncV3Client:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.ca = AsyncCaClient(base_client=self._base_client)
