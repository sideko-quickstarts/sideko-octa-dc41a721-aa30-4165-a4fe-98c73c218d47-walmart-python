import pydantic
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines import (
    V3CaOrdersRefundCreateBodyOrderLines,
    _SerializerV3CaOrdersRefundCreateBodyOrderLines,
)


class V3CaOrdersRefundCreateBody(typing_extensions.TypedDict):
    """
    V3CaOrdersRefundCreateBody
    """

    order_lines: typing_extensions.Required[V3CaOrdersRefundCreateBodyOrderLines]

    purchase_order_id: typing_extensions.Required[str]


class _SerializerV3CaOrdersRefundCreateBody(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersRefundCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_lines: _SerializerV3CaOrdersRefundCreateBodyOrderLines = pydantic.Field(
        alias="orderLines",
    )
    purchase_order_id: str = pydantic.Field(
        alias="purchaseOrderId",
    )
