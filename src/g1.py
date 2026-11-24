S = {}

S['3'] = dict(tag='syllabus',
simple="Section 3 is the <span class='hl'>dictionary of the Act</span>. It fixes the meaning of words used everywhere in s.5 to s.55: immovable property, instrument, attested, registered, attached to the earth, actionable claim and notice.",
deep="""<p>Section 3 does not create rights. It tells you how to read the words in every other section. Four groups matter.</p>
<ol>
<li><b>Immovable property (and "attached to the earth").</b> TPA gives only a <i>negative</i> definition: immovable property does <b>not include standing timber, growing crops or grass</b>. The positive meaning comes from the General Clauses Act, 1897, s.3(26): land, benefits to arise out of land, and things attached to the earth or permanently fastened to anything attached to the earth.
<ul><li><b>Standing timber</b> = trees meant to be cut for wood (teak, sal). Movable. The test is intention: a mango tree kept for fruit stays immovable.</li>
<li><b>Growing crops</b> (paddy, wheat) and <b>grass</b> grown to be cut: movable, because they are grown to be harvested.</li>
<li><b>Benefits to arise out of land</b> = a right to take something from land, such as fishing or cutting forest produce (a profit à prendre). Immovable, so a registered deed is needed.</li>
<li><b>Attached to the earth</b> has three forms: (a) rooted (trees, shrubs), (b) imbedded (walls, buildings, a borewell), (c) attached to what is imbedded for its <i>permanent beneficial enjoyment</i> (doors, windows, machinery bolted in so the factory can work). Test for (c): how firmly is it fixed, and why? To permanently improve the building: immovable. Only to keep it steady: movable.</li></ul></li>
<li><b>Instrument, attested, registered.</b> An <b>instrument</b> is any non-testamentary document, so not a will. <b>Attested</b> means: two or more witnesses; each one either (A) saw the executant sign or put his mark, or (B) saw another person sign in his presence and by his direction, or (C) received his personal acknowledgment; and each signs in the executant's presence. They need not be present at the same time and no special form is needed. The words "deemed always to have meant" make it retrospective (1926). <b>Registered</b> means registered under the Registration Act, 1908.</li>
<li><b>Actionable claim.</b> A claim to (1) an <b>unsecured debt</b>, or (2) a <b>beneficial interest in movable property not in the claimant's possession</b>, actual or constructive. Debts secured by mortgage of immovable property, hypothecation or pledge are excluded. The civil courts must recognise it as grounds for relief (so a wagering debt fails). It covers claims that are existent, accruing, conditional or contingent.</li>
<li><b>Notice.</b> A person has notice when he actually knows a fact, or would have known it but for <b>wilful abstention</b> from an enquiry he ought to have made, or <b>gross negligence</b>. Three Explanations add deemed notice: <b>(I) registration</b> of a compulsorily registrable instrument, from the date of registration, if the three proviso conditions are met; <b>(II) actual possession</b>: a buyer has notice of the title of whoever is in actual possession; <b>(III) agent</b>: what your agent learns while acting for you in that business is your notice, unless the agent fraudulently conceals it, in which case it does not count against anyone party to the fraud.</li></ol>
<p><b>Memory word for constructive notice:</b> W-G-R-P-A: Wilful abstention, Gross negligence, Registration, Possession, Agent.</p>""",
dissect=[
("does not include standing timber, growing crops or grass","A negative definition. These three are movable. Positive meaning comes from the General Clauses Act."),
("means a non-testamentary instrument","Any formal deed except a will."),
("two or more witnesses","Minimum two. One witness means the deed is not attested."),
("has seen the executant sign or affix his mark","Route A. A mark covers a thumb impression."),
("has seen some other person sign the instrument in the presence and by the direction of the executant","Route B: a proxy signs, in his presence and at his direction."),
("has received from the executant a personal acknowledgement","Route C: the executant personally admits the signature."),
("each of whom has signed the instrument in the presence of the executant","Every witness signs while the executant is present."),
("it shall not be necessary that more than one of such witnesses shall have been present at the same time","Witnesses can come at different times."),
("rooted in the earth","Form (a): trees, shrubs."),
("imbedded in the earth","Form (b): walls, buildings."),
("attached to what is so imbedded for the permanent beneficial enjoyment of that to which it is attached","Form (c): the purpose test for fixtures and machinery."),
("a claim to any debt, other than a debt secured by mortgage of immoveable property or by hypothecation or pledge of moveable property","Kind 1 of actionable claim: unsecured debts only."),
("beneficial interest in moveable property not in the possession, either actual or constructive, of the claimant","Kind 2: goods you are entitled to but nobody holds for you."),
("which the Civil Courts recognise as affording grounds for relief","Must be enforceable. A betting debt fails."),
("existent, accruing, conditional or contingent","All four states of a claim are covered."),
("wilful abstention from an enquiry or search which he ought to have made","Constructive notice: deliberately not checking."),
("gross negligence","Constructive notice: extreme carelessness."),
("is required by law to be and has been effected by a registered instrument","Explanation I applies only to compulsory registration that has been done."),
("in actual possession thereof","Explanation II: physical possession gives notice of the occupier's title."),
("if the agent fraudulently conceals the fact","Fraud exception to imputed notice."),
],
master=dict(story="Kabir agrees to buy Raghunath's Athagarh farm for ₹60 lakh. On it stand a farmhouse with fitted doors, old mango trees kept for fruit, teak trees already sold to a timber merchant to be felled next month, standing paddy, and a rice-husking machine bolted into a concrete floor. A diesel pump sits on a plank, screwed only to stop it shaking. Ramesh lives in a corner hut as a tenant. Raghunath had mortgaged the farm to a bank in 2024 by a registered and properly indexed deed. Kabir's lawyer found that mortgage during the title search but forgot to tell Kabir. The deed of sale is signed by Raghunath; Meera watched him sign and signed as witness on Monday; Priya was told by Raghunath on Tuesday \"that is my signature\" and signed in front of him. Raghunath also owns a ₹2 lakh unsecured debt owed by Ramesh's shop and a lottery ticket, which he separately assigns to Kabir.",
steps=[
("Which items on the farm are immovable?","Land, farmhouse, its doors (form (c)), mango trees (rooted, kept to stay), the bolted husking machine (fixed for the shed's permanent beneficial enjoyment). These need the registered sale deed."),
("Which items are movable?","Teak trees to be felled (standing timber), the paddy (growing crops), and the pump fixed only for steadiness. These can pass by delivery."),
("Is the sale deed attested?","Yes. Two witnesses: Meera by Route A, Priya by Route C. Both signed in Raghunath's presence. Different days do not matter. (A sale does not even need attestation under s.54, but it is valid attestation.)"),
("Does Kabir take subject to the bank mortgage?","Yes, on three grounds: Explanation I (registered and correctly indexed, so deemed notice from 2024), Explanation III (his lawyer learnt of it while acting for him), and he could not claim to lack notice."),
("What about Ramesh the tenant?","Explanation II: Kabir is deemed to know the title of the person in actual possession, so he takes subject to Ramesh's tenancy, even if he never visited."),
("Is the shop debt an actionable claim?","Yes: an unsecured, enforceable debt. It is transferred by a signed written instrument (s.130), not by the sale deed."),
("Is the lottery ticket an actionable claim?","Yes: a contingent claim to a prize. Not goods."),
]),
ills=[
("Fruit tree vs timber","Raghunath sells 20 mango trees to Kabir \"to stand and bear fruit for ten years\", and 20 teak trees to a merchant \"to be cut within a month\".","m","Mango: immovable. Teak: movable.","Same act of selling trees; the intention decides. Trees meant to stand are attached to the earth; trees meant to be cut are standing timber."),
("Growing crop","Kabir buys the standing paddy crop alone, harvest due in three weeks, without the land.","y","Movable","Growing crops are excluded from immovable property. No registered deed needed."),
("Right to fish","Raghunath orally grants Kabir the right to catch and take fish from the village tank for five years.","n","Grant fails","A benefit arising out of land is immovable property, so an oral grant does not pass it."),
("Machinery: two ways","A husking machine set into concrete so the mill can run, and a portable pump screwed to a plank only for steadiness.","m","Machine immovable, pump movable","Form (c) asks why it is fixed: permanent beneficial enjoyment of the building, or only steadiness."),
("One witness only","Raghunath's gift deed of a plot is signed by only Kabir as witness.","n","Not attested","\"Two or more witnesses\" is mandatory, and a gift of immovable property needs attestation (s.123)."),
("Witness signs at home","Meera saw the signing but signed as witness the next day at her own house.","n","Not a valid attesting witness","Each witness must sign in the presence of the executant."),
("Proxy signature","Raghunath's hand is in plaster; at his direction Arjun signs his name in front of him; two witnesses watch.","y","Valid","Route B: another person signs in the executant's presence and by his direction."),
("A will is not an instrument","Raghunath's will is attested by two witnesses.","n","Not a TPA instrument","Instrument means non-testamentary. Wills are governed by the Indian Succession Act."),
("Secured vs unsecured debt","Ramesh owes ₹2 lakh with no security; Das owes ₹5 lakh secured by mortgage of his house; a worker owes ₹50,000 against gold bangles pledged.","m","Only Ramesh's debt is an actionable claim","Debts secured by mortgage, hypothecation or pledge are excluded."),
("Goods held for you","Raghunath has paid for 100 fertiliser bags not yet delivered; separately, 200 rice bags lie in a warehouse whose keeper has issued him a receipt.","m","Fertiliser: actionable claim. Rice: not","The warehouse keeper holds for him: constructive possession, so nothing remains to claim."),
("Betting debt","A friend owes Raghunath ₹20,000 from a cricket bet.","n","Not an actionable claim","Civil courts will not grant relief on a wagering debt."),
("Wrong index entry","The 2024 mortgage was registered but indexed under the wrong plot number.","n","No deemed notice under Explanation I","Proviso (3) requires correct entry in the s.55 indexes."),
("Voluntary registration","Raghunath's will mentioning the farm was registered although wills need not be.","n","No Explanation I notice","It applies only where registration is required by law."),
("Agent's fraud","Suresh, the seller of another plot, bribes Kabir's lawyer to hide a mortgage, then argues Kabir had notice through the lawyer.","n","No notice against Suresh","Fraudulent concealment by the agent does not charge the principal as against a party to the fraud."),
],
exam=dict(q="Define immovable property / attestation / actionable claim / notice (short notes, 5 marks each).",
pts=["Immovable property: negative TPA definition plus General Clauses Act s.3(26); intention test for trees; three forms of attachment","Attested: 2+ witnesses, three routes, signed in executant's presence, not necessarily together, no form; retrospective","Actionable claim: unsecured debt or beneficial interest in movables not possessed; exclusions; enforceable; four states","Notice: actual, constructive (W-G-R-P-A), Explanations I to III with the proviso and fraud exception"],
line="Section 3 is the interpretation clause: it defines immovable property, instrument, attested, registered, attached to the earth, actionable claim and notice for the whole Act."),
quiz=[
("Teak trees sold to be felled next month are:",["Immovable property","Standing timber, so movable","An actionable claim"],1,"Standing timber is excluded from immovable property."),
("A witness who only received the executant's personal acknowledgment:",["Cannot attest","Can attest if he signs in the executant's presence","Can attest only if both witnesses sign together"],1,"Route C, and witnesses need not be together."),
("Explanation II gives deemed notice of:",["Any registered deed","The title of the person in actual possession","Facts known to neighbours"],1,"Actual possession puts a buyer on notice."),
],
links=[("General Clauses Act s.3(26), (36)","Positive meanings of immovable and movable property."),("s.123, s.59","Gift and mortgage need attestation by two witnesses."),("s.130","Mode of transferring an actionable claim."),("s.136","Court officers cannot buy actionable claims."),("Registration Act s.17, 51, 55","Compulsory registration, books and indexes behind Explanation I.")],
next="With the vocabulary fixed, Section 5 tells you what a transfer of property is.")

