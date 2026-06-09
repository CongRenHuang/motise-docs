# Appendix C | Acceptance Criteria

Agreement No.: MTS-2026-001
Version: v1.0
Date: June 09, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## C-1 Acceptance Principles

### C-1-1 Acceptance Structure

Acceptance is conducted in three tracks, each with an independent time window. Once a track passes acceptance, its items are locked and cannot be challenged in subsequent tracks.

| Track | Scope | Development Period | Acceptance Period |
|---|---|---|---|
| Track A | Backend and Infrastructure | 6/13 – 6/27 | 5 working days after completion |
| Track B | Frontend App and Web-based Admin | 6/23 – 7/4 | 5 working days after completion |
| Track C | Launch and Production Environment | 7/7 – 8/4 | 7 working days after launch |

### C-1-2 Acceptance Protection Clauses

1. **Acceptance standards rely on functional behavior.** Interface design must meet the minimum standards of written confirmed design drafts. Rejections based on subjective descriptions (e.g., "feels wrong") must be accompanied by specific functional issues; otherwise, they are deemed accepted.
2. **Failure to reply in writing implies acceptance.** If the Client does not submit written acceptance results within the acceptance period, the track is fully accepted.
3. **Weekly meeting confirmation mechanism.** If the Client does not raise written objections within 24 hours after a weekly sync, the stage progress is considered confirmed and cannot be challenged later.
4. **Track locking.** Once a track passes acceptance, it is locked and cannot be objected to during subsequent tracks or at formal delivery.
5. **New requests quoted separately.** New requirements raised during acceptance are excluded from the current scope and will be quoted separately for the next version.
6. **App Store / Google Play Rejection Handling:** Metadata rejections will receive a fixed version within 2 working days; functional rejections will receive a fixed version within 5 working days.

-----

## C-2 Preliminary Work Acceptance | Landing Page

**Nature:** Independent preliminary work, unattached to any track. Locked upon passing, unaffected by subsequent tracks.
**Deadline:** Within 3 working days after receipt of the first payment.
**Acceptance Method:** The Client browses motise.net via browser to verify it operates normally.

| # | Item | Criteria |
|---|---|---|
| P-01 | Landing Page Launch | motise.net is browsable; page contains company name (Motise Inc), service overview, contact info; layout meets Apple Developer org review standards |

> **Layout Notes:** Final layout is determined by the Developer based on review needs. The Client may provide brand assets for reference, but it is not mandatory. Post-delivery layout or content modifications are not covered by this Agreement.

**Preliminary Work Acceptance Result**

| Field | Value |
|---|---|
| Payment Receipt Date | |
| Deadline | 3rd working day after payment |
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-3 Track A Acceptance | Backend and Infrastructure

**Development Period: 2026/06/13 – 2026/06/27**
**Method:** API Documentation + Postman Test Report. The Client does not operate an interface; Developer provides test results for confirmation.

| # | Item | Criteria |
|---|---|---|
| A-01 | DB Schema | 5 core tables (courses, users, bookings, orders, attendance) created matching Appendix A. Method: ER Diagram or screenshot |
| A-02 | AWS Lightsail Env | Node.js Instance + PostgreSQL built. Method: Client logs into AWS Console to verify resources |
| A-03 | Auth API | Email reg/login, Google OAuth, Apple Sign-In (JWT), phone binding callable. Method: Postman report (200 OK) |
| A-04 | Role Permissions | Teacher/Student/Admin have correct access; cross-role returns 403. Method: Postman report |
| A-05 | Course CRUD API | Create, read, update, unlist APIs work. Capacity and deadlines stored correctly |
| A-06 | Booking Logic API | Concurrent capacity locking works; booking past deadline returns correct error |
| A-07 | Stripe Payment Intent | Backend API generates Payment Intent and returns client_secret. Method: Stripe Test Mode / Postman |
| A-08 | Stripe Webhook | Successful payment event updates order status. Method: Stripe CLI webhook trigger |
| A-09 | QR Code Gen API | Purchased users get a unique token bound to course/account; expires 15 mins after start |
| A-10 | QR Code Verify API | Teacher calling verification marks attendance; duplicates show "Already Checked-in"; invalid tokens error |

> ⚠️ **Stripe Prerequisite:** Client must start Stripe KYC within 3 working days of the first payment. Delays here will postpone A-07/A-08 acceptance without triggering Developer delay penalties.

**Track A Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-4 Track B Acceptance | Frontend App and Web Admin

