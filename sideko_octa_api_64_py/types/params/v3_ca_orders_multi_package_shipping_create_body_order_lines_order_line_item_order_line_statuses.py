import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item import (
    V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
    _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
)


class V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    typing_extensions.TypedDict
):
    """
    A list of status updates for that orderLine, including shipping status updates
    """

    order_line_status: typing_extensions.Required[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
        ]
    ]
    """
    Details about the Order Line status
    """


class _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatuses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line_status: typing.List[
        _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
    ] = pydantic.Field(
        alias="orderLineStatus",
    )
