import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_charges_charge_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItem,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemCharges(
    pydantic.BaseModel
):
    """
    Information relating to the charge for the orderLine
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charge: typing.Optional[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemChargesChargeItem
        ]
    ] = pydantic.Field(alias="charge", default=None)
    """
    List of elements that make up a charge
    """
