# SOFTWARE DEVELOPMENT SERVICES AGREEMENT

Agreement No.: MTS-2026-001
Date: June 11, 2026

-----

## PARTIES

**Client (hereinafter referred to as the "Client")**

Company Name: Motise Inc
Company Type: C Corporation (Registered in Delaware, USA)
Registered Address: 8 The Green STE R, Dover, Kent, Delaware 19901, USA
Signatory: Chiang Ching-Hsuan (Founder / Director)
Company Email: <hello@motise.net>
Authorized Project Communication Representative: Chiang Ching-Hsuan (<cchiang1124@gmail.com>)

> The Client designates Chiang Ching-Hsuan as the authorized communication representative for this project, representing the Client in daily project communications, requirement confirmations, and submitting written objections. Written confirmations from the aforementioned representative shall have equal binding force on the Client. Any change of representative must be notified to the Developer in writing by the Client via the company email (@motise.net).

**Developer (hereinafter referred to as the "Developer")**

Name: HUANG CONG REN
Nationality: Republic of China (Taiwan)
Contact Email: <tzuchihuang0214@gmail.com>

Both parties agree to cooperate on the software development services specified in this Agreement subject to the terms and conditions herein.

-----

## AGREEMENT APPENDICES

This Agreement includes the following appendices, each of which has the same legal effect as the main text of this Agreement:

| Appendix | Name | Description |
|---|---|---|
| Appendix A | Project Scope and Technical Specification | List of functional modules, technical architecture, exclusions from v1.0, and resources to be provided by the Client |
| Appendix B | Development Schedule | Key milestones, Gantt chart, prerequisites, and explanation of delay clauses |
| Appendix C | Acceptance Criteria | Three-track acceptance standards, acceptance checklist, and sign-off sections |
| Appendix D | Long-Term Cooperation Framework Agreement | Project-based renewal, four-cycle outsourcing obligation, and difference make-up mechanism |

-----

## ARTICLE 1 | PROJECT SCOPE

1.1 The Developer agrees to develop version 1.0 of the course booking mobile application (hereinafter referred to as the "System") for the Client, according to the scope specified in Appendix A "Project Scope and Technical Specification."

1.2 The primary modules, detailed functions, and technical specifications included in version 1.0 shall be subject to the provisions in Appendix A.

1.3 Items listed in Section A-4 of Appendix A are explicitly excluded from the development scope of v1.0. Any changes to the scope must be confirmed in writing by both parties before taking effect and will require a separate evaluation of their impact on the schedule and fees.

1.4 **Responsibility for Providing Legal Text:** The Developer agrees to provide a basic English template (Basic Template) of the Privacy Policy and Terms of Service that complies with general US regulatory compliance frameworks (such as GDPR, CCPA basic frameworks) before the end of Track A for the Client's confirmation. The Client shall confirm or provide modifications within 3 working days; failure to reply within the time limit will be deemed as confirmation of the template content, and the Developer may directly use the original template for embedding and deployment. After confirmation by the Client, the Developer is responsible for completely embedding, deploying, and linking it in the corresponding sections of the Landing Page and the App.

1.5 **Legal Compliance Disclaimer:** The Privacy Policy and Terms of Service provided in the preceding section are basic reference templates for technical integration purposes. The Client is solely responsible for confirming their final legal compliance, applicability, and completeness, and should consult qualified legal professionals if necessary. The Developer shall not bear any legal compliance responsibility arising from the content of these texts. The Client's confirmation of the content is deemed as having conducted its own review and assuming compliance responsibility.

-----

## ARTICLE 2 | SCHEDULE AND MILESTONES

2.1 The development schedule of the System shall be executed according to Appendix B "Development Schedule," which is expected to commence on **June 12, 2026**, with a target delivery date of **August 07, 2026**.

2.2 All timelines in Appendix B are contingent upon the Client providing all necessary resources listed in Section A-6 of Appendix A by **June 12, 2026**. For every week of delay in providing the resources, the milestones and delivery dates shall be proportionally postponed.

