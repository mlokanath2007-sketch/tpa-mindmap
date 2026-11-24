S = {}

S['35'] = dict(tag='syllabus',
simple="<span class='hl'>Election</span>: if a deed gives away <span class='hl'>your property</span> (which the transferor had no right to give) and in the same deed gives <span class='hl'>you a benefit</span>, you must choose: accept the whole deed (keep the benefit, lose your property) or reject it (keep your property, give up the benefit). You cannot take the benefit and refuse the burden.",
deep="""<ol>
<li><b>When election arises:</b> (i) A professes to transfer property he has no right to transfer (it belongs to C), and (ii) as part of the same transaction confers a benefit on C, the owner.</li>
<li><b>C must elect:</b> confirm the transfer (keep the benefit; the transferee gets C's property) or dissent (keep his property; give up the benefit).</li>
<li><b>Where the relinquished benefit goes:</b> back to the transferor or his representative, as if never given.</li>
<li><b>Compensation to the disappointed transferee:</b> out of the relinquished benefit, the transferee must be paid the value of the property he was promised, (a) where the transfer was gratuitous and the transferor has died or become incapable of making a fresh transfer before the election, and (b) in all cases where the transfer was for consideration.</li>
<li><b>Belief irrelevant:</b> it applies whether or not the transferor believed the property was his.</li>
<li><b>Indirect benefit:</b> a person who takes no direct benefit, only an indirect one, need not elect.</li>
<li><b>Two capacities:</b> a person who takes a benefit in one capacity may dissent in another (for example as a trustee).</li>
<li><b>Exception, benefit \"in lieu\":</b> if a particular benefit is expressly given in lieu of the property, the owner who claims his property gives up only that benefit, not other benefits under the same transaction.</li>
<li><b>Deemed election to confirm:</b> acceptance of the benefit with knowledge of the duty to elect and of the relevant circumstances (or waiver of enquiry); knowledge or waiver is presumed after enjoying the benefit for <b>two years</b> without dissent; or inferred from an act that makes restoration impossible (the coal-mine illustration).</li>
<li><b>One year rule:</b> if he does not signify his choice within one year of the transfer, the transferor or his representative may require him to elect; if he still does not within a reasonable time, he is deemed to have confirmed.</li>
<li><b>Disability:</b> election is postponed until the disability ends or a competent authority elects.</li></ol>
<p><b>Memory word for deemed acceptance:</b> U-E-D-I: Uses the benefit knowingly · Enjoys it 2 years · Destroys it · Ignores a request to elect after 1 year.</p>""",
dissect=[
("professes to transfer property which he has no right to transfer","Condition 1: property of another."),
("as part of the same transaction confers any benefit on the owner of the property","Condition 2: benefit to the owner in the same transaction."),
("such owner must elect either to confirm such transfer or to dissent from it","The choice."),
("he shall relinquish the benefit so conferred","Dissent means giving up the benefit."),
("shall revert to the transferor or his representative","Benefit goes back."),
("to the charge of making good to the disappointed transferee the amount or value of the property","Compensation to the disappointed transferee."),
("whether the transferor does or does not believe","Belief is irrelevant."),
("deriving a benefit under it indirectly, need not elect","Indirect benefit: no election."),
("in his one capacity takes a benefit under the transaction may in another dissent","Different capacities."),
("such benefit is expressed to be in lieu of that property","Exception: benefit in lieu."),
("has enjoyed it for two years without doing any act to express dissent","Two-year presumption."),
("renders it impossible to place the persons interested","Irreversible act."),
("within one year after the date of the transfer","One-year rule."),
("In case of disability, the election shall be postponed","Disability."),
],
master=dict(story="In one gift deed, Raghunath (A) gives Meera's flat worth ₹40 lakh to Kabir (Raghunath wrongly believes the flat is his), and gives Meera ₹50 lakh. Meera is also trustee of a temple trust which receives a garden under the same deed. Arjun, Meera's husband, benefits only because Meera's income rises. Case 1: Meera spends ₹10 lakh of the gift on her daughter's education knowing she must choose. Case 2: alternatively, she keeps silent; after one year Raghunath asks her to elect and she ignores it. Case 3: alternatively, Raghunath dies, and Meera then keeps her flat.",
steps=[("Is election required?","Yes: Raghunath professed to transfer Meera's flat and, in the same transaction, conferred benefits on Meera. His belief that it was his is irrelevant."),("Must Arjun elect?","No: his benefit is only indirect."),("Meera as trustee?","She may take her personal benefit and still dissent as trustee for the temple's garden, or vice versa (different capacities)."),("Case 1?","Deemed confirmation: she took the benefit knowing her duty. Kabir gets the flat."),("Case 2?","Deemed confirmation after the one-year rule and her failure to respond within a reasonable time."),("Case 3, she keeps the flat?","She must give up the ₹50 lakh, which reverts to Raghunath's representative. As the gift was gratuitous and Raghunath died before election, ₹40 lakh of it must be paid to the disappointed Kabir.")]),
ills=[
("Basic election","A gives C's farm (₹800) to B and ₹1,000 to C in one deed; C keeps the farm.","m","C forfeits ₹1,000","Act's illustration."),
("Transferor dead","Same, but A dies before C elects.","m","₹800 of the ₹1,000 goes to B","Gratuitous transfer, transferor dead before election."),
("For consideration","A sells C's land to B for ₹10 lakh and gives C ₹15 lakh in the same deed; C keeps his land.","m","B is compensated out of the ₹15 lakh","In all cases where the transfer is for consideration."),
("Indirect benefit","The owner's spouse benefits only indirectly.","y","No election needed","Indirect benefit."),
("Coal mine","A gives B an estate belonging to C, and gives C a coal-mine; C exhausts the mine.","y","C has confirmed","Act's illustration: irreversible act."),
("Two years","C uses the benefit for two years without objection.","y","Presumed confirmation","Two-year presumption."),
("One year then demand","C stays silent a year; A demands an election; C ignores it.","y","Deemed confirmation","One-year rule."),
("Disability","C is a minor.","m","Election postponed","Until majority or a competent authority elects."),
("Benefit in lieu","A gives C's house to B; in the same deed gives C a car \"in lieu of the house\" and also ₹5 lakh as a birthday gift. C keeps his house.","m","C loses only the car, keeps the ₹5 lakh","Exception: only the benefit expressed to be in lieu is relinquished."),
],
exam=dict(q="Explain the doctrine of election. When is a person deemed to have elected? (10 marks)",
pts=["Two conditions: property of another, and benefit to the owner in the same transaction","Confirm or dissent; benefit reverts","Compensation to the disappointed transferee","Belief irrelevant; indirect benefit; two capacities; benefit in lieu","Deemed election: knowledge, two years, irreversible act, one-year rule; disability"],
line="Under s.35, where a person professes to transfer property he has no right to transfer and in the same transaction confers a benefit on its owner, the owner must elect to confirm the transfer or to dissent and relinquish the benefit."),
quiz=[("C keeps his farm and rejects the deed. What happens to his gift?",["He keeps it","He relinquishes it","It goes to B"],1,"Dissent means giving up the benefit."),("A benefit enjoyed for two years without dissent:",["Proves nothing","Raises a presumption of confirmation","Makes the deed void"],1,"Two-year rule.")],
links=[("Indian Succession Act s.180 to s.190","Election under wills."),("s.6","General transferability.")],
next="Section 36 shifts to apportionment of periodic payments.")

