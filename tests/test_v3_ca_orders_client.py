import pytest

from sideko_octa_api_64_py import AsyncClient, Client
from sideko_octa_api_64_py.core import BinaryResponse
from sideko_octa_api_64_py.environment import Environment


def test_get_200_success_required_only():
    """Tests a GET request to the /v3/ca/orders/{purchaseOrderId} endpoint.

    Operation: get
    Test Case ID: success_required_only
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
    response = client.v3.ca.orders.get(
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
async def test_await_get_200_success_required_only():
    """Tests a GET request to the /v3/ca/orders/{purchaseOrderId} endpoint.

    Operation: get
    Test Case ID: success_required_only
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
    response = await client.v3.ca.orders.get(
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


def test_get_200_success_all_params():
    """Tests a GET request to the /v3/ca/orders/{purchaseOrderId} endpoint.

    Operation: get
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
    response = client.v3.ca.orders.get(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        purchase_order_id="string",
        product_info="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_200_success_all_params():
    """Tests a GET request to the /v3/ca/orders/{purchaseOrderId} endpoint.

    Operation: get
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
    response = await client.v3.ca.orders.get(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        purchase_order_id="string",
        product_info="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_list_200_success_required_only():
    """Tests a GET request to the /v3/ca/orders endpoint.

    Operation: list
    Test Case ID: success_required_only
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
    response = client.v3.ca.orders.list(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        created_start_date="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_required_only():
    """Tests a GET request to the /v3/ca/orders endpoint.

    Operation: list
    Test Case ID: success_required_only
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
    response = await client.v3.ca.orders.list(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        created_start_date="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_list_200_success_all_params():
    """Tests a GET request to the /v3/ca/orders endpoint.

    Operation: list
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
    response = client.v3.ca.orders.list(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        created_start_date="string",
        created_end_date="string",
        customer_order_id="string",
        from_expected_ship_date="string",
        limit="string",
        product_info="string",
        purchase_order_id="string",
        sku="string",
        status="string",
        to_expected_ship_date="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_200_success_all_params():
    """Tests a GET request to the /v3/ca/orders endpoint.

    Operation: list
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
    response = await client.v3.ca.orders.list(
        wm_consumer_channel_type="string",
        wm_consumer_id="Get the Consumer ID from Developer Center after logging in",
        wm_qos_correlation_id="b3261d2d-028a-4ef7-8602-633c23200af6",
        wm_sec_auth_signature="9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg=",
        wm_sec_timestamp="1443748249449",
        wm_svc_name="Walmart Service Name",
        created_start_date="string",
        created_end_date="string",
        customer_order_id="string",
        from_expected_ship_date="string",
        limit="string",
        product_info="string",
        purchase_order_id="string",
        sku="string",
        status="string",
        to_expected_ship_date="string",
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"
