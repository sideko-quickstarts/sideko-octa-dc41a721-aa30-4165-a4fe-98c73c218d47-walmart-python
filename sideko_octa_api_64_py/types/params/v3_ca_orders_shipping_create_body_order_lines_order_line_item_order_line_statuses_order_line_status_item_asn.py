import pydantic
import typing
import typing_extensions


class V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn
    """

    package_asn: typing_extensions.Required[str]

    pallet_asn: typing_extensions.NotRequired[str]


class _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemAsn handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    package_asn: str = pydantic.Field(
        alias="packageASN",
    )
    pallet_asn: typing.Optional[str] = pydantic.Field(alias="palletASN", default=None)
