S = {}

S['13'] = dict(tag='syllabus',
simple="You cannot give property <i>directly</i> to someone not yet born. You can do it only by first giving it to a <span class='hl'>living person</span> (usually for life) in the same deed, and then to the unborn person, who must get the <span class='hl'>whole remaining interest</span>, not just a life interest.",
deep="""<ol>
<li><b>Why a special rule:</b> s.5 requires a living transferee, so a direct transfer to an unborn person fails.</li>
<li><b>Condition 1, prior interest:</b> the deed must first create an interest for a living person (for example \"to Arjun for life\"). The property is held for the unborn person through that prior interest.</li>
<li><b>Condition 2, same transfer:</b> the prior interest and the gift to the unborn person must be in the same deed.</li>
<li><b>Condition 3, whole remaining interest:</b> the unborn person must take the entire remaining interest of the transferor, that is, absolute ownership. A life interest to an unborn person fails.</li>
<li><b>Why condition 3:</b> otherwise life estates to unborn persons could be stacked generation after generation, locking property in the family forever.</li>
<li><b>Birth timing:</b> the unborn person must come into existence by the time the prior interest ends, or he cannot take.</li>
<li><b>Child in the womb</b> at the date of transfer is treated as existing (if born alive), so s.13 does not apply to it.</li>
<li><b>Works with:</b> s.14 (time limit), s.20 (vests on birth), s.15 and s.16 (effect of failure).</li></ol>
<p><b>The Act's Illustration:</b> A transfers to B in trust for A and his intended wife successively for life, then for the eldest son of the marriage for life, then for A's second son. The eldest son's interest fails because it is only a life interest, not the whole remaining interest.</p>""",
dissect=[
("a person not in existence at the date of the transfer","The unborn person (a child in the womb counts as existing)."),
("subject to a prior interest created by the same transfer","A living person first, in the same deed."),
("shall not take effect, unless it extends to the whole of the remaining interest of the transferor","The unborn person must get absolute ownership."),
("The interest so created for the benefit of the eldest son does not take effect","Statutory example: a life interest to an unborn person fails."),
],
master=dict(story="Raghunath (A) owns a 10-acre farm. His son Arjun (B) is married but has no children. Raghunath signs Deed 1: \"To Arjun for life, then to Arjun's first son absolutely.\" He signs Deed 2 for his orchard: \"To Arjun for life, then to Arjun's first son for his life, then to Meera.\" On the same day he signs Deed 3 directly to \"Arjun's future son\" for a plot, with no prior interest. A year later he signs a separate Deed 4 giving the godown to Arjun's future son after Arjun's death, having already given Arjun a life interest in the godown by an earlier deed. At the date of the deeds Arjun's wife is three months pregnant; Rohan is born six months later. Arjun dies when Rohan is ten.",
steps=[
("Was Rohan \"not in existence\"?","No. He was in the womb at the date of the deeds, and born alive, so he is treated as existing. Strictly, s.13 does not bite. (Had Arjun had no child conceived, the steps below would apply.)"),
("Assuming Rohan unconceived: Deed 1?","Valid: prior life interest to living Arjun in the same deed; the unborn son takes the whole remaining interest."),
("Deed 2?","The son's life interest fails (not the whole remaining interest). Meera's gift after it also fails (s.16)."),
("Deed 3?","Fails: no prior interest to a living person."),
("Deed 4?","Fails: the prior interest was created by a different, earlier deed, not \"the same transfer\"."),
("When Arjun dies under Deed 1?","Rohan, already born, takes absolutely; a guardian manages it until he is 18. His interest vested at birth (s.20)."),
]),
ills=[
("Direct gift to unborn","\"To Arjun's future son\" with nothing before it.","n","Fails","No prior interest to a living person."),
("Valid route","\"To Arjun for life, then to his first son absolutely.\"","y","Valid","Prior interest, same deed, whole remaining interest."),
("Life interest to unborn","\"To Arjun for life, then to his first son for life.\"","n","Son's interest fails","Not the whole remaining interest."),
("Separate deeds","Life interest to Arjun in 2025; gift to his unborn son in 2026.","n","Fails","Prior interest must be by the same transfer."),
("Child in womb","Gift to a child already conceived, later born alive.","y","Valid directly","Treated as existing."),
("Not born in time","Unborn son not born when Arjun's life interest ends.","n","Cannot take","He must be in existence when the prior interest ends."),
],
exam=dict(q="Explain transfer for the benefit of an unborn person. (10 marks, often with s.14)",
pts=["Why: s.5 needs a living transferee","Conditions: prior interest to a living person; same transfer; whole remaining interest","Unborn must exist when the prior interest ends; child in womb treated as existing","Quote the Illustration","Link to s.14, s.20, s.15, s.16"],
line="Under s.13, an interest for a person not in existence can be created only subject to a prior interest in the same transfer, and must extend to the whole remaining interest of the transferor."),
quiz=[("\"To B for life, then to B's unborn son for life\": the son's gift is:",["Valid","Void under s.13","Valid until he is 18"],1,"An unborn person must take the whole remaining interest."),("A child in the womb at the date of transfer is:",["Unborn under s.13","Treated as existing if born alive","Never a transferee"],1,"Treated as in existence.")],
links=[("s.5","Living transferee required."),("s.14","Rule against perpetuity."),("s.20","Unborn person's interest vests on birth."),("s.15, s.16","Effect of failure on class and later gifts."),("Indian Succession Act s.113","Parallel rule for wills.")],
next="Section 14 sets the outer time limit for such future gifts.")

