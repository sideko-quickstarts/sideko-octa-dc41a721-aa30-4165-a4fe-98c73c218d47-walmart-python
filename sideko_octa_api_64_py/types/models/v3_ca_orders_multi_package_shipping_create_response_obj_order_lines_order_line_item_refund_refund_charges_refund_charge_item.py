import pydantic
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund_refund_charges_refund_charge_item_charge import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemCharge,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItem(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemCharge = pydantic.Field(
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
