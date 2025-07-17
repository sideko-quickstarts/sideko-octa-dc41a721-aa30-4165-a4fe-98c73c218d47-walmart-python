import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_asn import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn,
)
from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_shipment_packages import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages,
)
from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_status_quantity import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
)


class V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    typing_extensions.TypedDict
):
    """
    Details about the Order Line status
    """

    asn: typing_extensions.NotRequired[
        V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn
    ]

    shipment_packages: typing_extensions.Required[
        V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages
    ]
    """
    List of information about the shipment packages and tracking updates
    """

    status: typing_extensions.Required[
        typing_extensions.Literal[
            "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
        ]
    ]
    """
    Use 'Shipped'
    """

    status_quantity: typing_extensions.Required[
        V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity
    ]
    """
    Details about the status update
    """


class _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    asn: typing.Optional[
        _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn
    ] = pydantic.Field(alias="asn", default=None)
    shipment_packages: _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages = pydantic.Field(
        alias="shipmentPackages",
    )
    status: typing_extensions.Literal[
        "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
    ] = pydantic.Field(
        alias="status",
    )
    status_quantity: _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity = pydantic.Field(
        alias="statusQuantity",
    )