S['14'] = dict(tag='syllabus',
simple="Property cannot be tied up forever. A future interest must vest no later than <span class='hl'>the lifetime of people alive at the transfer plus the minority (until 18) of a person born by then</span>. Anything that might vest later is void.",
deep="""<ol>
<li><b>Perpetuity</b> means tying property up indefinitely. The rule keeps property in circulation.</li>
<li><b>Maximum period:</b> life or lives of persons living at the date of transfer + the minority of a person in existence when those lives end. The interest must belong to that person when he attains full age.</li>
<li><b>Age of majority:</b> 18.</li>
<li><b>Vesting, not enjoyment:</b> the interest must vest within the period; enjoyment may come later.</li>
<li><b>Test it at the date of transfer:</b> if the interest might vest beyond the period, it is void from the start.</li>
<li><b>Child in the womb</b> counts as existing, so the gestation period is allowed where actually needed.</li>
<li><b>s.13 vs s.14:</b> s.13 controls <i>what</i> the unborn person gets (the whole interest); s.14 controls <i>when</i> it must vest.</li>
<li><b>Exception:</b> transfers for public benefit (s.18).</li></ol>""",
dissect=[
("after the life-time of one or more persons living at the date of such transfer","Lives in being."),
("the minority of some person who shall be in existence at the expiration of that period","Plus minority of the ultimate beneficiary."),
("if he attains full age, the interest created is to belong","Must vest by his majority (18)."),
],
master=dict(story="Raghunath signs four deeds. Deed 1: farm \"to Arjun for life, then to Arjun's son Rohan (unborn) when he turns 18\". Deed 2: orchard \"to Arjun for life, then to Rohan when he turns 25\". Deed 3: a hall forever to a village school. Deed 4: a shop \"to Arjun for life, then to Rohan absolutely, Rohan to get possession at 25\".",
steps=[
("Deed 1?","Valid: vests at the latest when Rohan turns 18, within Arjun's life plus minority."),
("Deed 2?","Void: vesting at 25 can go beyond the perpetuity limit."),
("Deed 3?","Valid: s.18 exempts public benefit transfers from s.14."),
("Deed 4?","Valid: the gift vests in Rohan at birth (absolute, s.20); only possession waits till 25. s.14 tests vesting, not enjoyment."),
]),
ills=[
("Within limit","To B for life, then to B's son at 18.","y","Valid","Life in being plus minority."),
("Beyond limit","To B for life, then to B's son at 25.","n","Void","Might vest after the minority."),
("Vesting vs enjoyment","Vested at birth, enjoyment after B's death.","y","Valid","The rule tests vesting, not enjoyment."),
("Public benefit","Land forever to a hospital.","y","Valid","s.18 exception."),
],
exam=dict(q="Explain the rule against perpetuity. (10 marks with s.13)",
pts=["Meaning and object","Maximum period: lives in being plus minority","Vesting not enjoyment; test at date of transfer","Relation with s.13; exception in s.18"],
line="Under s.14, no transfer can create an interest to take effect after the lifetime of persons living at the transfer and the minority of a person then in existence."),
quiz=[("\"To B for life, then to B's unborn son at 25\":",["Valid","Void under s.14","Valid under s.18"],1,"Exceeds lives in being plus minority.")],
links=[("s.13","Whole interest to the unborn person."),("s.15, s.16","Effect of failure."),("s.17","Accumulation limits."),("s.18","Public benefit exception."),("Indian Succession Act s.114","Parallel rule for wills.")],
next="Section 15 deals with gifts to a class where only some members fail.")

