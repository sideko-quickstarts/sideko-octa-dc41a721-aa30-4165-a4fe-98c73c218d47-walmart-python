import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItem,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItem,
)


class V3CaOrdersMultiPackageShippingCreateBodyOrderLines(typing_extensions.TypedDict):
    """
    List of orderLines in the shipment
    """

    order_line: typing_extensions.Required[
        typing.List[V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItem]
    ]
    """
    Information about one order line shipment
    """


class _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLines(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBodyOrderLines handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line: typing.List[
        _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItem
    ] = pydantic.Field(
        alias="orderLine",
    )
