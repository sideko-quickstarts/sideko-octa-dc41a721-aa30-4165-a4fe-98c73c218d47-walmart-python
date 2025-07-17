import pydantic
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_response_obj_shipping_info_postal_address import (
    V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfoPostalAddress,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfo(pydantic.BaseModel):
    """
    The shipping information provided by the customer to the seller
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    estimated_delivery_date: str = pydantic.Field(
        alias="estimatedDeliveryDate",
    )
    """
    The estimated time and date for the delivery of the item. Format: yyyy-MM-ddThh:MM:ssZ Example: '2016-06-15T06:00:00Z'
    """
    estimated_ship_date: str = pydantic.Field(
        alias="estimatedShipDate",
    )
    """
    The estimated time and date when the item will be shipped. Format: yyyy-MM-ddThh:MM:ssZ Example: '2016-06-15T06:00:00Z'
    """
    method_code: typing_extensions.Literal[
        "Express", "Freight", "OneDay", "Standard", "Value", "WhiteGlove"
    ] = pydantic.Field(
        alias="methodCode",
    )
    """
    The shipping method. Can be one of the following: Standard, Express, Oneday, or Freight
    """
    phone: str = pydantic.Field(
        alias="phone",
    )
    """
    The customer's phone number
    """
    postal_address: V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfoPostalAddress = pydantic.Field(
        alias="postalAddress",
    )
    """
    Elements of the customer's postal address
    """
