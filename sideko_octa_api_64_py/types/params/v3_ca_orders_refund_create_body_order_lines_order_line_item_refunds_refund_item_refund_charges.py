import pydantic
import typing
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges_refund_charge_item import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges
    """

    refund_charge: typing_extensions.NotRequired[
        typing.List[
            V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem
        ]
    ]


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundCharges handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    refund_charge: typing.Optional[
        typing.List[
            _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem
        ]
    ] = pydantic.Field(alias="refundCharge", default=None)
