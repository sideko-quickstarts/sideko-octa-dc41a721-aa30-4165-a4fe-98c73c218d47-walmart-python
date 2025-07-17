import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses_order_line_status_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatuses(
    pydantic.BaseModel
):
    """
    A list of statuses for the Order Line
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    order_line_status: typing.Optional[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
        ]
    ] = pydantic.Field(alias="orderLineStatus", default=None)
    """
    Details about the Order Line status
    """