S['15'] = dict(tag='syllabus',
simple="If a gift is to a <span class='hl'>group (class)</span> and it fails for some members because of s.13 or s.14, it fails <span class='hl'>only for those members</span>, not the whole group.",
deep="""<ul><li><b>Class gift:</b> a gift to a group described generally, such as \"all of Arjun's children\".</li>
<li>Members who fail the s.13 or s.14 rule drop out; the rest take.</li>
<li>The 1929 amendment changed the old rule (where the whole class failed) to this narrower one.</li></ul>""",
dissect=[("a class of persons with regard to some of whom such interest fails","A group where some members fail."),("in regard to those persons only and not in regard to the whole class","Only they drop out.")],
master=dict(story="Raghunath gives land \"to Arjun for life, then to all of Arjun's children who reach 18, but for any child born after Arjun's death, only on reaching 25\". Arjun has two children at the date of the deed and one more later.",
steps=[("Children who must take by 18?","Valid: within s.14."),("Any child whose gift depends on reaching 25?","Fails under s.14."),("Does the whole class fail?","No: only the members affected drop out (s.15).")]),
ills=[("Partial failure","Gift to a class where two members satisfy s.14 and one does not.","m","Two take, one fails","Failure only for those persons.")],
exam=dict(q="Explain class gifts under s.15.",pts=["Meaning of class gift","Failure only for affected members","1929 change"],line="Under s.15, where a class gift fails for some members under s.13 or s.14, it fails for those members only."),
quiz=[("A class gift failing for some members fails:",["For all","Only for those members","Only for the eldest"],1,"s.15.")],
links=[("s.13, s.14","Rules causing failure."),("s.22","Class who must attain an age.")],
next="Section 16 says what happens to a later gift that depends on a failed one.")

S['16'] = dict(tag='linked',
simple="If an earlier gift fails because of s.13 or s.14, <span class='hl'>any later gift in the same deed that depends on it also fails</span>.",
deep="<p>A later gift meant to take effect after, or on failure of, a prior interest falls together with it when the prior interest fails under s.13 or s.14. The domino rule.</p>",
dissect=[("any interest created in the same transaction and intended to take effect after or upon failure of such prior interest also fails","The later gift falls with the earlier.")],
master=dict(story="Raghunath: \"To Arjun for life, then to Arjun's unborn son for life, then to Meera absolutely.\"",steps=[("Son's interest?","Fails under s.13 (only a life interest)."),("Meera's gift?","Also fails under s.16: it was to take effect after the failed interest.")]),
ills=[("Domino","Gift over after an interest void under s.14.","n","Also fails","s.16.")],
exam=dict(q="Explain s.16.",pts=["Later dependent gift fails with the prior"],line="Under s.16, where a prior interest fails under s.13 or s.14, any interest in the same transaction intended to take effect after or upon its failure also fails."),
quiz=[("Meera's gift after a void s.13 interest:",["Valid","Also fails","Becomes absolute"],1,"s.16.")],
links=[("s.13, s.14","Cause of the prior failure.")],
next="Section 17 limits directions to save up income.")

S['17'] = dict(tag='syllabus',
simple="You can order a property's income to be <span class='hl'>saved up (accumulated)</span> only for the <span class='hl'>longer of your own life or 18 years</span>. Any longer period is void. Saving to pay debts, to provide for children, or to maintain the property is allowed without this limit.",
deep="""<ol>
<li><b>Rule:</b> a direction to accumulate income for longer than (a) the transferor's life or (b) 18 years from the transfer is void beyond the longer of the two.</li>
<li><b>Effect:</b> only the excess is void; at the end of the allowed period the property and income are dealt with as if the accumulation period had ended.</li>
<li><b>Exceptions:</b> accumulation (i) to pay debts of the transferor or anyone taking under the transfer, (ii) to provide portions for children or remoter issue, (iii) to preserve or maintain the property.</li>
<li>Public benefit transfers are exempt (s.18).</li></ol>
<p><i>Note:</i> your Indian Kanoon copy reads "under the transferor" in (2)(i); the government text reads "under the transfer".</p>""",
dissect=[("the life of the transferor","Period (a)."),("a period of eighteen years from the date of transfer","Period (b)."),("exceeds the longer of the aforesaid periods","Void only beyond the longer period."),("the payment of the debts","Exception (i)."),("the provision of portions for children or remoter issue","Exception (ii)."),("the preservation or maintenance of the property transferred","Exception (iii).")],
master=dict(story="Raghunath, aged 60, transfers his farm to trustees in 2026: \"save all the farm income for 40 years, then pay it to Rohan\". In another deed: \"save income to repay my bank loan\"; in a third: \"save income to repair the farmhouse\"; in a fourth: \"save income for 30 years to build a public hospital\". Raghunath dies in 2041.",
steps=[("40-year direction?","Valid only up to the longer of his life (to 2041, 15 years) or 18 years (to 2044). Void after 2044; then the property and income go as if accumulation had ended."),("Loan repayment?","Exception (i): allowed."),("Repairs?","Exception (iii): allowed."),("Hospital?","s.18 exempts public benefit from s.17.")]),
ills=[("Excess period","Accumulate for 30 years; transferor dies after 10.","m","Valid for 18 years only","Longer of life or 18 years."),("Debts","Accumulate to pay the transferor's debts.","y","Valid","Exception (i)."),("Children's portions","Accumulate to provide for grandchildren's marriages.","y","Valid","Exception (ii).")],
exam=dict(q="Explain the doctrine of accumulation under s.17.",pts=["Limit: longer of transferor's life or 18 years","Excess void","Exceptions (i) to (iii)","s.18 exemption"],line="Under s.17, a direction to accumulate income beyond the longer of the transferor's life or 18 years is void to the extent of the excess, save for debts, children's portions and maintenance."),
quiz=[("Accumulation for upkeep of the property:",["Void after 18 years","Allowed","Void"],1,"Exception (iii).")],
links=[("s.18","Public benefit exemption."),("s.14","Rule against perpetuity.")],
next="Section 18 exempts gifts for the public good.")