2.3 The following circumstances shall not be counted towards the Developer's delay liability:
- App Store / Google Play review periods and waiting times for platform rejections
- Delays caused by the Client's failure to provide necessary resources, accounts, or access permissions on time
- Delays in payment functions caused by the failure to complete Stripe KYC verification on time
- Delays in submission dates caused by Apple Developer Organization Account D-U-N-S Number issuance delays
- Force majeure events (natural disasters, sudden changes in platform policies, etc.)

2.4 **Stripe Account Prerequisite:** The Client must initiate the Stripe account KYC application **within 3 working days after the signing of this Agreement and receipt of the first installment payment**. KYC must be completed by the Client personally (due to legal requirements, the Developer cannot act on their behalf). If not initiated before the deadline, the development of Stripe-related functions will be postponed, which will not be considered a delay by the Developer, nor will it trigger the delay compensation clause in Article 6.

-----

## ARTICLE 3 | ACCEPTANCE MECHANISM

3.1 The acceptance of the System will be conducted in three tracks according to Appendix C "Acceptance Criteria," and the acceptance standards for each track shall be subject to the provisions in Appendix C.

3.2 If the Client fails to submit written acceptance results within the acceptance period for each track, all items in that track shall be deemed accepted upon the expiration of the deadline.

3.3 If the Client does not raise written objections within 24 hours after the weekly sync meeting, it shall be deemed a confirmation of the progress at that stage, and objections cannot be raised again during subsequent acceptances.

3.4 Once a track is accepted, the items in that track are locked and cannot be objected to again during subsequent tracks or at the time of formal delivery.

3.5 New requirements raised during the acceptance period will not be included in the current acceptance scope and will enter the development of the next version after a separate quotation assessment.

3.6 **Invalidity of Subjective Rejection:** Any rejection or non-acceptance feedback raised by the Client must be accompanied by a clear explanation of functional issues or specific evidence of non-conformity with the mutually confirmed design specifications. Rejections based on subjective descriptions (such as "it feels wrong" or "the experience is not smooth") shall be deemed invalid, and the items will still be considered accepted.

3.7 **Re-inspection Limits and Timeframes:** Regarding the list of written modification requests submitted by the Client during the acceptance period, after the Developer completes the modifications, the Client may only perform a re-inspection on the results of the modifications for the items originally listed. The Client may not raise new modification requests outside the original list or repeatedly find fault during the re-inspection. The re-inspection period is limited to 3 working days; failure to submit re-inspection results within the timeframe will result in all items being deemed accepted.

3.7.1 **Regression Bug:** If the code changes made by the Developer to correct items in the current acceptance list directly cause new functional errors in other items within the same acceptance list or in existing functions of items that have previously passed acceptance (subject to the standards of Section 3.6, with a clear explanation of the functional issue), the Client may raise them during the re-inspection period together, free from the restriction of Section 3.7 "no new suggestions outside the original list" and without constituting a violation of Track Locking under Section 3.4. The Developer shall correct them together; for the additional correction time required, the re-inspection period for that specific item may be extended by 3 working days, and the re-inspection period for other items shall not be affected. The re-inspection of regression bugs is strictly limited to confirming that the defect has been corrected, and no other new suggestions may be derived and proposed.

3.8 **Weekly Sync Meeting:** Both parties shall, in principle, hold an online sync meeting every Friday from 24:00 to 01:00 of the following day (Saturday) (Taiwan Time, UTC+8; corresponding to Friday 09:00–10:00 AM US Pacific Time) to synchronize project progress. If either party cannot attend the meeting at the specified time, they shall notify the other party in advance and coordinate a rescheduled time, but a sync meeting must still be completed within that week.

-----

## ARTICLE 4 | FEES AND PAYMENT

4.1 The fees for this Agreement are calculated based on the cooperation scenario confirmed by both parties and shall be paid in three installments:

