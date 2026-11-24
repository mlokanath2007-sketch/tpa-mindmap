E = {}
def X(sid, why, steps, end, other, rows):
    E[sid] = dict(why=why, flow=dict(steps=steps, end=end), conf=dict(other=other, rows=rows))

X('3', "Every later section uses these words. Fixing their meaning once avoids fights over whether a tree is land, whether a deed was witnessed, or whether a buyer 'knew'. Notice in particular decides who is protected as an honest buyer.",
 [("Is the thing land, a benefit from land, or attached to the earth?",">","Movable property"),("Is it standing timber, a growing crop or grass?","Movable property",">")],
 "Immovable property: transfer usually needs a registered deed",
 "s.6(e) mere right to sue",
 [("What it is","Actionable claim: right to an unsecured debt or goods not in possession","Mere right to sue: bare right to bring a case, e.g. for damages"),("Transferable?","Yes, by signed writing (s.130)","No (s.6(e))"),("Example","Ramesh owes ₹2 lakh, no security","Claim for damages after a car accident")])

X('5', "TPA was written to regulate deliberate dealings between living people. Inheritance and wills already had their own laws, and courts sales their own procedure. So s.5 draws the boundary of what TPA governs.",
 [("Did the owner act himself (not the law or a court)?","Not a transfer: operation of law"),("Was the transferor alive at the time?","Not a transfer: a will"),("Is the transferee a living person or company (or a child in the womb)?","Fails: use s.13 for unborn persons"),("Does the property exist and belong to the transferor?","Not transferable: s.6(a)"),("Is a new right passing (not just separating existing shares)?","Not a transfer: partition or family settlement")],
 "It is a transfer: the rest of TPA applies",
 "Will",
 [("Takes effect","Now or on a fixed future date","Only after death"),("Parties","Living person to living person","Testator to legatees after death"),("Governing law","TPA","Indian Succession Act, 1925")])

X('6', "The law wants property to circulate, so the rule is transferability. The exceptions protect dependants (maintenance, pensions), public office, and prevent trading in hopes and lawsuits.",
 [("Is it a mere hope of inheriting or of a legacy?","Not transferable, s.6(a) (check s.43 if the seller claimed to own it)",">"),("Is it a bare re-entry right, an easement alone, or a personal right?","Not transferable, clauses (b) to (d)",">"),("Is it future maintenance, a mere right to sue, public office, salary or pension?","Not transferable, clauses (dd) to (g)",">"),("Is the object unlawful, against the nature of the interest, or the transferee disqualified?","Barred, clause (h)",">"),("Does another law (e.g. tribal land law) forbid it?","Barred by the opening words",">")],
 "If every answer is no: the property can be transferred",
 "s.21 contingent interest",
 [("Nature","Spes: a mere hope, no right","Contingent: a real right depending on an event"),("Transferable?","No","Yes"),("Example","Son's hope of inheriting father's farm","\"Farm to Meera if she becomes a judge\"")])

X('7', "Only people who understand a deal, and who have the right to deal with the property, should be able to pass it on. This protects minors and persons of unsound mind and stops strangers from selling other people's land.",
 [("Is the transferor a major of sound mind, not disqualified?","Void (minor) or invalid"),("Does he own it, or has he authority to transfer it?","No title passes (nemo dat), unless s.41 or s.43"),("Has he followed the manner the law prescribes (court permission, registration)?","Voidable or invalid as that law says")],
 "Competent transfer",
 "s.41 ostensible owner",
 [("Who transfers","Owner or authorised person","Apparent owner without real authority"),("Basis","Capacity and title","Real owner's consent creates an estoppel"),("Buyer's need","Nothing extra","Value, reasonable care, good faith")])

X('8', "Parties often forget to list every fixture, easement and rent instalment. s.8 fills the gap with what a reasonable person would expect to pass, while letting the parties say otherwise.",
 [("Does the deed express or imply a different intention?","Follow the deed",">"),("Did the transferor own the whole interest at that moment?",">","Only his part passes")],
 "Everything he then had, plus incidents, passes at once; income after the transfer goes to the transferee",
 "s.36 apportionment by time",
 [("Question answered","What passes with the property","How periodic income is split between them"),("Rent","Rent accruing after transfer goes to buyer","Rent accrues day by day and is split"),("Default?","Yes, subject to contrary intention","Yes, subject to contract or usage")])

X('9', "Writing is costly, so the law demands it only where certainty matters most: big immovable transactions, mortgages, long leases, gifts and debts. Everywhere else, people may deal orally.",
 [("Does any law expressly require writing for this transfer (s.54, 59, 107, 118, 123, 130)?","Writing (and registration where required) is compulsory","Oral transfer is valid")],
 "",
 "s.54 sale",
 [("Rule","Oral unless law demands writing","Registered deed if ₹100 or more, or intangible"),("Small value","Oral fine for movables","Under ₹100: deed or delivery"),("Role","General rule","Specific rule for sale")])

X('10', "If owners could forbid sale forever, land would be frozen in one family and the market would stop working. The law lets you choose who gets property, not control it forever after.",
 [("Does the condition restrain parting with the property (not just how it is used)?",">","Not s.10: see s.11"),("Is the restraint absolute in substance (no real freedom left)?",">","Partial restraint: valid"),("Is it a lessor's condition in a lease, or the proviso for a married woman who is not Hindu, Muslim or Buddhist?","Valid under the exception",">")],
 "Condition void; the transfer stands free of it",
 "s.11 repugnant direction",
 [("Restrains","Disposal (selling, gifting)","Enjoyment (how it is used)"),("Applies when","Any transfer with an absolute restraint","Interest given absolutely"),("Exception","Lease; married woman proviso","Direction protecting other land")])

