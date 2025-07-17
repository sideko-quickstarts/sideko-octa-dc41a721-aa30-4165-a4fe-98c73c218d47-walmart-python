import pydantic
import typing
import typing_extensions

from .v3_ca_orders_cancel_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item import (
    V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
    _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem,
)


class V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    typing_extensions.TypedDict
):
    """
    Information to update the orderLine with cancellation details
    """

    order_line_status: typing_extensions.Required[
        typing.List[
            V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
        ]
    ]
    """
    List of details about the cancellation status update
    """


class _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_line_status: typing.List[
        _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem
    ] = pydantic.Field(
        alias="orderLineStatus",
    )