S['5'] = dict(tag='syllabus',
simple="A <span class='hl'>transfer</span> means a living person, by his own act, hands over property (or some right in it) to another living person, or to himself. Sale, gift, exchange, lease and mortgage are all transfers. If a deal is not a transfer under s.5, most of TPA does not apply to it.",
deep="""<p>Think of TPA as a building. <b>Section 5 is the main door.</b> The rooms inside are sale, gift, exchange, lease and mortgage. A deal that does not pass through this door does not get TPA's rules.</p>
<ol>
<li><b>An act of the parties.</b> The owner must hand over the property himself. If property moves by operation of law (inheritance, a court auction, insolvency), it is not a s.5 transfer. Section 2(d) keeps those out, which is why TPA's long title says "by act of parties".</li>
<li><b>Between living persons (inter vivos).</b> Both sides must be alive at the moment of transfer. So a <span class="hl">will is not a transfer</span>: it works only after death. An unborn person cannot take directly; the Act gives a special route in s.13 and s.20. A child already in the mother's womb is treated as existing, if born alive.</li>
<li><b>"Living person" includes a company.</b> Added in 1929: a company, association or body of individuals, registered or not. But company law still applies, for example a board resolution.</li>
<li><b>"Conveys property."</b> To convey means to pass rights: the whole interest (sale, gift, exchange) or a part of it (lease, mortgage). Property means movable and immovable, tangible and intangible.</li>
<li><b>"In present or in future."</b> The transfer can operate now or from a later date. The trap: the property itself must exist today. You cannot transfer what you only hope to inherit (s.6(a)).</li></ol>
<p><b>Four modes:</b> (1) to one other living person, (2) to several, (3) to himself in a new capacity (owner declares himself trustee), (4) to himself and others together.</p>
<p><b>Not transfers:</b> will · inheritance · court sale or insolvency · partition (existing shares are only separated) · family settlement (existing rights recognised) · charge (s.100).</p>
<p><b>The 5-question test:</b> Did the owner act himself? Is the giver alive? Is the receiver alive? Does the property exist and belong to the giver? Is a new right passing? All yes: it is a transfer.</p>""",
dissect=[
("an act","Act of the parties. Transfers by operation of law are excluded."),
("a living person","The transferor must be alive. This shuts out a will."),
("conveys property","Passing rights: whole (sale, gift) or part (lease, mortgage)."),
("in present or in future","The transfer may operate now or later, but the property must exist today."),
("to one or more other living persons","Modes 1 and 2. The transferee must be living (link to s.13)."),
("or to himself","Mode 3: to himself in another capacity, such as trustee."),
("or to himself and one or more other living persons","Mode 4: himself and others together."),
("“living person” includes a company or association or body of individuals, whether incorporated or not","1929: artificial persons count as living persons."),
("nothing herein contained shall affect any law for the time being in force relating to transfer of property to or by companies","Saving clause: company law still applies."),
],
master=dict(story="On 1 March Raghunath signs five documents. (1) A sale deed of his Cuttack plot to Kabir. (2) A gift deed of his Puri house to \"Meera and Arjun jointly, and to myself as one of the joint owners\". (3) A deed declaring that he now holds his mango orchard as trustee for the village school. (4) A sale deed of his warehouse to Kalinga Agro Pvt Ltd, whose board has passed no resolution to buy. (5) A deed giving his godown to Kabir \"with effect from 1 January 2027\". The same day he writes a will leaving his farm to Arjun, and tries to gift a plot directly to Arjun's son Rohan, who is not yet conceived. Arjun separately \"sells\" Kabir the land he expects to inherit. Months later Raghunath dies; his heirs divide the remaining house into two halves.",
steps=[
("Document 1: plot to Kabir?","Transfer. Mode 1: one living person to another, by his own act."),
("Document 2: house to Meera, Arjun and himself?","Transfer. Mode 4: to himself and other living persons."),
("Document 3: orchard as trustee?","Transfer. Mode 3: to himself in a new capacity."),
("Document 4: warehouse to the company?","A company is a living person, so s.5 is satisfied; but the saving clause keeps company law alive, so the purchase may be challenged for want of board authority."),
("Document 5: godown from 2027?","Transfer \"in future\": the godown exists now; only its operation is postponed."),
("The will?","Not a transfer: it operates only after death."),
("The gift to unborn Rohan?","Fails under s.5 as a direct gift: the transferee is not a living person. The route is s.13."),
("Arjun's sale of his expected inheritance?","Not a valid transfer: a mere hope of inheriting cannot be transferred (s.6(a))."),
("Inheritance and the heirs' division?","Neither is a transfer: inheritance is by operation of law; partition only separates shares the heirs already own."),
]),
ills=[
("Act of parties vs operation of law","A court auctions Raghunath's plot to recover a decree debt; separately Raghunath himself sells another plot.","m","Court sale: not a s.5 transfer. Own sale: transfer","s.5 needs an act of the parties; s.2(d) excludes transfers by operation of law and court sales."),
("Transferor must be alive","Raghunath's will leaves his farm to Arjun.","n","Not a transfer","A will takes effect after death, so it is not between living persons."),
("Transferee must be alive","Raghunath gifts land directly to an unborn grandson.","n","Fails as a direct transfer","The receiver is not a living person. Use s.13 (prior interest to a living person)."),
("Child in the womb","Raghunath gifts land to Arjun's child, already in the womb, who is later born alive.","y","Valid","A child in the womb is treated as existing, if born alive."),
("Company as transferee","Raghunath sells his warehouse to Kalinga Agro Pvt Ltd after a board resolution.","y","Transfer","\"Living person\" includes a company (1929 amendment)."),
("Unregistered association","He gifts a hall to an unregistered village youth club.","y","Transfer","A body of individuals counts \"whether incorporated or not\"."),
("Partial interest","He leases his shop to Ramesh for five years.","y","Transfer of a partial interest","Conveying property includes passing part of the interest (lease)."),
("In future","He sells his godown today, ownership to pass on 1 January 2027.","y","Transfer","\"In present or in future\": only the operation is postponed."),
("Future property","Arjun sells land he expects to inherit from his father.","n","Not transferable","The property must exist and belong to the transferor; see s.6(a)."),
("To himself","Raghunath declares himself trustee of his orchard for the school.","y","Transfer","Mode 3: \"to himself\" in a different capacity."),
("Partition","Meera and Arjun divide the inherited house into two halves.","n","Not a transfer","Partition only separates shares already owned."),
("Charge","Raghunath makes his plot liable for a debt without transferring any interest.","n","Not a transfer","s.100: a charge is not a transfer of interest."),
],
exam=dict(q="Define transfer of property. Discuss its essentials. Is partition a transfer? (5 marks, sometimes 10 with s.6)",
pts=["Quote the s.5 definition","Essentials: act of parties; living persons (company included, 1929); conveyance of property; present or future; four modes","Not transfers: will, inheritance, court sale, partition, family settlement, charge","Conclude: s.5 is the gateway to the rest of TPA"],
line="Transfer of property under s.5 is an act inter vivos by which a living person, including a company, conveys property in present or in future to one or more living persons or to himself."),
quiz=[
("A will leaving land to a son is:",["A transfer under s.5","Not a transfer, as it works after death","A transfer if registered"],1,"It operates only after death."),
("Is a company a \"living person\"?",["No","Yes, since 1929","Only a government company"],1,"The 1929 amendment added companies and bodies of individuals."),
("Brothers divide an inherited house. Under s.5 this is:",["A transfer","Not a transfer","An exchange"],1,"Partition only separates existing shares."),
],
links=[("s.2(d)","Transfers by operation of law and court sales are outside Chapter II."),("s.54, 58, 105, 118, 122","Sale, mortgage, lease, exchange and gift: the kinds of transfer."),("s.100","A charge is not a transfer of interest."),("s.13, s.20","Route for unborn persons."),("s.129","Donatio mortis causa and Muslim law are saved.")],
next="Section 5 tells you what a transfer is. Section 6 tells you which property cannot be transferred.")

