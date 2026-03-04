"""
Randomizable data pools for generating absurd-but-legally-formatted lawsuits.

All content is intentionally ridiculous but written in proper legal style.
"""

PLAINTIFF_FIRST_NAMES = [
    "Gerald", "Patricia", "Reginald", "Brenda", "Thaddeus", "Dolores",
    "Cornelius", "Mildred", "Archibald", "Gertrude", "Bartholomew",
    "Ethel", "Humphrey", "Agnes", "Mortimer", "Beatrice", "Chadwick",
    "Prudence", "Nigel", "Winifred", "Clementine", "Rutherford",
    "Percival", "Hortense", "Algernon", "Gladys",
]

PLAINTIFF_MIDDLE_INITIALS = [
    "Q.", "J.", "M.", "T.", "R.", "K.", "P.", "B.", "W.", "X.",
]

PLAINTIFF_LAST_NAMES = [
    "Buttersworth", "Finklebottom", "Wobbleton", "Crumpet",
    "Snodgrass", "Flibbertigibbet", "Dingleberry", "Pumpernickel",
    "Waffleton", "Bumblecrumb", "Thistlewaite", "Noodleman",
    "Wigglesworth", "Croutonsworth", "Bumbershoot", "Flapdoodle",
    "Quibbleston", "Snickersnack", "Dillydally", "Periwinkle",
]

DEFENDANT_NAMES = [
    "THE NEIGHBORHOOD SQUIRREL COALITION, LLC",
    "DAVE'S DISCOUNT HAUNTED HOUSE, INC.",
    "THE GHOST OF APARTMENT 4B",
    "INTERNATIONAL BROTHERHOOD OF LOUD CHEWERS",
    "KEVIN (Last Name Unknown), OPERATOR OF THE ICE CREAM TRUCK",
    "MUNICIPAL DEPARTMENT OF UNNECESSARY ROUNDABOUTS",
    "BARKSWORTH THE DOG, by and through his owner JANET MILLER",
    "PROFESSOR QUACKENBUSH'S SCHOOL OF INTERPRETIVE YODELING, LLC",
    "THE HOMEOWNERS ASSOCIATION OF WHISPERING PINES (A Tyrannical Organization)",
    "CHAD'S ARTISANAL KOMBUCHA EMPORIUM, INC.",
    "THE SENTIENT POTHOLE AT 5TH AND MAIN",
    "CAROL FROM ACCOUNTING, Individually and in her Official Capacity as Lunch Thief",
    "MEGALODON ENERGY DRINK CORPORATION, d/b/a 'SHARK JUICE'",
    "THE RACCOON WHO LIVES IN PLAINTIFF'S ATTIC (Species: Procyon lotor)",
    "UNCLE FESTUS'S DISCOUNT FIREWORKS AND DENTAL CLINIC, LLC",
    "THE ALGORITHM (A Non-Corporeal Digital Entity)",
    "MYSTERIOUS PERSON KNOWN ONLY AS 'THE PARKING LOT WHISTLER'",
    "BRIGADIER GENERAL FLUFFYPAWS, a domesticated cat of unusual size",
    "FLAT EARTH PIZZA COMPANY, INC.",
    "THE CITY OF SPRINGFIELD, DEPARTMENT OF BAFFLING SIGNAGE",
]

COURTS = [
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF LOS ANGELES"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF SAN FRANCISCO"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF SAN DIEGO"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF SACRAMENTO"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF ALAMEDA"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF ORANGE"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF SANTA CLARA"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF RIVERSIDE"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF SAN BERNARDINO"},
    {"line1": "SUPERIOR COURT OF CALIFORNIA", "line2": "COUNTY OF FRESNO"},
]

