import pydantic
import pytest

from sideko_octa_api_64_py import AsyncClient, Client
from sideko_octa_api_64_py.core import BinaryResponse
from sideko_octa_api_64_py.environment import Environment
from sideko_octa_api_64_py.types import models


def test_create_200_success_all_params():
    """Tests a POST request to the /v3/ca/orders/{purchaseOrderId}/multiPackageShipping endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Union[models.V3CaOrdersMultiPackageShippingCreateResponseObj, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.v3.ca.orders.multi_package_shipping.create(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        order_lines={
            "order_line": [
                {
                    "line_number": "string",
                    "order_line_statuses": {
                        "order_line_status": [
                            {
                                "asn": {
                                    "package_asn": "string",
                                    "pallet_asn": "string",
                                },
                                "shipment_packages": {
                                    "shipment_package": [
                                        {
                                            "actual_delivery_date_time": "1970-01-01T00:00:00",
                                            "carrier_name": {
                                                "carrier": "17Track",
                                                "other_carrier": "string",
                                            },
                                            "method_code": "Express",
                                            "package_status": "string",
                                            "ship_date_time": "1970-01-01T00:00:00",
                                            "shipment_no": "string",
                                            "tracking_number": "string",
                                            "tracking_url": "string",
                                        }
                                    ]
                                },
                                "status": "ACKNOWLEDGED",
                                "status_quantity": {
                                    "amount": "string",
                                    "unit_of_measurement": "EA",
                                },
                            }
                        ]
                    },
                    "ship_from_country": "AD",
                }
            ]
        },
        purchase_order_id="string",
    )
    try:
        pydantic.TypeAdapter(
            models.V3CaOrdersMultiPackageShippingCreateResponseObj
        ).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /v3/ca/orders/{purchaseOrderId}/multiPackageShipping endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Union[models.V3CaOrdersMultiPackageShippingCreateResponseObj, BinaryResponse]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.v3.ca.orders.multi_package_shipping.create(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        order_lines={
            "order_line": [
                {
                    "line_number": "string",
                    "order_line_statuses": {
                        "order_line_status": [
                            {
                                "asn": {
                                    "package_asn": "string",
                                    "pallet_asn": "string",
                                },
                                "shipment_packages": {
                                    "shipment_package": [
                                        {
                                            "actual_delivery_date_time": "1970-01-01T00:00:00",
                                            "carrier_name": {
                                                "carrier": "17Track",
                                                "other_carrier": "string",
                                            },
                                            "method_code": "Express",
                                            "package_status": "string",
                                            "ship_date_time": "1970-01-01T00:00:00",
                                            "shipment_no": "string",
                                            "tracking_number": "string",
                                            "tracking_url": "string",
                                        }
                                    ]
                                },
                                "status": "ACKNOWLEDGED",
                                "status_quantity": {
                                    "amount": "string",
                                    "unit_of_measurement": "EA",
                                },
                            }
                        ]
                    },
                    "ship_from_country": "AD",
                }
            ]
        },
        purchase_order_id="string",
    )
    try:
        pydantic.TypeAdapter(
            models.V3CaOrdersMultiPackageShippingCreateResponseObj
        ).validate_python(response)
        is_valid_response_json = True
    except pydantic.ValidationError:
        is_valid_response_json = False
    is_valid_binary = isinstance(response, BinaryResponse)
    assert any([is_valid_response_json, is_valid_binary]), "failed response type check"
