import pydantic
import typing_extensions

from .v3_ca_orders_acknowledge_lines_create_body_order_lines import (
    V3CaOrdersAcknowledgeLinesCreateBodyOrderLines,
    _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLines,
)


class V3CaOrdersAcknowledgeLinesCreateBody(typing_extensions.TypedDict):
    """
    V3CaOrdersAcknowledgeLinesCreateBody
    """

    order_lines: typing_extensions.Required[
        V3CaOrdersAcknowledgeLinesCreateBodyOrderLines
    ]


class _SerializerV3CaOrdersAcknowledgeLinesCreateBody(pydantic.BaseModel):
    """
    Serializer for V3CaOrdersAcknowledgeLinesCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    order_lines: _SerializerV3CaOrdersAcknowledgeLinesCreateBodyOrderLines = (
        pydantic.Field(
            alias="orderLines",
        )
    )