S['6'] = dict(tag='syllabus',
simple="<span class='hl'>Property of any kind may be transferred</span>, unless this Act or another law says no. Section 6 then lists what cannot be transferred: a hope of inheriting, a bare right of re-entry, an easement on its own, a personal right, future maintenance, a mere right to sue, public office and salary, pensions, and transfers that are against the nature of the interest, unlawful, or to a disqualified person.",
deep="""<p><b>The rule is transferability; the exceptions are listed.</b> Whoever says a property cannot be transferred must point to a clause of s.6 or another law. The opening words also let <b>other laws</b> block transfers, for example the Orissa Scheduled Areas Transfer of Immovable Property (by Scheduled Tribes) Regulation, 1956 for tribal land in Scheduled Areas.</p>
<ol>
<li><b>(a) Spes successionis</b>: the chance of an heir-apparent succeeding, the chance of a relation getting a legacy, or any similar mere possibility. A hope is not a right, so it cannot be transferred. An agreement to transfer it is also unenforceable. <i>Twist:</i> if the transferor falsely or erroneously claims he already owns it, takes consideration, and later acquires it, s.43 lets the transferee claim it. <i>Contrast:</i> a contingent interest (s.21) is a real right and can be transferred.</li>
<li><b>(b) A mere right of re-entry</b> for breach of a condition subsequent can go only to the owner of the property affected, never to a stranger on its own.</li>
<li><b>(c) An easement</b> (right of way, light, water over a neighbour's land) cannot be separated from the dominant heritage. It passes with that land (s.8).</li>
<li><b>(d) An interest restricted in its enjoyment to the owner personally</b> cannot be transferred by him, for example a personal right of residence.</li>
<li><b>(dd) A right to future maintenance</b> cannot be transferred, however it arises. Arrears already due are a debt and can be transferred.</li>
<li><b>(e) A mere right to sue</b> (for damages) cannot be transferred. A right to recover a debt is an actionable claim and can be.</li>
<li><b>(f) A public office</b>, and the <b>salary of a public officer</b> before or after it becomes payable.</li>
<li><b>(g) Military, naval, air-force and civil pensions</b> of the Government, and political pensions.</li>
<li><b>(h)</b> No transfer (1) opposed to the nature of the interest, (2) for an unlawful object or consideration under Contract Act s.23, or (3) to a person legally disqualified to be transferee (for example s.136).</li>
<li><b>(i)</b> An occupancy tenant with an untransferable right, a defaulting revenue farmer, and a lessee of an estate under a Court of Wards cannot assign their interest.</li></ol>
<p><b>Mnemonic for (a) to (g):</b> Some Rich Elders Prefer My Simple Old Pension (Spes, Re-entry, Easement, Personal, Maintenance, Sue, Office, Pension).</p>
<p><i>Note:</i> your Indian Kanoon copy reads "All interest" in clause (d); the government text reads "An interest". The meaning is the same.</p>""",
dissect=[
("Property of any kind may be transferred","The general rule: transferability."),
("except as otherwise provided by this Act or by any other law for the time being in force","Other laws can also bar transfers."),
("any other mere possibility of a like nature","(a) Spes successionis: a hope, not a right."),
("cannot be transferred to any one except the owner of the property affected thereby","(b) Re-entry goes only with the property."),
("An easement cannot be transferred apart from the dominant heritage","(c) Tied to the land it benefits."),
("restricted in its enjoyment to the owner personally","(d) Personal rights."),
("A right to future maintenance","(dd) Protects the dependant; arrears are transferable."),
("A mere right to sue","(e) No trading in lawsuits."),
("A public office cannot be transferred, nor can the salary of a public officer","(f) Public policy."),
("political pensions","(g) Pensions protect the pensioner."),
("opposed to the nature of the interest affected thereby","(h)(1) Some interests by nature belong to one person."),
("for an unlawful object or consideration within the meaning of section 23 of the Indian Contract Act","(h)(2) Forbidden, fraudulent, immoral or against public policy."),
("to a person legally disqualified to be transferee","(h)(3) For example s.136 court officers."),
("a tenant having an untransferable right of occupancy","(i) Historical tenure restrictions."),
],
master=dict(story="Raghunath, 70, is alive. His son Arjun, short of cash, signs a deed \"selling\" Kabir the farm he expects to inherit, and falsely tells Kabir the farm is already his. Raghunath separately leases a shop to Ramesh with a clause allowing re-entry if Ramesh sublets; Raghunath then sells only that re-entry right to Suresh. Raghunath also tries to sell to Kabir just his right of way across a neighbour's field. His widowed sister sells her lifetime personal right to live in the family house, and also her right to future monthly maintenance, plus six months of unpaid arrears. Raghunath assigns to Kabir his claim for damages against a lorry owner who hit his car, and also Ramesh's unpaid ₹2 lakh debt. Meera, a government officer, assigns next year's salary to a moneylender. A retired soldier uncle sells his army pension. Raghunath gifts a plot to a revenue officer to obtain a favourable record entry, and sells an actionable claim to a sitting civil judge. Finally a tribal farmer in Nabarangpur sells his land to Kabir without permission. Years later Raghunath dies and Arjun actually inherits the farm.",
steps=[
("Arjun's sale of his expected inheritance?","Void under (a) when made. But because Arjun falsely represented that he owned it and took consideration, when he later inherits, Kabir can claim the farm under s.43."),
("Sale of the bare re-entry right to Suresh?","Barred by (b): it can go only to the owner of the property affected."),
("Sale of the right of way alone?","Barred by (c): an easement cannot be transferred apart from the dominant heritage."),
("Sister's personal right of residence?","Barred by (d): restricted to her personally."),
("Sister's future maintenance and arrears?","Future maintenance barred by (dd); the six months of arrears are a debt and can be transferred."),
("Damages claim vs Ramesh's debt?","Damages claim: a mere right to sue, barred by (e). The debt: an actionable claim, transferable by a signed writing (s.130)."),
("Meera's salary and the uncle's pension?","Barred by (f) and (g)."),
("Gift to the revenue officer?","Void under (h)(2): unlawful object under Contract Act s.23."),
("Sale of an actionable claim to a judge?","Barred by (h)(3) read with s.136."),
("The tribal land sale?","Barred by another law (the 1956 Regulation), through the opening words of s.6."),
]),
ills=[
("Spes: heir-apparent","Arjun sells the farm he hopes to inherit while Raghunath is alive.","n","Void","A mere chance of succession cannot be transferred."),
("Spes: legacy","Meera sells the ₹5 lakh she hopes to receive under an uncle's will while the uncle is alive.","n","Void","The chance of a relation obtaining a legacy is a mere possibility."),
("Spes vs contingent interest","Raghunath gives Meera land \"if she becomes a judge\"; Meera sells this right.","y","Transferable","A contingent interest is a real right, not a mere hope."),
("Re-entry to the owner","Raghunath sells the leased shop itself (with the re-entry clause) to Kabir.","y","Valid","The right of re-entry passes with the property to its new owner."),
("Easement with land","Raghunath sells his farmhouse; the deed is silent on the right of way.","y","Right of way passes","The easement goes with the dominant heritage (s.8)."),
("Arrears of maintenance","The widow sells six months of unpaid maintenance.","y","Transferable","Arrears are a debt; only future maintenance is barred."),
("Salary already credited","Meera's salary has been paid into her bank account; she gifts that money to Arjun.","y","Valid","Once received, it is her money; the bar is on the salary as a claim, before or after it is payable."),
("Nature of the interest","Raghunath tries to transfer to Kabir his personal right of pre-emption over a neighbour's plot.","n","Barred","A commonly cited example of an interest which by its nature cannot be transferred."),
("Other law","A Scheduled Tribe farmer in a Scheduled Area sells land to a non-tribal without permission.","n","Barred","\"Any other law\": the Orissa Scheduled Areas Regulation, 1956."),
("Occupancy tenant","A tenant whose occupancy right is untransferable assigns it to Kabir.","n","Barred","Clause (i)."),
],
exam=dict(q="\"Property of any kind may be transferred.\" Discuss the exceptions. Write a note on spes successionis. (10 marks)",
pts=["General rule and burden","Go through (a) to (i) with an example each","Spes successionis in depth: void; agreements unenforceable; s.43 twist; contrast with contingent interest","Other laws through the opening words","Conclude: free circulation balanced with protection and public policy"],
line="Under s.6, property of any kind may be transferred except as provided by TPA or any other law; clauses (a) to (i) list non-transferable interests, led by spes successionis."),
quiz=[
("A son sells land he expects to inherit. Valid?",["Yes","No, it is spes successionis","Yes, if registered"],1,"A mere hope cannot be transferred."),
("Which can be transferred?",["Future maintenance","Arrears of maintenance","A military pension"],1,"Arrears are a debt."),
("A right to recover a debt vs a right to sue for damages:",["Both transferable","Debt transferable, damages claim not","Neither"],1,"Debt is an actionable claim; damages claim is a mere right to sue."),
],
links=[("s.43","Feeding the grant by estoppel can rescue a spes sold on a false representation."),("s.21","Contingent interest: a transferable real right."),("s.8","Easements pass with the land."),("s.130, s.136","Transfer of actionable claims; incapacity of court officers."),("Contract Act s.23","Unlawful object or consideration."),("Easements Act, 1882","Meaning of dominant and servient heritage.")],
next="Section 6 tells you what can be transferred. Section 7 tells you who can transfer it.")

