# Appendix C | Acceptance Criteria

Agreement No.: MTS-2026-001
Date: June 15, 2026

Parties: Motise Inc (Client) / HUANG CONG REN (Developer)

-----

## C-1 Acceptance Principles

### C-1-1 Acceptance Structure

Acceptance is conducted in three tracks, each with an independent time window. Once a track passes acceptance, its items are locked and cannot be challenged in subsequent tracks.

| Track | Scope | Development Period | Acceptance Period |
|---|---|---|---|
| Track A | Backend and Infrastructure | 6/16 – 6/30 | 5 working days after completion |
| Track B | Frontend App and Web-based Admin | 6/26 – 7/7 | 5 working days after completion |
| Track C | Launch and Production Environment | 7/10 – 8/11 | 14 working days after launch |

### C-1-2 Acceptance Protection Clauses

1. **Acceptance standards rely on functional behavior.** Interface design must meet the minimum standards of written confirmed design drafts; if the Client does not provide UI/UX design source files by the deadline set in Appendix A, Section A-6 (before the kickoff of Track B), the Developer's own initial interface design shall serve as the interface acceptance baseline, and the Client may not reject delivery on the grounds that the interface appearance differs from designs it subsequently provides. Rejections based on subjective descriptions (e.g., "feels wrong") must be accompanied by specific functional issues; otherwise, they are deemed accepted.
2. **Failure to reply in writing implies acceptance.** Upon the expiration of the acceptance period for each track, if the Client fails to submit written acceptance results, the Developer shall issue a reminder notice; if the Client still fails to submit written acceptance results more than 3 working days after the reminder is delivered, all items in that track shall be deemed to have passed acceptance.
3. **Weekly meeting confirmation mechanism.** If the Client does not raise written objections within 48 hours after a weekly sync, the stage progress is considered confirmed and cannot be challenged later.
4. **Track locking.** Once a track passes acceptance, it is locked and cannot be objected to during subsequent tracks or at formal delivery.
5. **New requests quoted separately.** New requirements raised during acceptance are excluded from the current scope and will be quoted separately for the next version.
6. **App Store / Google Play Rejection Handling:** Metadata rejections will receive a fixed version within 2 working days; functional rejections will receive a fixed version within 5 working days.
7. **Re-acceptance limits:** For the list of written modification suggestions submitted by the Client during the acceptance period, after the Developer completes the modifications, the Client can only perform re-acceptance on the modification results of the items originally listed in the list, and shall not propose new modification suggestions outside the original list during re-acceptance. The re-acceptance period is limited to 3 working days; upon the expiration of the re-acceptance period, if the Client fails to submit re-acceptance results, the Developer shall issue a reminder notice, and if the Client still fails to submit re-acceptance results more than 3 working days after the reminder is delivered, all items in the list shall be deemed to have passed re-acceptance.
8. **Regression Bug:** If the code changes made by the Developer to correct items in the current list directly cause new functional errors in other items within the same acceptance list, or in existing functions of items that have previously passed acceptance (subject to the standards of Section 1, with a clear explanation of the functional issue), the Client may raise them during the re-acceptance period together, free from the restriction of Section 7 "no new suggestions outside the original list" and without constituting a violation of Track Locking under Section 4. The Developer shall correct them together; for the additional correction time required, the re-acceptance period for that specific item may be extended by 3 working days, and the re-acceptance period for other items shall not be affected. The re-acceptance of regression bugs is strictly limited to confirming that the defect has been corrected, and no other new suggestions may be derived and proposed.

### C-1-3 Technical Criteria and Stability Standards

1. **Technical Criteria for Determination:** Functional acceptance of each item shall be based on successful code compilation and operation, correct data return verified by API testing (e.g., Postman), or actual operational capability in a testing environment (e.g., Landing Page on a real browser, App on TestFlight), and "complete compliance with the corresponding Criteria description for that item in Appendix C" as the passing standard.
2. **System Stability Requirements:** The core functions and processes under acceptance must not contain blocker bugs or major defects that cause system crashes or freeze (Critical Bugs) during testing. Operational testing of the main flow must exhibit continuous running stability to be considered as passing the acceptance.

-----

## C-2 Preliminary Work Acceptance | Landing Page

**Nature:** Independent preliminary work, unattached to any track. Locked upon passing, unaffected by subsequent tracks.
**Deadline:** Within 3 working days after receipt of the first payment.
**Acceptance Method:** The Client browses motise.net via browser to verify it operates normally.

| # | Item | Criteria |
|---|---|---|
| P-01 | Landing Page Launch | motise.net is browsable; page contains company name (Motise Inc), service overview, contact info; layout meets Apple Developer org review standards |

> **Layout Notes:** Final layout is determined by the Developer based on review needs. The Client may provide brand assets (Logo, brand colors, copy) for reference, but it is not mandatory. Post-delivery layout or content modifications are not covered by this Agreement.

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

**Development Period: 2026/06/16 – 2026/06/30**
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
| A-11 | Track A Technical Documentation | Provide draft API documentation and database Schema description documents covering the completed modules of Track A, matching the specifications of Section A-3-9 of Appendix A |

