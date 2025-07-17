import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item_shipment_packages import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item_status_quantity import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item_tracking_info import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    pydantic.BaseModel
):
    """
    Details about the Order Line status
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cancellation_reason: typing.Optional[str] = pydantic.Field(
        alias="cancellationReason", default=None
    )
    """
    If order is cancelled, cancellationReason will explain the reason
    """
    shipment_packages: typing.Optional[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackages
    ] = pydantic.Field(alias="shipmentPackages", default=None)
    """
    List of information about the shipment packages and tracking updates
    """
    status: typing_extensions.Literal[
        "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Should be 'Created'
    """
    status_quantity: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity = pydantic.Field(
        alias="statusQuantity",
    )
    """
    Details about the status update
    """
    tracking_info: typing.Optional[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo
    ] = pydantic.Field(alias="trackingInfo", default=None)