S['7'] = dict(tag='syllabus',
simple="A person can transfer property if he is <span class='hl'>competent to contract</span> (adult, sound mind, not disqualified) and he either <span class='hl'>owns</span> the property or is <span class='hl'>authorised</span> to transfer it. He may transfer the whole or part, outright or on conditions, but only in the way the law allows.",
deep="""<ol>
<li><b>Competent to contract</b> (Contract Act s.11): a major (18), of sound mind, not disqualified by law. A person usually of unsound mind may contract in a lucid interval (Contract Act s.12). A <b>minor's transfer is void</b> from the start. A minor <b>can receive</b> property, because s.7 limits only the transferor.</li>
<li><b>Entitled to transferable property</b>: the owner of property that s.6 allows to be transferred.</li>
<li><b>Or authorised to dispose of property not his own</b>: an agent with a power of attorney, a guardian of a minor's property (court permission needed for immovable property under the Hindu Minority and Guardianship Act s.8; a sale without it is voidable at the minor's option), the karta of a Hindu joint family for legal necessity or benefit of the estate, a trustee, an executor, a receiver, a mortgagee with a power of sale.</li>
<li><b>Wholly or in part, absolutely or conditionally</b>: he can sell the whole or a share, outright or subject to a condition.</li>
<li><b>"In the circumstances, to the extent and in the manner allowed and prescribed by law"</b>: every other legal requirement still applies (court permission, registration, company resolutions, land-ceiling or tribal-land laws).</li></ol>
<p><b>Nemo dat quod non habet</b>: no one gives what he does not have. A person with neither ownership nor authority passes no title, subject to s.41 (ostensible owner) and s.43 (feeding the grant).</p>""",
dissect=[
("competent to contract","Major, sound mind, not disqualified (Contract Act s.11)."),
("entitled to transferable property","The owner, of property s.6 allows to be transferred."),
("authorised to dispose of transferable property not his own","Agent, guardian, karta, trustee, executor, receiver."),
("either wholly or in part","The whole or a share."),
("either absolutely or conditionally","Outright, or subject to a condition (s.25 to s.34 then apply)."),
("in the circumstances, to the extent and in the manner, allowed and prescribed by any law for the time being in force","Other legal requirements still bind him."),
],
master=dict(story="Raghunath's 16-year-old nephew inherits a plot and sells it to Kabir. Meera, the nephew's mother and natural guardian, then sells another plot of the nephew without court permission. Raghunath, who suffers from a mental illness with clear periods, sells a shop during a doctor-certified lucid interval and a second shop during an episode. Kabir, holding Raghunath's registered power of attorney \"to sell my Cuttack flat\", sells the flat and also Raghunath's farm. Arjun, karta of the joint family, sells family land to pay for his father's urgent surgery. Raghunath sells half his orchard on condition the buyer keeps the old well open. Suresh, a stranger, sells Raghunath's godown to an innocent buyer. Finally Raghunath gifts a plot to his 10-year-old grandson.",
steps=[
("Nephew's sale?","Void: a minor is not competent to contract."),
("Meera's sale without court permission?","She is authorised in principle, but the law's manner was not followed: voidable at the minor's option."),
("Shop sold in the lucid interval vs during an episode?","First valid (competent at that moment); second not, as he was not of sound mind."),
("Kabir's sales?","Flat: valid, he was authorised. Farm: no authority, so no title passes (nemo dat)."),
("Arjun as karta?","Valid if for legal necessity or benefit of the estate; urgent medical need qualifies."),
("Half the orchard on condition?","Valid: \"in part\" and \"conditionally\"."),
("Suresh's sale of the godown?","No title passes: neither owner nor authorised (unless s.41 or s.43 facts exist)."),
("Gift to the 10-year-old?","Valid: a minor can receive."),
]),
ills=[
("Minor transferor","A 17-year-old mortgages his house to a moneylender who knew his age.","n","Void","Not competent to contract; the mortgage has no effect."),
("Minor transferee","Raghunath gifts a plot to a 10-year-old grandson.","y","Valid","Section 7 restricts only the transferor."),
("Lucid interval","A person usually of unsound mind sells land during a lucid interval.","y","Valid","Competence is judged at the time of the transfer."),
("Power of attorney limits","Kabir, authorised only to sell the flat, also sells the farm.","m","Flat valid, farm not","Authority extends only as far as granted."),
("Guardian without permission","A guardian sells a minor's land without court permission.","m","Voidable","The transfer must be in the manner prescribed by law."),
("Conditional transfer","Raghunath sells half his land on condition the buyer keeps a path open.","y","Valid","Wholly or in part, absolutely or conditionally."),
("Stranger","Suresh sells Raghunath's land with no authority.","n","No title","Nemo dat, subject to s.41 and s.43."),
],
exam=dict(q="Who is competent to transfer property? (5 marks)",
pts=["Two conditions: competence to contract, and ownership or authority","Minor's transfer void; minor can be transferee","List of authorised persons","Wholly or in part, absolutely or conditionally, in the manner prescribed by law","Nemo dat and its exceptions (s.41, s.43)"],
line="Under s.7, every person competent to contract and entitled to transferable property, or authorised to dispose of property not his own, may transfer it wholly or in part, absolutely or conditionally, as the law allows."),
quiz=[
("A transfer by a 16-year-old is:",["Valid","Voidable","Void"],2,"A minor is not competent to contract."),
("Can a minor receive a gift of land?",["No","Yes","Only through a court"],1,"Section 7 limits only the transferor."),
],
links=[("Contract Act s.11, 12","Competence; lucid intervals."),("Hindu Minority and Guardianship Act s.8","Guardian needs court permission for immovable property."),("s.38","Transfer by a person authorised only in certain circumstances."),("s.41, s.43","Exceptions to nemo dat.")],
next="Once a competent person transfers, Section 8 says what exactly passes to the transferee.")

