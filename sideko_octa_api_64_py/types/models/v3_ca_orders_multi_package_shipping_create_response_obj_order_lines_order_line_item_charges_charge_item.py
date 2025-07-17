import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_charges_charge_item_charge_amount import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemChargeAmount,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_charges_charge_item_tax import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemTax,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItem(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge_amount: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemChargeAmount = pydantic.Field(
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
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemTax
    ] = pydantic.Field(alias="tax", default=None)
    """
    Tax information for the charge, including taxName and taxAmount
    """
