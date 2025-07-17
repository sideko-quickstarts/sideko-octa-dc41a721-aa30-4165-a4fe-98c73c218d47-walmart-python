import pydantic

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_charges_charge_item_tax_tax_amount import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemTaxTaxAmount,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemTax(
    pydantic.BaseModel
):
    """
    Tax information for the charge, including taxName and taxAmount
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_amount: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItemTaxTaxAmount = pydantic.Field(
        alias="taxAmount",
    )
    """
    The details for the amount of the tax charge
    """
    tax_name: str = pydantic.Field(
        alias="taxName",
    )
    """
    The name associated with the tax. Example: 'Sales Tax'
    """
