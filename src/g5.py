S = {}

S['25'] = dict(tag='syllabus',
simple="A transfer that depends on a condition <span class='hl'>fails</span> if the condition is <span class='hl'>impossible, illegal, would defeat a law, fraudulent, harmful to another person or property, immoral or against public policy</span>.",
deep="""<p>This section deals with conditions <b>precedent</b> (to be fulfilled before the interest arises). If such a condition is bad, the <b>whole interest fails</b>, because the interest was never meant to arise without it.</p>
<ol>
<li><b>Impossible</b>: \"walk a hundred miles in an hour\"; or impossible on the facts (\"marry my daughter C\" when C is already dead).</li>
<li><b>Forbidden by law</b>: \"commit a crime\".</li>
<li><b>Would defeat the provisions of any law</b>: a condition designed to get round a statute.</li>
<li><b>Fraudulent</b>: a condition to deceive creditors.</li>
<li><b>Involves or implies injury to the person or property of another</b>.</li>
<li><b>Immoral or opposed to public policy</b>, as the court regards it: \"desert your husband\".</li></ol>
<p><b>Contrast:</b> a bad condition <i>subsequent</i> (one that would take away an interest already given) is simply ignored and the interest stays (s.30, s.32). Under s.25 the interest itself fails.</p>""",
dissect=[
("dependent upon a condition","A condition precedent."),
("the fulfilment of the condition is impossible","Impossible conditions."),
("is forbidden by law","Illegal conditions."),
("it would defeat the provisions of any law","Conditions that evade a law."),
("is fraudulent","Fraudulent conditions."),
("involves or implies injury to the person or property of another","Harm to others."),
("immoral or opposed to public policy","Court's judgment on morality and policy."),
],
master=dict(story="Raghunath makes five promises. (1) A farm lease to Kabir \"on condition he walks 100 miles in an hour\". (2) ₹5 lakh to Ramesh \"on condition he marries my granddaughter Asha\"; unknown to Raghunath, Asha died last month. (3) A plot to Suresh \"on condition he burns down his rival's shop\". (4) ₹2 lakh to his niece \"if she leaves her husband\". (5) A house to Arjun \"on condition he transfers his assets to his wife's name so that his creditors cannot reach them\".",
steps=[("(1)?","Fails: physically impossible."),("(2)?","Fails: impossible at the date of transfer (Asha is dead)."),("(3)?","Fails: forbidden by law and injures another's property."),("(4)?","Fails: immoral / against public policy."),("(5)?","Fails: fraudulent and meant to defeat creditors.")]),
ills=[
("Impossible","Gift on condition the donee touches the sky.","n","Fails","Impossible."),
("Illegal","Gift on condition the donee sells drugs.","n","Fails","Forbidden by law."),
("Against public policy","Gift on condition the donee never marries anyone.","n","Generally fails","Courts treat total restraint of marriage as against public policy."),
("Valid condition","Gift on condition the donee completes a law degree.","y","Valid","Possible and lawful."),
],
exam=dict(q="Explain conditional transfer and invalid conditions under s.25.",pts=["Condition precedent","Six kinds of invalid condition with the Act's illustrations","Effect: interest fails","Contrast with conditions subsequent (s.30, s.32)"],line="Under s.25, an interest dependent on a condition fails if the condition is impossible, illegal, would defeat a law, is fraudulent, injures another, or is immoral or against public policy."),
quiz=[("\"Marry my daughter C\" when C is already dead:",["Valid","Fails as impossible","Valid after C's death"],1,"Act's illustration (b).")],
links=[("Contract Act s.23","Similar tests for unlawful object."),("s.26","Fulfilment of condition precedent."),("s.30, s.32","Invalid conditions subsequent.")],
next="Section 26 says how strictly a valid condition precedent must be fulfilled.")

