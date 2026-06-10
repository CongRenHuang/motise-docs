# Appendix B | Development Schedule

Agreement No.: MTS-2026-001
Version: v1.0
Date: June 09, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## B-1 Schedule Prerequisites

All timelines in this appendix are contingent upon the full completion of the following conditions by the specified dates:

| Prerequisite | Deadline | Note |
|---|---|---|
| Client provides all necessary access permissions | 2026/06/13 | See Appendix A, Section A-6 (Excluding Apple org access) |
| motise.net domain access provision | 2026/06/13 | DNS management access or assistance with DNS config, prerequisite for Landing Page deployment |
| Stripe Account KYC application initiation | Within 3 working days after receipt of first payment | KYC takes 3–5 working days, must be completed by the Client personally, Developer cannot act as a proxy |
| Apple Developer Organization Account Activation (including D-U-N-S Number issuance) | 2026/07/07 | Prerequisite for Track C review submission. D-U-N-S issuance takes 5–30 working days, and Apple account review time is outside Developer's control. Submission delays due to issuance delays are not considered Developer's liability. |
| Google Play Console Organization Account Activation | 2026/06/13 | Review times for newly established companies vary. Submission delays due to Google review delays are not considered Developer's liability. |

> ⚠️ For any delays in prerequisites, milestones and delivery dates will be proportionally postponed, and such delays are not considered the Developer's liability.

-----

## B-1-1 Preliminary Work | Landing Page

**Nature:** Preliminary required work before main development, not attached to any acceptance track.
**Purpose:** Ensure motise.net has a complete company information page, acting as a prerequisite for Apple Developer organization account approval.

| Item | Timing |
|---|---|
| Start Time | After the first installment ($540 USD) is fully received |
| Completion Deadline | Within **3 working days** after receipt of payment |
| Acceptance Method | motise.net is browsable, content meets Apple review requirements (See Appendix C P-01) |

> After the Landing Page is completed, the Client should immediately initiate the Apple Developer organization account application process to minimize overall schedule delays caused by D-U-N-S issuance wait times.

-----

## B-2 Key Milestones

| No. | Milestone | Target Date | Acceptance Track |
|---|---|---|---|
| M1 | Project Kickoff (All access granted) | 2026/06/13 | — |
| M2 | DB Schema + API Skeleton Complete | 2026/06/18 | Track A |
| M3 | Auth System Complete | 2026/06/20 | Track A |
| M4 | Course Features + Stripe Integration Complete | 2026/06/27 | Track A |
| M5 | QR Code + Push + Admin Panel Complete | 2026/07/04 | Track B |
| M6 | TestFlight Testing + Bug Fixes Complete | 2026/07/10 | — |
| M7 | iOS + Android Simultaneous Submission | 2026/07/11 | — |
| M8 | iOS / Android Official Launch (Target) | 2026/07/22 | Track C Opens |
| M9 | Formal Project Delivery | 2026/08/04 | Track C Complete |

-----

## B-3 Development Track Description

### Track A | Backend and Infrastructure (6/13 – 6/27)

| Task | Description |
|---|---|
| Architecture + Env Setup | AWS Lightsail Node.js Instance, PostgreSQL Setup |
| DB Schema | 5 core tables: users, courses, bookings, orders, attendance |
| Auth System | Email / Google / Apple Sign-In, JWT, Role Permissions (Student / Teacher / Admin) |
| Course CRUD API | Create, read, update, unlist, capacity, and deadline management |
| Booking Logic API | Concurrent capacity locking, booking deadline controls |
| Stripe Integration | Payment Intent creation, Webhook order status updates |
| QR Code API | Token generation & binding, 15-min expiration, verification API |

### Track B | Frontend App and Web-based Admin (6/23 – 7/4)

| Task | Description |
|---|---|
| Course List + Detail Page | Listed course display, remaining slots, instructor info |
| Booking + Purchase Flow | Stripe UI integration, payment failure handling, terms checkbox |
| QR Code Display + Scan | Student presentation, teacher scanning/verification, expiration alerts |
| Push Notifications | Firebase FCM course reminders, rush booking alert setup |
| Web-based Admin | Course listing/unlisting, member management, order inquiry, attendance records |

### Track C | Testing, Submission, and Launch (7/7 – 8/4)

| Task | Description |
|---|---|
| TestFlight + Firebase Dist | iOS / Android E2E testing |
| Bug Fixes | Fix issues discovered during testing |
| App Store Asset Prep | Screenshots, descriptions, Privacy Policy |
| iOS + Android Submission | Simultaneous submission on 7/11 |
| Review Rejection Handling | Metadata rejections: fixed within 2 working days; Functional rejections: fixed within 5 working days |
| Official Launch | Target 7/22, includes 11-day Apple review buffer (7/11–7/22) |
| Post-launch Maintenance + Bug Fixes | 7/22 – 8/4 |
| Tech Docs + Complete Code Handover | 8/4 |

-----

## B-4 Schedule Overview (Gantt Chart)

```
              W1       W2       W3       W4       W5       W6       W7       W8
              6/9      6/16     6/23     6/30     7/7      7/14     7/21     7/28
              ────────────────────────────────────────────────────────────────────

Track A · Backend & Infrastructure
Arch Design + Env Setup      [=]
DB Schema + API Skeleton     [=]
Auth System                           [=]
Backend API (Courses+Bookings+Orders) [========]
Stripe Payment + Webhook              [========]
QR Code Gen + Verification API                [========]

Track B · Frontend App & Admin
Course List + Detail Page                     [=]
Booking + Purchase + Stripe UI                [========]
QR Code Display + Scan + Push                         [=]
Admin Panel (Courses/Members/Orders)                  [=]

Track C · Testing · Submission · Launch
TestFlight + E2E + Bug Fix                            [=]
🍎🤖 iOS + Android Submission                         [7/11]
Apple / Google Review Pending                                 [////]
Rejection Handling Buffer                                     [////]
✅ iOS / Android Official Launch                                      [✓7/22]
Post-launch Maintenance + Bug Fixes                                   [=======]
📦 Formal Project Delivery                                                    [✓8/4]
```

-----

## B-5 Delay Clause Explanation

**Circumstances Not Constituting Developer's Liability:**

- App Store / Google Play review waiting times or platform rejection periods.
- Delays caused by the Client's failure to provide necessary resources, accounts, or access permissions on time.
- Delays in payment functions caused by failure to complete Stripe KYC verification on time.
- Force majeure events (natural disasters, sudden changes in platform policies, etc.).

**Conditions for Delay Compensation:**

If key milestones are delayed by more than 14 calendar days due to reasons attributable to the Developer, starting from the 15th day, 0.5% of the current installment amount will be deducted daily as compensation, capped at 20% of the current installment.

-----

*Appendix B has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
