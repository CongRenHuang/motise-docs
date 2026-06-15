# Appendix A | Project Scope and Technical Specification

Agreement No.: MTS-2026-001
Date: June 15, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## A-1 Project Overview

This document defines the development scope, functional modules, and technical specifications for version 1.0 of the "Course Booking Mobile Application" (hereinafter referred to as the "System"), serving as the technical basis for cooperation between both parties.

-----

## A-2 System Module List

All the following modules are included in the development scope of v1.0.

| No. | Module Name | Description | Platform |
|---|---|---|---|
| M-01 | Student App Interface | Course browsing, booking, online payment, QR Code check-in, push notification reception | iOS · Android |
| M-02 | Teacher App Interface | Assigned course viewing, student list management, QR Code scanning for attendance verification | iOS · Android |
| M-03 | Web-based Admin Panel | Course management, member management, order inquiry, attendance record inquiry | Web |
| M-04 | Account Authentication | Email registration/login, Google OAuth, Apple Sign-In, mobile number binding | All Platforms |
| M-05 | Online Payment Integration | Stripe Payment Intent, Webhook order status sync, payment failure handling, duplicate payment prevention | App · Web |
| M-06 | Push Notifications | Firebase FCM course reminders (24 hours and 1 hour before start), rush booking alerts | App |
| M-07 | Infrastructure | AWS Lightsail Node.js Instance, PostgreSQL Managed Database, Object Storage | Cloud |
| M-08 | Company Website Landing Page | Single-page Motise Inc website, deployed at motise.net, serving as a prerequisite for Apple Developer organization account approval | Web |

-----

## A-3 v1.0 Detailed Functions

### A-3-1 Accounts and Roles

- Supports three login methods: Email / Password, Google OAuth, Apple Sign-In (including Face ID / Touch ID).
- Supports independent mobile number binding (not a login method, functions as additional account info).
- System roles are divided into three levels: Student, Teacher, and Admin.
- API access permissions for each role are independent; cross-role access returns a 403 error.

### A-3-2 Course Features

- Course list display: Name, time, price, remaining slots; unlisted courses are not displayed.
- Course detail page: Full description, location, quota, instructor name, and personal introduction.
- Slot locking: Slot updates use database atomic operations (such as pessimistic locking or atomic decrement) to ensure concurrent bookings do not exceed capacity; the booking button is disabled when full.
- Booking deadline: The booking button automatically closes after the deadline has passed.
- Flash Sale: A course may be configured with a sale start time and end time, and can only be booked within that time window; the booking button closes when full, sharing the same slot-locking mechanism as regular courses.
- Slot release: If a user creates an order but does not complete payment within 10 minutes, the system automatically releases the slot they occupied for other users to book.
- Oversell prevention and data consistency: Slot changes (deduction, release) are guaranteed based on database transaction-level locking / atomic operations, ensuring the displayed and actual inventory are consistent; if, after launch, the traffic scale requires an additional caching layer (such as Redis) to improve read performance, this is a technical implementation option to be separately evaluated and introduced as actually needed under the Appendix D long-term collaboration framework, and does not affect the oversell prevention guarantee set out in this section.
- Cancellation policy (Class Pass mechanism):
  - Cancellation is allowed more than 24 hours before the course starts, upon which the system automatically releases the slot, issues no refund, and instead grants a Class Pass; cancellation is not allowed within 24 hours before the course starts.
  - A Class Pass is applicable to all courses; the credit value of one Class Pass equals the original purchase amount of the cancelled course.
  - A Class Pass is non-transferable; the same account may hold multiple Class Passes simultaneously.
  - Cancellation limit: Each account is limited to a maximum of 3 "cancellations made more than 24 hours in advance" per month (30 days); the same Class Pass (i.e., the credit issued from a cancellation) cannot be cancelled again.
  - A Class Pass is valid for 1 month (30 days) from the date of issuance; it expires if unused, with no remedy or extension mechanism.