S['26'] = dict(tag='syllabus',
simple="A condition <span class='hl'>before</span> getting property (condition precedent) is treated as fulfilled if it is <span class='hl'>substantially complied with</span>. This is the <span class='hl'>doctrine of cy-près</span> (as near as possible).",
deep="""<ol>
<li><b>Condition precedent:</b> must be satisfied before the interest arises.</li>
<li><b>Substantial compliance</b> is enough: the spirit and main purpose of the condition, not every literal detail.</li>
<li><b>Cy-près</b> (French: \"as near as possible\"): if exact performance is impossible for reasons beyond the person, doing it as nearly as possible counts.</li>
<li><b>Limits:</b> substantial compliance must happen in substance <i>before</i> the interest is claimed; a condition that required prior consent is not satisfied by consent taken afterwards.</li>
<li><b>Contrast:</b> conditions subsequent (s.29) need strict fulfilment.</li></ol>
<p><b>Act's illustrations:</b> (a) marry with consent of C, D and E; E dies; marrying with consent of C and D fulfils it. (b) Marrying without consent and getting it afterwards does not.</p>""",
dissect=[("a condition to be fulfilled before a person can take an interest","Condition precedent."),("if it has been substantially complied with","Cy-près: substantial compliance is enough."),("B is deemed to have fulfilled the condition","Illustration (a)."),("B has not fulfilled the condition","Illustration (b): consent after the event is not enough.")],
master=dict(story="Raghunath gives Kabir ₹5 lakh \"on condition he marries with the consent of Raghunath, Arjun and Meera\". Meera dies before the wedding. Kabir marries with the consent of Raghunath and Arjun. In a second gift, Raghunath gives Ramesh ₹2 lakh on the same type of condition; Ramesh marries secretly and obtains all three consents a week later. In a third, Raghunath gives Arjun a plot \"on condition he plants 100 mango saplings on it\"; Arjun plants 97 and 3 die in a flood before he can replace them.",
steps=[("Kabir?","Condition fulfilled: substantial compliance (Meera's death made her consent impossible)."),("Ramesh?","Not fulfilled: consent obtained after marriage is not compliance (illustration (b))."),("Arjun?","Substantially complied with: the purpose is achieved as near as possible.")]),
ills=[("Substantial","One of three consents becomes impossible by death.","y","Fulfilled","Illustration (a)."),("After the event","Consent after marriage.","n","Not fulfilled","Illustration (b)."),("Near enough","97 of 100 saplings planted, 3 lost to flood.","y","Fulfilled","Cy-près.")],
exam=dict(q="Explain the doctrine of cy-près under s.26.",pts=["Condition precedent","Substantial compliance","Both illustrations","Contrast with s.29 strict compliance"],line="Under s.26, a condition precedent is deemed fulfilled if substantially complied with (doctrine of cy-près)."),
quiz=[("Condition precedent requires:",["Strict compliance","Substantial compliance","No compliance"],1,"s.26.")],
links=[("s.29","Strict compliance for conditions subsequent."),("s.25","Invalid conditions.")],
next="Section 27 explains what happens to a back-up gift when the first gift fails.")