S['18'] = dict(tag='syllabus',
simple="Gifts for the <span class='hl'>benefit of the public</span> (religion, knowledge, commerce, health, safety or any purpose good for mankind) are free from s.14, s.16 and s.17. They can last forever.",
deep="""<ul><li>The rule against perpetuity exists to stop families locking up property for themselves; public gifts help everyone, so they may be permanent.</li>
<li>Exempt from: s.14 (perpetuity), s.16 (dependent failure), s.17 (accumulation).</li>
<li><b>Not</b> exempt from s.13.</li>
<li>The benefit must be to the public, not to a private family.</li></ul>""",
dissect=[("The restrictions in sections 14, 16 and 17 shall not apply","Only these three are lifted."),("for the benefit of the public","Must be public."),("any other object beneficial to mankind","General catch-all.")],
master=dict(story="Raghunath gives land forever to run a free village school; saves income for 50 years to build a hospital; and gives a house forever \"for the use of my descendants as a family residence\".",steps=[("School?","Valid: knowledge, public benefit."),("Hospital accumulation?","Valid: exempt from s.17."),("Family residence forever?","Not public benefit: s.14 applies.")]),
ills=[("Public","Land forever for a fire station.","y","Valid","Safety."),("Private","Land forever for family members only.","n","Not covered","Not for the public.")],
exam=dict(q="Short note on transfer in perpetuity for the benefit of the public.",pts=["Exemption from s.14, 16, 17","Listed objects","Not exempt from s.13; must be public"],line="Under s.18, s.14, 16 and 17 do not apply to transfers for the benefit of the public in the advancement of religion, knowledge, commerce, health, safety or any object beneficial to mankind."),
quiz=[("s.18 does NOT exempt from:",["s.14","s.13","s.17"],1,"Only s.14, 16, 17.")],
links=[("s.14, s.16, s.17","Rules lifted.")],
next="Section 20 says when an unborn person's interest vests.")

S['20'] = dict(tag='syllabus',
simple="When property is given for someone not yet born, he gets a <span class='hl'>vested interest the moment he is born</span>, even if he can enjoy it only later, unless the deed says otherwise.",
deep="""<ul><li>Vesting at birth, enjoyment may be postponed (for example until the prior life interest ends).</li>
<li>Because it is vested, if he dies after birth but before enjoyment, it passes to his heirs (s.19).</li>
<li>A contrary intention in the deed can change this.</li></ul>""",
dissect=[("he acquires upon his birth","Vesting at birth."),("unless a contrary intention appears from the terms of the transfer","The deed may say otherwise."),("although he may not be entitled to the enjoyment thereof immediately on his birth","Enjoyment can wait.")],
master=dict(story="\"To Arjun for life, then to Arjun's son absolutely.\" Rohan is born in 2030; Arjun is alive. Rohan dies in 2040 aged 10, unmarried; Arjun dies in 2045.",steps=[("When did Rohan's interest vest?","At birth in 2030."),("Rohan dies before Arjun?","His vested interest passes to his heirs; they take on Arjun's death in 2045.")]),
ills=[("Vesting at birth","Unborn son's absolute gift after a life interest.","y","Vests at birth","s.20."),("Contrary intention","\"Only if he survives his father.\"","m","Contingent","Contrary intention appears.")],
exam=dict(q="Explain s.20.",pts=["Vests on birth","Enjoyment may wait","Contrary intention"],line="Under s.20, a person not then living for whose benefit an interest is created acquires a vested interest upon his birth, unless a contrary intention appears."),
quiz=[("An unborn son's interest vests:",["When the prior interest ends","On his birth","At 18"],1,"s.20.")],
links=[("s.13","Creation of the interest."),("s.19","Nature of a vested interest.")],
next="Section 19 explains what a vested interest is.")
