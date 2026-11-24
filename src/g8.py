S = {}

S['44'] = dict(tag='beyond',
simple="When one <span class='hl'>co-owner sells his share</span>, the buyer steps into his shoes: he gets the seller's right to joint possession and to demand partition, subject to existing burdens. But if the share is in a <span class='hl'>family dwelling house of an undivided family</span> and the buyer is an outsider, he <span class='hl'>cannot move in</span>; he can only sue for partition.",
deep="""<ol><li><b>Transferee steps into the co-owner's shoes:</b> right to joint possession or common enjoyment, and to enforce partition, so far as needed to give effect to the transfer.</li>
<li><b>Subject to</b> the conditions and liabilities affecting the share at the date of transfer.</li>
<li><b>Exception (second paragraph):</b> the transferee of a share in a dwelling-house belonging to an undivided family, who is not a family member, gets no right to joint possession or common enjoyment of the house. \"Undivided family\" means a family that has not divided the house, of any religion. His remedy is a partition suit (and the Partition Act, 1893 s.4 lets family members buy him out).</li></ol>""",
dissect=[("the transferee acquires as to such share or interest","Steps into the co-owner's shoes."),("the transferor's right to joint possession or other common or part enjoyment of the property, and to enforce a partition","Rights acquired."),("subject to the conditions and liabilities affecting at the date of the transfer","Takes with burdens."),("a dwelling-house belonging to an undivided family is not a member of the family","Exception: outsider buying into the family home."),("nothing in this section shall be deemed to entitle him to joint possession","No moving in.")],
master=dict(story="Arjun and Meera co-own (half each) a commercial building and also the undivided family home where both live. Arjun sells his half of the commercial building to Kabir; the building is mortgaged to a bank. Arjun also sells his half of the family home to Suresh, an outsider, who wants to move in.",steps=[("Kabir?","Gets joint possession of the commercial building and can sue for partition, subject to the bank mortgage."),("Suresh?","Cannot claim joint possession of the family dwelling house; he may sue for partition only.")]),
ills=[("Ordinary co-ownership","Buyer of a half share in a shop.","y","Joint possession and partition","First paragraph."),("Family dwelling house","Outsider buys a brother's share in the family home.","n","No joint possession","Second paragraph.")],
exam=dict(q="Explain transfer by one co-owner under s.44.",pts=["Transferee's rights","Subject to burdens","Dwelling-house exception"],line="Under s.44, a transferee of a co-owner's share acquires the transferor's right to joint possession and partition, but an outsider buying a share in an undivided family's dwelling-house gets no right to joint possession."),
quiz=[("An outsider who buys a share in a family dwelling house can:",["Move in","Only sue for partition","Evict the family"],1,"Second paragraph.")],
links=[("s.47","Co-owners transferring a share."),("Partition Act, 1893 s.4","Family members may buy out the stranger.")],
next="Section 45 decides shares when two or more people buy together.")

S['45'] = dict(tag='beyond',
simple="When <span class='hl'>two or more people buy property together</span>: if paid from a common fund, their shares mirror their shares in that fund; if paid from separate money, shares are in proportion to what each paid; if nothing can be proved, <span class='hl'>equal shares</span>.",
deep="<ul><li>Common fund: interests identical, as nearly as may be, to their interests in the fund.</li><li>Separate funds: in proportion to each one's contribution.</li><li>No evidence: presumed equal.</li><li>All subject to a contract to the contrary.</li></ul>",
dissect=[("paid out of a fund belonging to them in common","Common fund."),("in proportion to the shares of the consideration which they respectively advanced","Separate funds."),("shall be presumed to be equally interested in the property","No evidence: equal.")],
master=dict(story="Arjun and Meera buy a flat for ₹60 lakh: Arjun pays ₹40 lakh, Meera ₹20 lakh. Separately, Kabir and Ramesh buy a shop from their joint business account in which Kabir holds 70% and Ramesh 30%. A third property is bought by Arjun and Kabir with no record of who paid what.",steps=[("Flat?","Arjun two-thirds, Meera one-third."),("Shop?","70:30, mirroring the fund."),("Third property?","Presumed equal.")]),
ills=[("Separate funds","₹3 lakh and ₹1 lakh contributions.","m","3:1 shares","s.45."),("No evidence","Unknown contributions.","m","Equal shares","Presumption.")],
exam=dict(q="Short note on joint transfer for consideration.",pts=["Common fund","Separate funds","Presumption of equality"],line="Under s.45, joint purchasers take in proportion to their interests in a common fund or their separate contributions, and are presumed equal in the absence of evidence."),
quiz=[("No evidence of contributions:",["Eldest takes most","Equal shares","Void purchase"],1,"Presumption.")],
links=[("s.46","Sharing the price among joint sellers.")],
next="Section 46 divides the price among joint sellers with different interests.")

