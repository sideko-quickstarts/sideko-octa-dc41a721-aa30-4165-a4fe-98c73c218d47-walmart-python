
### Cancel Order Lines <a name="create"></a>

You can cancel one or more order lines. You must include a purchaseOrderId when cancelling an order line. After cancelling your order, update the inventory for the cancelled order and send it in the next inventory feed.

The response to a successful call contains the order with the cancelled line item.

Cancellation Reasons supported:
- CANCEL_BY_SELLER
- CUSTOMER_REQUESTED_SELLER_TO_CANCEL

**API Endpoint**: `POST /v3/ca/orders/{purchaseOrderId}/cancel`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `WM_CONSUMER.CHANNEL.TYPE` | ✓ | A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding | `"string"` |
| `WM_CONSUMER.ID` | ✓ | A unique ID required to access the API | `"Get the Consumer ID from Developer Center after logging in"` |
| `WM_QOS.CORRELATION_ID` | ✓ | A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID | `"b3261d2d-028a-4ef7-8602-633c23200af6"` |
| `WM_SEC.AUTH_SIGNATURE` | ✓ | The vendor's digital signature, generated by running the JAR file or custom generation code | `"9fg3TPeRt0WSGbXNGGj4kSQ9L6PMBX.....9Zj5aDyg="` |
| `WM_SEC.TIMESTAMP` | ✓ | The Epoch timestamp | `"1443748249449"` |
| `WM_SVC.NAME` | ✓ | Walmart Service Name | `"Walmart Service Name"` |
| `orderLines` | ✓ | Container for the cancellation details | `{"order_line": [{"line_number": "string", "order_line_statuses": {"order_line_status": [{"cancellation_reason": "CANCEL_BY_SELLER", "status": "ACKNOWLEDGED", "status_quantity": {"amount": "string", "unit_of_measurement": "EA"}}]}}]}` |
| `purchaseOrderId` | ✓ | The purchase order ID | `"string"` |

#### Synchronous Client

```python
from sideko_octa_api_64_py import Client

client = Client()
res = client.v3.ca.orders.cancel.create(
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
                            "cancellation_reason": "CANCEL_BY_SELLER",
                            "status": "ACKNOWLEDGED",
                            "status_quantity": {
                                "amount": "string",
                                "unit_of_measurement": "EA",
                            },
                        }
                    ]
                },
            }
        ]
    },
    purchase_order_id="string",
)

```

#### Asynchronous Client

```python
from sideko_octa_api_64_py import AsyncClient

client = AsyncClient()
res = await client.v3.ca.orders.cancel.create(
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
                            "cancellation_reason": "CANCEL_BY_SELLER",
                            "status": "ACKNOWLEDGED",
                            "status_quantity": {
                                "amount": "string",
                                "unit_of_measurement": "EA",
                            },
                        }
                    ]
                },
            }
        ]
    },
    purchase_order_id="string",
)

```
