import pydantic
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItem(typing_extensions.TypedDict):
    """
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItem
    """

    line_number: typing_extensions.Required[str]

    refunds: typing_extensions.Required[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds
    ]


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItem(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    line_number: str = pydantic.Field(
        alias="lineNumber",
    )
    refunds: _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds = (
        pydantic.Field(
            alias="refunds",
        )
    )
