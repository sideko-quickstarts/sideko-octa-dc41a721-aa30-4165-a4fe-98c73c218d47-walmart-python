import pydantic
import typing_extensions

from .v3_ca_orders_shipping_create_body_order_lines import (
    V3CaOrdersShippingCreateBodyOrderLines,
    _SerializerV3CaOrdersShippingCreateBodyOrderLines,
)


class V3CaOrdersShippingCreateBody(typing_extensions.TypedDict):
    """
    Information about a shipment
    """

    order_lines: typing_extensions.Required[V3CaOrdersShippingCreateBodyOrderLines]
    """
    List of orderLines in the shipment
    """


class _SerializerV3CaOrdersShippingCreateBody(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersShippingCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_lines: _SerializerV3CaOrdersShippingCreateBodyOrderLines = pydantic.Field(
        alias="orderLines",
    )
