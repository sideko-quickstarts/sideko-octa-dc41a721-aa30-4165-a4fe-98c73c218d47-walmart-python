import pydantic
import typing_extensions

from .v3_ca_orders_cancel_create_body_order_lines_order_line_item_order_line_statuses import (
    V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses,
    _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses,
)


class V3CaOrdersCancelCreateBodyOrderLinesOrderLineItem(typing_extensions.TypedDict):
    """
    A list of orderLines to be cancelled
    """

    line_number: typing_extensions.Required[str]
    """
    OrderLine number
    """

    order_line_statuses: typing_extensions.Required[
        V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses
    ]
    """
    Information to update the orderLine with cancellation details
    """


class _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItem(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersCancelCreateBodyOrderLinesOrderLineItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    line_number: str = pydantic.Field(
        alias="lineNumber",
    )
    order_line_statuses: _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatuses = pydantic.Field(
        alias="orderLineStatuses",
    )
