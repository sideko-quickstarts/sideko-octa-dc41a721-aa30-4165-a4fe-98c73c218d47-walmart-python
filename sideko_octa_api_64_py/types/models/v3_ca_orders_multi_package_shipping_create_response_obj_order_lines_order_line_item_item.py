import pydantic


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemItem(
    pydantic.BaseModel
):
    """
    The information for the item on the orderLine
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    product_name: str = pydantic.Field(
        alias="productName",
    )
    """
    The name of the product associated with the line item. Example: 'Kenmore CF1' or '2086883 Canister Secondary Filter Generic 2 Pack'
    """
    sku: str = pydantic.Field(
        alias="sku",
    )
    """
    An arbitrary alphanumeric unique ID, assigned to each item in the XSD file.
    """