X('11', "Full ownership means freedom to use as you like. A giver who wants to control use should give a limited interest, not absolute ownership.",
 [("Was the interest created absolutely?",">","s.11 does not apply; direction may be valid"),("Does the direction protect another piece of the transferor's land?","Direction enforceable by the transferor",">")],
 "Direction ignored: the transferee uses the property freely",
 "s.40 restrictive covenant",
 [("Who enforces","The transferor","A third person"),("Against whom","The transferee","Later transferees with notice or gratuitous"),("Purpose","Protect transferor's other land","Protect the third person's land or contract")])

X('12', "A clause that makes property vanish on insolvency would let debtors hide assets from creditors, and a clause ending the gift on sale is a disguised ban on selling.",
 [("Does the condition end the interest on insolvency or an attempt to transfer?",">","Not s.12 (check s.31, s.32)"),("Is it a condition in a lease for the lessor's benefit?","Valid lease forfeiture",">")],
 "Condition void; the interest continues",
 "s.31 ending condition",
 [("Event","Insolvency or attempted transfer","Any lawful uncertain event"),("Result","Condition void","Interest ceases on the event"),("Relation","Limits s.31","Subject to s.12")])

X('13', "Allowing gifts to the unborn lets families provide for future children, but stacking life interests on unborn generations would lock land up forever. So the unborn person must take the whole.",
 [("Is the beneficiary unborn and not even in the womb at the date of transfer?","Not s.13: an existing person can take directly"),("Is there a prior interest to a living person in the same deed?","Fails"),("Does the unborn person get the whole remaining interest?","Fails"),("Will he be born before the prior interest ends?","Cannot take")],
 "Valid; it vests on his birth (s.20), subject to s.14",
 "s.14 perpetuity",
 [("Controls","What the unborn gets (the whole)","When it must vest (by 18)"),("Failure","Life interest to unborn","Vesting beyond lives + minority"),("Exception","None","s.18 public benefit")])

X('14', "Tying property up for generations takes it out of circulation and lets the dead control the living. The rule sets a fair outer limit: people now alive plus a child's minority.",
 [("Is the transfer for public benefit (s.18)?","s.14 does not apply",">"),("Must the interest vest within the lives in being plus 18 years of a person then existing?",">","Void for perpetuity")],
 "Valid",
 "s.17 accumulation",
 [("Limits","Vesting of an interest","Saving up income"),("Period","Lives in being + minority","Transferor's life or 18 years"),("Excess","Whole interest void","Only the excess period void")])

X('15', "Before 1929 one bad member spoiled the whole class gift, punishing members who were perfectly valid. The amended rule saves the good members.",
 [("Is the gift to a class?","Not s.15"),("Does it fail under s.13 or s.14 for some members?","All members take")],
 "It fails only for those members",
 "s.16 dependent gift",
 [("What fails","Some members of a class","A later gift depending on a failed one"),("Others","Remaining members take","Later gift also fails"),("Trigger","s.13 or s.14 for some","s.13 or s.14 for the prior gift")])

X('16', "A later gift built on a void earlier gift would let the giver achieve indirectly what s.13 and s.14 forbid directly.",
 [("Did a prior interest fail under s.13 or s.14?","Not s.16"),("Was the later interest in the same transaction, meant to take effect after or on failure of it?","Later gift unaffected by s.16")],
 "The later gift also fails",
 "s.30 invalid ulterior disposition",
 [("Which gift is bad","The earlier one","The later one"),("Effect on the other","Later one also fails","Earlier one stands"),("Direction","Falls forward","Protects backward")])

X('17', "Ordering income to pile up for decades is another way to keep property locked away. The law allows saving for a reasonable time and for genuine needs.",
 [("Is it for public benefit (s.18)?","No time limit",">"),("Is it to pay debts, provide portions for children, or maintain the property?","No time limit",">"),("Does it exceed the longer of the transferor's life or 18 years?",">","Valid in full")],
 "Void for the excess period",
 "s.14 perpetuity",
 [("Concerns","Income","The interest itself"),("Limit","Life or 18 years","Lives in being + minority"),("Exceptions","Debts, children, maintenance, public","Public benefit only")])

X('18', "Perpetuity rules stop private families hoarding property. A school, hospital or temple serves everyone, so permanence is a benefit, not a harm.",
 [("Is the transfer for the public, in religion, knowledge, commerce, health, safety or a similar object?","Ordinary rules of s.14, 16, 17 apply")],
 "Exempt from s.14, 16 and 17 (but s.13 still applies)",
 "s.14 perpetuity",
 [("Who benefits","The public","Private persons"),("Time limit","None","Lives in being + minority"),("s.13","Still applies","Works with s.13")])

X('20', "Once the unborn child arrives, his right should be secure, so it vests at birth and passes to his heirs even if he dies young.",
 [("Was an interest created for a person not then living?",">","Not s.20"),("Does the deed show a contrary intention?","As the deed says (often contingent)",">")],
 "Vested at birth",
 "s.21 contingent interest",
 [("When fixed","At birth","When the uncertain event happens"),("Death before enjoyment","Passes to heirs","Fails"),("Default","Yes, unless deed says otherwise","Only if deed makes it depend on an event")])
