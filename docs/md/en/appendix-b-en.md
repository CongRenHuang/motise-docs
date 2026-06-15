# Appendix B | Development Schedule

Agreement No.: MTS-2026-001
Date: June 15, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## B-1 Schedule Prerequisites

All timelines in this appendix are contingent upon the full completion of the following conditions by the specified dates:

| Prerequisite | Deadline | Note |
|---|---|---|
| Client provides all necessary access permissions | 2026/06/16 | See Appendix A, Section A-5 "Before Kickoff" listed items |
| motise.net domain access provision | 2026/06/16 | DNS management access or assistance with DNS configuration, prerequisite for Landing Page deployment |
| Stripe Account KYC application initiation | Within 3 working days after receipt of first payment | KYC takes 3–5 working days, must be completed by the Client personally, Developer cannot act as a proxy |
| Apple Developer Organization Account Activation (including D-U-N-S Number issuance) | 2026/07/10 | Prerequisite for Track C review submission. D-U-N-S issuance takes 5–30 working days, and Apple account review time is outside Developer's control. Submission delays due to issuance delays are not considered Developer's liability. |
| Google Play Console Organization Account Activation | 2026/06/16 | Review times for newly established companies vary. Submission delays due to Google review delays are not considered Developer's liability. |

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
| M1 | Project Kickoff (All access granted) | 2026/06/16 | — |
| M2 | DB Schema + API Skeleton Complete | 2026/06/21 | Track A |
| M3 | Auth System Complete | 2026/06/23 | Track A |
| M4 | Course Features + Stripe Integration Complete | 2026/06/30 | Track A |
| M5 | QR Code + Push + Admin Panel Complete | 2026/07/07 | Track B |
| M6 | TestFlight Testing + Bug Fixes Complete | 2026/07/13 | — |
| M7 | iOS + Android Simultaneous Submission | 2026/07/14 | — |
| M8 | iOS / Android Official Launch (Target) | 2026/07/25 | Track C Opens |
| M9 | Formal Project Delivery | 2026/08/11 | Track C Complete |

-----

## B-3 Development Track Description

### Track A | Backend and Infrastructure (6/16 – 6/30)

| Task | Description |
|---|---|
| Architecture + Env Setup | AWS Lightsail Node.js Instance, PostgreSQL Setup |
| DB Schema | 5 core tables: users, courses, bookings, orders, attendance |
| Auth System | Email / Google / Apple Sign-In, JWT, Role Permissions (Student / Teacher / Admin) |
| Course CRUD API | Create, read, update, unlist, capacity, and deadline management |
| Booking Logic API | Concurrent capacity locking, booking deadline controls |
| Stripe Integration | Payment Intent creation, Webhook order status updates |
| QR Code API | Token generation & binding, 15-min expiration, verification API |

### Track B | Frontend App and Web-based Admin (6/26 – 7/7)

| Task | Description |
|---|---|
| Course List + Detail Page | Listed course display, remaining slots, instructor info |
| Booking + Purchase Flow | Stripe UI integration, payment failure handling, terms checkbox |
| QR Code Display + Scan | Student presentation, teacher scanning/verification, expiration alerts |
| Push Notifications | Firebase FCM course reminders, rush booking alert setup |
| Web-based Admin | Course listing/unlisting, member management, order inquiry, attendance records |

### Track C | Testing, Submission, and Launch (7/10 – 8/11)

| Task | Description |
|---|---|
| TestFlight + Firebase Dist | iOS / Android E2E testing |
| Bug Fixes | Fix issues discovered during testing |
| App Store Asset Prep | Screenshots, descriptions, Privacy Policy |
| iOS + Android Submission | Simultaneous submission on July 14 |
| Review Rejection Handling | Metadata rejections: fixed within 2 working days; Functional rejections: fixed within 5 working days |
| Official Launch | Target July 25, includes 11-day Apple review buffer (7/14–7/25) |
| Post-launch Maintenance + Bug Fixes | July 25 – August 11 |
| Tech Docs + Complete Code Handover | August 11 |

-----

## B-4 Delay Clause Explanation

**Circumstances Not Constituting Developer's Liability:**

- App Store / Google Play review waiting times or platform rejection periods.
- Delays caused by the Client's failure to provide necessary resources, accounts, or access permissions on time.
- Delays in payment functions caused by failure to complete Stripe KYC verification on time.
- Delays in submission dates caused by Apple Developer Organization Account D-U-N-S Number issuance delays.
- Force majeure events (natural disasters, sudden changes in platform policies, etc.).

**Conditions for Delay Compensation:**

If functions remain incomplete due to reasons attributable to the Developer, and the milestone time is exceeded by more than 14 calendar days, the Client may calculate compensation according to the following formula. The compensation will only be calculated once during the formal delivery and acceptance of Track C, and will not accumulate across tracks:

```
Compensation Amount = Paid Amount × (Number of Incomplete Acceptance Items ÷ Total Acceptance Items in Appendix C) × 50%
Compensation Cap = 20% of the Paid Amount
```

-----

*Appendix B has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
