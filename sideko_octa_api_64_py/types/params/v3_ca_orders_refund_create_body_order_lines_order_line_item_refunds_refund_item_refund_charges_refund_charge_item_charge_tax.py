import pydantic
import typing_extensions

from .v3_ca_orders_refund_create_body_order_lines_order_line_item_refunds_refund_item_refund_charges_refund_charge_item_charge_tax_tax_amount import (
    V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTaxTaxAmount,
    _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTaxTaxAmount,
)


class V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax(
    typing_extensions.TypedDict
):
    """
    Tax information for the charge, including taxName and taxAmount
    """

    tax_amount: typing_extensions.Required[
        V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTaxTaxAmount
    ]
    """
    The details for the amount of the tax charge
    """

    tax_name: typing_extensions.Required[str]
    """
    The name associated with the tax. Example: 'Sales Tax'
    """


class _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_amount: _SerializerV3CaOrdersRefundCreateBodyOrderLinesOrderLineItemRefundsRefundItemRefundChargesRefundChargeItemChargeTaxTaxAmount = pydantic.Field(
        alias="taxAmount",
    )
    tax_name: str = pydantic.Field(
        alias="taxName",
    )