- My Courses page: Three categories: Booked, Purchased, and History.

### A-3-3 Payment Process

- Create payment requests via Stripe Payment Intent.
- Order status uses the Stripe Webhook as the sole basis for updates, and Webhook events are processed idempotently: even if the user disconnects immediately after completing payment, the backend can still correctly update the order status, deduct the slot, and generate the QR Code; after the user reconnects, the generated ticket is properly displayed in "My Courses."
- Display clear error messages upon payment failure; course will not be unlocked.
- Purchased courses will not show the purchase button to prevent duplicate payments.
- Display cancellation policy terms before purchase; users must check to agree before making payment.

### A-3-4 QR Code Check-in

- Students who have booked can view and present their unique QR Code from the course card.
- QR Code is bound to the student's account and the course; it automatically expires 15 minutes after the course starts.
- The teacher interface provides a camera scanning entrance; scanning displays student name, course info, and attendance status.
- Scanning an already verified QR Code will display "Already Checked-in" and will not double-count.
- Scanning an invalid or expired QR Code displays a clear error message.

### A-3-5 Admin Panel (Web-based)

- Course management: Add, modify, list, unlist; listed courses appear instantly on the front end.
- Member management: Query members, assign or remove teacher roles, deactivate accounts.
- Order inquiry: Student name, course name, payment status, amount.
- Attendance records: Attendance lists and check-in statuses for each course.

### A-3-6 Push Notifications

- Course reminders: Sent 24 hours and 1 hour before the start of a booked course.
- Rush booking alerts: Users can set rush alerts for specific courses and receive a push notification before booking opens.
- Users can customize whether to turn on various types of push notifications.

### A-3-7 Company Website Landing Page (M-08)

- Deployed on the Client's existing domain, motise.net.
- Content includes: Company name, brief introduction, service description, contact information.
- Layout design and presentation are determined by the Developer, aiming to meet Apple Developer organization account review requirements.
- The Client may provide brand assets (Logo, brand color codes (if any); if not provided, the Developer will decide) for the Developer's reference; final presentation is at the Developer's discretion.
- Once completed, it is the final version; subsequent layout or content modifications are excluded from the scope of this Agreement.

### A-3-8 Privacy Policy & Terms of Service Templates

- The Developer will provide basic English templates (Basic Templates) of the Privacy Policy and Terms of Service that comply with general US regulatory compliance frameworks (GDPR, CCPA basic frameworks) before the end of Track A.
- The Client shall confirm or provide modifications within 3 working days after receiving the templates; failure to reply within the timeframe will be deemed as confirmation of the original templates, and the Developer may directly use them for embedding and deployment.
- The Client may still request modifications to the **text content** of the Privacy Policy and Terms of Service after the aforementioned confirmation and before embedding and deployment in Track C. The Developer shall assist in updating and deploying such modifications, provided that they do not affect the established schedule of Track C. If the requests involve adding new consent workflows, new types of clauses, or structural changes, they shall be handled as a change of scope in accordance with Section 1.3 of the Main Agreement.
- The Developer is responsible for completely embedding, deploying, and linking the confirmed content in the corresponding sections of the Landing Page and the App.
- The aforementioned templates serve as a reference basis for technical integration purposes, and the Client is solely responsible for confirming final legal compliance. The Client's confirmation of the content is deemed as having conducted its own review and assuming compliance responsibility.

### A-3-9 Technical Documentation Delivery Specifications

The Developer shall provide technical documentation in accordance with the following specifications, which shall serve as the content basis for the corresponding acceptance items in Appendix C (A-11, B-23, C-09):

- **Deployment Guide:** Build steps for the local development environment, deployment steps for the backend server (AWS Lightsail), list and explanation of environment variables, configuration methods for third-party services (Stripe, Firebase, etc.), and instructions for the App packaging and publishing process.
- **Architecture Documentation:** Database schema description, API documentation (including key field definitions), and technical architecture and operational logic description for each module (M-01 to M-08) listed in Section A-2 of Appendix A.

