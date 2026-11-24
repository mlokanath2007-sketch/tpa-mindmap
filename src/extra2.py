E = {}
def X(sid, why, steps, end, other, rows):
    E[sid] = dict(why=why, flow=dict(steps=steps, end=end), conf=dict(other=other, rows=rows))

X('19', "Certainty helps families plan: a right that is sure to arrive should be treated as owned now, so it can be sold, mortgaged or inherited before it falls into possession.",
 [("Does the deed show a contrary intention (e.g. 'only if he survives')?","Contingent or as the deed says",">"),("Is no time stated, or is it to take effect now, or on an event that must happen?",">","Contingent (s.21)")],
 "Vested: survives the holder's death and can be transferred",
 "s.21 contingent interest",
 [("Certainty","Will surely come","May never come"),("Holder dies early","Goes to his heirs","Fails"),("Example","To C after B's death","To C if he becomes a lawyer")])

X('21', "Some gifts are meant only for those who meet a test (qualify, reach an age, avoid an event). Until the test is met, the right should not be treated as owned.",
 [("Does the interest depend on an uncertain event happening or not happening?",">","Vested (s.19)"),("Is it tied to an age, with the income given to him (or applied for him) meanwhile?","Vested under the Exception",">")],
 "Contingent: vests when the event happens or becomes impossible; fails if he dies first",
 "s.6(a) spes successionis",
 [("Is it a right?","Yes, a real but conditional right","No, a mere hope"),("Transferable?","Yes","No"),("Created by","A transfer naming the event","Nothing: just expectation of inheritance")])

X('22', "A gift to 'those who reach 21' is meant only for those who actually reach 21, so nobody below that age owns anything yet.",
 [("Is the gift to members of a class who reach a stated age?",">","Not s.22"),("Has this member reached the age?","Vested in him","Not vested yet")],
 "",
 "s.15 class gift",
 [("Question","When does a member's interest vest?","What if some members fail s.13 or s.14?"),("Answer","Only on reaching the age","Fails only for those members"),("Link","A type of contingent gift","A saving rule")])

X('23', "Without a deadline, an uncertain event could hang over the property forever. The end of the earlier interest is the natural deadline.",
 [("Is there an interest to accrue on an uncertain event with no time stated?",">","Not s.23"),("Did the event happen before or when the prior interest ended?","Interest takes effect","Interest fails")],
 "",
 "s.24 survivors",
 [("Unknown","When the event must happen","Who counts as survivor"),("Test date","End of prior interest","End of prior interest"),("If late","Gift fails","Dead persons excluded")])

X('24', "'To the survivors' needs a date to count survivors. The law picks the end of the earlier interest, the moment the gift falls into possession.",
 [("Is the gift to such of certain persons as survive, without a stated time?",">","Not s.24"),("Does the deed show a contrary intention?","Follow the deed",">")],
 "Those alive when the prior interest ends take",
 "s.23 no time fixed",
 [("Uncertainty","Who survives","When an event happens"),("Rule","Count survivors at end of prior interest","Event must occur by end of prior interest"),("Illustration","C dies in B's life; D takes","Rohan marries after Arjun dies: fails")])

X('25', "The law will not help anyone enforce a condition that is impossible, illegal or harmful. Since the interest was meant to arise only on that condition, the interest itself falls.",
 [("Is the interest dependent on a condition to be met first?",">","Not s.25 (see s.31, s.32)"),("Is the condition impossible, illegal, against a law, fraudulent, injurious, immoral or against public policy?","Interest fails",">")],
 "Valid condition: fulfil it to take (s.26)",
 "s.32 invalid ending condition",
 [("Type","Condition precedent","Condition subsequent"),("If invalid","Whole interest fails","Condition struck out, interest stays"),("Example","'Murder C, then take ₹500'","'Lose it unless you desert your husband'")])

X('26', "Conditions before a gift are means to an end. If the purpose is achieved in substance, it would be unfair to deny the gift over a technical shortfall the person could not control.",
 [("Is it a condition to be fulfilled before the interest arises?",">","See s.29 (strict)"),("Has it been complied with in substance, before the interest is claimed?","Deemed fulfilled (cy-près)","Not fulfilled")],
 "",
 "s.29 condition subsequent",
 [("Standard","Substantial compliance","Strict compliance"),("Why","Helps the beneficiary get the gift","Protects the holder from losing it"),("Example","Two of three consents, third person dead","Gift over to D only if B marries without C's consent while a minor: it must happen exactly that way")])