JUDGE_NAMES = [
    "Hon. Margaret P. Sternface",
    "Hon. Robert Q. Gavelbang",
    "Hon. Susan K. Overruled",
    "Hon. William T. Sidebar",
    "Hon. Dorothy M. Contempt",
    "Hon. Franklin J. Objection",
    "Hon. Eleanor V. Sustained",
    "Hon. Chester B. Continuance",
]

ATTORNEY_FIRMS = [
    {"name": "Dewey, Cheatem & Howe, LLP", "bar": "SBN 123456",
     "address": "100 Wilshire Blvd, Suite 500", "city": "Los Angeles, CA 90017",
     "phone": "(310) 555-0199"},
    {"name": "Sue, Grabbit and Runne, PC", "bar": "SBN 654321",
     "address": "1 Market Street, Floor 30", "city": "San Francisco, CA 94105",
     "phone": "(415) 555-0177"},
    {"name": "Hammer, Tong & Anvil, LLP", "bar": "SBN 789012",
     "address": "2000 Broadway, Suite 800", "city": "Oakland, CA 94612",
     "phone": "(510) 555-0133"},
    {"name": "Billum & Billum Associates", "bar": "SBN 345678",
     "address": "450 Capitol Mall, Suite 300", "city": "Sacramento, CA 95814",
     "phone": "(916) 555-0155"},
    {"name": "Writ, Appeal & Motion, LLP", "bar": "SBN 901234",
     "address": "600 B Street, Suite 1400", "city": "San Diego, CA 92101",
     "phone": "(619) 555-0188"},
]

DAMAGE_AMOUNTS = [
    "$47.50 (the cost of one ruined pair of khakis)",
    "$500,000.00 in general damages",
    "$1,000,000.00 (or the emotional equivalent thereof)",
    "$2,500,000.00 in compensatory damages",
    "$99.99 plus applicable tax and gratuity",
    "$12,000.00 (the appraised value of Plaintiff's prized begonia collection)",
    "$750,000.00 in damages, both tangible and existential",
    "$3.50 (but it's the principle of the thing)",
    "$175,000.00 representing the cost of therapy, past and future",
    "$50,000.00 per incident of psychic disturbance",
]

LOCATIONS = [
    "the parking lot of a Costco in Bakersfield",
    "a community garden in the Sunset District, San Francisco",
    "the food court of the Galleria Mall, Roseville",
    "an improperly zoned bounce house in Pasadena",
    "the self-checkout lane of a grocery store in Elk Grove",
    "a suspiciously quiet cul-de-sac in Irvine",
    "the break room of a WeWork in downtown Los Angeles",
    "a dog park in Pacific Beach, San Diego",
    "an Airbnb treehouse in Big Sur",
    "the drive-through lane of a Taco Bell in Stockton",
]

# ── Case Types ──────────────────────────────────────────────────────────────
# Each case type has:
#   - title: document title for the pleading
#   - facts: list of paragraph templates ({plaintiff}, {defendant}, {location},
#            {date}, {amount} placeholders)
#   - causes: list of dicts with "heading" and "body" paragraph templates
#   - prayer: list of relief items

