import pydantic
import typing_extensions

from .v3_ca_orders_acknowledge_lines_create_body_order_lines_order_line_item_order_line_statuses import (
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses,
    _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses,
)


class V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem
    """

    line_number: typing_extensions.Required[str]

    order_line_statuses: typing_extensions.Required[
        V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses
    ]


class _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    line_number: str = pydantic.Field(
        alias="lineNumber",
    )
    order_line_statuses: _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLinesOrderLineItemOrderLineStatuses = pydantic.Field(
        alias="orderLineStatuses",
    )