X('27', "The giver clearly wanted the second person to take if the first gift did not work out. The exact way it failed rarely matters to that intention, unless the giver said so.",
 [("Is there a prior and an ulterior disposition in the same transaction?",">","Not s.27"),("Has the prior disposition failed?",">","Ulterior gift waits"),("Did the giver intend the ulterior gift only for failure in a particular manner?",">","Ulterior gift takes effect (acceleration)"),("Did it fail in that particular manner?","Ulterior gift takes effect","Ulterior gift does not take effect")],
 "",
 "s.30 invalid ulterior disposition",
 [("What fails","The prior gift","The ulterior gift"),("Result","Ulterior gift accelerates","Prior gift stands"),("Illustration","B dies in A's life: C takes","To C if B does not desert husband: B keeps")])

X('28', "Givers often want property to shift if circumstances change. The law allows it, but checks the shifting condition against the other rules so it cannot be used as a disguised restraint or perpetuity.",
 [("Is an interest given with a condition that on an uncertain event it passes to another?",">","Not s.28"),("Does the condition break s.10, 12, 21, 22, 23, 24, 25 or 27?","Gift over invalid (first gift stands, s.30)",">")],
 "Valid gift over; it operates only if strictly fulfilled (s.29)",
 "s.31 ending condition",
 [("After the event","Interest passes to another person","Interest simply ceases"),("Tested by","s.10, 12, 21 to 25, 27","s.12 and s.32"),("Fulfilment","Strict (s.29)","As stated")])

X('29', "Taking away property already given is drastic, so the law insists the event happen exactly as stated before the holder loses it.",
 [("Is it a gift over under s.28?",">","Not s.29"),("Has the condition been fulfilled exactly as stated?","Gift over takes effect","Holder keeps the property")],
 "",
 "s.26 condition precedent",
 [("Standard","Strict","Substantial"),("Effect","Divests an existing interest","Creates a new interest"),("Leniency","None","Cy-près")])

X('30', "An invalid add-on should not destroy a valid main gift. The giver's main purpose survives.",
 [("Is the ulterior (later) disposition invalid?",">","Both operate as written")],
 "Prior disposition stands as if no condition were inserted",
 "s.16 dependent failure",
 [("Bad gift","Later","Earlier"),("Other gift","Survives","Also fails"),("Logic","Main gift protected","Dependent gift falls")])

X('31', "A giver may fairly want a gift to end if something happens (cutting a protected wood, failing to settle somewhere). Only the insolvency and alienation tricks are forbidden.",
 [("Is it a condition that the interest ceases on an uncertain event?",">","Not s.31"),("Is the event insolvency or an attempt to transfer?","Void under s.12",">"),("Is the event lawful (s.32)?",">","Condition struck out")],
 "Valid: the interest ceases when the event happens or fails to happen",
 "s.28 gift over",
 [("After event","Interest ends (returns to transferor)","Interest passes to another"),("Subject to","s.12, s.32","s.10, 12, 21 to 25, 27"),("Illustration","B cuts the wood: loses life interest","B marries at 17 without consent: D takes")])

X('32', "The same public-policy limits that stop bad conditions creating rights must also stop bad conditions destroying them.",
 [("Could this event lawfully be a condition for creating an interest (s.25 test)?","Valid ending condition","Condition struck out; interest stays")],
 "",
 "s.25 conditional transfer",
 [("Condition type","Subsequent","Precedent"),("If invalid","Struck out, interest continues","Interest fails"),("Same test?","Yes","Yes")])

X('33', "Without a deadline the person can act whenever he likes. Only when he himself makes performance impossible has he truly broken the condition.",
 [("Is there a condition to perform an act with no time fixed?",">","Not s.33 (see s.34)"),("Has he made the act impossible, permanently or indefinitely?","Condition broken","Not broken yet")],
 "",
 "s.34 fraud preventing the act",
 [("Who blocks the act","The holder himself","A person who benefits from failure, by fraud"),("Result","Condition broken","Extra time or deemed fulfilled against the fraudster"),("Time fixed?","No","Either")])

X('34', "No one may profit from his own fraud. If the person waiting to gain from failure causes the failure by fraud, the law treats the act as done (or gives more time) against him.",
 [("Was performance prevented by fraud of a person directly benefited by non-fulfilment?",">","Normal rules apply"),("Was a time specified for the act?","Extra time against him equal to the delay","Condition deemed fulfilled against him")],
 "",
 "s.33 no time fixed",
 [("Who caused failure","Beneficiary of failure, by fraud","The holder"),("Effect","Extra time or deemed fulfilled","Broken if he makes it impossible"),("Purpose","Punish fraud","Fix a breach point")])