S['27'] = dict(tag='syllabus',
simple="\"To B, and if that fails, to C.\" If B's gift fails <span class='hl'>in any manner</span>, C's gift takes effect, even if it failed differently from what was planned. This is the <span class='hl'>doctrine of acceleration</span>. But if the deed meant C to take only on one particular kind of failure, C takes only if it fails that way.",
deep="""<ol>
<li><b>Prior and ulterior disposition</b> in the same transaction.</li>
<li><b>General rule:</b> if the prior disposition fails, the ulterior one takes effect, \"although the failure may not have occurred in the manner contemplated\". The ulterior gift is accelerated.</li>
<li><b>Exception:</b> if the intention was that the ulterior gift should take effect only on failure in a particular manner, it takes effect only if the failure happens that way.</li></ol>
<p><b>Act's illustrations:</b> (a) ₹500 to B on condition he executes a lease within three months after A's death, and if he neglects, to C; B dies in A's lifetime; C takes. (b) Property to A's wife, but if she dies in his lifetime, to B; A and his wife die together and it cannot be proved she died first; B does not take.</p>""",
dissect=[("an ulterior disposition of the same interest is made in favour of another","Back-up gift in the same transaction."),("although the failure may not have occurred in the manner contemplated by the transferor","Acceleration: any failure triggers it."),("shall not take effect unless the prior disposition fails in that manner","Exception: a particular manner was intended.")],
master=dict(story="Raghunath gives Arjun ₹10 lakh \"on condition he builds a school within one year of my death; if he neglects to do so, to Meera\". Arjun dies before Raghunath. Separately Raghunath gives his house to his wife, \"but if she dies in my lifetime, to Kabir\". Raghunath and his wife die together in a car crash and no one can tell who died first.",
steps=[("Arjun dies before he could neglect anything. Does Meera take?","Yes: the prior gift failed, though not by neglect; s.27 accelerates Meera's gift (illustration (a))."),("House: does Kabir take?","No: Kabir was to take only if the wife died in Raghunath's lifetime, which cannot be proved (illustration (b)).")]),
ills=[("Failure in another manner","Prior gift fails by death rather than the planned breach.","y","Ulterior gift takes effect","Acceleration."),("Particular manner required","Gift over only if wife predeceases; simultaneous death unproven.","n","Ulterior gift fails","Exception.")],
exam=dict(q="Explain the doctrine of acceleration under s.27.",pts=["Prior and ulterior disposition","Takes effect on any failure","Exception for particular manner","Both illustrations"],line="Under s.27, where a prior disposition fails, the ulterior disposition takes effect though the failure is not in the manner contemplated, unless it was intended to take effect only on failure in a particular manner."),
quiz=[("B dies before the condition could be broken; C was the back-up:",["C takes","C does not take","B's heirs take"],0,"Illustration (a).")],
links=[("s.28","Conditional gift over."),("s.30","Invalid ulterior disposition does not affect the prior one.")],
next="Section 28 allows gifts that shift to another person on an uncertain event.")

S['28'] = dict(tag='syllabus',
simple="You can give property to one person with a condition that <span class='hl'>if an uncertain event happens (or does not happen), it shifts to another person</span>. Such gifts must obey s.10, 12, 21, 22, 23, 24, 25 and 27.",
deep="<p>This creates a <b>condition subsequent</b> with a gift over: B gets the interest now, but it will pass to C on the specified event. The gift over is tested by the listed sections (no absolute restraint, no insolvency forfeiture, contingency rules, validity of conditions, acceleration).</p>",
dissect=[("in case a specified uncertain event shall happen such interest shall pass to another person","Gift over on an event happening."),("in case a specified uncertain event shall not happen such interest shall pass to another person","Gift over on an event not happening."),("subject to the rules contained in sections 10, 12, 21, 22, 23, 24, 25 and 27","Tested by these rules.")],
master=dict(story="Raghunath gives Arjun a farm, \"but if Arjun stops farming it for three years, it shall pass to Meera\"; and gives Kabir a shop, \"but if Kabir ever sells it, it shall pass to Ramesh\".",steps=[("Farm gift over?","Valid: a lawful uncertain event."),("Shop gift over on sale?","Void: it is a forfeiture on attempted alienation, hit by s.10 and s.12.")]),
ills=[("Lawful event","Passes to C if B leaves the village permanently.","y","Valid","s.28."),("Restraint in disguise","Passes to C if B sells.","n","Void","Subject to s.10 and s.12.")],
exam=dict(q="Explain s.28.",pts=["Gift over on happening or not happening of uncertain event","Subject to listed sections"],line="Under s.28, an interest may be given with a condition that on a specified uncertain event it shall pass to another, subject to s.10, 12, 21 to 25 and 27."),
quiz=[("\"Passes to C if B sells\":",["Valid","Void under s.10/12","Valid under s.28"],1,"Subject to s.10 and s.12.")],
links=[("s.29","Strict fulfilment."),("s.10, s.12","Limits on such conditions.")],
next="Section 29 says a gift over of this kind needs strict fulfilment.")

S['29'] = dict(tag='syllabus',
simple="A gift over under s.28 (a condition that takes property away from one and gives it to another) takes effect <span class='hl'>only if the condition is strictly fulfilled</span>.",
deep="""<ul><li>Conditions subsequent divest an interest already given, so the law reads them strictly.</li>
<li>Contrast s.26: conditions precedent need only substantial compliance.</li>
<li><b>Act's illustration:</b> ₹500 to B, payable on majority or marriage; if B dies a minor or marries without C's consent, to D. B marries at 17 without C's consent: the transfer to D takes effect, because the condition (marriage without consent while a minor) is strictly fulfilled.</li></ul>""",
dissect=[("cannot take effect unless the condition is strictly fulfilled","Strict fulfilment."),("The transfer to D takes effect","Illustration.")],
master=dict(story="Raghunath gives Arjun a farm, \"but if Arjun leaves India to live permanently abroad, the farm shall pass to Meera\". Arjun first takes a two-year job in Dubai, keeping his Cuttack home and returning every Diwali. Later he sells his Cuttack home and emigrates to Canada with his family as a permanent resident.",steps=[("Dubai job?","Not strictly fulfilled: he did not leave to live permanently abroad. Meera cannot claim."),("Canada?","Strictly fulfilled: the gift over to Meera takes effect."),("Lesson","A condition subsequent is read exactly; near enough is not enough (contrast s.26).")]),
ills=[("Strict","Statutory illustration: B marries at 17 without consent.","y","Gift to D takes effect","Strictly fulfilled."),("Not strictly","Condition is \"if B leaves India\"; B goes to Nepal for a week and returns.","n","Gift over fails","Not strictly fulfilled.")],
exam=dict(q="Distinguish condition precedent and condition subsequent.",pts=["s.26 substantial vs s.29 strict","Precedent: before interest arises; subsequent: divests","Illustrations"],line="Under s.29, an ulterior disposition under s.28 cannot take effect unless the condition is strictly fulfilled."),
quiz=[("Condition subsequent requires:",["Substantial","Strict","No"],1,"s.29.")],
links=[("s.26","Contrast."),("s.28","Gift over.")],
next="Section 30 protects the first gift if the gift over is invalid.")

S['30'] = dict(tag='syllabus',
simple="If the <span class='hl'>later (ulterior) gift is invalid</span>, the <span class='hl'>earlier gift still stands</span>, free of the bad condition.",
deep="<p><b>Act's illustration:</b> a farm to B for her life, and if she do not desert her husband, to C. The condition is immoral, so C's gift is invalid; B keeps the farm for life as if no condition had been inserted.</p>",
dissect=[("If the ulterior disposition is not valid, the prior disposition is not affected by it","The first gift survives."),("as if no condition had been inserted","Illustration.")],
master=dict(story="Raghunath gives Meera a flat for life, \"and if she does not leave her husband, then to Kabir\".",steps=[("Kabir's gift?","Invalid: immoral condition."),("Meera's life interest?","Unaffected: she holds for life.")]),
ills=[("Statutory","Farm to B for life; to C if B does not desert her husband.","y","B keeps for life","s.30.")],
exam=dict(q="Explain s.30.",pts=["Invalid ulterior disposition","Prior disposition unaffected"],line="Under s.30, if the ulterior disposition is not valid, the prior disposition is not affected by it."),
quiz=[("Gift over void; the first gift:",["Fails","Stands","Becomes conditional"],1,"s.30.")],
links=[("s.25","Invalid conditions."),("s.32","Lawful conditions only.")],
next="Section 31 allows conditions that end an interest.")

S['31'] = dict(tag='syllabus',
simple="You can give an interest with a condition that it <span class='hl'>ends</span> if an uncertain event happens (or does not happen), subject to s.12.",
deep="""<ul><li>A condition subsequent that cuts an interest short, without a gift over to another person (the interest then returns to the transferor).</li>
<li>Subject to s.12: it cannot be insolvency or attempted alienation.</li>
<li><b>Act's illustrations:</b> (a) farm to B for life, ceasing if he cuts down a certain wood; B cuts it; he loses his life interest. (b) Farm to B, ceasing if he does not go to England within three years; he does not; his interest ceases.</li></ul>""",
dissect=[("Subject to the provisions of section 12","No forfeiture on insolvency or alienation."),("it shall cease to exist in case a specified uncertain event shall happen","Interest ends on event."),("in case a specified uncertain event shall not happen","Or on event not happening.")],
master=dict(story="Raghunath gives Arjun the farm for life, \"ceasing if he cuts down the old banyan grove\", and gives Kabir a shop, \"ceasing if he does not open it within one year\", and gives Meera a plot, \"ceasing if she becomes insolvent\". Arjun cuts the grove; Kabir never opens the shop; Meera becomes insolvent.",steps=[("Arjun?","Loses his life interest (illustration (a))."),("Kabir?","His interest ceases after one year (illustration (b))."),("Meera?","The condition is void under s.12; she keeps the plot.")]),
ills=[("Event happens","Life interest ceasing if B cuts the wood.","y","Ceases","Illustration (a)."),("Event fails","Interest ceasing if B does not go abroad in 3 years.","y","Ceases","Illustration (b)."),("Insolvency","Interest ceasing on insolvency.","n","Condition void","Subject to s.12.")],
exam=dict(q="Explain s.31 with illustrations.",pts=["Condition subsequent ending interest","Subject to s.12","Illustrations"],line="Under s.31, subject to s.12, an interest may be created with a condition that it shall cease on a specified uncertain event happening or not happening."),
quiz=[("Interest ceasing on insolvency:",["Valid","Void under s.12","Voidable"],1,"Subject to s.12.")],
links=[("s.12","Limit."),("s.32","The condition must be lawful.")],
next="Section 32 requires such a condition to be lawful.")

S['32'] = dict(tag='syllabus',
simple="A condition that ends an interest is valid only if the event is one that could <span class='hl'>lawfully be a condition for creating</span> an interest.",
deep="<p>The tests of s.25 apply to conditions subsequent too: an impossible, illegal, immoral or fraudulent ending-condition is invalid. The difference: an invalid ending-condition is simply struck out and the interest remains (unlike s.25, where the interest fails).</p>",
dissect=[("be one which could legally constitute the condition of the creation of an interest","Same lawfulness test as s.25.")],
master=dict(story="Raghunath gives Meera a house, \"ceasing if she visits her brother Arjun\", and gives Kabir a shop, \"ceasing if he does not commit a fraud on the bank within a year\".",steps=[("Meera?","Condition likely against public policy (restraining family relations): struck out; she keeps the house."),("Kabir?","Illegal condition: struck out; he keeps the shop.")]),
ills=[("Unlawful ending-condition","Interest ceasing unless the holder commits a crime.","n","Condition void, interest stays","s.32.")],
exam=dict(q="Explain s.32.",pts=["Ending-condition must be lawful","Invalid one is struck out"],line="Under s.32, a condition that an interest shall cease is valid only if its event could legally be the condition of creating an interest."),
quiz=[("Invalid condition subsequent:",["Destroys the interest","Is struck out; interest stays","Makes the deed void"],1,"s.32 with s.30.")],
links=[("s.25","Same tests."),("s.31","Ending-conditions.")],
next="Section 33 deals with conditions requiring an act where no time is fixed.")