The document version shall be consistent with the source code delivered for the corresponding track. Documents updated along with the development progress shall be submitted in versions applicable to the current scope during the acceptance of each track; there is no need to provide the complete version during Tracks A and B. The complete version shall be handed over together during Track C (C-09).

### A-3-10 Performance Baseline

The following baselines serve as the basis for the objective determination of performance disputes under Section 3.6.1 of the Main Agreement. The testing environment is TestFlight (or an equivalent testing environment) on general consumer-grade devices (such as iPhone 12 or equivalent or above):

- Course list page scrolling: FPS ≥ 30
- Cold start load time for main pages (course list, course detail, My Courses): ≤ 3 seconds
- Average response time between the App and the backend API: ≤ 1.5 seconds (excluding the network latency of third-party services such as Stripe and Firebase themselves, and already accounting for reasonable cloud service latency and high-load conditions)

Performance items not listed in this section, or cases where the device/network environment does not meet the above testing prerequisites, are not subject to the objective determination under Section 3.6.1 of the Main Agreement and shall still be handled under the principle of invalidity of subjective rejection in Section 3.6.

-----

## A-4 Exclusions from v1.0

The following items are explicitly excluded from the development scope of this Agreement and will be separately quoted and planned for subsequent versions:

| Item | Description |
|---|---|
| Refund UI | Refund-related functional pages; course purchase term configuration is already included in v1.0. |
| Advanced Search/Filtering | Advanced course filtering and sorting features. |
| Custom Admin App | Custom requirements beyond the standard admin panel scope. |
| Landing Page Modifications | Any layout design or content adjustments after delivery are excluded from this Agreement. |

-----

## A-5 Technical Architecture

### A-5-1 System Layers

```
┌─────────────────────────────────────────┐
│         React Native App                │
│      iOS + Android Mobile Application   │
└──────────────────┬──────────────────────┘
                   ↕ HTTPS / REST API
┌─────────────────────────────────────────┐
│      Node.js — AWS Lightsail Instance   │
│      Backend API and Business Logic     │
└──────────────────┬──────────────────────┘
                   ↕
┌─────────────────────────────────────────┐
│      PostgreSQL                         │
│      AWS Lightsail Managed Database     │
│      + Lightsail Object Storage         │
└─────────────────────────────────────────┘

Third-party Integrations
├── Stripe          Online Payments
├── Firebase FCM    Push Notifications
├── Apple OAuth     Apple Sign-In
└── Google OAuth    Google Sign-In
```

### A-5-2 Technology Stack

| Technology | Purpose | Rationale |
|---|---|---|
| React Native | iOS / Android App | Single codebase supports both platforms, lowering long-term maintenance costs. |
| Node.js | Backend API and Logic | Unified JavaScript across frontend and backend, lowering hiring barriers for maintenance. |
| PostgreSQL | Relational Database | Mature and stable; Lightsail provides managed services avoiding manual operations. |
| AWS Lightsail | Cloud Infrastructure | Fixed monthly fee (approx. $25 USD/mo), predictable costs. |
| Stripe | Online Payments | Industry standard, high compliance, mature API. |
| Firebase FCM | Push Notifications | Supports both iOS / Android, generous free tier. |

### A-5-3 Core Database Tables

| Table | Description |
|---|---|
| users | User accounts, roles, mobile numbers |
| courses | Course data, capacity, deadlines, listing status |
| bookings | Booking records, statuses |
| orders | Order data, Stripe Payment Intent IDs, payment statuses |
| attendance | QR Code tokens, verification statuses, check-in times |

-----

## A-6 Resources Provided by Client

### Before Kickoff (By June 16, 2026)