S['36'] = dict(tag='beyond',
simple="When an interest is transferred, <span class='hl'>rent, pensions, dividends and other periodic income</span> are treated, between transferor and transferee, as <span class='hl'>earning day by day</span>, and split accordingly, though still payable on the usual due date.",
deep="<p>Unless a contract or local usage says otherwise, periodic payments in the nature of income accrue from day to day between transferor and transferee. They are still payable on the appointed day, but the amount is divided by the number of days each held the interest.</p>",
dissect=[("In the absence of a contract or local usage to the contrary","Default rule."),("to accrue due from day to day, and to be apportionable accordingly","Day-by-day split."),("but to be payable on the days appointed for the payment thereof","Due date unchanged.")],
master=dict(story="Raghunath sells a shop to Kabir on 20 March. The tenant pays ₹31,000 monthly rent on 31 March for March.",steps=[("Who gets what?","As between them, Raghunath gets 19 days' share (₹19,000) and Kabir 12 days' (₹12,000); the tenant still pays on 31 March.")]),
ills=[("Day-by-day","Sale mid-month; monthly rent paid at month end.","m","Split by days","s.36."),("Contract to contrary","Deed says buyer takes the whole month's rent.","y","Contract prevails","Default rule only.")],
exam=dict(q="Short note on apportionment by time (s.36).",pts=["Periodic income accrues day to day","Payable on due date","Subject to contract or usage"],line="Under s.36, periodical payments in the nature of income are deemed to accrue from day to day between transferor and transferee, subject to contract or local usage."),
quiz=[("Rent on transfer mid-month is:",["All to buyer","All to seller","Split day by day"],2,"s.36.")],
links=[("s.8","Rents accruing after transfer go to the transferee.")],
next="Section 37 deals with obligations when property is divided.")