S['46'] = dict(tag='beyond',
simple="When <span class='hl'>several people with different interests sell together</span>, the price is shared <span class='hl'>equally</span> if their interests were equal in value, and <span class='hl'>in proportion to value</span> if unequal, unless they agree otherwise.",
deep="<p><b>Act's illustrations:</b> (a) A (half) and B and C (a quarter each) of Sultanpur exchange an eighth share of it for a quarter share of Lalpura; A gets an eighth of Lalpura, B and C a sixteenth each. (b) A has a life interest worth ₹600 and B and C the reversion worth ₹400; on sale for ₹1,000, A gets ₹600 and B and C ₹400.</p><p><i>Note:</i> your Indian Kanoon copy drops \"Lalpura\" from illustration (a).</p>",
dissect=[("persons having distinct interests therein","Different interests."),("share in the consideration equally, where their interests in the property were of equal value","Equal value: equal shares."),("proportionately to the value of their respective interests","Unequal: proportionate.")],
master=dict(story="Raghunath has a life interest in the farm valued at ₹24 lakh; Arjun and Meera hold the reversion valued at ₹36 lakh. They sell the farm together for ₹60 lakh.",steps=[("Division?","Raghunath ₹24 lakh; Arjun and Meera ₹36 lakh between them (₹18 lakh each if their reversionary shares are equal).")]),
ills=[("Life interest and reversion","Life interest worth 60%, reversion 40%.","m","60:40","Illustration (b).")],
exam=dict(q="Short note on s.46.",pts=["Equal value: equal","Unequal: proportionate","Illustrations"],line="Under s.46, joint transferors with distinct interests share the consideration equally if their interests are equal in value, otherwise proportionately."),
quiz=[("Life interest worth ₹600, reversion ₹400, sale for ₹1,000. Life tenant gets:",["₹500","₹600","₹400"],1,"Illustration (b).")],
links=[("s.45","Joint purchase.")],
next="Section 47 decides whose share is reduced when co-owners sell part.")

S['47'] = dict(tag='beyond',
simple="If <span class='hl'>co-owners together sell a share</span> without saying whose share it comes from, it comes from their shares <span class='hl'>equally</span> if equal, otherwise <span class='hl'>proportionately</span>.",
deep="<p><b>Act's illustration:</b> A (eight-anna share) and B and C (four annas each) of Sultanpur transfer a two-anna share to D without specifying; one anna comes from A and half an anna each from B and C. (16 annas = the whole.)</p>",
dissect=[("without specifying that the transfer is to take effect on any particular share","No share named."),("takes effect on such shares equally where the shares were equal","Equal shares."),("proportionately to the extent of such shares","Unequal shares.")],
master=dict(story="Raghunath (50%), Arjun (25%) and Meera (25%) co-own a field and together sell 20% of it to Kabir without saying whose share it comes from.",steps=[("Effect?","10% comes from Raghunath, 5% each from Arjun and Meera. They are left with 40%, 20% and 20%.")]),
ills=[("Statutory","Two-anna share from 8:4:4 holdings.","m","1 : ½ : ½","Illustration.")],
exam=dict(q="Short note on s.47.",pts=["Unspecified share","Proportionate reduction","Illustration"],line="Under s.47, where co-owners transfer a share without specifying from whose share, it takes effect on their shares equally or proportionately."),
quiz=[("50:25:25 co-owners sell 20% unspecified. Reduction:",["Equal 6.67% each","10:5:5","All from the largest"],1,"Proportionate.")],
links=[("s.44","One co-owner transferring.")],
next="Section 49 gives the buyer a claim on fire-insurance money.")

