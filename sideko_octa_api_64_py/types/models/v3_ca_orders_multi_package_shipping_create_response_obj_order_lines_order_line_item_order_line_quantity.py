import pydantic
import typing_extensions


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineQuantity(
    pydantic.BaseModel
):
    """
    Details about the status update
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: str = pydantic.Field(
        alias="amount",
    )
    """
    The quantity of the unit of measurement for the item.
    """
    unit_of_measurement: typing_extensions.Literal["EA", "EACH"] = pydantic.Field(
        alias="unitOfMeasurement",
    )
    """
    Unit of quantity
    """
