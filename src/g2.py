S = {}

S['10'] = dict(tag='linked',
simple="If you transfer property with a condition that the transferee can <span class='hl'>never sell or part with it</span>, that condition is <span class='hl'>void</span>. The transfer stands and the transferee is free. A <i>partial</i> restraint is allowed. Two exceptions: a lessor's condition in a lease, and a married woman who is not Hindu, Muslim or Buddhist.",
deep="""<ol>
<li><b>Principle:</b> property must circulate freely. Once you give it away, you cannot permanently tie the new owner's hands.</li>
<li><b>Condition or limitation.</b> A condition ("on condition you never sell") or a limitation ("to you until you try to sell") are both covered.</li>
<li><b>Absolutely restraining.</b> Only an absolute restraint is void. The test is <i>substance</i>, not wording: a clause that in practice leaves no real freedom to sell (sell only to one person at a fraction of the value) is absolute. A restraint that leaves real freedom (not to sell to one named rival, or not outside the family) is partial and valid.</li>
<li><b>Transferee or any person claiming under him</b>: restraints on heirs and successors are also hit.</li>
<li><b>Effect:</b> only the condition is void. The transfer remains, free of it.</li>
<li><b>Exception 1, lease:</b> a condition for the lessor's benefit (no subletting, no assignment) is valid.</li>
<li><b>Exception 2, proviso:</b> property may be given to or for a woman who is not Hindu, Muslim or Buddhist so that during her marriage she cannot transfer or charge it (restraint on anticipation), to protect her from pressure.</li></ol>
<p><i>Note:</i> your Indian Kanoon copy has a typo, "a women".</p>""",
dissect=[
("a condition or limitation","Both forms are covered."),
("absolutely restraining","Only absolute restraint, judged by substance."),
("or any person claiming under him","Heirs and successors too."),
("the condition or limitation is void","Only the condition fails; the transfer stands."),
("except in the case of a lease where the condition is for the benefit of the lessor","Lease exception."),
("not being a Hindu, Muhammadan or Buddhist","Proviso: restraint on anticipation during marriage."),
],
master=dict(story="Raghunath makes six gifts. (1) A house to Arjun \"on condition that he and his heirs shall never sell, mortgage or gift it\". (2) A plot worth ₹50 lakh to Meera, \"but if she ever wishes to sell, she must first offer it to Arjun for ₹5 lakh\". (3) Under a family settlement, a field to Meera \"not to be sold to anyone outside the Mishra family\". (4) A shop to Kabir \"not to be sold to Suresh\". (5) A lease of a godown to Ramesh, \"tenant shall not sublet or assign\". (6) Land to his Christian god-daughter Priya, \"she shall not sell or charge it during her marriage\". Arjun sells the house; Meera sells her plot to a stranger for ₹50 lakh; Ramesh sublets the godown.",
steps=[
("Gift 1, never sell?","Absolute restraint: condition void; Arjun owns the house and can sell it."),
("Gift 2, offer to Arjun for ₹5 lakh?","Absolute in substance: it leaves no real freedom. Condition void; her sale stands."),
("Gift 3, family only?","Partial: she can still sell within the family. Valid."),
("Gift 4, not to Suresh?","Partial: only one buyer excluded. Valid."),
("Lease 5?","Valid: condition for the lessor's benefit in a lease. Ramesh's subletting breaches it."),
("Gift 6?","Valid under the proviso: restraint during marriage for a woman not Hindu, Muslim or Buddhist."),
]),
ills=[
("Absolute restraint","Gift of a house \"never to be sold\".","n","Condition void","Absolute restraint on alienation."),
("Restraint on heirs","Gift \"neither the donee nor his heirs shall ever sell\".","n","Condition void","\"Any person claiming under him\" is covered."),
("Disguised absolute restraint","Sale allowed only to one named person at a nominal price.","n","Void","Substance over form."),
("Partial restraint","\"Not to be sold outside the family.\"","y","Valid","Real freedom remains."),
("Limitation form","\"To Kabir until he attempts to sell.\"","n","Limitation void","Limitations are covered as much as conditions."),
("Lease","\"Lessee shall not assign.\"","y","Valid","For the lessor's benefit."),
("Proviso","Gift to a Parsi woman restraining transfer during marriage.","y","Valid","Proviso applies; not to Hindu, Muslim or Buddhist women."),
("Proviso not available","The same clause in a gift to a Hindu woman.","n","Condition void","The proviso excludes Hindu, Muslim and Buddhist women."),
],
exam=dict(q="Discuss the rule against restraint on alienation under s.10. (5 or 10 marks)",
pts=["Principle of free alienation","Absolute restraint void; partial valid; test of substance","Condition or limitation; transferee and those claiming under him","Only the condition fails","Exceptions: lease; proviso for married women not Hindu, Muslim or Buddhist"],
line="Under s.10, a condition or limitation absolutely restraining the transferee from parting with his interest is void, except a lessor's condition in a lease and the proviso for certain married women."),
quiz=[("\"Never sell\" in a gift deed:",["Makes the gift void","Is void; gift stands","Is valid"],1,"Only the condition fails."),("\"Not to sell to Suresh\" is:",["Absolute","Partial, so valid","Void"],1,"Real freedom remains.")],
links=[("s.11","Restraint on enjoyment (s.10 is restraint on disposal)."),("s.12","Forfeiture on insolvency or attempted alienation."),("s.111(g)","Forfeiture of a lease."),("s.31","Conditions subsequent are subject to s.12.")],
next="Section 11 deals with directions about how an absolutely transferred property must be used.")

