import typing

from sideko_octa_api_64_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.acknowledge import (
    AcknowledgeClient,
    AsyncAcknowledgeClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.acknowledge_lines import (
    AcknowledgeLinesClient,
    AsyncAcknowledgeLinesClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.cancel import (
    AsyncCancelClient,
    CancelClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.multi_package_shipping import (
    AsyncMultiPackageShippingClient,
    MultiPackageShippingClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.refund import (
    AsyncRefundClient,
    RefundClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.released import (
    AsyncReleasedClient,
    ReleasedClient,
)
from sideko_octa_api_64_py.resources.v3.ca.orders.shipping import (
    AsyncShippingClient,
    ShippingClient,
)


class OrdersClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.released = ReleasedClient(base_client=self._base_client)
        self.acknowledge = AcknowledgeClient(base_client=self._base_client)
        self.acknowledge_lines = AcknowledgeLinesClient(base_client=self._base_client)
        self.cancel = CancelClient(base_client=self._base_client)
        self.multi_package_shipping = MultiPackageShippingClient(
            base_client=self._base_client
        )
        self.refund = RefundClient(base_client=self._base_client)
        self.shipping = ShippingClient(base_client=self._base_client)

    def list(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        created_start_date: str,
        created_end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_order_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_expected_ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product_info: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_order_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sku: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_expected_ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Get all orders

        Retrieves the details of all the orders for specified search criteria.
        Value of nextCursor to be used as query parameter for getting next set of purchase orders, when more than 200 orders are retrieved.
        For Ex: If the nextCursor value is ?limit=10&amp;soIndex=2&amp;poIndex=2&amp, then in order to get next set of records , call by appending the nextCursor value in request URL /v3/ca/orders?limit=10&amp;soIndex=2&amp;poIndex=2&amp.

        GET /v3/ca/orders

        Args:
            createdEndDate: Limits orders returned to those created before this createdEndDate. Two formats, based on ISO 8601, are allowed: UTC date or timestamp. Examples: '2016-08-16T10:30:30.155Z' or '2016-08-16'.
            customerOrderId: The customer order ID
            fromExpectedShipDate: Limits orders returned to those that have orderLines with an expected ship date after this fromExpectedShipDate. Format: YYYY-MM-DD
            limit: The number of orders to be returned.Cannot be larger than 200.
            productInfo: Provides the image URL and product weight in response, if available. This parameter must be boolean, e.g.: productInfo=true.
            purchaseOrderId: The purchase order ID. One customer may have multiple purchase orders.
            sku: A seller-provided Product ID
            status: Status may be specified to return orders of that type. Valid statuses are: Created, Acknowledged, Shipped, and Cancelled.
            toExpectedShipDate: Limits orders returned to those that have orderLines with an expected ship date before this toExpectedShipDate. Format: YYYY-MM-DD
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            createdStartDate: Start Date for querying all purchase orders after that date. Use one of the following formats, based on UTC, ISO 8601. Date example: '2013-08-16' Timestamp example: '2013-08-16T10:30:15Z'
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v3.ca.orders.list(
            wm_consumer_channel_type="string",
            wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
            wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
            wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
            wm_sec_timestamp="1443748249449",
            wm_svc_name="Walmart Service Name",
            created_start_date="string",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "createdStartDate",
            to_encodable(item=created_start_date, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(created_end_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "createdEndDate",
                to_encodable(item=created_end_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(customer_order_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customerOrderId",
                to_encodable(item=customer_order_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_expected_ship_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromExpectedShipDate",
                to_encodable(item=from_expected_ship_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(product_info, type_utils.NotGiven):
            encode_query_param(
                _query,
                "productInfo",
                to_encodable(item=product_info, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(purchase_order_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "purchaseOrderId",
                to_encodable(item=purchase_order_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(sku, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sku",
                to_encodable(item=sku, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_expected_ship_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toExpectedShipDate",
                to_encodable(item=to_expected_ship_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        return self._base_client.request(
            method="GET",
            path="/v3/ca/orders",
            query_params=_query,
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        purchase_order_id: str,
        product_info: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Get an order

        Retrieves an order detail for a specific purchaseOrderId

        GET /v3/ca/orders/{purchaseOrderId}

        Args:
            productInfo: Provides the image URL and product weight in response, if available. This parameter must be boolean, e.g.: productInfo=true.
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            purchaseOrderId: The purchase order ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v3.ca.orders.get(
            wm_consumer_channel_type="string",
            wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
            wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
            wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
            wm_sec_timestamp="1443748249449",
            wm_svc_name="Walmart Service Name",
            purchase_order_id="string",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(product_info, type_utils.NotGiven):
            encode_query_param(
                _query,
                "productInfo",
                to_encodable(item=product_info, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        return self._base_client.request(
            method="GET",
            path=f"/v3/ca/orders/{purchase_order_id}",
            query_params=_query,
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncOrdersClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.released = AsyncReleasedClient(base_client=self._base_client)
        self.acknowledge = AsyncAcknowledgeClient(base_client=self._base_client)
        self.acknowledge_lines = AsyncAcknowledgeLinesClient(
            base_client=self._base_client
        )
        self.cancel = AsyncCancelClient(base_client=self._base_client)
        self.multi_package_shipping = AsyncMultiPackageShippingClient(
            base_client=self._base_client
        )
        self.refund = AsyncRefundClient(base_client=self._base_client)
        self.shipping = AsyncShippingClient(base_client=self._base_client)

    async def list(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        created_start_date: str,
        created_end_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        customer_order_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        from_expected_ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        limit: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        product_info: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        purchase_order_id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sku: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        status: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        to_expected_ship_date: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Get all orders

        Retrieves the details of all the orders for specified search criteria.
        Value of nextCursor to be used as query parameter for getting next set of purchase orders, when more than 200 orders are retrieved.
        For Ex: If the nextCursor value is ?limit=10&amp;soIndex=2&amp;poIndex=2&amp, then in order to get next set of records , call by appending the nextCursor value in request URL /v3/ca/orders?limit=10&amp;soIndex=2&amp;poIndex=2&amp.

        GET /v3/ca/orders

        Args:
            createdEndDate: Limits orders returned to those created before this createdEndDate. Two formats, based on ISO 8601, are allowed: UTC date or timestamp. Examples: '2016-08-16T10:30:30.155Z' or '2016-08-16'.
            customerOrderId: The customer order ID
            fromExpectedShipDate: Limits orders returned to those that have orderLines with an expected ship date after this fromExpectedShipDate. Format: YYYY-MM-DD
            limit: The number of orders to be returned.Cannot be larger than 200.
            productInfo: Provides the image URL and product weight in response, if available. This parameter must be boolean, e.g.: productInfo=true.
            purchaseOrderId: The purchase order ID. One customer may have multiple purchase orders.
            sku: A seller-provided Product ID
            status: Status may be specified to return orders of that type. Valid statuses are: Created, Acknowledged, Shipped, and Cancelled.
            toExpectedShipDate: Limits orders returned to those that have orderLines with an expected ship date before this toExpectedShipDate. Format: YYYY-MM-DD
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            createdStartDate: Start Date for querying all purchase orders after that date. Use one of the following formats, based on UTC, ISO 8601. Date example: '2013-08-16' Timestamp example: '2013-08-16T10:30:15Z'
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v3.ca.orders.list(
            wm_consumer_channel_type="string",
            wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
            wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
            wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
            wm_sec_timestamp="1443748249449",
            wm_svc_name="Walmart Service Name",
            created_start_date="string",
        )
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "createdStartDate",
            to_encodable(item=created_start_date, dump_with=str),
            style="form",
            explode=True,
        )
        if not isinstance(created_end_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "createdEndDate",
                to_encodable(item=created_end_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(customer_order_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "customerOrderId",
                to_encodable(item=customer_order_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(from_expected_ship_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fromExpectedShipDate",
                to_encodable(item=from_expected_ship_date, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(product_info, type_utils.NotGiven):
            encode_query_param(
                _query,
                "productInfo",
                to_encodable(item=product_info, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(purchase_order_id, type_utils.NotGiven):
            encode_query_param(
                _query,
                "purchaseOrderId",
                to_encodable(item=purchase_order_id, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(sku, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sku",
                to_encodable(item=sku, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(status, type_utils.NotGiven):
            encode_query_param(
                _query,
                "status",
                to_encodable(item=status, dump_with=str),
                style="form",
                explode=True,
            )
        if not isinstance(to_expected_ship_date, type_utils.NotGiven):
            encode_query_param(
                _query,
                "toExpectedShipDate",
                to_encodable(item=to_expected_ship_date, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        return await self._base_client.request(
            method="GET",
            path="/v3/ca/orders",
            query_params=_query,
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        purchase_order_id: str,
        product_info: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Get an order

        Retrieves an order detail for a specific purchaseOrderId

        GET /v3/ca/orders/{purchaseOrderId}

        Args:
            productInfo: Provides the image URL and product weight in response, if available. This parameter must be boolean, e.g.: productInfo=true.
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            purchaseOrderId: The purchase order ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v3.ca.orders.get(
            wm_consumer_channel_type="string",
            wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
            wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
            wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
            wm_sec_timestamp="1443748249449",
            wm_svc_name="Walmart Service Name",
            purchase_order_id="string",
        )
        ```
        """
        _query: QueryParams = {}
        if not isinstance(product_info, type_utils.NotGiven):
            encode_query_param(
                _query,
                "productInfo",
                to_encodable(item=product_info, dump_with=str),
                style="form",
                explode=True,
            )
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        return await self._base_client.request(
            method="GET",
            path=f"/v3/ca/orders/{purchase_order_id}",
            query_params=_query,
            headers=_header,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
