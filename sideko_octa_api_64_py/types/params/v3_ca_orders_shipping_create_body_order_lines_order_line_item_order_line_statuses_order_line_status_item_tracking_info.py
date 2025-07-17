import pydantic
import typing
import typing_extensions

from .v3_ca_orders_shipping_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_tracking_info_carrier_name import (
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfoCarrierName,
    _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfoCarrierName,
)


class V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo(
    typing_extensions.TypedDict
):
    """
    V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo
    """

    actual_delivery_date_time: typing_extensions.NotRequired[str]
    """
    Delivery datetime of the shipment package
    """

    carrier_name: typing_extensions.Required[
        V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfoCarrierName
    ]
    """
    Information about the package carrier(s)
    """

    method_code: typing_extensions.Required[
        typing_extensions.Literal[
            "Express", "Freight", "OneDay", "Standard", "Value", "WhiteGlove"
        ]
    ]
    """
    The shipping method. Can be one of the following: Standard, Express, Oneday, or Freight
    """

    package_status: typing_extensions.NotRequired[str]
    """
    Status of the shipment package
    """

    ship_date_time: typing_extensions.Required[str]
    """
    The date the package was shipped
    """

    shipment_no: typing_extensions.NotRequired[str]
    """
    The shipment number. This will be same for all packages in a shipment
    """

    tracking_number: typing_extensions.Required[str]
    """
    The shipment tracking number required for all non-Lettermail shipments
    """

    tracking_url: typing_extensions.NotRequired[str]
    """
    The URL for tracking the shipment
    """


class _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfo handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    actual_delivery_date_time: typing.Optional[str] = pydantic.Field(
        alias="actualDeliveryDateTime", default=None
    )
    carrier_name: _SerializerV3CaOrdersShippingCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemTrackingInfoCarrierName = pydantic.Field(
        alias="carrierName",
    )
    method_code: typing_extensions.Literal[
        "Express", "Freight", "OneDay", "Standard", "Value", "WhiteGlove"
    ] = pydantic.Field(
        alias="methodCode",
    )
    package_status: typing.Optional[str] = pydantic.Field(
        alias="packageStatus", default=None
    )
    ship_date_time: str = pydantic.Field(
        alias="shipDateTime",
    )
    shipment_no: typing.Optional[str] = pydantic.Field(alias="shipmentNo", default=None)
    tracking_number: str = pydantic.Field(
        alias="trackingNumber",
    )
    tracking_url: typing.Optional[str] = pydantic.Field(
        alias="trackingURL", default=None
    )