**Development Period: 2026/06/23 – 2026/07/04**
**Method:** Real-device testing via TestFlight (iOS) + Firebase Distribution (Android). The Client operates the full flow.

### Authentication

| # | Item | Criteria |
|---|---|---|
| B-01 | Email Login | Reg, login, logout work; wrong password shows error |
| B-02 | Google/Apple Login | Auth page pops up, successful entry; Apple supports Face ID / Touch ID |
| B-03 | Phone Binding | Settings page allows phone binding, shows success status |
| B-04 | Role Interface | Student sees Student UI; Teacher sees Teacher UI |

### Course Features

| # | Item | Criteria |
|---|---|---|
| B-05 | Course List | Shows listed courses (name, time, price, slots). Test: List 3 courses via admin |
| B-06 | Course Detail | Full descriptions, time, location, slots, instructor profile |
| B-07 | Capacity Limits | Booking button disabled when full. Test: Set slot=1, verify 2nd user fails |
| B-08 | Booking Deadline | Button disables after deadline |
| B-09 | My Courses | Booked, Purchased, History display correctly; QR Code viewable |

### Stripe Payments

| # | Item | Criteria |
|---|---|---|
| B-10 | Payment Flow | Credit card payment marks course "Purchased". Test: Stripe 4242 4242 4242 4242 |
| B-11 | Payment Failure | Failed cards show error, course unlocked. Test: Stripe 4000 0000 0000 0002 |
| B-12 | Duplicate Prevention | Buy button disappears for purchased courses |
| B-13 | Order Sync | Admin panel shows updated order and payment status immediately |

### QR Code Check-in

| # | Item | Criteria |
|---|---|---|
| B-14 | QR Code Display | Valid QR Code shown with expiration warning and "Personal use only" notice |
| B-15 | QR Code Expiration | Invalidates 15 mins after course start. Test: Set start to +16 mins, verify failure |
| B-16 | Teacher Scan | Camera scan shows info, confirms attendance |
| B-17 | Duplicate Scan Guard | Scanning an used QR Code shows "Already Checked-in" |
| B-18 | Invalid QR Handling | Invalid tokens show clear error messages |

### Admin Panel (Web-based)

| # | Item | Criteria |
|---|---|---|
| B-19 | Course Management | Add, modify, list, unlist courses; reflects on frontend instantly |
| B-20 | Member Management | Query members, assign/remove Teacher roles, deactivate |
| B-21 | Order Inquiry | Search orders by student, course, status, amount |
| B-22 | Attendance Records | View attendance lists and check-in statuses |

**Track B Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-5 Track C Acceptance | Launch and Production

**Development Period: 2026/07/07 – 2026/08/04**
**Method:** Final validation using the official release App (Target acceptance start: 7/22).

| # | Item | Criteria |
|---|---|---|
| C-01 | App Store Launch | Passed Apple review, downloadable on App Store |
| C-02 | Google Play Launch | Passed Google review, downloadable on Google Play |
| C-03 | Course Reminders | Push notifications received 24h & 1h prior; toggles work. Test: Send test push |
| C-04 | Rush Alerts | "Set Alert" triggers push before booking opens. Test: Limited-time course alert |
| C-05 | AWS Production | Node.js + DB deployed fully on AWS. Method: Console access validation |
| C-06 | Privacy & Consent | First launch demands privacy policy consent; link works |
| C-07 | Purchase Terms | Cancellation policy shown; must check box to pay. Refund UI not in v1.0 |
| C-08 | Stability Check | Browse → Book → Pay → Check-in runs 3 times without crash (Stripe Live Mode) |
| C-09 | Docs Handover | API docs, DB Schema, 3rd-party configs, handover docs complete |
| C-10 | Code Handover | GitHub Repo transferred, README complete. Collaborator roles updated |

> ⚠️ **App Store and Google Play review times are outside Developer's control.** Delays non-attributable to code issues will not count as Developer failure. Functional rejections will be fixed until approved.

**Track C Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-6 Overall Acceptance Summary

| Track | Total Criteria |
|---|---|
| Preliminary (Landing) | 1 |
| Track A | 10 |
| Track B | 22 |
| Track C | 10 |
| **Total** | **43** |

**Final Delivery Confirmation**

| Field | Value |
|---|---|
| Delivery Date | |
| Cooperation Scenario | ☐ Scenario 1 (Long-term, $1,800)　☐ Scenario 2 (One-off, $2,499) |
| Client Signature | |
| Developer Signature | |

-----

*Appendix C has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
