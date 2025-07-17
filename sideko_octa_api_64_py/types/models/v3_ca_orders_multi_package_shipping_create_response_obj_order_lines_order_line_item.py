import pydantic
import typing
import typing_extensions

from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_charges import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemCharges,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_fulfillment import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemFulfillment,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_item import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemItem,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_quantity import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineQuantity,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_order_line_statuses import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatuses,
)
from .v3_ca_orders_multi_package_shipping_create_response_obj_order_lines_order_line_item_refund import (
    V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefund,
)


class V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItem(
    pydantic.BaseModel
):
    """
    Purchase Order line information for each item
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    charges: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemCharges = pydantic.Field(
        alias="charges",
    )
    """
    Information relating to the charge for the orderLine
    """
    config_id: typing.Optional[str] = pydantic.Field(alias="configId", default=None)
    fulfillment: typing.Optional[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemFulfillment
    ] = pydantic.Field(alias="fulfillment", default=None)
    intent_to_cancel: typing.Optional[str] = pydantic.Field(
        alias="intentToCancel", default=None
    )
    item: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemItem = (
        pydantic.Field(
            alias="item",
        )
    )
    """
    The information for the item on the orderLine
    """
    line_number: str = pydantic.Field(
        alias="lineNumber",
    )
    """
    The line number associated with the details for each individual item in the purchase order
    """
    order_line_quantity: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineQuantity = pydantic.Field(
        alias="orderLineQuantity",
    )
    """
    Details about the status update
    """
    order_line_statuses: V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemOrderLineStatuses = pydantic.Field(
        alias="orderLineStatuses",
    )
    """
    A list of statuses for the Order Line
    """
    original_carrier_method: typing.Optional[str] = pydantic.Field(
        alias="originalCarrierMethod", default=None
    )
    reference_line_id: typing.Optional[str] = pydantic.Field(
        alias="referenceLineId", default=None
    )
    refund: typing.Optional[
        V3CaOrdersMultiPackageShippingCreateResponseObjOrderLinesOrderLineItemRefund
    ] = pydantic.Field(alias="refund", default=None)
    """
    Details about any refund on the order
    """
    ship_from_country: typing.Optional[
        typing_extensions.Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AX",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BQ",
            "BR",
            "BS",
            "BT",
            "BV",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CW",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "EH",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GF",
            "GG",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GP",
            "GQ",
            "GR",
            "GS",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HM",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IO",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JE",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MQ",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NF",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PS",
            "PT",
            "PW",
            "PY",
            "QA",
            "RE",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SJ",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "SS",
            "ST",
            "SV",
            "SX",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TF",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "UM",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ]
    ] = pydantic.Field(alias="shipFromCountry", default=None)
    """
    The ship from country is associated with the details for each individual item in the purchase order
    """
    status_date: str = pydantic.Field(
        alias="statusDate",
    )
    """
    The date shown on the recent order status
    """