X('35', "A person cannot approve a document where it helps him and reject it where it hurts him. Equity forces a fair choice, while compensating the disappointed transferee.",
 [("Did the transferor profess to transfer property he had no right to transfer?",">","No election"),("Did the same transaction confer a direct benefit on that owner?",">","No election (indirect benefit is not enough)"),("Did the owner confirm, or is he deemed to (knowing use, 2 years, irreversible act, silence after demand)?","Transfer confirmed: owner keeps benefit, loses property","Owner keeps property, gives up benefit (compensation to transferee where required)")],
 "",
 "s.43 feeding the grant",
 [("Whose property","Belongs to a third person (the owner)","Transferor later acquires it"),("Who chooses","The owner","The transferee"),("Basis","Equity of election","Estoppel")])

X('36', "Income earns steadily over time, so it is fair to divide it by days between the old and new holder.",
 [("Is it periodic income (rent, pension, dividend)?",">","Not s.36"),("Is there a contract or local usage to the contrary?","Follow it","Split day by day; pay on due date")],
 "",
 "s.8 operation of transfer",
 [("Focus","Splitting periodic income","What passes"),("Rent","Day by day","After transfer goes to buyer"),("Default","Yes","Yes")])

X('37', "When a property is split, the person bound should not be burdened more, and each new owner should get his fair share.",
 [("Has the property been divided among several owners after a transfer?",">","Not s.37"),("Can the duty be severed without substantially increasing the burden?","Perform to each in proportion to share","Perform to the owner they jointly designate")],
 "",
 "s.36 apportionment by time",
 [("Splits by","Shares among owners","Days between holders"),("Applies to","Any obligation on the property","Periodic income"),("Notice needed","Yes, of the severance","No")])

X('38', "Buyers cannot investigate everything. If they honestly check the claimed necessity, they should be safe even if the seller misled them.",
 [("Is the seller authorised only in certain variable circumstances (necessity, benefit)?",">","Not s.38"),("Did he transfer for consideration, alleging those circumstances?",">","Not protected"),("Did the buyer use reasonable care and act in good faith?","Circumstances deemed to exist: buyer protected","Not protected")],
 "",
 "s.41 ostensible owner",
 [("Seller","Has limited authority","Appears to be owner"),("Buyer's need","Reasonable enquiry into necessity","Reasonable care about power to transfer"),("Basis","Protects honest enquiry","Estoppel against real owner")])

X('39', "Dependants should not lose support because the property was sold, but an honest buyer who paid and could not know should not suffer either.",
 [("Does a third person have a right to maintenance (or advancement or marriage) from the property's profits?",">","Not s.39"),("Is the buyer a transferee for consideration without notice?","Not bound","Bound (notice or gratuitous)")],
 "",
 "s.40 obligations on land",
 [("Right protected","Maintenance from profits","Restriction on use or contractual obligation"),("Bound","Notice or gratuitous transferee","Notice or gratuitous transferee"),("Free","Bona fide purchaser for value","Bona fide purchaser for value")])

X('40', "A promise about land (not to build high, to sell to someone) should follow the land into the hands of anyone who knew about it or got it free.",
 [("Is there a right to restrain use for other land, or a contractual obligation annexed to ownership?",">","Not s.40"),("Is the transferee for consideration and without notice?","Not bound","Bound")],
 "",
 "s.11 repugnant direction",
 [("Enforced by","Third person","Transferor"),("Against","Later transferees with notice","The transferee"),("Source","Contract or right for other land","Direction in the transfer")])

X('41', "The owner who lets someone pose as owner created the risk. Between him and an innocent buyer who checked carefully and paid, the owner should bear the loss.",
 [("Is the transferor an ostensible owner with the real owner's express or implied consent?",">","Not protected (e.g. forger)"),("Was the transfer for consideration?",">","Not protected (gift)"),("Did the buyer take reasonable care and act in good faith?","Transfer not voidable","Not protected")],
 "",
 "s.43 feeding the grant",
 [("Transferor","Not the owner, but appears so with owner's consent","Claims authority, later acquires it"),("Who is estopped","Real owner","Transferor"),("Buyer's right","Keeps property now","Option on later-acquired interest")])

X('42', "A reserved power to revoke is exercised by acting on it. A later sale for value shows the owner has chosen to revoke.",
 [("Did the transferor reserve a power to revoke?",">","Not s.42"),("Did he later transfer for consideration?",">","No revocation by s.42"),("Are any conditions on the power satisfied?","Earlier transfer revoked to the extent of the power","No revocation")],
 "",
 "s.48 priority",
 [("Earlier transfer","Revoked","Prevails"),("Why","Power to revoke was reserved","First in time"),("Later transfer","Takes effect","Subject to earlier")])

X('43', "Someone who sold land he did not yet own should not keep the land when he later gets it, and the buyer who relied on his word should get what was promised.",
 [("Did the transferor fraudulently or erroneously represent authority to transfer?",">","Not s.43"),("Was it for consideration?",">","Not s.43 (gift)"),("Has he later acquired an interest in that property?",">","Buyer waits or rescinds"),("Does the contract still subsist (buyer has not rescinded)?",">","Option lost"),("Has a later good-faith buyer for value without notice intervened?","His rights are not impaired","Buyer may claim the property at his option")],
 "",
 "s.41 ostensible owner",
 [("When title arrives","Later","Never with the transferor"),("Who chooses","Transferee","No choice: transfer valid"),("Gift covered?","No","No")])

X('44', "A buyer of a co-owner's share should get what the co-owner had. But a family home is private, so an outsider cannot force his way into it.",
 [("Did a co-owner transfer his share?",">","Not s.44"),("Is it a dwelling house of an undivided family and the buyer an outsider?","No joint possession; partition only","Joint possession and partition, subject to burdens")],
 "",
 "s.47 co-owners transfer a share",
 [("Who transfers","One co-owner","Several co-owners together"),("Issue","Buyer's rights","Whose share is reduced"),("Rule","Steps into shoes","Proportionate reduction")])

X('45', "Shares in jointly bought property should mirror what each actually contributed; where proof is missing, equality is the fairest guess.",
 [("Was the property bought by two or more for consideration?",">","Not s.45"),("Is there a contract on shares?","Follow it",">"),("Is there evidence of contributions or fund shares?","Shares follow contributions","Equal shares")],
 "",
 "s.46 joint sellers",
 [("Side","Buyers","Sellers"),("Divides","Shares in property","Price"),("Default","By contribution, else equal","By value of interests")])

X('46', "Each seller should get the part of the price that matches what he gave up.",
 [("Did persons with distinct interests sell together?",">","Not s.46"),("Is there a contract on sharing?","Follow it","Share by value of interests")],
 "",
 "s.45 joint buyers",
 [("Side","Sellers","Buyers"),("Divides","Price","Property"),("Equal when","Interests of equal value","No evidence")])

X('47', "If co-owners do not say whose share is sold, the fair default is to take it from each in proportion.",
 [("Did several co-owners transfer a share without specifying whose?",">","Follow what they specified")],
 "Taken equally (equal shares) or proportionately (unequal)",
 "s.44 one co-owner",
 [("Transferors","All co-owners together","One co-owner"),("Question","Whose share shrinks","What buyer gets"),("Answer","Proportionate","Transferor's rights")])

X('48', "An owner cannot take back rights he has already granted by granting them again. The earlier grantee comes first.",
 [("Were rights over the same property created at different times?",">","Not s.48"),("Can they all exist fully together?","No conflict",">"),("Is there a special contract or reservation binding the earlier transferee?","Follow it","Earlier right prevails")],
 "",
 "s.42 power to revoke",
 [("Earlier right","Prevails","Revoked"),("Exception","Special contract","Reserved power"),("Principle","First in time","Owner's reserved choice")])

X('49', "A buyer who pays for a building should not lose it to fire while the seller pockets the insurance.",
 [("Was the transfer for consideration?",">","Not s.49"),("Was the property insured against fire at the date of transfer and then damaged by fire?",">","Not s.49"),("Is there a contract to the contrary?","Follow it","Buyer can require the money received to be used for reinstatement")],
 "",
 "s.55(5)(c) buyer's risk",
 [("Issue","Who uses the insurance money","Who bears loss after ownership passes"),("Rule","Applied to reinstate","Buyer bears loss not caused by seller"),("Link","Softens the buyer's risk","Allocates risk")])

X('50', "A tenant who honestly pays the person he has always paid should not be made to pay twice.",
 [("Did the person pay rent or profits in good faith to the person he held from?",">","Not protected"),("Did he have notice that the person had no right?","Not protected","Not chargeable again")],
 "",
 "s.36 apportionment by time",
 [("Question","Is the payer discharged?","How is rent split?"),("Protects","Honest tenant","Transferor and transferee"),("Key","Good faith","Days")])