**Scenario 1: Full Acceptance + Confirmation of Long-Term Cooperation (Total Fee $1,800 USD) (Long-Term Cooperation Service Period: 12 months, from August 07, 2026 to August 07, 2027)**

| Installment | Timing | Amount |
|---|---|---|
| First Installment (30%) | Upon signing | $540 USD |
| Second Installment (30%) | Within 3 working days after full acceptance of Track B | $540 USD |
| Third Installment (40%) | Within 3 working days after full acceptance of Track C and formal delivery | $720 USD |

**Scenario 2: Full Acceptance + Clear Decision Not to Continue Cooperation (Total Fee $2,499 USD)**

| Installment | Timing | Amount |
|---|---|---|
| First Installment (30%) | Upon signing | $540 USD |
| Second Installment (30%) | Within 3 working days after full acceptance of Track B | $540 USD |
| Third Installment | Within 3 working days after full acceptance of Track C and formal delivery | Make up the difference to $2,499 ($1,419 USD) |

**Scenario 3: Delayed Development Schedule and Failure to Pass Full Acceptance**

The fee is calculated based on $2,499 USD, with deductions made according to the delay compensation clause in Article 6.

4.2 **Method of Scenario Determination:** Whether Scenario 1 is established shall be subject to the time when this Agreement is electronically signed by both parties: if Appendix D "Long-Term Cooperation Framework Agreement" has been signed in writing by both parties at that time, Scenario 1 shall be deemed established, and the third installment payment shall be calculated based on the Scenario 1 amount ($720 USD). If Appendix D has not been signed in writing by both parties when this Agreement is electronically signed, it will automatically be calculated as Scenario 2, and the third installment payment shall make up the difference to $2,499 USD, and Appendix D shall be deemed invalid.

4.3 **Definition of Long-Term Cooperation:** "Confirmation of long-term cooperation" refers to the project-based renewal method agreed upon by both parties under Appendix D "Long-Term Cooperation Framework Agreement," where the written signing of Appendix D is completed before the deadline for scenario confirmation. The specific scope, compensation, and terms of long-term cooperation shall be subject to Appendix D and subsequent individual Statements of Work (SOW).

4.4 **Tax Clause:** All amounts are net of taxes (USD). The Developer will provide a W-8BEN form. Upon receipt, the Client shall not deduct US Withholding Tax from the payments under this Agreement.

4.5 **Remittance Clause:** Payments shall be made in US Dollars (USD) to the Wise account designated by the Developer. All remittance fees shall be borne by the Client, and the actual amount received by the Developer shall not be less than the agreed amount for each installment.

4.6 **Publishing Fees:** App Store publishing fees (Apple Developer Program annual fee $99 USD, Google Play one-time fee $25 USD) shall be borne by the Client and are not included in the development fees of this Agreement.

4.7 **Start of Acceptance from Delivery Testing:** For Track C acceptance, the acceptance period begins when the Developer submits the App to TestFlight/Firebase Distribution for delivery testing, or when it passes platform (App Store / Google Play) review. If the App cannot be officially released due to non-developer reasons, such as the Client failing to provide accounts, platform policy changes, or the Client's subjective decision to suspend the launch, it will not affect the progress of Track C acceptance, which will still be calculated as 14 working days from the date of delivery testing or passing the review.

4.7.1 **Platform Review Buffer:** If the App cannot be officially published on the App Store or Google Play due to reasons not attributable to the Developer (limited to: Client failing to provide a valid Apple / Google Developer account in a timely manner, Client explicitly requesting to postpone launch, or platform rejection not caused by defects in the App code), a buffer period of 14 working days for review and platform communication will be given starting from the date the Developer delivers the complete TestFlight (or equivalent testing environment) and submits it for review to both platforms. During the buffer period, if the App is rejected by the platform due to App code defects or technical non-compliance with the specifications of Appendix A, the Developer shall correct it free of charge and resubmit it, and the buffer period shall not be recalculated.

