import pydantic
import typing
import typing_extensions


class V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName(
    typing_extensions.TypedDict
):
    """
    Information about the package carrier(s)
    """

    carrier: typing_extensions.NotRequired[
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
    ]
    """
    The package shipment carrier
    """

    other_carrier: typing_extensions.NotRequired[str]
    """
    Other carrier name
    """


class _SerializerV3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersMultiPackageShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemShipmentPackagesShipmentPackageItemCarrierName handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
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
    other_carrier: typing.Optional[str] = pydantic.Field(
        alias="otherCarrier", default=None
    )
