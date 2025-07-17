import pydantic
import typing
import typing_extensions


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName(
    pydantic.BaseModel
):
    """
    Information about the package carrier(s)
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    carrier: typing.Optional[
        typing_extensions.Literal[
            "17Track",
            "ASL",
            "CANPAR",
            "CEVA",
            "CPC",
            "DHL",
            "FEDEX_SWWEXPRESS",
            "FedEx",
            "GLB",
            "JIAYOU",
            "LETTERMAIL",
            "LOOMIS",
            "PCLINT",
            "PURINTL_SWWGROUND",
            "SAMEDAY",
            "SWYFT",
            "TFORCE",
            "UBI",
            "UPS",
            "USPS",
        ]
    ] = pydantic.Field(alias="carrier", default=None)
    """
    The package shipment carrier
    """
    other_carrier: typing.Optional[str] = pydantic.Field(
        alias="otherCarrier", default=None
    )
    """
    Other carrier name
    """
