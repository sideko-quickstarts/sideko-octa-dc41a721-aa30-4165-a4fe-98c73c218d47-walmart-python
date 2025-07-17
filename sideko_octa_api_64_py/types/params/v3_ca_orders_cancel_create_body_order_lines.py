import pydantic
import typing
import typing_extensions

from .v3_ca_orders_cancel_create_body_order_lines_order_line_item import (
    V3CaOrdersCancelCreateBodyOrderLinesOrderLineItem,
    _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItem,
)


class V3CaOrdersCancelCreateBodyOrderLines(typing_extensions.TypedDict):
    """
    Container for the cancellation details
    """

    order_line: typing_extensions.Required[
        typing.List[V3CaOrdersCancelCreateBodyOrderLinesOrderLineItem]
    ]
    """
    A list of orderLines to be cancelled
    """


class _SerializerV3CaOrdersCancelCreateBodyOrderLines(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersCancelCreateBodyOrderLines handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line: typing.List[
        _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItem
    ] = pydantic.Field(
        alias="orderLine",
    )
