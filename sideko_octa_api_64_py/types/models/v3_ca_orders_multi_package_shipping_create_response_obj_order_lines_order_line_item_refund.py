import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund_refund_charges import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundCharges,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefund(
    pydantic.BaseModel
):
    """
    Details about any refund on the order
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    refund_charges: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefundRefundCharges = pydantic.Field(
        alias="refundCharges",
    )
    refund_comments: typing.Optional[str] = pydantic.Field(
        alias="refundComments", default=None
    )
    refund_id: typing.Optional[str] = pydantic.Field(alias="refundId", default=None)
