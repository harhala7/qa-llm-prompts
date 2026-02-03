### Summary
- Change intent: Refactor order status handling and introduce CANCELLED state
- Areas touched: Order status enum, transition logic, API response mapping
- Non-obvious side effects: Invalid transitions from CANCELLED, incomplete API responses

### Assumptions
- A1: Existing clients may not recognize CANCELLED and must handle unknown enum values safely.
- A2: Cancelled orders must not expose shipment details in API responses.

### Risk Register
| Risk ID | Area | Impact | Likelihood | Evidence in diff | What could break |
|---|---|---|---|---|---|
| R1 | state transitions | High | Med | canTransition changed to block from CANCELLED and allow others | Orders may allow forbidden transitions or end in inconsistent states |
| R2 | api contract | High | Med | mapper comment: CANCELLED should not expose shipment details | Clients may receive unexpected fields or missing fields |
| R3 | backward compatibility | Med | Low | new enum value CANCELLED | Older clients fail to parse or display status |

### Regression Checklist (ordered by priority)
| Test ID | Priority | Execution (manual / auto) | Automation plan (now / later / n/a) | Scope (unit / component / integration / e2e) | What to execute | Expected result | Risk refs |
|---|---|---|---|---|---|---|---|
| T1 | P0 | auto | now | integration | Create order, cancel it, attempt transition to PAID/SHIPPED | Transition blocked after CANCELLED | R1 |
| T2 | P0 | auto | now | integration | GET order with status CANCELLED | Status returned, shipment details not present | R2 |
| T3 | P1 | manual | n/a | e2e | Verify client behavior when receiving CANCELLED | No client-side failure, graceful handling | R3 |
| T4 | P1 | auto | later | component | Attempt to cancel an order in SHIPPED state | Cancel rejected or handled per rules, no inconsistent state | R1 |

### Targeted Negative & Edge Cases
- EC-1: Cancel order twice
- EC-2: Cancel order after shipment

### Observability & Rollback Signals
- Metrics or logs to watch: error rate on order status transitions, API 4xx/5xx for order endpoints, client error logs for enum parsing
- Symptoms that require rollback: sustained increase in transition failures, client parsing failures breaking core journey
- Data integrity checks post-deploy: CANCELLED orders do not expose shipment details, no illegal transitions recorded