S['8'] = dict(tag='linked',
simple="Unless the parties say otherwise, a transfer passes <span class='hl'>immediately</span> to the transferee <span class='hl'>everything the transferor then has</span> in the property, together with its attached rights and things (easements, later rent, fixtures, securities, later income).",
deep="""<ol>
<li><b>Default rule.</b> It applies unless a different intention is <i>expressed</i> in the deed or <i>necessarily implied</i>.</li>
<li><b>Forthwith</b>: the interest passes at once.</li>
<li><b>All the interest the transferor is then capable of passing</b>: no more and no less. If he owns half, half passes. Later-acquired interests do not pass under s.8 (see s.43).</li>
<li><b>Legal incidents</b> pass automatically:
<ul><li><b>Land:</b> easements annexed; rents and profits accruing after the transfer; all things attached to the earth.</li>
<li><b>Machinery attached to the earth:</b> its movable parts.</li>
<li><b>House:</b> easements; rent accruing after transfer; locks, keys, bars, doors, windows and everything provided for permanent use.</li>
<li><b>Debt or actionable claim:</b> the securities for it, unless they also secure other debts not transferred; but not arrears of interest accrued before the transfer.</li>
<li><b>Money or income-yielding property:</b> interest or income accruing after the transfer takes effect.</li></ul></li></ol>
<p><b>Timing rule:</b> before the transfer stays with the transferor; after goes to the transferee.</p>""",
dissect=[
("Unless a different intention is expressed or necessarily implied","Default rule; parties may change it."),
("passes forthwith","Immediately."),
("all the interest which the transferor is then capable of passing","Only what he has at that moment."),
("the legal incidents thereof","Attached rights and things."),
("the rents and profits thereof accruing after the transfer","Income after the transfer goes to the buyer."),
("the moveable parts thereof","Movable parts of attached machinery."),
("all other things provided for permanent use therewith","House fixtures, not furniture."),
("except where they are also for other debts or claims not transferred to the transferee","Security shared with another debt stays."),
("not arrears of interest accrued before the transfer","Old interest stays with the transferor."),
],
master=dict(story="On 1 March Raghunath sells his rice mill and farm to Kabir. The deed is silent except for one line: \"Seller keeps this season's mango crop.\" The farm has a right of way across a neighbour's field, a borewell and mango trees. The tenant's February rent is unpaid; the rent for March, payable in advance, falls due on 5 March. The mill has a husking machine bolted to the floor with spare belts fitted and blades in a drawer. The farmhouse has doors, locks and a sofa. Raghunath owned only a half share in a small attached plot. On the same day he also assigns to Kabir a ₹1 lakh loan owed by Das, secured by gold that also secures another ₹50,000 loan Das owes Raghunath, with ₹8,000 of interest already overdue; and he transfers a fixed deposit whose quarterly interest is credited on 31 March.",
steps=[
("Right of way, borewell, trees?","Pass automatically as incidents of land."),
("February and March rent?","February stays with Raghunath; March rent (accruing after the transfer) goes to Kabir."),
("This season's mangoes?","Stay with Raghunath: a different intention is expressed."),
("Belts and blades?","Movable parts of machinery attached to the earth pass."),
("Doors and locks vs sofa?","Doors and locks pass (permanent use); the sofa does not."),
("The half-share plot?","Only the half share passes: all the interest he is then capable of passing."),
("Das's gold?","Does not pass, because it also secures the other ₹50,000 debt not transferred."),
("₹8,000 overdue interest?","Stays with Raghunath."),
("FD interest on 31 March?","Goes to Kabir: income accruing after the transfer."),
]),
ills=[
("Different intention","The sale deed says the seller keeps the standing crop.","y","Seller keeps it","s.8 yields to an expressed intention."),
("Half share","A co-owner of half sells \"the plot\".","m","Only half passes","He passes only what he is then capable of passing."),
("Easement","Sale of a house silent about its right to light.","y","Passes","Easements annexed pass with the house."),
("Rent split","Sale on 15 June; June rent payable on 30 June.","m","Split: 1 to 14 June to the seller, 15 to 30 June to the buyer","Only rent accruing after the transfer passes, and s.36 makes rent accrue day by day."),
("Security shared","Debt assigned; the security also covers another debt kept by the assignor.","n","Security does not pass","Exception in the debt clause."),
("Arrears of interest","Debt assigned with interest overdue before assignment.","n","Overdue interest stays","Not arrears of interest accrued before the transfer."),
],
exam=dict(q="Explain the operation of transfer under s.8. (5 marks)",
pts=["Default rule, subject to contrary intention","Forthwith; all interest then capable of passing","List incidents by type of property","Timing rule"],
line="Under s.8, unless a different intention appears, a transfer passes forthwith all the interest the transferor then has, with its legal incidents."),
quiz=[("Rent for the month before the sale goes to:",["Buyer","Seller","Split equally"],1,"Only rent accruing after the transfer passes.")],
links=[("s.3","\"Attached to the earth\"."),("s.6(c)","Easements cannot be transferred apart from the land."),("s.43","Later-acquired interests."),("s.55","Buyer's and seller's rights on sale.")],
next="Section 9 asks whether the transfer must be in writing.")

