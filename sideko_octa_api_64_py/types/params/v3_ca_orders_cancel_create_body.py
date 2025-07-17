import pydantic
import typing_extensions

from .v3_ca_orders_cancel_create_body_order_lines import (
    V3CaOrdersCancelCreateBodyOrderLines,
    _SerializerV3CaOrdersCancelCreateBodyOrderLines,
)


class V3CaOrdersCancelCreateBody(typing_extensions.TypedDict):
    """
    V3CaOrdersCancelCreateBody
    """

    order_lines: typing_extensions.Required[V3CaOrdersCancelCreateBodyOrderLines]
    """
    Container for the cancellation details
    """


class _SerializerV3CaOrdersCancelCreateBody(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersCancelCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_lines: _SerializerV3CaOrdersCancelCreateBodyOrderLines = pydantic.Field(
        alias="orderLines",
    )