S['48'] = dict(tag='beyond',
simple="If the same owner creates <span class='hl'>rights over the same property at different times</span> and they cannot all fully exist together, the <span class='hl'>earlier right wins</span> (first in time, first in right), unless there is a special contract or reservation binding the earlier transferee.",
deep="<p>The maxim <i>qui prior est tempore, potior est jure</i>. Each later right is subject to rights already created. A later transferee cannot be better off simply because he is later. Registration and notice rules (s.3 Explanation I) help later buyers discover earlier rights.</p>",
dissect=[("rights in or over the same immoveable property","Competing rights."),("such rights cannot all exist or be exercised to their full extent together","Conflict."),("each later created right shall","Later rights are subordinate."),("in the absence of a special contract or reservation binding the earlier transferees","Exception.")],
master=dict(story="Raghunath mortgages his farm to Bank A in January, then to Bank B in March, then leases it to Kabir in June. The farm is worth less than both loans.",steps=[("Priority?","Bank A first, then Bank B; Kabir's lease is subject to both mortgages."),("Exception?","If Bank A had agreed in writing to rank after Bank B, that special contract would bind Bank A.")]),
ills=[("First in time","Two mortgages of the same land.","m","Earlier ranks first","s.48."),("Special contract","Earlier mortgagee agrees to postpone.","y","Later ranks first","Exception.")],
exam=dict(q="Short note on priority under s.48.",pts=["First in time, first in right","Later rights subject to earlier","Special contract or reservation"],line="Under s.48, where rights created at different times over the same property cannot co-exist fully, each later right is subject to the earlier ones, absent a special contract or reservation."),
quiz=[("Two mortgages of the same land; the earlier ranks:",["Second","First","Equally"],1,"s.48.")],
links=[("s.3","Notice and registration."),("s.78","Postponement of prior mortgagee.")],
next="Section 50 protects tenants who pay rent in good faith to the wrong person.")

S['49'] = dict(tag='beyond',
simple="If property sold for value was <span class='hl'>insured against fire</span> at the date of sale and is then damaged by fire, the buyer can require that the <span class='hl'>insurance money actually received by the seller</span> be used to <span class='hl'>reinstate the property</span>, unless agreed otherwise.",
deep="<ul><li>Transfer for consideration.</li><li>Property insured against fire at the date of transfer.</li><li>Loss or damage by fire.</li><li>Transferee may require the money the transferor actually receives (or what is needed) to be applied to reinstatement.</li><li>Subject to contract to the contrary.</li></ul>",
dissect=[("at the date of the transfer insured against loss or damage by fire","Insured at transfer."),("any money which the transferor actually receives under the policy","Money actually received."),("to be applied in reinstating the property","Reinstatement.")],
master=dict(story="Raghunath sells his rice mill to Kabir; the policy is still in Raghunath's name. A fire damages the mill; the insurer pays Raghunath ₹15 lakh.",steps=[("Kabir's right?","He can require the ₹15 lakh (or what is needed) to be spent on reinstating the mill.")]),
ills=[("Fire after sale","Insurer pays the seller.","y","Buyer can demand reinstatement","s.49.")],
exam=dict(q="Short note on s.49.",pts=["Insurance at transfer","Fire loss","Reinstatement"],line="Under s.49, the transferee of insured immovable property may require insurance money actually received by the transferor for fire damage to be applied in reinstating the property."),
quiz=[("s.49 covers loss by:",["Theft","Fire","Flood"],1,"Fire only.")],
links=[("s.135","Assignment of fire insurance policies.")],
next="Section 52 sets out the doctrine of lis pendens.")

