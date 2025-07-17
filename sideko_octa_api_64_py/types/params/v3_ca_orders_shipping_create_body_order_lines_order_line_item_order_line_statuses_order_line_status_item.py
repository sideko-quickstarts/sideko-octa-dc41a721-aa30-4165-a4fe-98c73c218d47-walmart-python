import pydantic
import typing
import typing_extensions

from .v3_ca_orders_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_asn import (
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn,
    _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn,
)
from .v3_ca_orders_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_status_quantity import (
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
    _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
)
from .v3_ca_orders_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_tracking_info import (
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo,
    _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo,
)


class V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    typing_extensions.TypedDict
):
    """
    Details about the Order Line status
    """

    asn: typing_extensions.NotRequired[
        V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn
    ]

    status: typing_extensions.Required[
        typing_extensions.Literal[
            "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
        ]
    ]
    """
    Use 'Shipped'
    """

    status_quantity: typing_extensions.Required[
        V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity
    ]
    """
    Details about the status update
    """

    tracking_info: typing_extensions.Required[
        V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo
    ]


class _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    asn: typing.Optional[
        _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn
    ] = pydantic.Field(alias="asn", default=None)
    status: typing_extensions.Literal[
        "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
    ] = pydantic.Field(
        alias="status",
    )
    status_quantity: _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity = pydantic.Field(
        alias="statusQuantity",
    )
    tracking_info: _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo = pydantic.Field(
        alias="trackingInfo",
    )
