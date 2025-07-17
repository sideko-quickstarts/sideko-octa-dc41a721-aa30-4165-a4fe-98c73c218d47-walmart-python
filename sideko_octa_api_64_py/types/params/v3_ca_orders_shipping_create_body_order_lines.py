import pydantic
import typing
import typing_extensions

from .v3_ca_orders_shipping_create_body_order_lines_order_line_item import (
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItem,
    _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItem,
)


class V3CaOrdersShippingCreateBodyOrderLines(typing_extensions.TypedDict):
    """
    List of orderLines in the shipment
    """

    order_line: typing_extensions.Required[
        typing.List[V3CaOrdersShippingCreateBodyOrderLinesOrderLineItem]
    ]
    """
    Information about one order line shipment
    """


class _SerializerV3CaOrdersShippingCreateBodyOrderLines(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersShippingCreateBodyOrderLines handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line: typing.List[
        _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItem
    ] = pydantic.Field(
        alias="orderLine",
    )
