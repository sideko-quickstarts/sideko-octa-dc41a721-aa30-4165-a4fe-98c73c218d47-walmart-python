import pydantic
import typing

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItem,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLines(pydantic.BaseModel):
    """
    A list of order lines in the order
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    order_line: typing.Optional[
        typing.List[
            V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItem
        ]
    ] = pydantic.Field(alias="orderLine", default=None)
    """
    Purchase Order line information for each item
    """
