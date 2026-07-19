# Booking Management System — RFP (extracted from BMS_updated.docx)

REQUEST FOR PROPOSAL — June 10, 2016
Issuer: EPAM Systems Inc., Newtown, PA

## Executive Summary

Established in 1993, EPAM Systems, Inc. (NYSE: EPAM) is recognized as a leader in software product development... EPAM serves clients worldwide utilizing its award-winning global delivery platform and its locations in over 26 countries. EPAM employs over 19,000 professionals. It requires frequent traveling of employees across different EPAM's and clients' offices.

EPAM procured in average 5000 hotel rooms and 1000 taxis in 2015. EPAM employs mostly manual approach for booking, which requires significant amount of time for communication with employees, travel department and hotel and transport suppliers.

EPAM is looking for robust booking management system for hotel and transport suppliers which can incorporate all current and planned future level of accommodation and transport management requirements.

## Project Overview

EPAM wants to work with a Supplier to create a **SaaS-based booking management system which the Supplier will then host and support**. This system will become the sole source of accurate Hotel and Transport bookings allowing access for travel department, transport suppliers and employees to manage their confirmed bookings.

EPAM is open to recommendations on system design. Supplier should meet the requirements in a cost-efficient manner.

Key aspects:
- **Cost Reduction:** centralized reporting tool for day-to-day management, improved hotel management and financial budgeting.
- **Automation:** enhanced automation to remove existing manual processes.
- **Integration:** integrated with EPAM's Cost Tracking Center (API), UPSA (API) and SSO (Documentation).
- **Simplistic and Intuitive:** common look and feel for all users, clear business processes.
- **Flexibility:** highly configurable solution which can support EPAM's evolution.
- **Performance:** highly performant system, supports high demand and critical instances such as major disruption situations.

### Context diagram (image2.png in the docx)

- Внутри системы: **Employees Portal**, **Administration Portal**, **Suppliers Portal**, **Admin and Support**.
- Акторы: Employees (review/accept bookings; review/update trip details в CTC), Travel Department (alerts/notifications, manage bookings, configuration and rules, reports), IT Support, Hotel suppliers (manual upload of available bookings), Transport suppliers (manual upload of pricing).
- Внешние системы: **Cost Tracking Center** (hotel and transport requirements → BMS), **External Hotel Booking Systems** (automatic search and booking), **External Transport Booking Systems** (automatic search and booking).

## Functional Requirements

### Supplier Search and Prioritization
Intelligent search across multiple third-party systems and manually uploaded bookings based on requirements specified in the system. Prioritization based on matching to booking requirements and custom rules defined by Travel Manager in Administration Portal. Booking requirements initially defined in Cost Tracking Center, amendable in Employees Portal / Administration Portal. Prioritization may change over time as requirements or rules change.

### Approval and Booking
Robust approval and booking processes. Stages: Proposed, Accepted/Rejected, Approved/Declined, Booked/Canceled, Paid. Stage changes supported by notifications via **email and SMS**. Ability to change and extend booking process in future. Along with automatic booking — manual hotel booking managed by Travel Manager via web site forms.

### Changes Management
Frequent integration to CTC to update booking requirements. New requirements, changes and cancellations driven by these updates. Merge according to defined policy; on conflicts — alerts to parties. Manual change of selected hotel as required.

### 3rd Party Hotel Suppliers
Access to the system, manual upload of available booking, pricing and other details. Booking handled manually.

### Support Transport Suppliers
Only one transport supplier integrated automatically (**Uber**); all others manual. Pick-up/drop-off locations initially loaded from CTC, amendable in Employees and Administration portals; ability to override.

### Transport Combining Opportunities
Combining of multiple transport bookings.

### 3rd Party Transport Suppliers
Access to the system, manual upload of pricing details. Booking handled manually.

### Employees Portal
- View details and status of each booking.
- Confirm hotel and transport reservations.
- View and print confirmed reservations.
- Seamless access via SSO.
- Capture feedback from employees, associated to a particular booking.

### Administration Portal
Capabilities for Travel Manager: system configuration, visibility of booking statuses, reporting; front-end to administer the system and control configuration.

### Reporting Capabilities
Reports: booking details, suppliers reporting, financial reporting.

## Non-Functional Requirements

| Category | Requirement |
|---|---|
| Usability | Modern web-based technologies, fresh/clean/intuitive UX |
| Usability | Multiple display resolutions incl. mobile/portable devices |
| Architectural | Scalable, high-performing structured database platform, large volumes |
| Architectural | Keep technologies up to date; periodic reviews and planned upgrades |
| Architectural | High configurability for changes in legislation, policy, process, org structure |
| Availability & Performance | Screen loads <2 s; report generation not excessive; criteria defined at design stage |
| Disaster Recovery | Highly available and resilient |
| Configuration Management | Config management and version control across all environments and documents |
| Deployability | Robust release/patch promotion procedures minimizing business impact |
| Scalability | Designed to grow in the future |
| Data Security | TLS 1.2 minimum for all authenticated client traffic |
| Data Security | Customer data compliant with Data Protection Act |

## Чего в РФП нет (важно для оценки)

- Сроков, бюджета, критериев выбора поставщика, процедуры подачи предложений.
- Объёмов нагрузки кроме косвенных (5000 отелей + 1000 такси в год ≈ низкая транзакционная нагрузка).
- Деталей API CTC/UPSA (только факт наличия API), деталей SSO (только "Documentation").
- Состава команды, Definition of Done, модели поддержки после запуска (кроме "Supplier will host and support").
