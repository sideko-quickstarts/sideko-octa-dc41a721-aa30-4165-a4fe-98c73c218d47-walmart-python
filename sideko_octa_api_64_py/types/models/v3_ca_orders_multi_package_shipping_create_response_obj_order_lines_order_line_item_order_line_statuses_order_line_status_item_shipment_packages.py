import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item_shipment_packages_shipment_package_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages(
    pydantic.BaseModel
):
    """
    List of information about the shipment packages and tracking updates
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    shipment_package: typing.List[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem
    ] = pydantic.Field(
        alias="shipmentPackage",
    )
