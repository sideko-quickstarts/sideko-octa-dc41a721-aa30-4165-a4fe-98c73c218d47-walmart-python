import pydantic
import typing
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges_refund_charge_item_charge_charge_amount import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeChargeAmount,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeChargeAmount,
)
from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges_refund_charge_item_charge_tax import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge
    """

    charge_amount: typing_extensions.Required[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeChargeAmount
    ]
    """
    The details for the amount of the tax charge
    """

    charge_name: typing_extensions.Required[str]
    """
    If chargeType is PRODUCT, chargeName is Item Price. If chargeType is SHIPPING, chargeName is Shipping
    """

    charge_type: typing_extensions.Required[str]
    """
    The charge type for line items can be one of the following: PRODUCT or SHIPPING For details, refer to 'Charge Types'
    """

    tax: typing_extensions.NotRequired[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax
    ]
    """
    Tax information for the charge, including taxName and taxAmount
    """


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemCharge handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    charge_amount: _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeChargeAmount = pydantic.Field(
        alias="chargeAmount",
    )
    charge_name: str = pydantic.Field(
        alias="chargeName",
    )
    charge_type: str = pydantic.Field(
        alias="chargeType",
    )
    tax: typing.Optional[
        _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax
    ] = pydantic.Field(alias="tax", default=None)
