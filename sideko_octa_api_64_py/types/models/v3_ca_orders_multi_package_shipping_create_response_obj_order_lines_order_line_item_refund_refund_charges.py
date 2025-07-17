import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund_refund_charges_refund_charge_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItem,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundCharges(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundCharges
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    refund_charge: typing.Optional[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundChargesRefundChargeItem
        ]
    ] = pydantic.Field(alias="refundCharge", default=None)
