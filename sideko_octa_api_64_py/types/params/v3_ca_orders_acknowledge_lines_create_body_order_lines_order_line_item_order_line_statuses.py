import pydantic
import typing
import typing_extensions

from .v3_ca_orders_acknowledge_lines_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item import (
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
    _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
)


class V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses
    """

    order_line_status: typing_extensions.Required[
        typing.List[
            V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
        ]
    ]


class _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line_status: typing.List[
        _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
    ] = pydantic.Field(
        alias="orderLineStatus",
    )
