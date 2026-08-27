# Software Engineering Lab Submissions (PES1UG24CS031)

**Student Name:** Aditya T J  
**SRN:** PES1UG24CS031  
**Department:** Computer Science & Engineering  
**Institution:** PES University  

---

## Lab Index

| Lab | Topic | Problem Statement | Domain | Status | Deliverables |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **Lab 1** | Requirements Engineering & UML Use-Case Modelling | **#31: Multi-Vendor Artisan E-Commerce Marketplace** | Retail, E-Commerce & Finance | **Completed** | [Lab 1 Folder](LAB1/) &bull; [Docs](LAB1/docs/) |

---

## Lab 1: Multi-Vendor Artisan E-Commerce Marketplace

An online marketplace enabling independent craftspeople to set up storefronts, manage product catalogs, receive orders, and receive automated split payouts with platform commission deductions.

### Quick Deliverable Links
- 📋 **Requirements Table:** [`01_Requirements_Table.pdf`](LAB1/docs/01_Requirements_Table.pdf) · [`01_Requirements_Table.docx`](LAB1/docs/01_Requirements_Table.docx) · [`01_Requirements_Table.xlsx`](LAB1/docs/01_Requirements_Table.xlsx)
- 📊 **UML Use-Case Diagram:** [`02_UseCase_Diagram.pdf`](LAB1/docs/02_UseCase_Diagram.pdf) · [`02_UseCase_Diagram.png`](LAB1/docs/02_UseCase_Diagram.png) · [Editable `.drawio`](LAB1/diagram/artisan_marketplace_usecase.drawio)
- 📄 **Use-Case Flow Spec:** [`03_UseCase_Flow_Specification.pdf`](LAB1/docs/03_UseCase_Flow_Specification.pdf) · [`03_UseCase_Flow_Specification.docx`](LAB1/docs/03_UseCase_Flow_Specification.docx)

---

### UML Use-Case Diagram

![UML Use-Case Diagram](LAB1/docs/02_UseCase_Diagram.png)


---

### Requirements Summary Table

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **FR-001** | Functional | The system shall split customer cart payments at checkout, allocating respective item earnings to multiple independent vendor accounts after deducting a 5% platform fee. | **High** | **Pass:** Split payout calculations balance to total cart value.<br>**Fail:** Payout calculation discrepancies. | Ensures accurate, automated financial distribution to independent artisans while securing platform transaction revenue. *(Given in PS #31)* |
| **FR-002** | Functional | The system shall allow artisan vendors to set up and manage an independent storefront profile, including artisan bio, shop policies, and linked payout disbursement account details. | **High** | **Pass:** Storefront profile updates and verified payout details are successfully saved and rendered publicly.<br>**Fail:** Missing mandatory fields or unvalidated payout details prevent publishing. | Enables independent craftspeople to establish their distinct brand identity and receive automated financial payouts. |
| **FR-003** | Functional | The system shall allow artisan vendors to create, update, and manage handcrafted product listings with titles, descriptions, pricing, inventory quantities, and high-resolution product media. | **High** | **Pass:** New/updated product listings appear in search within 5 seconds with accurate stock counts.<br>**Fail:** Listings with invalid pricing (≤ 0) or missing mandatory attributes fail validation. | Empowers artisans to maintain an up-to-date catalog of handcrafted items and prevent overselling. |
| **FR-004** | Functional | The system shall allow shoppers to add handcrafted items from multiple independent artisan vendors into a unified cart and execute a single consolidated checkout order. | **High** | **Pass:** Cart aggregates items across distinct vendors, calculates itemized totals, applies coupons, and initiates payment.<br>**Fail:** Cart fails to itemize multi-vendor items or calculation mismatch occurs. | Provides a seamless purchasing experience for shoppers buying from multiple artisans simultaneously. |
| **FR-005** | Functional | The system shall notify artisan vendors of confirmed customer orders containing their respective products and allow vendors to update fulfillment status (Processing, Dispatched, Delivered) with carrier tracking details. | **Medium** | **Pass:** Vendor dashboard immediately displays incoming sub-orders and status transitions trigger automated notifications.<br>**Fail:** Order details fail to isolate vendor-specific items or status updates fail to persist. | Enables independent artisans to fulfill customer orders independently while keeping shoppers informed. |
| **NFR-001** | Performance & Security | The product catalog must support high-resolution image rendering with CDN caching delivering load times < 500 ms. | **High** | **Pass:** Benchmarking tests confirm target latency (< 500 ms) and security standards under simulated peak load.<br>**Fail:** Catalog page load latency ≥ 500 ms or CDN caching failure under peak load. | Ensures fast page loading for image-heavy handcrafted goods, preserving user engagement and minimizing bounce rates. *(Given in PS #31)* |
| **NFR-002** | Security & Compliance | The system shall encrypt all sensitive financial transactions and payout account data in transit using TLS 1.3 and at rest using AES-256 encryption, adhering to PCI-DSS Level 1 compliance standards. | **High** | **Pass:** Automated audits confirm 100% encryption coverage for payment payloads with zero plain-text storage of credentials.<br>**Fail:** Any unencrypted transmission or unmasked storage of sensitive banking/card data detected. | Protects shoppers' financial credentials and vendors' banking payout information against unauthorized access and data breaches. |

---

### Core Use Case Flow: UC-03 Place Order (Multi-Vendor Checkout)

* **Primary Actor:** Shopper &bull; **Secondary Actors:** Payment Gateway, Artisan Vendor
* **Traces to:** FR-001, FR-004, NFR-002 &bull; **Stereotypes:** `«include»` UC-04 Process Split Payment, `«extend»` UC-05 Apply Discount Code

#### Main Success Scenario
1. Shopper navigates to the checkout view from the multi-vendor shopping cart.
2. System retrieves cart items across all artisan vendors, locks inventory quantities, and displays an itemized order summary.
3. Shopper selects or confirms the delivery shipping address and recipient contact details.
4. System computes shipping costs per artisan vendor, applicable taxes, and presents the grand total payable amount.
5. Shopper selects payment method (Credit/Debit Card, UPI, Net Banking) and enters payment credentials.
6. System invokes **`«include»` UC-04: Process Split Payment**, routing encrypted transaction payload (TLS 1.3) to the **Payment Gateway**.
7. Payment Gateway authorizes the full consolidated cart amount and returns a success authorization token.
8. System automatically **deducts the 5% platform commission** and allocates remaining item earnings to respective artisan vendor payout accounts (adhering to **FR-001**).
9. System decrements catalog inventory quantities, decomposes master order into isolated vendor sub-orders, and schedules disbursement settlements.
10. System displays an order confirmation screen with order ID and transmits confirmation receipts to the shopper and alert notifications to respective artisan vendors. Use case ends successfully.

---

For complete detailed specifications, visit the [`LAB1/` directory](LAB1/).
