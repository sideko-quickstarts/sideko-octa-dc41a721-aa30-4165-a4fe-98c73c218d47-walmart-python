import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item_shipment_packages_shipment_package_item_carrier_name import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    actual_delivery_date_time: typing.Optional[str] = pydantic.Field(
        alias="actualDeliveryDateTime", default=None
    )
    """
    Delivery datetime of the shipment package
    """
    carrier_name: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName = pydantic.Field(
        alias="carrierName",
    )
    """
    Information about the package carrier(s)
    """
    method_code: typing_extensions.Literal[
        "Express", "Freight", "OneDay", "Standard", "Value", "WhiteGlove"
    ] = pydantic.Field(
        alias="methodCode",
    )
    """
    The shipping method. Can be one of the following: Standard, Express, Oneday, or Freight
    """
    package_status: typing.Optional[str] = pydantic.Field(
        alias="packageStatus", default=None
    )
    """
    Status of the shipment package
    """
    ship_date_time: str = pydantic.Field(
        alias="shipDateTime",
    )
    """
    The date the package was shipped
    """
    shipment_no: typing.Optional[str] = pydantic.Field(alias="shipmentNo", default=None)
    """
    The shipment number. This will be same for all packages in a shipment
    """
    tracking_number: str = pydantic.Field(
        alias="trackingNumber",
    )
    """
    The shipment tracking number required for all non-Lettermail shipments
    """
    tracking_url: typing.Optional[str] = pydantic.Field(
        alias="trackingURL", default=None
    )
    """
    The URL for tracking the shipment
    """
