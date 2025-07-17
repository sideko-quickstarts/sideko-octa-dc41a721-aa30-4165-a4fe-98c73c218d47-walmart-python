import pydantic
import typing
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItem,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItem,
)


class V3CaOrdersRefundCreateBodyOrderLines(typing_extensions.TypedDict):
    """
    V3CaOrdersRefundCreateBodyOrderLines
    """

    order_line: typing_extensions.Required[
        typing.List[V3CaOrdersRefundCreateBodyOrderLinesOrderLineItem]
    ]


class _SerializerV3CaOrdersRefundCreateBodyOrderLines(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLines handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line: typing.List[
        _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItem
    ] = pydantic.Field(
        alias="orderLine",
    )