S['11'] = dict(tag='linked',
simple="If you give someone property <span class='hl'>absolutely</span> but tell him <span class='hl'>how he must use it</span>, he can ignore the direction. Exception: a direction about one piece of land made to protect another piece of land can be enforced.",
deep="""<ol>
<li><b>Absolute interest + direction on enjoyment</b> = the direction is ignored. You cannot make someone full owner and also control him.</li>
<li><b>Key word "absolutely".</b> If only a limited interest is given (a life interest), directions about its use may be valid.</li>
<li><b>Exception (second paragraph):</b> where the direction about one piece of immovable property is meant to secure the beneficial enjoyment of another piece (for example, not to build above one floor so the neighbour keeps light and air), the transferor may enforce it.</li>
<li><b>s.10 vs s.11:</b> s.10 restrains <i>disposal</i>; s.11 restrains <i>enjoyment</i>.</li></ol>""",
dissect=[
("created absolutely in favour of any person","Applies only to an absolute interest."),
("applied or enjoyed by him in a particular manner","A direction on use or enjoyment."),
("as if there were no such direction","The direction is ignored."),
("for the purpose of securing the beneficial enjoyment of another piece of such property","Exception: protecting other land."),
],
master=dict(story="Raghunath gifts Arjun a house absolutely, \"but Arjun must live in it himself and never let it out\". He gives Meera a flat only for her life, with a direction that she must live there personally. He sells the front half of his plot to Kabir and keeps the back half with his own house; the deed says Kabir shall not build above one floor so that Raghunath's house keeps its light. He also gives Kabir a shop absolutely \"to be run only as a sweet shop\". Arjun lets the house to a tenant; Kabir builds three floors and opens a phone shop.",
steps=[
("Arjun's direction to live personally?","Ignored: absolute interest. He may let it out."),
("Meera's life interest direction?","s.11 does not apply (not absolute); the direction can be valid."),
("One-floor limit on Kabir's half?","Enforceable: it protects Raghunath's other land."),
("\"Only a sweet shop\"?","Ignored: absolute interest, and no other land is being protected."),
]),
ills=[
("Absolute gift with use direction","House gifted absolutely; donee must live in it personally.","n","Direction void","Repugnant to an absolute interest."),
("Limited interest","Life interest with the same direction.","y","Can be valid","Not an absolute interest."),
("Protecting other land","No building above one floor to keep light to the transferor's adjoining house.","y","Enforceable","Second paragraph exception."),
],
exam=dict(q="Explain s.11 and distinguish it from s.10.",pts=["Absolute interest plus direction on enjoyment: direction ignored","Exception for directions protecting other land","s.10 disposal vs s.11 enjoyment"],line="Under s.11, where an interest is created absolutely but its enjoyment is directed in a particular manner, the transferee takes as if there were no such direction, except where the direction secures the beneficial enjoyment of other land."),
quiz=[("\"Must live in it himself\" in an absolute gift:",["Binding","Ignored","Makes the gift void"],1,"Repugnant to the absolute interest.")],
links=[("s.10","Restraint on alienation."),("s.40","Obligations restricting use of land, enforceable against transferees with notice.")],
next="Section 12 strikes down forfeiture on insolvency or attempted transfer.")

