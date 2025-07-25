import typing

from sideko_octa_api_64_py.core import (
    AsyncBaseClient,
    BinaryResponse,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_content,
)
from sideko_octa_api_64_py.types import params


class RefundClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def create(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        order_lines: params.V3CaOrdersRefundCreateBodyOrderLines,
        purchase_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Refund Order Lines

        Refunds one or more order lines that have been shipped.

        The response to a successful call contains the order with the refunded line item.

        You can only refund an order line that has a status of **Shipped**.

        The value for the **amount** element in the refund must be negative. The magnitude of the amount specified as the refund cannot be greater than the original amount that was charged for the line.

        POST /v3/ca/orders/{purchaseOrderId}/refund

        Args:
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            orderLines: V3CaOrdersRefundCreateBodyOrderLines
            purchaseOrderId: str
            purchaseOrderId: The purchase order ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.v3.ca.orders.refund.create(wm_consumer_channel_type="string", wm_consumer_id="Get the Consumer ID from Developer Center after logging in", wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6", wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=", wm_sec_timestamp="1443748249449", wm_svc_name="Walmart Service Name", order_lines={"order_line": [{"line_number": "string", "refunds": {"refund": [{"refund_charges": {}}]}}]}, purchase_order_id="string", purchase_order_id="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        _content = to_content(
            file={"order_lines": order_lines, "purchase_order_id": purchase_order_id}
        )
        _content_type = "application/xml"
        return self._base_client.request(
            method="POST",
            path=f"/v3/ca/orders/{purchase_order_id}/refund",
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncRefundClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def create(
        self,
        *,
        wm_consumer_channel_type: str,
        wm_consumer_id: str,
        wm_qos_correlation_id: str,
        wm_sec_auth_signature: str,
        wm_sec_timestamp: str,
        wm_svc_name: str,
        order_lines: params.V3CaOrdersRefundCreateBodyOrderLines,
        purchase_order_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BinaryResponse:
        """
        Refund Order Lines

        Refunds one or more order lines that have been shipped.

        The response to a successful call contains the order with the refunded line item.

        You can only refund an order line that has a status of **Shipped**.

        The value for the **amount** element in the refund must be negative. The magnitude of the amount specified as the refund cannot be greater than the original amount that was charged for the line.

        POST /v3/ca/orders/{purchaseOrderId}/refund

        Args:
            WM_CONSUMER.CHANNEL.TYPE: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
            WM_CONSUMER.ID: A unique ID required to access the API
            WM_QOS.CORRELATION_ID: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
            WM_SEC.AUTH_SIGNATURE: The vendor's digital signature, generated by running the JAR file or custom generation code
            WM_SEC.TIMESTAMP: The Epoch timestamp
            WM_SVC.NAME: Walmart Service Name
            orderLines: V3CaOrdersRefundCreateBodyOrderLines
            purchaseOrderId: str
            purchaseOrderId: The purchase order ID
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful Operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.v3.ca.orders.refund.create(wm_consumer_channel_type="string", wm_consumer_id="Get the Consumer ID from Developer Center after logging in", wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6", wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=", wm_sec_timestamp="1443748249449", wm_svc_name="Walmart Service Name", order_lines={"order_line": [{"line_number": "string", "refunds": {"refund": [{"refund_charges": {}}]}}]}, purchase_order_id="string", purchase_order_id="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["WM_CONSUMER.CHANNEL.TYPE"] = str(wm_consumer_channel_type)
        _header["WM_CONSUMER.ID"] = str(wm_consumer_id)
        _header["WM_QOS.CORRELATION_ID"] = str(wm_qos_correlation_id)
        _header["WM_SEC.AUTH_SIGNATURE"] = str(wm_sec_auth_signature)
        _header["WM_SEC.TIMESTAMP"] = str(wm_sec_timestamp)
        _header["WM_SVC.NAME"] = str(wm_svc_name)
        _content = to_content(
            file={"order_lines": order_lines, "purchase_order_id": purchase_order_id}
        )
        _content_type = "application/xml"
        return await self._base_client.request(
            method="POST",
            path=f"/v3/ca/orders/{purchase_order_id}/refund",
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )
