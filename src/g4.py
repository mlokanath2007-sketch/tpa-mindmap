S = {}

S['19'] = dict(tag='syllabus',
simple="A <span class='hl'>vested interest</span> is a right that is <span class='hl'>fixed and certain now</span>, even if enjoyment comes later. \"You WILL get it.\" If the holder dies before getting possession, it passes to his heirs.",
deep="""<ol>
<li><b>When an interest is vested:</b> (a) no time is specified for it to take effect, or (b) it is to take effect forthwith, or (c) it is to take effect on an event that <i>must</i> happen (such as someone's death). Unless a contrary intention appears.</li>
<li><b>Not defeated by death:</b> if the transferee dies before possession, the interest goes to his heirs or legatees.</li>
<li><b>Transferable and heritable:</b> it can be sold or passed on even before possession.</li>
<li><b>Explanation:</b> an intention that the interest is not vested is NOT to be inferred merely from: (i) enjoyment being postponed, (ii) a prior interest given or reserved to someone else, (iii) income being directed to accumulate until enjoyment, or (iv) a provision that if an event happens the interest will pass to another (a gift over).</li>
<li><b>Vested in interest vs vested in possession:</b> vested in interest = right fixed now, enjoyment later; vested in possession = right fixed and enjoyed now.</li></ol>""",
dissect=[
("without specifying the time when it is to take effect","No time stated: vested."),
("to take effect forthwith","Immediately: vested."),
("on the happening of an event which must happen","A certain event (death): vested."),
("unless a contrary intention appears from the terms of the transfer","The deed may say otherwise."),
("A vested interest is not defeated by the death of the transferee before he obtains possession","Passes to heirs."),
("the enjoyment thereof is postponed","Postponed enjoyment does not prevent vesting."),
("a prior interest in the same property is given or reserved to some other person","A prior life interest does not prevent vesting."),
("income arising from the property is directed to be accumulated","Accumulation does not prevent vesting."),
("if a particular event shall happen the interest shall pass to another person","A gift over does not prevent vesting."),
],
master=dict(story="Raghunath's deed: \"My farm to Arjun for life, and after Arjun's death to Rohan. Until Arjun dies, the surplus income shall be saved and handed to Rohan with the farm. If Rohan ever moves abroad permanently, the farm shall go to Meera.\" Rohan is 20 when the deed is signed. Rohan sells his interest to Kabir in 2028. Rohan dies in 2030; Arjun dies in 2035.",
steps=[("Is Rohan's interest vested?","Yes: it takes effect on Arjun's death, an event which must happen."),("Does postponed enjoyment, Arjun's prior life interest, accumulation or the Meera gift-over make it contingent?","No: the Explanation says none of these alone shows an intention against vesting."),("Rohan's sale to Kabir in 2028?","Valid: a vested interest is transferable."),("Rohan dies before Arjun?","Not defeated: whatever Rohan still held would go to his heirs; here Kabir, as transferee, takes on Arjun's death in 2035 (subject to the Meera gift-over clause, which never operated).")]),
ills=[
("No time stated","\"My shop to Kabir.\"","y","Vested","No time specified."),
("Certain event","\"To Rohan after Arjun's death.\"","y","Vested","Death must happen."),
("Death before possession","Rohan dies before Arjun; the gift was vested.","y","Goes to Rohan's heirs","Not defeated by death."),
("Postponed enjoyment","\"To Rohan, possession at 25\", vested now.","y","Vested","Postponement alone does not prevent vesting."),
("Gift over","\"To Rohan; if he moves abroad, to Meera.\"","y","Vested in Rohan, subject to divesting","A gift-over clause does not prevent vesting."),
("Contrary intention","\"To Rohan only if he survives Arjun.\"","n","Not vested","Survival is uncertain: contingent."),
],
exam=dict(q="Distinguish between vested and contingent interest. (10 marks)",
pts=["s.19 definition: no time, forthwith, or certain event","Not defeated by death; transferable and heritable","Explanation: four things that do not prevent vesting","Contrast table with s.21","s.20 for unborn persons"],
line="Under s.19, an interest is vested where it is to take effect without stated time, forthwith, or on an event that must happen, and it is not defeated by the transferee's death before possession."),
quiz=[("\"To C after B's death\" gives C:",["A contingent interest","A vested interest","No interest"],1,"Death must happen."),("A vested holder dies before possession. The interest:",["Fails","Goes to his heirs","Returns to the transferor"],1,"Not defeated by death.")],
links=[("s.21","Contingent interest."),("s.20","Unborn person vests on birth."),("s.6(a)","Contrast: spes successionis is not an interest at all.")],
next="Section 21 defines the opposite: a contingent interest.")

S['21'] = dict(tag='syllabus',
simple="A <span class='hl'>contingent interest</span> depends on an <span class='hl'>uncertain event</span> happening or not happening. \"You MAY get it, IF…\" It becomes vested when the event happens (or becomes impossible). If the holder dies before that, it fails.",
deep="""<ol>
<li><b>Two forms:</b> takes effect only (a) if a specified uncertain event happens (\"if Rohan becomes a lawyer\"), or (b) if a specified uncertain event does not happen (\"if Rohan does not marry before 21\").</li>
<li><b>Becomes vested:</b> in (a) when the event happens; in (b) when the event becomes impossible.</li>
<li><b>Death before the event:</b> the interest fails; nothing passes to the heirs.</li>
<li><b>Still a real right:</b> it can be transferred (unlike spes successionis).</li>
<li><b>Exception:</b> where a person is to get an interest on attaining an age, and the transferor also gives him the income absolutely before that age, or directs the income (or what is needed) to be applied for his benefit, the interest is <i>not</i> contingent; it is vested.</li></ol>
<table class="cmp"><tr><th></th><th>Vested (s.19)</th><th>Contingent (s.21)</th></tr><tr><td>Right</td><td>Fixed now</td><td>Depends on uncertain event</td></tr><tr><td>Death before possession</td><td>Goes to heirs</td><td>Fails</td></tr><tr><td>Example</td><td>To C after B's death</td><td>To C if he turns 18 / becomes a lawyer</td></tr></table>""",
dissect=[
("only on the happening of a specified uncertain event","Form (a): if something happens."),
("if a specified uncertain event shall not happen","Form (b): if something does not happen."),
("on the happening of the event","(a) vests when it happens."),
("when the happening of the event becomes impossible","(b) vests when it can no longer happen."),
("the transferor also gives to him absolutely the income","Exception: income given before the age."),
("such interest is not contingent","Then it is vested."),
],
master=dict(story="Raghunath signs three gifts. Gift 1: a plot \"to Rohan if he becomes an advocate\". Gift 2: a shop \"to Meera if she does not marry before 25\". Gift 3: a farm \"to Kabir's son when he turns 18; until then the farm income is his, to be spent on his education\". Rohan sells his Gift 1 interest to a friend when he is 20, and dies at 24, before enrolling. Meera turns 25 unmarried. Kabir's son dies at 15.",
steps=[("Gift 1 nature?","Contingent: becoming an advocate is uncertain."),("Rohan's sale at 20?","Valid as a transfer of a contingent interest, but the buyer takes the same risk."),("Rohan dies before enrolling?","The event never happened: the interest fails for Rohan's heirs and his buyer."),("Gift 2?","Contingent on a negative event; it vests when Meera turns 25 unmarried (the event becomes impossible)."),("Gift 3?","Vested, not contingent: the income is given to him for his benefit before 18 (Exception)."),("Kabir's son dies at 15?","Because the interest was vested, it passes to his heirs.")]),
ills=[
("Positive event","\"To Rohan if he becomes a lawyer.\"","m","Contingent","Uncertain event must happen."),
("Negative event","\"To Meera if she does not leave India before 30.\"","m","Contingent until 30","Vests when the event becomes impossible."),
("Age without income","\"To Rohan when he turns 18.\"","m","Contingent","He may not reach 18."),
("Age with income","\"To Rohan at 18; income meanwhile spent for him.\"","y","Vested","Exception to s.21."),
("Death before event","Rohan dies at 15 under \"to Rohan at 18\".","n","Fails","Contingent interest not fulfilled."),
],
exam=dict(q="Distinguish vested and contingent interests with examples. (10 marks)",
pts=["s.21 definition: two forms","When it becomes vested","Effect of death","Exception: income before age","Contrast with s.19 in a table"],
line="Under s.21, an interest to take effect only on the happening or not happening of a specified uncertain event is contingent; it becomes vested when the event happens or becomes impossible."),
quiz=[("\"To C if he passes the Bar exam\":",["Vested","Contingent","Void"],1,"Uncertain event."),("\"To C at 18, income for his maintenance meanwhile\":",["Contingent","Vested","Void"],1,"Exception.")],
links=[("s.19","Vested interest."),("s.22, s.23, s.24","Particular forms of contingent gifts."),("s.6(a)","Spes is not even a contingent interest.")],
next="Section 22 applies the same idea to a class that must reach an age.")

S['22'] = dict(tag='linked',
simple="If a gift is to <span class='hl'>those members of a group who reach a particular age</span>, a member who has not yet reached that age gets <span class='hl'>nothing yet</span>.",
deep="<p>A gift to \"such of Arjun's children as reach 21\" does not vest in any child under 21. It is contingent for each member until he reaches the age. (Read with s.21's Exception if income is given meanwhile.)</p>",
dissect=[("such members only of a class as shall attain a particular age","Class gift tied to an age."),("does not vest in any member of the class who has not attained that age","No vesting before the age.")],
master=dict(story="\"To such of Arjun's children as attain 21.\" Arjun has three children aged 22, 19 and 10.",steps=[("The 22-year-old?","Vested."),("The 19 and 10-year-olds?","Not vested until each reaches 21."),("If the 10-year-old dies at 15?","He never qualifies.")]),
ills=[("Below age","Child aged 19 in a gift to those attaining 21.","n","Not vested","s.22.")],
exam=dict(q="Short note on s.22.",pts=["Class gift to members reaching an age","No vesting before that age"],line="Under s.22, an interest for such members of a class as attain a particular age does not vest in any member who has not attained it."),
quiz=[("A child below the stated age in a class gift:",["Has a vested interest","Has nothing vested yet","Takes double"],1,"s.22.")],
links=[("s.15","Class gifts failing in part."),("s.21","Contingent interest.")],
next="Section 23 deals with an uncertain event where no time is fixed.")

S['23'] = dict(tag='linked',
simple="If a gift depends on an uncertain event and <span class='hl'>no time is fixed</span>, the event must happen <span class='hl'>before (or when) the earlier interest ends</span>; otherwise the gift fails.",
deep="<p>Example: \"To Arjun for life, then to Rohan if he marries.\" Rohan must marry before or at Arjun's death. If he marries later, the gift fails.</p>",
dissect=[("no time is mentioned for the occurrence of that event","No deadline stated."),("before, or at the same time as, the intermediate or precedent interest ceases to exist","Implied deadline: the end of the prior interest.")],
master=dict(story="\"To Arjun for life, then to Rohan if he marries.\" Arjun dies in 2040; Rohan marries in 2042.",steps=[("Did the event happen in time?","No: Rohan married after Arjun's interest ended. The gift fails.")]),
ills=[("Event in time","Rohan marries in 2038; Arjun dies in 2040.","y","Gift takes effect","Event before the prior interest ended."),("Event late","Rohan marries after Arjun's death.","n","Fails","s.23.")],
exam=dict(q="Explain s.23.",pts=["Uncertain event, no time fixed","Must happen before prior interest ends"],line="Under s.23, where no time is mentioned for an uncertain event, the interest fails unless the event happens before or when the prior interest ceases."),
quiz=[("Event happens after the prior life interest ends:",["Gift valid","Gift fails","Gift delayed"],1,"s.23.")],
links=[("s.21","Contingent interest.")],
next="Section 24 deals with gifts to whoever survives.")

S['24'] = dict(tag='linked',
simple="If property is to go to <span class='hl'>whichever of certain persons survive</span>, and the time is not specified, it goes to those <span class='hl'>alive when the earlier interest ends</span>, unless the deed shows otherwise.",
deep="<p>The Act's Illustration: A transfers property to B for life, then to C and D equally, or to the survivor of them. C dies during B's life; D survives B. At B's death the property passes to D.</p>",
dissect=[("such of certain persons as shall be surviving at some period","Gift to survivors."),("such of them as shall be alive when the intermediate or precedent interest ceases to exist","Survivorship tested at the end of the prior interest.")],
master=dict(story="\"To Arjun for life, then to Meera and Kabir equally, or to the survivor.\" Kabir dies in 2035; Arjun dies in 2040; Meera is alive.",steps=[("Who takes?","Meera alone: she is alive when Arjun's interest ends.")]),
ills=[("Survivor","Statutory illustration: C dies during B's life; D survives.","y","D takes all","s.24.")],
exam=dict(q="Explain s.24 with its illustration.",pts=["Survivors determined at end of prior interest","Contrary intention"],line="Under s.24, where an interest is to accrue to such of certain persons as survive at an unspecified period, it goes to those alive when the prior interest ceases."),
quiz=[("C dies during B's life; D survives B. Who takes?",["C's heirs and D","D alone","B's heirs"],1,"Statutory illustration.")],
links=[("s.21","Contingent interest.")],
next="Section 25 begins the rules on conditional transfers.")
