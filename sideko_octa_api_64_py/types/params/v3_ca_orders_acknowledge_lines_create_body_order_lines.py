import pydantic
import typing
import typing_extensions

from .v3_ca_orders_acknowledge_lines_create_body_order_lines_order_line_item import (
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem,
    _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem,
)


class V3CaOrdersAcknowledgeLinesCreateBodyOrderLines(typing_extensions.TypedDict):
    """
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLines
    """

    order_line: typing_extensions.Required[
        typing.List[V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem]
    ]


class _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLines(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersAcknowledgeLinesCreateBodyOrderLines handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line: typing.List[
        _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem
    ] = pydantic.Field(
        alias="orderLine",
    )
