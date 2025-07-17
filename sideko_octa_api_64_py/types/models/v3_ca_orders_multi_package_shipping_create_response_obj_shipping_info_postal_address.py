import pydantic
import typing


class V3CaOrdersMultiPackageShippingCreateResponseObjShippingInfoPostalAddress(
    pydantic.BaseModel
):
    """
    Elements of the customer's postal address
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address1: str = pydantic.Field(
        alias="address1",
    )
    """
    The first line of the shipping address
    """
    address2: typing.Optional[str] = pydantic.Field(alias="address2", default=None)
    """
    The second line of the shipping address
    """
    address_type: typing.Optional[str] = pydantic.Field(
        alias="addressType", default=None
    )
    """
    The address type, example: 'RESIDENTIAL'
    """
    city: str = pydantic.Field(
        alias="city",
    )
    """
    The city of the shipping address
    """
    country: str = pydantic.Field(
        alias="country",
    )
    """
    The country of the shipping address
    """
    name: str = pydantic.Field(
        alias="name",
    )
    """
    The name for the shipment
    """
    postal_code: str = pydantic.Field(
        alias="postalCode",
    )
    """
    The zip code of the shipping address
    """
    state: str = pydantic.Field(
        alias="state",
    )
    """
    The state of the shipping address
    """