4.7.2 **Criteria for Passing Acceptance and Triggering Payment:** Track C acceptance shall be established upon the earliest occurrence of any of the following circumstances, which shall serve as the starting date for the 3-working-day payment instruction for the third installment:
- The App completes official launch on both iOS and Android platforms;
- Both parties hold an online acceptance meeting, complete real-device functional testing for the Track C items in Appendix C, and confirm approval. The payment instruction shall be issued on the day of the meeting or within the next working day;
- From the day following the expiration of the buffer period mentioned in the preceding section, the acceptance period calculated in accordance with Section 3.2 expires, and the Client does not raise written objections, which shall be deemed as passing acceptance.

4.7.3 **Code Defect Warranty:** If the Client has paid the final installment, and the App's subsequent official launch process is functionally rejected (Functional Rejection) by the platforms due to defects in the "original source code" delivered this time, the Developer is still obligated to fix the code free of charge until review approval. This warranty obligation is valid within 60 calendar days after the final payment is made.

4.7.4 **Platform Policy Changes:** If a functional rejection occurs due to a sudden and major change in platform policies, and such change affects the code logic of the core functions of this project, the Developer agrees to evaluate the feasibility of modifications and actively cooperate. For modifications taking less than 8 hours, the Developer will assist free of charge; for the portion exceeding 8 hours, both parties shall negotiate reasonable compensation and extended development and acceptance schedules separately.

4.8 **Overdue Payment and Service Suspension:** If the Client fails to pay the full amount for more than 7 calendar days after the payment timing for each installment has arrived, the Developer has the right to suspend all subsequent development, review submission, launch, maintenance, consultation, or ownership transfer services. The Client shall pay a late fee on the unpaid amount at a monthly interest rate of one percent (1%, annual rate of 12%) starting from the date of overdue, with portions of a month calculated proportionally on a daily basis.

4.9 **Withdrawal of Control and Termination:** If the Client's payment is overdue for 14 calendar days, the Developer has the right to unilaterally terminate this Agreement and may revoke the Client's access and Collaborator permissions to the codebase (GitHub Repository) and server (AWS Production) at any time, and the Developer is under no obligation to refund any fees already received. However, for the parts of the intellectual property rights that have already been transferred under Section 5.1 of Article 5 due to the receipt of previous installment payments, their ownership status shall not be affected; the Developer may only suspend access permissions but shall not revoke the transferred intellectual property rights.

-----

## ARTICLE 5 | INTELLECTUAL PROPERTY, CODE HANDOVER AND TERMINATION

5.1 The intellectual property rights of this project shall be transferred in stages according to the development milestones and payment progress, and the transfer conditions for each stage are as follows:
- Upon full receipt of the first installment payment ($540 USD), the intellectual property rights of all deliverables and codes corresponding to Track A shall be automatically transferred to the Client (Motise Inc.).
- Upon full receipt of the second installment payment ($540 USD), the intellectual property rights of all deliverables and codes corresponding to Track B shall be automatically transferred to the Client (Motise Inc.).
- Upon full receipt of the third installment payment, the intellectual property rights of all deliverables and codes corresponding to Track C shall be automatically transferred to the Client (Motise Inc.).

5.2 Prior to the receipt of the payment for each stage, the intellectual property rights of the deliverables and codes corresponding to that track shall remain with the Developer. The Client shall obtain an exclusive, non-transferable license to use such deliverables during that stage solely for internal business operations, but shall not claim ownership, sub-license, or transfer them to a third party.

5.3 **Governing Law Note:** This Agreement is governed by the laws of the Republic of China (Taiwan). The concept of "Work Made for Hire" under US copyright law does not apply to this Agreement. The transfer of intellectual property rights shall automatically take effect by way of assignment upon receipt of each installment payment under Section 5.1 of this Article, in compliance with the Copyright Act of the Republic of China.

5.4 The GitHub Repository shall be established under the Client's account (or an organization designated by the Client), and the Developer shall join as a Collaborator and obtain Admin permissions to facilitate development operations such as branch protection rules, CI/CD workflow settings, and key and permission management for third-party services (e.g., Stripe, Firebase).