> ⚠️ **Stripe Prerequisite:** Client must start Stripe KYC within 3 working days of the first payment. Delays here will postpone A-07/A-08 acceptance without triggering Developer delay penalties.

**Track A Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-4 Track B Acceptance | Frontend App and Web Admin

**Development Period: 2026/06/26 – 2026/07/07**
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
| B-23 | Track B Technical Documentation | Provide interface description documentation for the frontend App and Web-based backend, and draft setup instructions for third-party services (Firebase), matching the specifications of Section A-3-9 of Appendix A |

**Track B Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-5 Track C Acceptance | Launch and Production

**Development Period: 2026/07/10 – 2026/08/11**
**Method:** Final validation using the official release App (Target acceptance start: July 25).
**Acceptance Period:** 14 working days after official launch.

**Platform Review Buffer and Acceptance Payment Trigger Instructions (in accordance with Sections 4.7.1 and 4.7.2 of the Main Agreement):**

If the App cannot be officially published on the App Store or Google Play due to the following reasons not attributable to the Developer, the start date of the acceptance period shall be adjusted as follows:
- The Client fails to provide a valid Apple / Google Developer account in a timely manner.
- The Client explicitly requests to postpone launch.
- Platform rejection not caused by defects in the App code (administrative rejection, queue delays, etc.).

Under the above circumstances, a buffer period of 14 working days starting from the date the Developer delivers the complete TestFlight (or equivalent testing environment) and submits it for review to both platforms shall be granted. During the buffer period, if the App is rejected by the platform due to App code defects or technical non-compliance with the specifications of Appendix A, the Developer shall correct it free of charge and resubmit it, and the buffer period shall not be recalculated.

Track C acceptance shall be established upon the earliest occurrence of any of the following circumstances, which shall serve as the starting date for the payment instruction of the third installment (final payment):
- The App completes official launch on both iOS and Android platforms;
- Both parties hold an online acceptance meeting, complete real-device functional testing for the Track C items in this section, and confirm approval. The payment instruction shall be issued on the day of the meeting or within the next working day;
- From the day following the expiration of the buffer period mentioned in the preceding paragraph, the acceptance period calculated in accordance with Section 3.2 of the Main Agreement expires, and the Client does not raise written objections, which shall be deemed as passing acceptance.

**Code Defect Warranty:**
After the Client pays the final installment, if the App's subsequent official launch process is functionally rejected (Functional Rejection) by the platforms due to defects in the original source code delivered this time, the Developer is obligated to fix the code free of charge until review approval within 60 calendar days after the final payment is made. Bugs or crashes affecting the normal operation of the core functions set out in this Appendix shall be fixed before each track passes acceptance; such issues discovered after formal delivery acceptance is completed shall be handled under the maintenance services of Section D-5.6 of Appendix D (if Appendix D is not in effect or there is no corresponding SOW, they shall be quoted separately under Section 1.3 of the Main Agreement).

**Major Platform Policy Changes:**
If a functional rejection occurs due to a sudden and major change in platform policies, the Developer will assist free of charge if the modification takes 12 hours or less; for the portion exceeding 12 hours, or for changes occurring after formal delivery acceptance is completed, both parties shall negotiate compensation separately.

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
| C-09 | Docs Handover | Complete technical documentation including: Deployment Guide (comprising local environment build, AWS deployment steps, environment variables and third-party service settings, and packaging/publishing instructions), System Architecture Documentation (comprising database Schema, API documentation, and technical architecture description for each module), and System Handover Documentation, matching the specifications of Section A-3-9 of Appendix A |
| C-10 | AWS Environment Handover | AWS Lightsail Production environment access and ownership transferred to the Client within 3 working days after the settlement of the third installment in accordance with Section 5.5 of the Main Agreement, with a README explaining the deployment process; the GitHub Repository is created under the Client's account from the beginning, and the survival of the Developer's Admin permissions shall be handled in accordance with Section 5.4.1 of the Main Agreement |
| C-11 | Privacy Policy & Terms of Service Embedding | Privacy Policy and Terms of Service have been fully embedded and deployed in the corresponding sections of the Landing Page and the App according to the version confirmed in writing by both parties; links open normally, and the content matches the version confirmed by both parties. |

> ⚠️ **App Store and Google Play review times are outside Developer's control.** Delays non-attributable to code issues will not count as Developer failure. Functional rejections will be fixed until approved.

**Track C Acceptance Result**

| Field | Value |
|---|---|
| Acceptance Date | |
| Client Signature | |
| Notes | |

-----

## C-6 Overall Acceptance Summary

| Item | Number of Acceptance Criteria |
|---|---|
| Preliminary (Landing Page) | 1 |
| Track A | 11 |
| Track B | 23 |
| Track C | 11 |
| **Total** | **46** |

**Final Delivery Confirmation**

| Field | Value |
|---|---|
| Delivery Date | |
| Client Signature | |
| Developer Signature | |

-----

*Appendix C has the same legal effect as the Main Agreement (MTS-2026-001). The signing of the Main Agreement by both parties is deemed as confirmation of the contents of this Appendix.*
