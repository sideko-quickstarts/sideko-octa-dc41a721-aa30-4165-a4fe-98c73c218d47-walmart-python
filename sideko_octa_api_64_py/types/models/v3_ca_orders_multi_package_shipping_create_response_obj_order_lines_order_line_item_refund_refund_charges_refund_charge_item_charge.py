import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund_refund_charges_refund_charge_item_charge_charge_amount import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemChargeChargeAmount,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund_refund_charges_refund_charge_item_charge_tax import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemChargeTax,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemCharge(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemCharge
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge_amount: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemChargeChargeAmount = pydantic.Field(
        alias="chargeAmount",
    )
    """
    The details for the amount of the tax charge
    """
    charge_name: str = pydantic.Field(
        alias="chargeName",
    )
    """
    If chargeType is PRODUCT, chargeName is Item Price. If chargeType is SHIPPING, chargeName is Shipping
    """
    charge_type: str = pydantic.Field(
        alias="chargeType",
    )
    """
    The charge type for line items can be one of the following: PRODUCT or SHIPPING For details, refer to 'Charge Types'
    """
    tax: typing.Optional[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItemChargeTax
    ] = pydantic.Field(alias="tax", default=None)
    """
    Tax information for the charge, including taxName and taxAmount
    """
