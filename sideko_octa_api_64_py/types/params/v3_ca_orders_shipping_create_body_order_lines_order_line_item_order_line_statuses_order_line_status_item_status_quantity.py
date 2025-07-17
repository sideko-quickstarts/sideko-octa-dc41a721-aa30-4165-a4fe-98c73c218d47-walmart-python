import pydantic
import typing_extensions


class V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity(
    typing_extensions.TypedDict
):
    """
    Details about the status update
    """

    amount: typing_extensions.Required[str]
    """
    The quantity of the unit of measurement for the item.
    """

    unit_of_measurement: typing_extensions.Required[
        typing_extensions.Literal["EA", "EACH"]
    ]
    """
    Unit of quantity
    """


class _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: str = pydantic.Field(
        alias="amount",
    )
    unit_of_measurement: typing_extensions.Literal["EA", "EACH"] = pydantic.Field(
        alias="unitOfMeasurement",
    )
