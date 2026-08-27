# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Problem Statement #31 (Retail, E-Commerce & Finance): Multi-Vendor Artisan E-Commerce Marketplace**
Actors: Shopper, Artisan Vendor

## Contents

| File | Deliverable |
|---|---|
| `Requirements_Table.docx` | Requirements table — FR-001 to FR-005 (Functional) and NFR-001 to NFR-002 (Non-Functional), each with ID, Type, Description, Priority, Acceptance Criteria, and Rationale. |
| `UseCase_Diagram.pdf` | UML Use-Case Diagram — actors (Shopper, Artisan Vendor, external Payment Gateway), 7 use cases (UC-01–UC-07), one `<<include>>` relationship (Place Order → Process Split Payment) and one `<<extend>>` relationship (Apply Discount Code → Process Split Payment). |
| `UseCase_Flow_PlaceOrder.docx` | One-page use-case flow specification for **UC-03 Place Order**: Preconditions, Postconditions, Main Success Scenario, and one Alternate Flow (payment declined). |

## Summary

The system splits customer cart payments at checkout across independent vendor accounts (after a 5% platform fee), lets artisan vendors self-manage their storefront catalog, and lets shoppers search across vendors and check out multiple vendors' items in a single order.