S['50'] = dict(tag='beyond',
simple="If a tenant <span class='hl'>pays rent in good faith</span> to the person he held from, he is <span class='hl'>not liable to pay again</span> even if that person later turns out to have had no right to it.",
deep="<p><b>Act's illustration:</b> A lets a field to B at ₹50 rent and then transfers it to C. B, with no notice of the transfer, pays the rent to A in good faith. B is not liable to pay it again to C.</p>",
dissect=[("in good faith paid or delivered to any person of whom he in good faith held such property","Good faith payment to the person he held from."),("had no right to receive such rents or profits","Even if that person had no right."),("B is not chargeable with the rent so paid","Illustration.")],
master=dict(story="Ramesh rents a shop from Raghunath. Raghunath sells it to Kabir on 1 April but tells no one. Ramesh pays April and May rent to Raghunath. Kabir writes to Ramesh on 1 June; Ramesh still pays June rent to Raghunath.",steps=[("April and May?","Protected: paid in good faith without notice."),("June?","Not protected: Ramesh had notice of the transfer.")]),
ills=[("No notice","Tenant pays the old landlord.","y","Discharged","s.50."),("With notice","Tenant pays the old landlord after being told of the sale.","n","Not protected","No good faith.")],
exam=dict(q="Short note on s.50.",pts=["Good faith payment","No double liability","Illustration"],line="Under s.50, no person is chargeable with rents or profits paid in good faith to the person from whom he held the property, though that person had no right to receive them."),
quiz=[("Tenant pays old landlord before learning of the sale:",["Must pay again","Is discharged","Pays half again"],1,"s.50.")],
links=[("s.36","Apportionment of rent."),("s.3","Notice.")],
next="Section 51 compensates honest holders who improved property under a defective title.")

S['51'] = dict(tag='beyond',
simple="If a transferee <span class='hl'>improves property believing in good faith he is the absolute owner</span>, and is later evicted by someone with a better title, he can make the true owner either <span class='hl'>pay the value of the improvement</span> or <span class='hl'>sell him the property</span> at market value ignoring the improvement. He can also take his growing crops.",
deep="""<ol><li><b>Conditions:</b> a transferee; makes an improvement; believing in good faith he is absolutely entitled; is evicted by a person with a better title.</li>
<li><b>Option of the evicted transferee:</b> require the evictor (a) to pay or secure the estimated value of the improvement, or (b) to sell his interest to the transferee at the then market value, ignoring the improvement.</li>
<li><b>Value</b> is assessed at the time of eviction.</li>
<li><b>Crops:</b> crops he planted or sowed and still growing at eviction are his, with free entry and exit to gather them.</li></ol>
<p><i>Note:</i> your Indian Kanoon copy drops \"is\" and \"his\" in this section; restored here.</p>""",
dissect=[("believing in good faith that he is absolutely entitled thereto","Good faith belief in absolute title."),("evicted therefrom by any person having a better title","Eviction by true owner."),("to have the value of the improvement estimated and paid or secured","Option (a)."),("to sell his interest in the property to the transferee at the then market value thereof, irrespective of the value of such improvement","Option (b)."),("he is entitled to such crops and to free ingress and egress to gather and carry them","Growing crops.")],
master=dict(story="Kabir buys a plot from Suresh, honestly believing Suresh's title is good. He builds a ₹20 lakh warehouse and sows sugarcane. Meera proves she is the true owner and evicts him. At eviction the warehouse is worth ₹18 lakh and the bare land ₹30 lakh.",steps=[("Kabir's options?","Require Meera to pay ₹18 lakh (value at eviction), or require her to sell him the land for ₹30 lakh."),("Sugarcane?","His, with free access to harvest it.")]),
ills=[("Good faith","Buyer improves, honestly believing he owns.","y","Compensation or purchase option","s.51."),("Bad faith","Buyer knew of the dispute and still built.","n","No protection","Good faith missing.")],
exam=dict(q="Short note on improvements by bona fide holders (s.51).",pts=["Conditions","Two options","Value at eviction","Growing crops"],line="Under s.51, a transferee who improves property believing in good faith he is absolutely entitled, and is evicted by a better title, may require the evictor to pay the value of the improvement or sell him the property at market value without it."),
quiz=[("The improvement is valued at:",["Cost of building","Time of eviction","Date of purchase"],1,"s.51.")],
links=[("s.41","Ostensible owner."),("s.43","Feeding the grant.")],
next="Next come the co-owner rules: Section 44 says what the buyer of one co-owner's share gets.")
