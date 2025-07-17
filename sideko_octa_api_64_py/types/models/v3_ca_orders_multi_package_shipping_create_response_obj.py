import pydantic

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLines,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_shipping_info import (
    V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfo,
)


class V3CaOrdersMultiPackageShippingCreateResponseObj(pydantic.BaseModel):
    """
    Information about the purchase order
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_email_id: str = pydantic.Field(
        alias="customerEmailId",
    )
    """
    The email address of the customer for the sales order
    """
    customer_order_id: str = pydantic.Field(
        alias="customerOrderId",
    )
    """
    A unique ID associated with the sales order for specified customer
    """
    order_date: str = pydantic.Field(
        alias="orderDate",
    )
    """
    The date the customer submitted the sales order
    """
    order_lines: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLines = (
        pydantic.Field(
            alias="orderLines",
        )
    )
    """
    A list of order lines in the order
    """
    purchase_order_id: str = pydantic.Field(
        alias="purchaseOrderId",
    )
    """
    A unique ID associated with the seller's purchase order
    """
    shipping_info: V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfo = (
        pydantic.Field(
            alias="shippingInfo",
        )
    )
    """
    The shipping information provided by the customer to the seller
    """
