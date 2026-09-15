# Step 1: the "who pays whom" question

A market map is only worth building if every row can be sorted by one question: does this entity already pay a separate party for the thing your client sells? That question splits the market into proven buyers of the deal shape (the table) and everyone else (counted, not listed). Web research answers "who is well known"; public records answer "who pays whom". Write the question before touching a source, because it decides which records you pull.

## Write the question in four moves

1. Name what the client sells and who signs for it (the payer). For a restaurant operator, the payer is the hotel's owner or its asset manager, never the hotel's brand or its management company.
2. Name the party the client would replace, join or become (the payee). For a restaurant operator, that is whoever runs the restaurant today: an outside operator, or the hotel itself.
3. Phrase it so a public record can answer it. "Does a party other than the owner or its manager hold the licence for the restaurant inside this hotel?" is answerable from a licence file. "Is the restaurant good?" is not.
4. Decide what YES and NO mean for the map. YES: the owner has already bought this deal shape once; that is the table. NO: in-house today; a different and harder conversation; it stays in the count (it proves you looked at the whole market) and off the table.

## Worked examples (all fictional)

| Niche the client sells into | Payer | Payee today | Split question | Record that answers it |
| --- | --- | --- | --- | --- |
| Restaurant operator for hotels | Hotel owner | Outside operator, or the hotel itself | Is the restaurant's licence held by a party other than the hotel entity, and does that party employ the staff? | State liquor and food-service licence files by address; the hotel's own dining page |
| Practice acquirer (dental, veterinary, physio) | The selling owner | The owner-clinician, or a group that already holds it | Is the practice's licence and entity held by an individual clinician, or by a group entity that owns several? | State professional and facility licence files; corporate registry; clustering by owner mailing address |
| Association management for HOAs and clubs | The board | An outside management company, or self-managed | Does the association's registered agent or filing contact belong to a management company? | Corporate registry (registered agent); county association registrations where they exist |
| Facility services (landscaping, security, cleaning) for commercial property | Property owner or asset manager | An incumbent contractor, or in-house staff | Does a service permit, contractor licence or procurement award at the address name an outside contractor? | City business licences; procurement portals for public owners; contractor licence files |
| Outsourced billing for clinics | The clinic owner | A billing company, or an in-house team | Does a public payer enrolment or vendor register list a billing agent for this provider? | Payer enrolment files; vendor registers; corporate registry |

The pattern holds across niches: the payee's footprint shows up in a licence, a permit, a registration or a filing tied to the payer's address or entity. That is what Step 2 pulls in bulk.

## The false positive to design against: the name on the door

An outside name on the unit does not mean an outside operator. Hotels put a celebrated chef's name on a room they staff themselves. Clinics say "powered by" a software vendor. Buildings carry a brand under a franchise while a local franchisee runs it. In every case ask who employs the people doing the work and who holds the licence. The employer of record decides:

- Chef-partner or consulting deal: the hotel employs the team, the chef licenses a name. Not a separate operator. The map calls this Licensed.
- Lease, franchise held by a third party, or management agreement: the outside party employs the team and usually holds its own licence. That is a separate operator. The map calls this Ready.
- Franchisor versus franchisee: the franchisor licenses the brand; the franchisee operates. The counterparty in the row is the franchisee, named as such.

## The second false positive: adjacent, not inside

A tenant that shares the building's street number can sit in the office podium, the retail strip or a neighbouring parcel. Same address is a candidate, not proof. Step 4 checks that the unit is inside the entity's own premises.

## What to write down before Step 2

Put this block at the top of `journal.md`:

- Niche and geography, as the user gave them.
- Payer and payee, one line each.
- The split question, in one sentence a public record can answer.
- The four tests from `verification-bar.md`, instantiated for this niche (what "separate party", "employer of record", "inside" and "live today" mean here).
- The inclusion rule for the count (for example "full-service hotels with an on-premises licence", or "practices with an active facility licence and two or more providers").
- The region granularity for the chips (state, county, metro).