S['9'] = dict(tag='linked',
simple="A transfer can be made <span class='hl'>orally</span> unless some law <span class='hl'>expressly requires writing</span>.",
deep="""<p>Oral is the default. Writing is needed only where a law says so. In TPA:</p>
<ul><li><b>Sale</b> of tangible immovable property worth ₹100 or more, or of a reversion or other intangible thing: registered instrument (s.54). Under ₹100: registered instrument or delivery.</li>
<li><b>Mortgage</b> securing ₹100 or more: registered instrument signed and attested by two witnesses (s.59). <b>Mortgage by deposit of title deeds</b> (s.58(f)) needs no writing.</li>
<li><b>Lease</b> from year to year, for more than a year, or reserving a yearly rent: registered instrument (s.107). Shorter leases: oral agreement plus delivery of possession.</li>
<li><b>Exchange</b> (s.118): as for sale.</li>
<li><b>Gift</b> of immovable property: registered and attested instrument (s.123). Gift of movables: registered instrument or delivery.</li>
<li><b>Actionable claim</b> (s.130): written instrument signed by the transferor.</li></ul>
<p>Oral transfers are valid for movables by delivery, small sales by delivery, short leases, and gifts of movables by delivery.</p>""",
dissect=[
("may be made without writing","Oral is the default."),
("in which a writing is not expressly required by law","Writing only where a statute demands it."),
],
master=dict(story="In one week Arjun sells his bicycle by handing it over; Raghunath sells his ₹40 lakh farm by a handshake; he sells a tiny strip worth ₹80 by placing the buyer in possession; he leases a shop for 11 months orally and hands over the keys; he leases another shop for 3 years orally; he deposits his title deeds with a bank in Bhubaneswar for a loan without writing anything; he gifts Meera a gold chain by putting it round her neck; he orally gifts Arjun a plot; and he orally assigns Ramesh's ₹2 lakh debt to Kabir.",
steps=[
("Bicycle?","Valid oral transfer of a movable by delivery."),
("Farm by handshake?","Invalid: s.54 requires a registered instrument."),
("₹80 strip by possession?","Valid: under ₹100, delivery is enough."),
("11-month lease?","Valid: oral agreement plus possession (s.107)."),
("3-year lease?","Not valid as a lease: needs a registered instrument."),
("Deposit of title deeds?","Valid mortgage without writing (s.58(f)) in a notified town."),
("Gold chain?","Valid gift of a movable by delivery."),
("Plot orally?","Invalid: s.123 needs a registered and attested deed."),
("Debt orally?","Invalid: s.130 requires a signed writing."),
]),
ills=[
("Movable by delivery","Arjun sells his phone by handing it over.","y","Valid","No law requires writing."),
("Immovable over ₹100","Sale of a house by oral agreement.","n","Invalid","s.54: registered instrument."),
("Short lease","Shop let for 6 months orally with keys handed over.","y","Valid","s.107 permits it."),
("Deposit of title deeds","Title deeds deposited with a bank, nothing written.","y","Valid mortgage","s.58(f)."),
("Actionable claim","Debt assigned by phone call.","n","Invalid","s.130 needs a signed writing."),
],
exam=dict(q="Short note on oral transfer (2 to 5 marks).",
pts=["Oral is the default","List the sections requiring writing","Exception: mortgage by deposit of title deeds"],
line="Under s.9, a transfer may be made without writing unless writing is expressly required by law, as in s.54, 59, 107, 118, 123 and 130."),
quiz=[("Which needs no writing?",["Gift of a house","Mortgage by deposit of title deeds","Sale of land worth ₹5 lakh"],1,"s.58(f).")],
links=[("s.54, 58(f), 59, 107, 118, 123, 130","Where writing is or is not required."),("Registration Act s.17","Compulsory registration.")],
next="Section 10 starts the rules on conditions that the law will not allow.")