5.4.1 Prior to passing the acceptance of this project and settling the final payment, unless through the formal termination procedure under Section 5.9 of this Agreement or other formal termination procedures:
- The Client shall not restrict or remove the Developer's Admin permissions; the Developer shall not use Admin permissions to restrict the Client's access permissions, or perform acts that affect the project progress such as deleting or transferring the Repository.
- If the Client violates the preceding provision, it shall be deemed that the Client terminates this Agreement for convenience under Section 5.9, and the Client shall still pay the Developer the amount calculated according to the termination settlement formula under Section 5.9, which shall be settled within 10 working days from the date of the violation.
- If the Developer violates the preceding provision, it shall be deemed that the Developer terminates this cooperation for convenience under Section 5.9, and the Developer shall have no right to claim corresponding compensation for acceptance items that have not been completed after the termination date. The settlement between both parties shall still be calculated according to the termination settlement formula under Section 5.9.

5.5 The transfer of access and ownership to the AWS Production environment will be handed over to the Client within 3 working days after the settlement of the third installment, and the Developer has an obligation to assist in completing the transfer settings.

5.6 Third-party service accounts (Stripe, Firebase, Apple Developer, Google Play) used during development are inherently registered under the Client's name, and their ownership will not be affected by this Article.

5.7 Technical documentation (including but not limited to deployment guides and system architecture description documents, with detailed specifications subject to Section A-3-9 of Appendix A) shall be submitted concurrently with the acceptance of each track according to the corresponding acceptance items listed in Appendix C (A-11, B-23, C-09) and completely handed over upon formal delivery; its acceptance shall be handled in accordance with the mechanism specified in Article 3 (including Sections 3.4, 3.6, and 3.7).

5.8 **Remedies for Breach:** If the Client commits a material breach by failing to make payments as agreed and fails to cure such breach within seven (7) calendar days after written notice from the Developer, the Developer shall have the right to: (1) suspend development work for the current and subsequent stages; (2) suspend delivery of the latest development progress; and (3) seek damages from the Client in accordance with the law. The exercise of the aforementioned rights shall not affect the validity of the transfer of intellectual property rights corresponding to the payments already received.

5.9 **Termination for Convenience:** Either party may terminate this Agreement at any time, for any reason or no reason, upon 14 calendar days’ prior written notice to the other party. Upon termination, the Client shall pay the "Amount Due on Termination Date," calculated as follows:

```
Amount Due on Termination Date
= Total Fee of Applicable Scenario
  × (Number of Acceptance Items Passed as of Termination Date ÷ Total Number of Acceptance Items in Appendix C)
− Amount Paid
```

Upon receipt of the aforementioned Amount Due on Termination Date, the Developer shall, within 1 working day, deliver the work results completed as of the termination date to the Client by transferring Repository ownership or granting full access rights. If the calculation of the Amount Due on Termination Date results in zero or a negative number, the Developer is not required to refund any fees received and shall complete the delivery within 1 working day after confirmation. During the notice period, the Developer is under no obligation to develop new features. Before the Amount Due on Termination Date is settled, the intellectual property rights of the corresponding code shall not be transferred.

5.9.1 **Client's Accelerated Right of Termination (For Cause Attributable to Developer):** Upon the occurrence of any of the following objective circumstances, the Client may waive the prior notice period under the preceding section and immediately terminate this Agreement by written notice to the Developer, which shall terminate on the date of delivery of such notice; the termination settlement amount shall still be calculated according to the formula under Section 5.9:
- Any acceptance item in Appendix C is not completed more than 7 working days after the completion deadline agreed upon in Appendix B, and the Developer fails to provide a written explanation for the delay; or
- The Developer completely fails to respond to the Client's contact regarding project-related matters (including written communication channels such as Email, instant messaging, etc.) for 5 consecutive working days without a reasonable explanation or force majeure afterward.

