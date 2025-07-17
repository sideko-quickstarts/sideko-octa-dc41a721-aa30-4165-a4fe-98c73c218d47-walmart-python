import pydantic
import typing
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem(
    typing_extensions.TypedDict
):
    """
    Details about any refund on the order
    """

    refund_charges: typing_extensions.Required[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges
    ]

    refund_comments: typing_extensions.NotRequired[str]

    refund_id: typing_extensions.NotRequired[str]


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    refund_charges: _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges = pydantic.Field(
        alias="refundCharges",
    )
    refund_comments: typing.Optional[str] = pydantic.Field(
        alias="refundComments", default=None
    )
    refund_id: typing.Optional[str] = pydantic.Field(alias="refundId", default=None)
