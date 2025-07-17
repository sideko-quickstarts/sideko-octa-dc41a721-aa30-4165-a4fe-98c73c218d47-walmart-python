import pydantic
import typing


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemFulfillment(
    pydantic.BaseModel
):
    """
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemFulfillment
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    fulfillment_option: typing.Optional[str] = pydantic.Field(
        alias="fulfillmentOption", default=None
    )
    offer_id: typing.Optional[str] = pydantic.Field(alias="offerId", default=None)
    pick_up_by: typing.Optional[str] = pydantic.Field(alias="pickUpBy", default=None)
    pick_up_date_time: typing.Optional[str] = pydantic.Field(
        alias="pickUpDateTime", default=None
    )
    ship_method: typing.Optional[str] = pydantic.Field(alias="shipMethod", default=None)
    store_id: typing.Optional[str] = pydantic.Field(alias="storeId", default=None)