CASE_TYPES = [
    {
        "title": "COMPLAINT FOR TORTIOUS INTERFERENCE WITH BACKYARD BARBECUE",
        "facts": [
            "{plaintiff} is, and at all relevant times was, a resident of the State "
            "of California and an enthusiastic practitioner of the culinary art of "
            "outdoor grilling.",

            "On or about {date}, {plaintiff} organized and hosted a backyard barbecue "
            "at the location commonly known as Plaintiff's backyard, inviting "
            "approximately fifteen (15) guests for an afternoon of fellowship and "
            "smoked meats.",

            "{defendant} did, with willful and malicious intent, interfere with said "
            "barbecue by means including but not limited to: (a) deploying an "
            "industrial-grade leaf blower at approximately 2:47 p.m.; (b) playing "
            "polka music at unreasonable volume; and (c) releasing what appeared to "
            "be a flock of trained pigeons over the serving area.",

            "As a direct and proximate result of Defendant's tortious conduct, "
            "Plaintiff's brisket was rendered inedible, three guests departed "
            "prematurely, and Plaintiff suffered extreme emotional distress, "
            "including but not limited to feelings of inadequacy as a grill master.",

            "Plaintiff has suffered damages in the amount of {amount}, representing "
            "the cost of wasted provisions, replacement of soiled tablecloths, and "
            "intensive barbecue therapy.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Tortious Interference with Prospective Barbecue Enjoyment)",
                "body": "By engaging in the conduct described above, {defendant} "
                        "intentionally and without justification interfered with "
                        "{plaintiff}'s reasonable expectation of a peaceful and "
                        "delicious barbecue gathering, causing damages as alleged herein.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Intentional Infliction of Emotional Distress)",
                "body": "{defendant}'s conduct was so outrageous and extreme as to "
                        "exceed all bounds of decency tolerated in a civilized "
                        "barbecue-adjacent community. {plaintiff} suffered severe "
                        "emotional distress, including recurring nightmares about "
                        "pigeons and an inability to hear polka music without trembling.",
            },
            {
                "heading": "THIRD CAUSE OF ACTION (Nuisance)",
                "body": "{defendant}'s actions constituted a substantial and "
                        "unreasonable interference with {plaintiff}'s use and "
                        "enjoyment of their property, specifically the backyard grill "
                        "area and adjacent picnic zone, which Plaintiff maintains is "
                        "a sacred space.",
            },
        ],
        "prayer": [
            "For general damages according to proof at trial",
            "For special damages in the amount of {amount}",
            "For an injunction prohibiting {defendant} from operating leaf blowers, "
            "polka speakers, or trained birds within 500 feet of Plaintiff's property "
            "during barbecue season (April through October)",
            "For costs of suit incurred herein",
            "For such other and further relief as the Court deems just and proper",
        ],
    },
    {
        "title": "COMPLAINT FOR NEGLIGENT INFLICTION OF BAD KARAOKE",
        "facts": [
            "{plaintiff} is a resident of the State of California with a documented "
            "sensitivity to off-key vocal performances, as certified by Plaintiff's "
            "audiologist.",

            "On or about {date}, {plaintiff} was peacefully patronizing an "
            "establishment located at {location} when {defendant} took the stage and "
            "commenced an extended karaoke performance.",

            "{defendant} proceeded to perform no fewer than seven (7) consecutive "
            "songs, including but not limited to a twelve-minute rendition of "
            "'Bohemian Rhapsody' in which not a single note was accurately reproduced.",

            "{defendant} owed a duty of care to the patrons of said establishment to "
            "perform at a minimally competent level, or in the alternative, to limit "
            "their performance to no more than two (2) songs as dictated by the "
            "unwritten but universally acknowledged laws of karaoke etiquette.",

            "As a direct and proximate result of {defendant}'s negligent singing, "
            "{plaintiff} suffered acute auditory distress, a persistent ringing in "
            "the left ear, and what Plaintiff's therapist describes as 'Bohemian "
            "Rhapsody-induced PTSD.' Plaintiff seeks damages in the amount of {amount}.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Negligence)",
                "body": "{defendant} owed a duty of care to all patrons within earshot "
                        "to perform karaoke at a standard that would not cause physical "
                        "or emotional harm. {defendant} breached this duty by performing "
                        "seven songs of escalating awfulness, directly and proximately "
                        "causing {plaintiff}'s injuries as described herein.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Negligence Per Se)",
                "body": "{defendant}'s conduct violated the implied warranty of "
                        "karaoke competence established by community standards and "
                        "the posted rules of the establishment, which state: 'Please "
                        "be respectful of other guests.' Defendant was not respectful. "
                        "Not even a little.",
            },
        ],
        "prayer": [
            "For general damages according to proof at trial",
            "For special damages in the amount of {amount}, representing audiological "
            "treatment and noise-canceling headphones",
            "For a permanent injunction barring {defendant} from performing karaoke "
            "in any establishment within the State of California",
            "For punitive damages to deter future tone-deaf performances",
            "For costs of suit incurred herein",
        ],
    },
    {
        "title": "COMPLAINT FOR BREACH OF UNSPOKEN ELEVATOR ETIQUETTE AGREEMENT",
        "facts": [
            "{plaintiff} is a law-abiding citizen of the State of California who, at "
            "all relevant times, has conducted themselves in elevators with dignity, "
            "restraint, and appropriate spatial awareness.",

            "On or about {date}, at approximately 8:47 a.m., {plaintiff} entered the "
            "elevator at {location} and positioned themselves in the universally "
            "accepted rear-corner configuration.",

            "{defendant} entered the elevator on the third floor and, despite the "
            "availability of all four corners and the center-rear position, chose to "
            "stand directly adjacent to {plaintiff}, at a distance of approximately "
            "four (4) inches, in flagrant violation of the Unspoken Elevator Etiquette "
            "Agreement ('UEEA'), which has been in continuous effect since the "
            "invention of the passenger elevator in 1857.",

            "{defendant} further compounded this breach by: (a) initiating unsolicited "
            "conversation about the weather; (b) consuming a hard-boiled egg; and "
            "(c) pressing the button for every single floor between 3 and 17.",

            "{plaintiff} suffered severe discomfort, a ruined morning, and persistent "
            "anxiety about future elevator encounters. Plaintiff seeks damages in the "
            "amount of {amount}.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Breach of Implied Contract)",
                "body": "By entering the elevator, {defendant} implicitly agreed to "
                        "abide by the universally recognized terms of the UEEA, "
                        "including but not limited to: maintaining maximum possible "
                        "distance from other passengers, facing forward, avoiding eye "
                        "contact, and refraining from aromatic foods. {defendant} "
                        "breached each and every one of these terms.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Intentional Infliction of Emotional Distress)",
                "body": "No reasonable person would stand four inches from a stranger "
                        "in a half-empty elevator while eating a hard-boiled egg. "
                        "{defendant}'s conduct was extreme, outrageous, and calculated "
                        "to cause maximum discomfort to {plaintiff}.",
            },
            {
                "heading": "THIRD CAUSE OF ACTION (Assault — Olfactory)",
                "body": "The hard-boiled egg produced a sulfurous odor that constituted "
                        "an offensive contact with {plaintiff}'s person, specifically "
                        "Plaintiff's nasal passages, without Plaintiff's consent. "
                        "Plaintiff alleges this constitutes olfactory assault.",
            },
        ],
        "prayer": [
            "For general damages in the amount of {amount}",
            "For an order requiring {defendant} to complete a court-approved course "
            "in Elevator Etiquette and Personal Space Awareness",
            "For a restraining order requiring {defendant} to maintain a distance of "
            "no less than six (6) feet from {plaintiff} in all enclosed spaces",
            "For the cost of Plaintiff's elevator-avoidance therapy",
            "For costs of suit and such other relief as this Court deems just",
        ],
    },
    {
        "title": "COMPLAINT FOR FRAUDULENT MISREPRESENTATION OF GUACAMOLE QUALITY",
        "facts": [
            "{plaintiff} is a resident of the State of California and a self-described "
            "guacamole connoisseur with over twenty (20) years of experience in the "
            "evaluation and consumption of avocado-based condiments.",

            "On or about {date}, {plaintiff} patronized the establishment operated by "
            "{defendant} located at {location}, where {defendant} prominently "
            "advertised 'World-Famous Handmade Guacamole' on no fewer than three (3) "
            "menu boards, two (2) table tents, and a sidewalk sandwich board.",

            "Upon receiving and tasting said guacamole, {plaintiff} immediately "
            "determined, through years of expertise and a discerning palate, that the "
            "product was neither handmade nor world-famous, but was in fact a "
            "pre-packaged commercial product that had been transferred into a "
            "rustic-looking bowl to create the false impression of artisanal preparation.",

            "Further investigation revealed that the so-called guacamole contained "
            "less than 40% actual avocado, had been supplemented with fillers "
            "including but not limited to pea purée and 'natural flavoring,' and "
            "exhibited a suspicious uniformity of color achievable only through "
            "industrial manufacturing processes.",

            "{plaintiff} suffered damages including the $14.99 paid for the fraudulent "
            "guacamole, emotional betrayal, and a crisis of faith in the restaurant "
            "industry. Total damages sought: {amount}.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Fraudulent Misrepresentation)",
                "body": "{defendant} knowingly and intentionally made false "
                        "representations regarding the nature, quality, and origin of "
                        "its guacamole. {plaintiff} justifiably relied on these "
                        "representations in making the decision to order and consume "
                        "the product. {plaintiff} suffered damages as a proximate "
                        "result of this reliance.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Violation of California Consumer Protection Laws)",
                "body": "{defendant}'s labeling and advertising of the guacamole as "
                        "'handmade' and 'world-famous' constitutes an unfair and "
                        "deceptive business practice in violation of California "
                        "Business & Professions Code Section 17200 et seq.",
            },
        ],
        "prayer": [
            "For restitution of the $14.99 purchase price",
            "For general damages in the amount of {amount}",
            "For an injunction requiring {defendant} to accurately label all "
            "avocado-based products, including disclosure of actual avocado percentage",
            "For punitive damages to deter future guacamole fraud",
            "For costs of suit and attorney's fees as permitted by law",
        ],
    },
    {
        "title": "COMPLAINT FOR INTENTIONAL INFLICTION OF EMOTIONAL DISTRESS VIA LEAF BLOWER",
        "facts": [
            "{plaintiff} is a resident of the State of California who values peace, "
            "quiet, and the ability to sleep past 6:00 a.m. on a Saturday.",

            "Beginning on or about {date}, and continuing every Saturday and Sunday "
            "morning thereafter for a period of no less than fourteen (14) consecutive "
            "weekends, {defendant} has operated a gas-powered leaf blower at {location}, "
            "commencing operations at precisely 6:03 a.m.",

            "Said leaf blower produces noise at approximately 95 decibels, which "
            "Plaintiff's expert witness will testify is equivalent to standing next "
            "to a motorcycle engine, a food blender operating at maximum speed, or "
            "a particularly enthusiastic trombone player.",

            "{defendant} has been informed of the disturbance on no fewer than "
            "twelve (12) occasions via: (a) polite verbal requests; (b) written "
            "letters; (c) a formal petition signed by seventeen neighbors; and "
            "(d) one strongly worded Post-it note affixed to Defendant's front door.",

            "Despite these entreaties, {defendant} has continued and indeed "
            "intensified the leaf-blowing campaign, leading {plaintiff} to believe "
            "the conduct is not merely negligent but deliberately malicious. "
            "Plaintiff seeks damages in the amount of {amount}.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Intentional Infliction of Emotional Distress)",
                "body": "{defendant}'s relentless weekend leaf-blowing campaign "
                        "constitutes extreme and outrageous conduct that no reasonable "
                        "member of a residential community would tolerate. {plaintiff} "
                        "has suffered severe emotional distress including sleep "
                        "deprivation, irritability, and an involuntary flinch response "
                        "upon hearing any two-stroke engine.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Private Nuisance)",
                "body": "{defendant}'s operation of a 95-decibel leaf blower at "
                        "6:03 a.m. on weekend mornings constitutes a substantial and "
                        "unreasonable interference with {plaintiff}'s use and enjoyment "
                        "of their home, and specifically their right to a Saturday "
                        "morning lie-in.",
            },
        ],
        "prayer": [
            "For general damages in the amount of {amount}",
            "For a permanent injunction prohibiting {defendant} from operating any "
            "gas-powered leaf blower before 10:00 a.m. on weekends and holidays",
            "For an order requiring {defendant} to switch to a rake",
            "For the cost of noise-canceling windows, earplugs, and a white noise machine",
            "For punitive damages and costs of suit",
        ],
    },
    {
        "title": "COMPLAINT FOR STRICT LIABILITY — DEFECTIVE FORTUNE COOKIE ADVICE",
        "facts": [
            "{plaintiff} is a resident of the State of California who, on or about "
            "{date}, dined at a Chinese restaurant located at {location}.",

            "At the conclusion of the meal, {plaintiff} received a fortune cookie "
            "manufactured, distributed, and/or sold by {defendant}.",

            "The fortune contained within said cookie read: 'A great investment "
            "opportunity awaits you. Act now without hesitation.'",

            "Relying on this fortune — which {plaintiff} reasonably interpreted as "
            "professional financial guidance, given its authoritative tone and the "
            "solemn context in which it was delivered — {plaintiff} invested their "
            "entire savings of $47,000 in a cryptocurrency called 'DogeCoinButWorse.'",

            "Within seventy-two (72) hours, the value of said cryptocurrency declined "
            "by 99.7%. {plaintiff} has suffered damages in the amount of {amount} "
            "and a profound loss of faith in both fortune cookies and cryptocurrency.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Strict Product Liability — Defective Fortune)",
                "body": "The fortune cookie manufactured and/or distributed by "
                        "{defendant} contained advice that was unreasonably dangerous "
                        "when used as intended. The fortune was defective in its design "
                        "(too vague), its manufacture (printed without adequate "
                        "disclaimers), and its warnings (no 'this is not financial "
                        "advice' caveat).",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Negligent Misrepresentation)",
                "body": "{defendant} had a duty to ensure that fortunes contained in "
                        "its cookies were either (a) accurate, (b) harmless, or "
                        "(c) sufficiently vague as to be unactionable. The fortune "
                        "in question was none of these things.",
            },
        ],
        "prayer": [
            "For compensatory damages in the amount of {amount}",
            "For the return of Plaintiff's original $47,000 investment",
            "For an order requiring {defendant} to include the disclaimer 'This is "
            "not financial, legal, medical, or life advice' in all future fortune cookies",
            "For punitive damages",
            "For costs of suit and such other relief as this Court deems just",
        ],
    },
    {
        "title": "COMPLAINT FOR TRESPASS BY EMOTIONAL SUPPORT PEACOCK",
        "facts": [
            "{plaintiff} is the owner and occupant of a single-family residence in "
            "the State of California, with a well-maintained front lawn and a prize-"
            "winning rose garden.",

            "{defendant} is the owner and custodian of a peacock (hereinafter 'the "
            "Peacock'), which {defendant} claims is a registered emotional support "
            "animal, though no documentation to this effect has been produced.",

            "Beginning on or about {date}, the Peacock has repeatedly and without "
            "invitation entered {plaintiff}'s property at {location}, where it has: "
            "(a) consumed no fewer than thirty-seven (37) rose buds; (b) deposited "
            "waste products of considerable volume on the front walkway; and "
            "(c) displayed its plumage aggressively at Plaintiff's mail carrier, "
            "causing a three-day interruption in postal service.",

            "The Peacock's vocalizations, which Plaintiff's acoustic expert describes "
            "as 'somewhere between a car alarm and a human scream,' have been recorded "
            "at 5:15 a.m. on multiple occasions.",

            "Plaintiff has suffered property damage to the rose garden valued at "
            "{amount}, emotional distress from peacock-related sleep deprivation, and "
            "the indignity of explaining to visitors why there is a peacock on the porch.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Trespass)",
                "body": "{defendant}, through its agent the Peacock, has repeatedly "
                        "entered {plaintiff}'s property without permission or legal "
                        "right. {defendant} is strictly liable for the trespass "
                        "committed by any animal under its ownership or control, "
                        "including but not limited to peacocks.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Destruction of Property)",
                "body": "The Peacock, acting under the dominion and control of "
                        "{defendant}, has destroyed {plaintiff}'s rose garden, which "
                        "Plaintiff had cultivated over a period of fifteen (15) years "
                        "and which held both financial and sentimental value beyond "
                        "calculation (though Plaintiff will attempt to calculate it "
                        "at trial).",
            },
            {
                "heading": "THIRD CAUSE OF ACTION (Nuisance)",
                "body": "The Peacock's presence, vocalizations, waste deposits, and "
                        "aggressive plumage displays constitute a continuing nuisance "
                        "that substantially and unreasonably interferes with "
                        "{plaintiff}'s use and enjoyment of their property.",
            },
        ],
        "prayer": [
            "For compensatory damages in the amount of {amount}",
            "For an injunction requiring {defendant} to confine the Peacock to "
            "Defendant's own property at all times",
            "For the cost of rose garden restoration by a licensed horticulturist",
            "For the cost of a fence of sufficient height and strength to repel peacocks",
            "For costs of suit and such other and further relief as this Court deems proper",
        ],
    },
    {
        "title": "COMPLAINT FOR NUISANCE — UNREASONABLE WIND CHIME DEPLOYMENT",
        "facts": [
            "{plaintiff} is a resident of the State of California who, at all "
            "relevant times, has maintained a reasonable expectation of not being "
            "driven slowly insane by tinkling sounds.",

            "{defendant} resides at the property adjacent to {plaintiff}'s home and "
            "has, beginning on or about {date}, installed and maintained a collection "
            "of wind chimes numbering no fewer than forty-seven (47) individual units.",

            "Said wind chimes are distributed across {defendant}'s front porch, back "
            "patio, fence line, three (3) trees, and what appears to be a purpose-"
            "built wind chime tower erected in Defendant's side yard.",

            "Due to the prevailing winds at {location}, the wind chimes produce a "
            "continuous cacophony of sound that {plaintiff}'s expert witness will "
            "characterize as 'weaponized whimsy.' The sound is audible twenty-four "
            "(24) hours per day, seven (7) days per week, and intensifies during "
            "the afternoon sea breeze.",

            "{plaintiff} has suffered chronic sleep disruption, an inability to "
            "concentrate on work, and a Pavlovian stress response to the sound of "
            "any metallic tinkling. Plaintiff seeks damages in the amount of {amount}.",
        ],
        "causes": [
            {
                "heading": "FIRST CAUSE OF ACTION (Private Nuisance)",
                "body": "{defendant}'s deployment of forty-seven (47) wind chimes in "
                        "a residential neighborhood constitutes a substantial and "
                        "unreasonable interference with {plaintiff}'s use and enjoyment "
                        "of their property. No reasonable person requires forty-seven "
                        "wind chimes.",
            },
            {
                "heading": "SECOND CAUSE OF ACTION (Negligence)",
                "body": "{defendant} owed a duty of care to neighboring residents to "
                        "maintain a reasonable number of wind chimes (which Plaintiff "
                        "contends is no more than three). By installing forty-seven "
                        "(47) wind chimes, {defendant} breached this duty, proximately "
                        "causing {plaintiff}'s injuries.",
            },
        ],
        "prayer": [
            "For general damages in the amount of {amount}",
            "For an injunction requiring the removal of no fewer than forty-four (44) "
            "of the forty-seven (47) wind chimes, leaving {defendant} a generous "
            "allowance of three (3)",
            "For the cost of soundproofing Plaintiff's home",
            "For punitive damages reflecting the deliberate and excessive nature of "
            "Defendant's wind chime collection",
            "For costs of suit",
        ],
    },
]