S['12'] = dict(tag='linked',
simple="A condition that says <span class='hl'>\"you lose it if you go bankrupt\"</span> or <span class='hl'>\"you lose it if you try to sell\"</span> is void. The person keeps the property. Only a landlord's condition in a lease is allowed.",
deep="""<ol>
<li><b>Why:</b> such a clause would hide property from creditors just when they come to collect, and \"lose it if you sell\" is just \"never sell\" in disguise (s.10).</li>
<li><b>Reserved or given:</b> it covers an interest given to someone else and one the transferor keeps for himself. You cannot make your own property creditor-proof.</li>
<li><b>Effect:</b> the condition is void; the interest continues and creditors can reach it.</li>
<li><b>Exception:</b> a condition in a lease for the lessor's benefit (lease ends on the lessee's insolvency or assignment) is valid, matching s.111(g).</li></ol>""",
dissect=[
("reserved or given to or for the benefit of any person","Covers the transferor's own retained interest too."),
("on his becoming insolvent or endeavouring to transfer or dispose of the same","Forfeiture on insolvency or attempted alienation."),
("such condition or limitation is void","The interest continues."),
("Nothing in this section applies to a condition in a lease for the benefit of the lessor","Lease exception."),
],
master=dict(story="Raghunath gifts Kabir a shop \"for life, but if Kabir becomes insolvent his interest shall end and pass to Meera\". He gifts Meera a plot, \"but if she tries to sell it, it goes to Arjun\". He transfers his own farm to a trust, keeping a life interest for himself \"which shall cease if I become insolvent\". He leases a godown to Ramesh, \"lease ends if the lessee becomes insolvent\". Kabir, Raghunath and Ramesh all later become insolvent; Meera tries to sell.",
steps=[
("Kabir's shop?","Condition void; Kabir keeps his life interest, and his creditors can reach it."),
("Meera's plot?","Condition void; she keeps it and may sell."),
("Raghunath's own life interest?","\"Reserved\" interests are covered: the condition is void; his creditors can reach it."),
("Ramesh's lease?","Valid: lease exception for the lessor's benefit."),
]),
ills=[
("Insolvency forfeiture","Gift to B for life, ending if B becomes insolvent.","n","Condition void","Would defeat creditors."),
("Attempted sale forfeiture","Gift ending if the donee tries to sell.","n","Condition void","Back-door restraint on alienation."),
("Reserved interest","Owner keeps a life interest ending on his own insolvency.","n","Condition void","\"Reserved\" is covered."),
("Lease","Lease ends on lessee's insolvency.","y","Valid","Lease exception."),
],
exam=dict(q="Explain s.12.",pts=["Forfeiture on insolvency or attempted alienation is void","Reserved or given","Lease exception"],line="Under s.12, a condition making an interest cease on insolvency or attempted transfer is void, except a lessor's condition in a lease."),
quiz=[("\"Lease ends if tenant becomes insolvent\":",["Void","Valid","Voidable"],1,"Lease exception.")],
links=[("s.10","Absolute restraint on alienation."),("s.31","Conditions subsequent are subject to s.12."),("s.111(g)","Forfeiture of lease.")],
next="Section 13 turns to transfers for the benefit of unborn persons.")
