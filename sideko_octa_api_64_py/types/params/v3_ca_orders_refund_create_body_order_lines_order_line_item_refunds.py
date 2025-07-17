import pydantic
import typing
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds
    """

    refund: typing_extensions.Required[
        typing.List[V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem]
    ]


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefunds handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    refund: typing.List[
        _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem
    ] = pydantic.Field(
        alias="refund",
    )