S['37'] = dict(tag='beyond',
simple="When property is <span class='hl'>divided among several owners</span> after a transfer, a duty owed to the property (like rent) is performed <span class='hl'>to each owner in proportion to his share</span>, if it can be split without extra burden; otherwise to the one owner they jointly nominate.",
deep="""<ol><li>Benefit of an obligation relating to the whole property passes to several owners.</li>
<li>The duty is performed to each in proportion to the value of his share, if severable without substantially increasing the burden.</li>
<li>If not severable, or severance would increase the burden, performance goes to the owner they jointly designate.</li>
<li>The person bound is not liable until he has reasonable notice of the severance.</li>
<li>Does not apply to agricultural leases unless the State Government so directs.</li></ol>
<p><b>Act's illustrations:</b> (a) house sold to B (half the price), C and D (a quarter each); tenant E pays ₹30 yearly rent and one fat sheep; E pays ₹15 to B, ₹7½ each to C and D, and delivers the sheep as they jointly direct. (b) E's duty of ten days' dyke work is not multiplied by the split.</p>""",
dissect=[("in proportion to the value of his share in the property","Proportionate performance."),("provided that the duty can be severed and that the severance does not substantially increase the burden","Severability limit."),("as they shall jointly designate for that purpose","Non-severable duty."),("unless and until he has had reasonable notice of the severance","Protection for the person bound.")],
master=dict(story="Raghunath sells his leased house to Arjun (half), Meera and Kabir (a quarter each). Tenant Ramesh pays ₹36,000 a year and delivers one goat every Diwali.",steps=[("Rent?","₹18,000 to Arjun, ₹9,000 each to Meera and Kabir, after Ramesh gets notice."),("Goat?","Cannot be split: delivered as the three jointly direct.")]),
ills=[("Severable","Cash rent split by shares.","m","Proportionate","s.37."),("Non-severable","One animal or one fixed labour duty.","m","To the jointly named owner","s.37.")],
exam=dict(q="Short note on s.37.",pts=["Proportionate performance","Severability limit","Joint designation","Notice"],line="Under s.37, when property is divided, an obligation relating to it is performed to each owner in proportion to his share if severable without extra burden, otherwise to the owner jointly designated."),
quiz=[("A single goat owed as rent to three new owners is delivered:",["To each","As they jointly direct","To the eldest"],1,"Non-severable.")],
links=[("s.36","Apportionment by time.")],
next="Part B begins: Section 38 protects buyers from persons with conditional authority.")