X('51', "Someone who honestly improved land thinking it was his should not lose the value of his work to the true owner.",
 [("Did the transferee make an improvement believing in good faith he was absolutely entitled?",">","No protection"),("Was he evicted by a better title?",">","Not s.51")],
 "He can claim the improvement's value or require the owner to sell; growing crops are his",
 "s.41 ostensible owner",
 [("Buyer keeps land?","No, gets compensation or option to buy","Yes"),("Condition","Good faith belief, eviction","Owner's consent, value, care"),("Remedy","Money or purchase","Title protected")])

X('52', "If parties could sell the disputed property during the case, no court decree would ever be effective. The rule keeps the subject matter frozen for the court.",
 [("Is a suit or proceeding pending in a competent court?",">","Not s.52"),("Is it non-collusive?",">","Not s.52"),("Is a right to immovable property directly and specifically in question?",">","Not s.52 (e.g. money suit)"),("Did a party transfer or deal with it without the court's authority?","Transfer subject to the decree, whatever the buyer knew","Valid on the court's terms")],
 "",
 "s.53 fraudulent transfer",
 [("Basis","Public policy; notice irrelevant","Intent to defeat creditors or later buyer"),("Effect","Subject to decree","Voidable"),("Good faith buyer","Still bound","Protected if for value")])

X('53', "Debtors must not hide their land to cheat creditors, but honest buyers who paid must not suffer for the debtor's fraud.",
 [("Was there intent to defeat or delay creditors (or to defraud a later transferee, for a gift)?",">","Valid"),("Is the transferee in good faith and for consideration?","Protected","Voidable at the defrauded person's option")],
 "",
 "s.52 lis pendens",
 [("Needs intent?","Yes","No"),("Who can challenge","Creditors (for all) or later transferee","Other party to the suit"),("Honest buyer","Protected","Bound")])

X('53A', "People often pay and move in long before the formal deed. It would be unjust to let the seller throw them out on a technicality while they are ready to complete.",
 [("Is there a written contract signed by the transferor, terms reasonably certain (registered if after 2001)?",">","No protection"),("Has the transferee taken possession (or continued in possession and done an act) in part performance?",">","No protection"),("Has he performed or is he willing to perform his part?",">","No protection"),("Is the challenger a later buyer for value without notice?","Not protected against him","Transferor debarred: possession protected (shield, not sword)")],
 "",
 "s.54 contract for sale",
 [("Gives","A shield to keep possession","No interest at all"),("Needs","Written contract + possession + readiness","Just an agreement"),("Ownership","Not passed","Not passed")])

X('54', "Ownership of land is valuable and must be certain and public, so sales above a small value must be by registered deed, and a mere agreement gives no ownership.",
 [("Is ownership passing in exchange for a money price (paid or promised)?",">","Not a sale (exchange, gift or lease)"),("Is it intangible, or tangible worth ₹100 or more?",">","Registered deed or delivery is enough"),("Is there a registered instrument?","Valid sale","No sale (at most a contract for sale)")],
 "",
 "s.118 exchange",
 [("Consideration","Money price","Another property"),("Mode","Registered deed if ₹100+","Same as sale"),("Each party","Buyer and seller","Both are buyer and seller")])

X('55', "Sale is a bargain between parties with unequal information. The law sets default duties so each discloses what the other cannot discover and risks fall fairly.",
 [("Is there a contract to the contrary?","Follow it",">"),("Has ownership passed to the buyer?","Buyer bears risk and outgoings; seller has charge for unpaid price","Seller keeps rents and must take care; buyer has charge for advance")],
 "",
 "s.54 sale",
 [("Covers","Duties and rights of parties","Definition and mode of sale"),("Disclosure","Latent defects; value-raising facts","Not covered"),("Risk","Passes with ownership","Not covered")])

X('56', "A buyer who paid for one property should not have it eaten up by a mortgage that could be paid from the seller's other mortgaged properties.",
 [("Did the owner mortgage two or more properties to one person and then sell one?",">","Not s.56"),("Is there a contract to the contrary?","Follow it",">"),("Would paying from the unsold property prejudice the mortgagee or another purchaser for value?","Not to that extent","Mortgage paid first from unsold property")],
 "",
 "s.81 marshalling securities",
 [("Who claims","Later buyer of one property","Later mortgagee of one property"),("Relief","Debt paid from unsold property","Prior mortgage paid from other property"),("Limit","No prejudice to mortgagee or others","Same")])
