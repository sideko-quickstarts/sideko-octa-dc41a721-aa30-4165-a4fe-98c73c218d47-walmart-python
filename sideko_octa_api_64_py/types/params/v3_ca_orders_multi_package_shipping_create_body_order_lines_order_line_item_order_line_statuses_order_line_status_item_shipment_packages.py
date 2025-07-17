import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_shipment_packages_shipment_package_item import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem,
)


class V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages(
    typing_extensions.TypedDict
):
    """
    List of information about the shipment packages and tracking updates
    """

    shipment_package: typing_extensions.Required[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem
        ]
    ]


class _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipment_package: typing.List[
        _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem
    ] = pydantic.Field(
        alias="shipmentPackage",
    )