S['33'] = dict(tag='syllabus',
simple="If an interest depends on the person <span class='hl'>doing an act</span> and <span class='hl'>no time is fixed</span>, the condition is broken only when he makes the act <span class='hl'>impossible</span>, permanently or indefinitely.",
deep="<p>With no deadline, he can perform at any time; the condition is broken only by his own conduct making performance impossible (for example, destroying the thing or putting it permanently out of reach).</p>",
dissect=[("no time is specified for the performance of the act","No deadline."),("the condition is broken when he renders impossible, permanently or for an indefinite period, the performance of the act","Broken only by his making it impossible.")],
master=dict(story="Raghunath gives Arjun a plot \"on condition he restores the old temple on it\", fixing no time. Ten years pass without restoration. Then Arjun sells the temple stones to a builder who removes them abroad.",steps=[("Ten years of inaction?","Not broken: no time was fixed."),("Selling the stones abroad?","Broken: he has made performance impossible.")]),
ills=[("Delay","No time fixed; act not yet done.","y","Not broken","s.33."),("Impossibility","He destroys the means of doing the act.","n","Broken","s.33.")],
exam=dict(q="Explain s.33.",pts=["Act with no time fixed","Broken only by rendering it impossible"],line="Under s.33, where no time is fixed for an act forming a condition, it is broken when the person renders performance impossible permanently or indefinitely."),
quiz=[("No time fixed; act not done yet:",["Broken","Not broken","Void"],1,"s.33.")],
links=[("s.34","Fraud preventing performance.")],
next="Section 34 deals with fraud by someone who benefits from the act not being done.")

S['34'] = dict(tag='syllabus',
simple="If someone who <span class='hl'>benefits from the condition failing</span> uses <span class='hl'>fraud</span> to stop the act: where a time was fixed, <span class='hl'>extra time</span> is given against him; where no time was fixed and the act is made impossible or indefinitely postponed, the condition is <span class='hl'>treated as fulfilled</span> against him.",
deep="""<ol><li>Applies to acts that are a condition precedent to enjoyment, or a condition whose non-fulfilment passes the interest to another.</li>
<li><b>Time specified + fraud</b> by the person directly benefited by non-fulfilment: as against him, extra time equal to the delay caused.</li>
<li><b>No time specified + fraud</b> making performance impossible or indefinitely postponed: as against him, the condition is deemed fulfilled.</li>
<li>Nobody may profit from his own fraud.</li></ol>""",
dissect=[("prevented by the fraud of a person who would be directly benefited by non-fulfilment of the condition","Fraud by the person who gains."),("such further time shall as against him be allowed","Time fixed: extra time."),("the condition shall as against him be deemed to have been fulfilled","No time fixed: deemed fulfilled.")],
master=dict(story="Raghunath gives Kabir ₹10 lakh \"if he passes the judicial service exam by December 2027; otherwise to Suresh\". Suresh steals Kabir's admit card, so Kabir misses the June 2027 attempt; the next attempt is in March 2028. In a second gift with no time limit, Raghunath gives Ramesh a shop \"on condition he marries Priya; otherwise to Suresh\"; Suresh fraudulently persuades Priya's family she has emigrated for good, so the marriage becomes indefinitely postponed.",steps=[("First gift?","Time fixed and fraud by Suresh, who benefits: as against Suresh, Kabir gets extra time to make up the delay."),("Second gift?","No time fixed; fraud made performance indefinitely postponed: as against Suresh, the condition is deemed fulfilled; Ramesh takes.")]),
ills=[("Time fixed","Beneficiary's fraud delays the act by 6 months.","y","6 months extra against him","s.34 para 1."),("No time fixed","Beneficiary's fraud makes the act impossible.","y","Deemed fulfilled against him","s.34 para 2.")],
exam=dict(q="Explain s.34.",pts=["Fraud by person benefited","Time fixed: extra time","No time: deemed fulfilled"],line="Under s.34, where performance of a conditional act is prevented by the fraud of a person benefited by its non-fulfilment, further time is allowed against him, or, if no time is fixed, the condition is deemed fulfilled against him."),
quiz=[("No time fixed; beneficiary's fraud makes the act impossible:",["Condition broken","Deemed fulfilled against him","Gift void"],1,"s.34.")],
links=[("s.33","Act with no time fixed.")],
next="Section 35 sets out the doctrine of election.")
