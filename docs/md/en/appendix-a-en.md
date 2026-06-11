# Appendix A | Project Scope and Technical Specification

Agreement No.: MTS-2026-001
Version: v1.0
Date: June 09, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## A-1 Project Overview

This document defines the development scope, functional modules, and technical specifications for version 1.0 of the "Course Booking Mobile Application" (hereinafter referred to as the "System"), serving as the technical basis for cooperation between both parties.

-----

## A-2 System Module List

The following modules are entirely included in the development scope for v1.0.

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
- Slot locking: Concurrent bookings will not exceed capacity; booking button disabled when full.
- Booking deadline: Booking button automatically disabled after the deadline has passed.
- My Courses page: Three categories: Booked, Purchased, and History.

### A-3-3 Payment Process

- Create payment requests via Stripe Payment Intent.
- Webhook automatically updates order status upon successful payment.
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
- The Client shall confirm or provide modifications within 3 working days after receiving the templates; failure to reply within the time limit will be deemed as confirmation of the original templates, and the Developer may directly use them for embedding and deployment.
- The Developer is responsible for completely embedding, deploying, and linking the confirmed content in the corresponding sections of the Landing Page and the App.
- The aforementioned templates serve as a reference basis for technical integration purposes, and the Client is solely responsible for confirming final legal compliance. The Client's confirmation of the content is deemed as having conducted its own review and assuming compliance responsibility.

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

### Before Kickoff (By June 13, 2026)

| Item | Delivery Method |
|---|---|
| GitHub Repository Setup | Created and hosted under Developer's account, inviting Client as Viewer (ownership transferred upon final payment). |
| AWS Lightsail Access | Provide IAM user account or invite as Lightsail Administrator. |
| Google Play Console Access | Add as Release Manager. |
| Stripe Account API Keys | Client creates and provides them (KYC is a legal requirement). |
| motise.net Domain Access | Provide DNS management access or assist with DNS configuration. |

### Before Track B Kickoff (By June 23, 2026)

| Item | Delivery Method |
|---|---|
| Firebase Project Access | Add Developer as Editor in Firebase Console. |

### Landing Page Assets (Provide as soon as possible after first payment)

| Item | Description |
|---|---|
| Brand Assets | Logo, brand color codes (if any); if not provided, Developer will decide. |
| Company Copy | Company profile, service description, contact info; if not provided, Developer will draft based on review needs. |

> ⚠️ Failure to provide Landing Page assets will not affect the development schedule. The Developer will independently determine content and layout based on review requirements; once completed, it will be the final version.

### Before Launch and Submission (Before Track C Kickoff, Target July 07, 2026)

| Item | Description |
|---|---|
| Apple Developer Team Access | Add as App Manager in App Store Connect (Requires organization account to be activated first). |
| App Icon | 1024 × 1024 PNG format. |
| Privacy Policy URL | Notion page or any public URL. |
| Sample Course Data | Used for testing and demonstration. |
| Test Accounts (5 Sets) | 3 Students, 1 Teacher, 1 Admin. |

-----

*Appendix A has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
