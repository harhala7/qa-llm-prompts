### Summary
- Change intent: Refactor order status handling and introduce CANCELLED state
- Areas touched: Order status enum, transition logic, API response mapping
- Non-obvious side effects: Invalid transitions from CANCELLED, incomplete API responses

---

### Risk Register
| Risk ID | Area | Impact | Likelihood | Evidence in diff | What could break |
|-------|------|--------|------------|------------------|------------------|
| R1 | State transitions | High | Med | canTransition logic changed | Orders may move to invalid states |
| R2 | API contract | High | Med | mapper.ts comment on CANCELLED | Clients may receive unexpected responses |
| R3 | Backward compatibility | Med | Low | New enum value | Older clients may not handle CANCELLED |

---

### Regression Checklist
| Test ID | Priority | Type | Scope | What to execute | Expected result | Risk refs |
|------|----------|------|-------|-----------------|-----------------|-----------|
| T1 | P0 | auto | integration | Create order → cancel → attempt further transition | Transition blocked | R1 |
| T2 | P0 | auto | api | GET order with CANCELLED status | Status returned, no shipment data | R2 |
| T3 | P1 | manual | api | Existing clients parse status field | No client-side failure | R3 |
| T4 | P1 | auto | component | Cancel already SHIPPED order | Transition rejected | R1 |

---

### Targeted Negative & Edge Cases
- Cancel order twice
- Cancel order after shipment
- Cancel order with missing shipment info

---

### Observability & Rollback Signals
- Monitor error rate on order status transitions
- Watch API client error logs for enum parsing failures
- Rollback if order lifecycle errors spike after deploy