| Item | Delivery Method |
|---|---|
| GitHub Repository Setup | Created under the Client's account (or an organization designated by the Client), inviting the Developer as a Collaborator and granting Admin permissions (see Section 5.4 of the Main Agreement for details). |
| AWS Lightsail Access | Provide IAM user account or invite as Lightsail Administrator. |
| Google Play Console Access | Add as Release Manager. |
| motise.net Domain Access | Provide DNS management access or assist with DNS configuration. |

### Stripe Account Settings (KYC to be initiated within 3 working days after the first installment payment is received)

| Item | Description |
|---|---|
| Stripe Account API Keys | The Client shall apply for the Stripe account and provide the API keys after completing the KYC verification. The KYC must be completed by the Client personally (due to legal requirements, the Developer cannot act on their behalf), which takes about 3–5 working days for review. The application shall be initiated within 3 working days after the receipt of the first installment payment in accordance with Section 2.4 of the Main Agreement. If provided late, the acceptance items related to Stripe (A-07 / A-08 in Appendix C) shall be postponed, which will not be considered a delay by the Developer, nor will it trigger the delay compensation clause. |

### Before Track B Kickoff (By June 26, 2026)

| Item | Delivery Method |
|---|---|
| Firebase Project Access | Add Developer as Editor in Firebase Console. |
| UI/UX Design Source Files | The Client shall provide complete UI/UX design source files (including screen flows and visual specifications) before the kickoff of Track B (2026/06/26). If not provided on time, the Developer may proceed with development based on its own initial interface design, and such initial design shall serve as the interface acceptance baseline for Tracks B/C; the Client may not refuse acceptance or claim a Developer delay on the grounds that the interface appearance differs from designs it subsequently provides. The UI/UX provided by the Client before 2026/06/26 (or the Developer's initial design substituted for it due to late provision) constitutes the interface **design freeze** for the v1.0 launch (target 2026/08/11) and acceptance; any interface changes after this freeze are not included in the v1.0 scope of this Agreement and shall be deferred to the development period after 2026/08/11, to be separately evaluated, quoted, and scheduled under the scope-change procedure in Section 1.3 of the Main Agreement, within the Appendix D long-term cooperation framework or a separate SOW. |

> ⚠️ **Disclaimer on Design Source and Intellectual Property:** The legality of any UI/UX design source files, reference materials provided by the Client, or third-party website/App interface designs the Client designates for reference, and whether they infringe third-party intellectual property rights, shall be confirmed by and be the responsibility of the Client. If the Client requests the Developer to reference, approximate, or reproduce the interface design of a specific third-party website or App, the Client shall bear any resulting intellectual property disputes and liabilities (including copyright, trademark, trade dress, or unfair competition), and the Developer shall bear **no liability whatsoever** for infringement arising from such design sources. Based on professional judgment, the Developer has the right to refuse to reproduce a design that clearly constitutes infringement and to instead implement an original or sufficiently differentiated design, which shall not be deemed a breach or a reduction of scope.

### Landing Page Assets (Provide as soon as possible after first payment)

| Item | Description |
|---|---|
| Brand Assets | Logo, brand color codes (if any); if not provided, Developer will decide. |
| Company Copy | Company profile, service description, contact info; if not provided, Developer will draft based on review needs. |

> ⚠️ Failure to provide Landing Page assets will not affect the development schedule. The Developer will independently determine content and layout based on review requirements; once completed, it will be the final version.

### Before Launch and Submission (Before Track C Kickoff, Target July 10, 2026)

| Item | Description |
|---|---|
| Apple Developer Team Access | Add as App Manager in App Store Connect (Requires organization account to be activated first). |
| App Icon | 1024 × 1024 PNG format. |
| Privacy Policy URL | Any public URL on motise.net. |
| Sample Course Data | Used for testing and demonstration. |
| Test Accounts (5 Sets) | 3 Students, 1 Teacher, 1 Admin. |

-----

*Appendix A has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
