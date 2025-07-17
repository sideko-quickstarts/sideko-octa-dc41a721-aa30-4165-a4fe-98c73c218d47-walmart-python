import pydantic
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges_refund_charge_item_charge import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem
    """

    charge: typing_extensions.Required[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge
    ]

    refund_reason: typing_extensions.Required[
        typing_extensions.Literal[
            "BillingError",
            "Buyer canceled",
            "CancelledYetShipped",
            "Customer returned item",
            "CustomerChangedMind",
            "CustomerReceivedItemLate",
            "DamagedItem",
            "DefectiveItem",
            "Finance -> Goodwill",
            "Finance -> Rollback",
            "General adjustment",
            "IncorrectItemReceived",
            "IncorrectShippingPrice",
            "ItemNotAsAdvertised",
            "ItemNotReceivedByCustomer",
            "Merchandise not received",
            "Missing Parts / Instructions",
            "Others",
            "Quality -> Missing Parts / Instructions",
            "Shipping & Delivery -> Damaged",
            "Shipping & Delivery -> Shipping Price Discrepancy",
            "TaxExemptCustomer",
        ]
    ]


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    charge: _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge = pydantic.Field(
        alias="charge",
    )
    refund_reason: typing_extensions.Literal[
        "BillingError",
        "Buyer canceled",
        "CancelledYetShipped",
        "Customer returned item",
        "CustomerChangedMind",
        "CustomerReceivedItemLate",
        "DamagedItem",
        "DefectiveItem",
        "Finance -> Goodwill",
        "Finance -> Rollback",
        "General adjustment",
        "IncorrectItemReceived",
        "IncorrectShippingPrice",
        "ItemNotAsAdvertised",
        "ItemNotReceivedByCustomer",
        "Merchandise not received",
        "Missing Parts / Instructions",
        "Others",
        "Quality -> Missing Parts / Instructions",
        "Shipping & Delivery -> Damaged",
        "Shipping & Delivery -> Shipping Price Discrepancy",
        "TaxExemptCustomer",
    ] = pydantic.Field(
        alias="refundReason",
    )