5.10 **Originality Warranty:** The Developer warrants that the delivered code is original, does not infringe upon any third-party intellectual property rights, and is free of any liens or encumbrances.

-----

## ARTICLE 6 | DELAY COMPENSATION

6.1 If the completion of features is delayed by more than **14 calendar days** beyond the milestone timeline due to **reasons attributable to the Developer**, the Client may claim compensation according to the following formula:

```
Compensation Amount = Amount Paid × (Number of Uncompleted Acceptance Items ÷ Total Number of Acceptance Items) × 50%
Compensation Cap = 20% of the Amount Paid
```

6.2 Compensation is calculated solely at the time of formal delivery acceptance for Track C and does not accumulate track by track.

6.3 The following circumstances shall not be included in the Developer's delay calculation and will not trigger compensation under this Article:
- App Store / Google Play review waiting periods or platform rejection periods
- Delays caused by the Client's failure to provide necessary resources, accounts, or access permissions on time
- Delays in payment functions caused by the failure to complete Stripe KYC verification on time
- Delays in submission dates caused by Apple Developer Organization Account D-U-N-S Number issuance delays
- Force majeure events

-----

## ARTICLE 7 | CONFIDENTIALITY OBLIGATIONS

7.1 Both parties bear confidentiality obligations regarding the business logic, user data structure, system architecture, financial information, and other project-related confidential information learned during the cooperation period.

7.2 The confidentiality obligation remains fully effective after the termination or expiration of this Agreement, with no time limit.

7.3 The following information is not bound by the confidentiality obligations in this Article:
- Information that was already public before exposure
- Information legally provided by a third party without confidentiality obligations
- Information required to be disclosed by law or orders from competent authorities

-----

## ARTICLE 8 | GENERAL PROVISIONS

8.1 **Governing Law:** This Agreement is governed by the laws of the Republic of China (Taiwan).

8.2 **Dispute Resolution:** Any disputes arising between the parties regarding this Agreement shall primarily be resolved through amicable negotiation. If negotiations fail, both parties agree to submit to the jurisdiction of the courts of Taiwan, Republic of China, as the court of first instance.

8.3 **Document Validity and Order of Precedence:** The main text of this Agreement and Appendix A, Appendix B, Appendix C, and Appendix D jointly constitute the complete basis for cooperation between both parties and have equal legal effect. If there is a conflict between the documents, the provisions in the main text of this Agreement shall prevail.

8.4 **Amendment Clause:** Any amendment to this Agreement must be agreed upon in writing by both parties before taking effect; oral agreements are invalid.

8.5 **Severability:** If any provision of this Agreement is determined to be invalid or unenforceable, it shall not affect the validity of the remaining provisions.

8.6 **Entire Agreement:** This Agreement supersedes all prior oral or written communications and agreements between both parties regarding this project.

-----

## ARTICLE 9 | SIGNATURE

Both parties have read and understood all the terms of this Agreement and the contents of all appendices and agree to be bound by them.

9.1 **Method of Signing:** This Agreement is signed electronically via the Dropbox Sign platform. The signing invitation for the Client is sent to the company email (hello@motise.net) and must be completed by the signatory Chiang Ching-Hsuan personally. An electronic signature received and completed via the company email has the same legal effect as a handwritten signature.

9.2 **Time of Signing Completion:** After both parties have completed the electronic signatures, the timestamps and signing records automatically generated by the Dropbox Sign system shall serve as evidence of the entry into force of this Agreement.

&nbsp;

**Client**

Company Name: Motise Inc

Signatory: Chiang Ching-Hsuan (Founder / Director)

Signing Email: <hello@motise.net>

Electronic Signature Timestamp: 

&nbsp;

**Developer**

Name: HUANG CONG REN

Contact Email: <tzuchihuang0214@gmail.com>

Electronic Signature Timestamp: 

-----

*This Agreement, together with Appendix A, Appendix B, Appendix C, and Appendix D, consists of five documents. Both parties shall each hold one electronic copy, which shall have equal validity.*
