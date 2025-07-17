import pydantic
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_body_order_lines import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLines,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLines,
)


class V3CaOrdersMultiPackageShippingCreateBody(typing_extensions.TypedDict):
    """
    Information about a shipment
    """

    order_lines: typing_extensions.Required[
        V3CaOrdersMultiPackageShippingCreateBodyOrderLines
    ]
    """
    List of orderLines in the shipment
    """


class _SerializerV3CaOrdersMultiPackageShippingCreateBody(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_lines: _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLines = (
        pydantic.Field(
            alias="orderLines",
        )
    )
