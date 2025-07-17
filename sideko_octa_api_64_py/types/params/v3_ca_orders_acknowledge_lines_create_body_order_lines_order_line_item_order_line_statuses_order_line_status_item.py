import pydantic
import typing_extensions

from .v3_ca_orders_acknowledge_lines_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_status_quantity import (
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
    _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
)


class V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
    """

    status: typing_extensions.Required[
        typing_extensions.Literal[
            "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
        ]
    ]

    status_quantity: typing_extensions.Required[
        V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity
    ]
    """
    Details about the status update
    """


class _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    status: typing_extensions.Literal[
        "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
    ] = pydantic.Field(
        alias="status",
    )
    status_quantity: _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity = pydantic.Field(
        alias="statusQuantity",
    )
