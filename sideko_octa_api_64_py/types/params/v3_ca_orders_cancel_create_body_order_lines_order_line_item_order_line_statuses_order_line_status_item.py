import pydantic
import typing_extensions

from .v3_ca_orders_cancel_create_body_order_lines_order_line_item_order_line_statuses_order_line_status_item_status_quantity import (
    V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
    _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity,
)


class V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    typing_extensions.TypedDict
):
    """
    List of details about the cancellation status update
    """

    cancellation_reason: typing_extensions.Required[
        typing_extensions.Literal[
            "CANCEL_BY_SELLER",
            "CUSTOMER_REQUESTED_SELLER_TO_CANCEL",
            "SUPPLIER_CANCEL",
            "SUPPLIER_CANCEL_BACKORDER",
            "SUPPLIER_CANCEL_CUSTOMER_REQUEST",
            "SUPPLIER_CANCEL_DISCONTINUE",
            "SUPPLIER_CANCEL_UNRECOGNIZED",
        ]
    ]
    """
    Reason for cancellation. Example: 'CUSTOMER_REQUESTED_SELLER_TO_CANCEL'
    """

    status: typing_extensions.Required[
        typing_extensions.Literal[
            "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
        ]
    ]
    """
    Use 'Cancelled'
    """

    status_quantity: typing_extensions.Required[
        V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity
    ]
    """
    Details about the status update
    """


class _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem(
    pydantic.BaseModel
):
    """
    Serializer for V3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    cancellation_reason: typing_extensions.Literal[
        "CANCEL_BY_SELLER",
        "CUSTOMER_REQUESTED_SELLER_TO_CANCEL",
        "SUPPLIER_CANCEL",
        "SUPPLIER_CANCEL_BACKORDER",
        "SUPPLIER_CANCEL_CUSTOMER_REQUEST",
        "SUPPLIER_CANCEL_DISCONTINUE",
        "SUPPLIER_CANCEL_UNRECOGNIZED",
    ] = pydantic.Field(
        alias="cancellationReason",
    )
    status: typing_extensions.Literal[
        "ACKNOWLEDGED", "CANCELLED", "CREATED", "REFUND", "SHIPPED"
    ] = pydantic.Field(
        alias="status",
    )
    status_quantity: _SerializerV3CaOrdersCancelCreateBodyOrderLinesOrderLineItemOrderLineStatusesOrderLineStatusItemStatusQuantity = pydantic.Field(
        alias="statusQuantity",
    )
