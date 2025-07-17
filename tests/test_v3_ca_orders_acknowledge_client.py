import pytest

from sideko_octa_api_64_py import AsyncClient, Client
from sideko_octa_api_64_py.core import BinaryResponse
from sideko_octa_api_64_py.environment import Environment


def test_create_200_success_all_params():
    """Tests a POST request to the /v3/ca/orders/{purchaseOrderId}/acknowledge endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(environment=Environment.MOCK_SERVER)
    response = client.v3.ca.orders.acknowledge.create(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        purchase_order_id="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_200_success_all_params():
    """Tests a POST request to the /v3/ca/orders/{purchaseOrderId}/acknowledge endpoint.

    Operation: create
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(environment=Environment.MOCK_SERVER)
    response = await client.v3.ca.orders.acknowledge.create(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        purchase_order_id="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"
