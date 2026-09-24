# -*- coding: utf-8 -*-
"""
Finnish Culture (tier-3) — content data model.

Each content page: slug, category (nav group), title (browser tab), h1, meta_desc,
intro (list of paragraphs), blocks (body blocks in order), faq (list of (q,a)).

Block types:
  ("p",  text)        paragraph
  ("h2", text)        section heading
  ("h3", text)        subsection heading
  ("ul", [item,...])  bullet list
Block "lead" paragraphs and supporting detail are authored directly.
"""

CATEGORIES = [
    ("Values & Society", "Values & Society", "values"),
    ("Traditions & Celebrations", "Traditions & Celebrations", "traditions"),
    ("Sauna & Wellbeing", "Sauna & Wellbeing", "sauna"),
    ("Food & Drink", "Food & Drink", "food"),
    ("Language & Communication", "Language & Communication", "language"),
    ("Arts & Everyday Life", "Arts & Everyday Life", "arts"),
]


def page(slug, cat, title, h1, meta, intro, blocks, faq):
    return {
        "slug": slug, "cat": cat, "title": title, "h1": h1,
        "meta": meta, "intro": intro, "blocks": blocks, "faq": faq,
    }


PAGES = []

# ---------------------------------------------------------------------------
# VALUES & SOCIETY
# ---------------------------------------------------------------------------
PAGES.append(page(
    "sisu", "Values & Society",
    "Finnish Sisu: Resilience and National Spirit",
    "Sisu: Finland’s Spirit of Resilience",
    "What is Finnish sisu, what does the word really mean, and how does it show up in everyday life, work and well-being?",
    ["Few Finnish words travel as far as sisu. It is often translated as courage or grit, but to Finns it means something quieter and more stubborn: the ability to keep going when you would rather stop.",
     "Sisu is not loud bravado. It is the quiet decision to push on through cold, long winters, hard work and hard days, one step at a time."],
    [
        ("h2", "What “sisu” really means"),
        ("p", "The word comes from the Finnish root for the inside of something — the core, the inner part. So sisu is literally the strength found within, not the strength you show at the surface."),
        ("p", "Unlike some ideas of resilience that focus on quick recovery or optimism, sisu is about endurance. It is the will that appears when comfort, motivation and even hope are thin, but the task still needs doing."),
        ("ul", ["It is steady, not flashy.", "It grows with use, not with comfort.", "It belongs to everyone, not to a chosen few."]),
        ("h2", "Sisu in everyday life"),
        ("p", "You do not need to run a marathon to meet sisu. It shows up in everyday choices: walking to the bus stop in a blizzard, doing the final hour of a hard shift, or finishing a project when the deadline hurts."),
        ("p", "This everyday stubbornness is part of why Finland’s culture values doing over speaking. A Finn is more likely to show you they can manage than to tell you they are struggling."),
        ("h2", "Sisu and well-being"),
        ("p", "There is a healthy side to sisu: it builds confidence, self-reliance and trust in your own abilities. But researchers also point out that too much sisu can mean ignoring your own limits."),
        ("p", "Modern Finns balance the old ideal with a newer lesson: rest, self-compassion and asking for help are also strengths. The happiest-country reputation rests partly on learning when to stop as well as when to push."),
        ("h2", "Sisu vs. resilience"),
        ("p", "Resilience is often described as a capacity that helps you bounce back. Sisu adds a stubborn refusal to let go of the effort, even when bouncing back is slow."),
        ("p", "Seen this way, sisu is a bridge between endurance and care: it is the will to keep going, softened by the wisdom to pace yourself. That combination is a large part of the national character visitors meet."),
    ],
    [
        ("Is sisu only for extreme situations?", "No. Sisu lives in everyday persistence too — cold mornings, hard work and finishing what you start. The extreme version is just a clearer highlight of the same trait."),
        ("Is sisu the same as being tough or uncaring?", "Not at all. Sisu coexists with strong social trust and care. Finns are stubborn about effort precisely because they respect their own and others’ commitments."),
        ("Can you learn sisu?", "Mostly, yes. It is built through practice, routine and learning to tolerate discomfort in small steps, much like any endurance skill."),
    ],
))

PAGES.append(page(
    "honesty-trust", "Values & Society",
    "Honesty and Social Trust in Finland",
    "Honesty and Social Trust in Finland",
    "Why Finland runs on trust: the honest culture, keeping promises, and the social contract behind everyday life.",
    ["If you visit Finland, you will notice something unusual: strangers trust each other. Bags are left by shop doors, fruit is sold from unmanned roadside stands, and promises are taken seriously.",
     "This is not naivety. It is a deliberate, centuries-deep social choice — a culture built on honesty and a shared assumption that people can be relied on."],
    [
        ("h2", "Why honesty matters"),
        ("p", "In a country with long, dark winters and small, spread-out communities, cooperation has always been a survival necessity. When people depend on each other for real things — help, firewood, honesty — keeping your word becomes a moral fact, not a nicety."),
        ("p", "Finns tend to say what they mean and mean what they say. Failing to do so is felt as a small betrayal, because honesty is treated as the glue of the community."),
        ("h2", "The high-trust society"),
        ("p", "Finland regularly ranks among the most trusting countries in the world. This shows up in practical ways: few people lock their bikes in small towns, farmers sell produce on an honour system, and offices often work on open trust rather than heavy supervision."),
        ("p", "That trust is not free. It is protected by strong institutions, clear rules and an expectation that everybody participates. The reward is a society that simply works — faster queues, fewer disputes, less bureaucracy."),
        ("h2", "Everyday honesty"),
        ("p", "Honesty appears in small routines: returning a lost wallet, admitting a mistake at work, or telling you the meal is spicy before you take a bite. Finns prize plain words over polite ones."),
        ("p", "This can take getting used to. A straightforward “no, that does not work” sounds blunt to some ears, but it is meant as respect — clarity — not as rudeness."),
        ("h2", "Trust and institutions"),
        ("p", "Finns trust their state, their police, their courts and each other to a degree that surprises newcomers from many other countries. The state is seen as a service, not an enemy."),
        ("p", "This trust underpins the welfare model: people accept paying high taxes partly because they believe the money is used fairly and for the common good."),
    ],
    [
        ("Is everyone in Finland really that honest?", "No society is perfectly honest, but Finland’s shared commitment to trust is unusually strong. It shapes rules, habits and what people expect of one another."),
        ("Why are Finns so direct?", "Directness is seen as respect. Being clear saves time and prevents misunderstanding, so Finns prefer honest words over vague politeness."),
        ("Does trust make life easier?", "Generally yes. High trust reduces conflict, paperwork and fear, which works out to a calmer, safer and more cooperative everyday life."),
    ],
))

PAGES.append(page(
    "equality", "Values & Society",
    "Equality and the Finnish Social Model",
    "Equality and the Finnish Social Model",
    "How equality, consensus and the welfare model shape Finnish society, work and everyday life.",
    ["Equality runs deep in Finland. Children learn it at school, workers expect it in offices, and politics treats it as a baseline rather than a demand.",
     "It shows up in small things (first-name workplaces, flat hierarchies) and large ones (free education, universal healthcare, a strong welfare state)."],
    [
        ("h2", "Equality as a value"),
        ("p", "The Finnish word for equality, tasa-arvo, covers both equal rights and a sense that no one is above or below anyone else in everyday dignity. The idea is older than the modern state, rooted in free, self-governing peasant communities."),
        ("p", "The result is an unusually flat social culture. Titles matter less, bosses are approachable, and children address adults by first name — unheard of in many countries."),
        ("h2", "Gender balance"),
        ("p", "Finland was the first country in the world to give women full voting rights, in 1906. Fifty years later, the proportion of women in professional and political life grew into one of the highest in the world."),
        ("p", "Daddy months in parental leave, shared household expectations and equal pay discussions are normal parts of public life. The aim is practical: capabilities, not gender, should decide who does what."),
        ("h2", "Consensus and the welfare model"),
        ("p", "Finnish decision-making favours consensus. From workplaces to politics, the instinct is to negotiate until a workable compromise is found, rather than to have one side simply win."),
        ("p", "This consensus instinct pairs with the welfare model: taxes fund education, healthcare, childcare and elderly care so that basic security does not depend on your income or your family’s luck."),
        ("h2", "Everyday equality"),
        ("p", "In practice this means small things: everyone queues, everyone pays their share, and nobody expects special treatment for being rich or important. Flashy displays of status are often looked down on."),
        ("p", "For newcomers, the lesson is simple: approach everyone with the same courtesy, do your share, and you will fit in — regardless of background."),
    ],
    [
        ("Is Finland really equal today?", "Equal in rights and in everyday culture to a high degree, though, as everywhere, real-life gaps remain and are frankly discussed. The direction of public life treats equality as unfinished work."),
        ("Does equality mean sameness?", "No. Equality is about rights, dignity and opportunity, not making everyone identical. Finnish culture still celebrates individuality, reserve and personal space."),
        ("Why do Finns avoid showing off?", "Status displays clash with the equality value. Modesty and “everyone is ordinary” wins more social respect than boasting."),
    ],
))

PAGES.append(page(
    "personal-space", "Values & Society",
    "Personal Space and the Comfort of Silence",
    "Personal Space and the Comfort of Silence",
    "Why Finns value personal space and silence — and what that means for conversations, friendships and everyday life.",
    ["Travel guides warn visitors: Finns do not like small talk. That is only half true. It is not that Finns dislike people — they simply give silence and space real value.",
     "Understanding this takes most foreigners from confusion to relief, because lives there are allowed to be quiet without anyone taking it as a problem."],
    [
        ("h2", "The value of silence"),
        ("p", "In many cultures, silence is a gap to fill, a social failure to repair. In Finland, silence is a normal, comfortable part of conversation. People think before they speak, and nobody panics at a pause."),
        ("p", "Silence is also a way to listen. A Finn who stays quiet is often giving you their full attention, not ignoring you. Comfort with silence is a form of respect."),
        ("h2", "Personal space in daily life"),
        ("p", "Finns keep more physical distance than people in many European cultures. On an empty bus, a Finn will choose the seat farthest from you — not to insult you, but because the space exists and invading it would feel odd."),
        ("p", "Queues are orderly, voices are kept low, and waiting rooms are calm. This restraint is a courtesy: the aim is not to bother others."),
        ("h2", "Talking about feelings"),
        ("p", "Finns are not famously talkative about emotions, but they feel them intensely. Feelings tend to be shown more than told — through actions, reliability and presence rather than effusive words."),
        ("p", "A compliment, a shared silence by a fire, or a helpfully fixed shelf can carry more weight than a long emotional speech. Do not mistake understatement for indifference."),
        ("h2", "Reading the room"),
        ("p", "Because Finns are quiet, they tend to read rooms well. They notice moods, awkwardness and fatigue, and they adjust — stepping back when someone needs space, helping when someone struggles."),
        ("ul", ["If a Finn is quiet with you, assume they are comfortable, not annoyed.", "Small talk exists but is shorter and more information-based than social filler.", "When a Finn does open up, they usually mean it."]),
    ],
    [
        ("Do Finns dislike small talk entirely?", "They dislike forced filler. Purposeful, honest conversation is welcome; chatter for its own sake feels like noise. Talking about the weather, nature or practical things is a safe, common entry point."),
        ("How do I make Finnish friends?", "Through shared activities — sports, clubs, work, hobbies. Trust builds slowly but deeply once a connection forms; reliability matters more than quick friendliness."),
        ("Is silence a sign something is wrong?", "Almost never. Comfortable silence is normal in Finland. If a Finn is actually upset, they usually tell you directly, in their own way."),
    ],
))

PAGES.append(page(
    "punctuality", "Values & Society",
    "Punctuality and Respect for Time",
    "Punctuality and the Respect for Time",
    "Why being on time is a core Finnish value — and how it shapes work, friendships and daily life.",
    ["Arrive five minutes late to a Finnish meeting the first time and you will be welcomed warmly. Arrive late again, and you will quietly fall in people’s eyes.",
     "Punctuality is one of Finland’s most reliable cultural values. It is not an obsession with clocks; it is respect for other people and their time."],
    [
        ("h2", "Being on time"),
        ("p", "Five minutes early is effectively on time; being right on time is good; being late is a choice you make at your own reputational cost. Finns plan for punctuality and expect others to do the same."),
        ("p", "This applies to work, doctors’ appointments, private visits and even social events — not because Finns are cold, but because they assume your word and your time matter equally to everyone."),
        ("h2", "Time as a promise"),
        ("p", "In a culture built on trust, punctuality is a promise kept. Being on time tells people they matter. Being late signals that their schedule is less important than yours."),
        ("p", "This logic explains why lateness feels personal in Finland in a way it might not elsewhere. It is rarely about anger; it is about the shared belief that respect is shown through reliability."),
        ("h2", "Seasonal time"),
        ("p", "Finns also have a seasonal relationship with time. Summers are lived fully and outdoors; winters are for rest and indoors. Deadlines bend differently around midsummer and Christmas, because those weeks are sacred."),
        ("p", "So punctuality is not rigid rule-following. It is a social rhythm: punctual when a promise is made, but wise about when the whole country slows down."),
        ("h2", "Time at work"),
        ("p", "In Finnish workplaces, meetings start on time, end on time, and respect people’s calendars. In return, there is real trust that work gets done without someone watching the clock for you."),
        ("p", "The balance is the point: punctual about commitments, flexible about life, and suspicious of anyone who treats other people’s time as cheap."),
    ],
    [
        ("Is it rude to be late in Finland?", "Yes, visibly late is considered disrespectful. Tell people if you are delayed; a quick message fixes most situations far better than silent lateness."),
        ("What if public transport is late?", "Finns understand external delays and adapt without drama. The value is about intention and respect — making the effort and communicating — not about machine-like precision."),
        ("Does punctuality apply to private visits?", "Generally yes, though friends relax once a bond is strong. For first invitations, arrive on time — or even a little early is fine in Finland."),
    ],
))

# ---------------------------------------------------------------------------
# TRADITIONS & CELEBRATIONS
# ---------------------------------------------------------------------------
PAGES.append(page(
    "juhannus", "Traditions & Celebrations",
    "Juhannus: Finnish Midsummer",
    "Juhannus: Finnish Midsummer",
    "Midsummer in Finland: the summer solstice, lakeside rituals, food and the traditions that make June 20–26 sacred.",
    ["If you ask a Finn for the most important evening of the year, many will skip Christmas and say juhannus — Midsummer.",
     "Around the summer solstice, the country slows to a stop. Cities empty, cottages fill, and Finns gather by water and fire to celebrate a night when the sun barely sets."],
    [
        ("h2", "The summer solstice"),
        ("p", "Juhannus falls on the Saturday between 20 and 26 June. In the far north the sun does not set at all, and even in Helsinki the night stays nearly bright — an almost magical light that the Finns greet with relief after a dark winter."),
        ("p", "The tradition has pre-Christian roots as a fertility and sunrise festival that later merged with the Christian feast of John the Baptist. The name itself, Juhannus, is the Finnish form of that saint’s name."),
        ("h2", "Lakeside rituals"),
        ("p", "Many Finns spend the weekend at a summer cottage by a lake. The classic evening includes a sauna, a swim, and a large bonfire, kokko, built by the water and lit as darkness falls."),
        ("p", "In some areas, young women once placed wildflowers under their pillows to dream of their future spouse. Few take that literally today, but flowers and birch branches still decorate homes and boats."),
        ("h2", "Midsummer food"),
        ("p", "The table features grilled sausage, herring and new potatoes with dill, fresh strawberries, and plenty of cold drinks. Grilling over an open fire is practically the national sport of juhannus."),
        ("ul", ["New potatoes with dill and herring", "Grilled makkara (sausage) straight from the fire", "Fresh strawberries, often with cream", "Herbal schnapps and berries for those who drink"]),
        ("h2", "Midsummer today"),
        ("p", "Finland has a law that places Midsummer’s Eve on a Friday so everyone gets a long weekend. It is also a time for traditional silja cruises to the islands, open-air dancing and “spring cleaning” of life worries."),
        ("p", "Above all, juhannus is about pausing. For a few days, screens are closed, phones go quiet, and the whole country resets by the water — which is exactly its point."),
    ],
    [
        ("Is Midsummer a bigger deal than Christmas in Finland?", "For many, yes. Christmas is about family and food; Midsummer is about nature, fire, water and the joy of light after winter. Both matter, but juhannus owns the summer."),
        ("Is dancing around a maypole a Finnish thing?", "Not really — that is Swedish. Finland’s symbol is the bonfire, kokko, lit by the water, though some Swedish-speaking coastal areas do have maypole influences."),
        ("Can visitors join?", "Yes, warmly. If invited to a cottage for juhannus, accept — bring good food, take part in the sauna and bonfire, and you will be welcomed as family."),
    ],
))

PAGES.append(page(
    "vappu", "Traditions & Celebrations",
    "Vappu: Finland’s May Day Celebration",
    "Vappu: Finland’s May Day Celebration",
    "Vappu, Finland’s May Day: the student carnival, the picnic tradition, sima and tippaleipä — and a welcome to spring.",
    ["Vappu is Finland’s loudest holiday — and the loudest is said with love. On the last night of April and the first day of May, winter-weary Finns pour into the streets to welcome spring in style.",
     "Part student carnival, part labour day, part friend festival, Vappu is celebrated by everyone from students in white caps to families with balloons and home-made sima."],
    [
        ("h2", "Welcome to spring"),
        ("p", "After months of snow and darkness, Vappu is a communal exhale. It marks the moment when spring feels real, and the winter mood finally lifts into light, laughter and being outside again."),
        ("p", "The holiday has two public faces: vappuaatto (Walpurgis Night, 30 April) when parties begin in earnest, and the first of May itself, when picnics and processions take over."),
        ("h2", "Student celebrations"),
        ("p", "The white student cap is the emblem of Vappu. New graduates receive their lyceum cap on 30 April, and in Helsinki a famous statue, Havis Amanda, is washed and crowned with a cap by students at the very start of the celebrations."),
        ("p", "Universities and civic groups organise events, and the caps stay on heads — young and old — for the whole holiday as a mark of pride and belonging."),
        ("h2", "The picnic tradition"),
        ("p", "On 1 May, Finns picnic in parks despite the often-chilly weather, spreading blankets on grass and shared benches. Helsinki’s Kaivopuisto park becomes a sea of bubbles, balloons and white caps."),
        ("ul", ["Sparkling sima and fresh pulla", "Balloons tied to prams and trees", "Falafel, cakes and cold drinks shared on blankets", "Music, games and long, cheerful afternoons"]),
        ("h2", "Sima and tippaleipä"),
        ("p", "No Vappu is complete without sima, a lightly sparkling home-made lemon and yeast drink, and tippaleipä, a lilting, yellow fried dough somebody calls funnel cake, dusted with sugar."),
        ("p", "Together with the white cap and the bonhomie, they are the unmistakable taste of spring in Finland — simple, sweet and shared."),
    ],
    [
        ("When exactly is Vappu celebrated?", "The party starts on the evening of 30 April (vappuaatto) and continues through 1 May. Both are effectively a single festival."),
        ("Do I need a white student cap to take part?", "No. Caps are traditional for graduates and many adults who keep theirs, but everyone celebrates regardless. Bring good company and a blanket — that is the real kit."),
        ("Is Vappu a children’s or adults’ holiday?", "Both. Families enjoy daytime picnics and balloons on 1 May, while students and adults own the lively evening of 30 April. Everyone finds a corner that fits."),
    ],
))

PAGES.append(page(
    "joulu", "Traditions & Celebrations",
    "Joulu: Finnish Christmas Traditions",
    "Joulu: Finnish Christmas Traditions",
    "Finnish Christmas: the Declaration of Christmas Peace, the family sauna, festive food and traditions that stretch from the 13th of December to Epiphany.",
    ["Finnish Christmas, joulu, is a family-deep, slow-burning festival that begins weeks before and keeps its hold well into January.",
     "Its most distinctive rituals — the Christmas sauna, the Declaration of Christmas Peace and a grave-candle walk on Christmas Eve — reveal a holiday balanced between light, tradition and quiet devotion."],
    [
        ("h2", "A season, not a day"),
        ("p", "Christmas in Finland unrolls across a whole season. Advent begins with the lighting of candles, and 13 December celebrates Saint Lucia’s Day, when a chosen Lucia in a white dress and candle crown sings through the winter dark."),
        ("p", "Markets open, glögi (spiced mulled wine) is served, and homes fill with the scent of gingerbread and candlelight. The mood is one of hushed anticipation, not rush."),
        ("h2", "The Declaration of Christmas Peace"),
        ("p", "On Christmas Eve at noon, in Turku — the country’s oldest town — a civic event reads the Declaration of Christmas Peace, a tradition dating back to the Middle Ages. It calls on citizens to observe the feast in peace and goodwill."),
        ("p", "Broadcast nationwide, the declaration is a poignant blend of civic duty and religion, telling a whole nation: slow down, be gentle, honour the season."),
        ("h2", "Food and the Christmas sauna"),
        ("p", "Before the meal, many families take their Christmas sauna — a calm, hot, quiet ritual that cleans both body and mind before the celebration. Christmas Eve dinner is the heart of it all."),
        ("ul", ["Rosolli (beetroot salad) and baked ham (kinkku)", "Casseroles of swede, carrot and liver", "Gravlax and herring in many forms", "Rice porridge, with one almond hidden — the finder gets a prize"]),
        ("h2", "Gifts and the day itself"),
        ("p", "In many families, Santa Claus — Joulupukki, who famously lives in Finnish Lapland — knocks on the door on Christmas Eve evening and hands out presents in person, in his red coat and cap."),
        ("p", "Christmas Day is quieter: visits, more food, and rest. Many end the day visiting cemeteries to light candles on family graves — a moving sight of row upon row of small flames in the snow."),
    ],
    [
        ("Is the main celebration on Christmas Eve?", "Yes. Christmas Eve, 24 December, carries the meal, the sauna and the gifts. Christmas Day (25th) and Boxing Day (26th) are for calm, visits and leftovers."),
        ("Where is Finland’s “real” Santa?", "The official Santa Claus Village is in Rovaniemi, Lapland, on the Arctic Circle — and Santa is so strongly Finnish that his home is often called Rovaniemi itself."),
        ("Why do Finns light candles at graves at Christmas?", "It is a tradition of remembrance and warmth against the winter dark — a quiet act of love for family members no longer present at the table."),
    ],
))

PAGES.append(page(
    "independence-day", "Traditions & Celebrations",
    "How Finland Celebrates Independence Day",
    "How Finland Celebrates Independence Day",
    "Finland’s Independence Day, 6 December: a quiet national day of candlelight, remembrance, home and the famous presidential reception.",
    ["For a country that loves silence, it is fitting that Finland’s most important national day, 6 December, is marked more by candles in windows than by fireworks in the sky.",
     "Independence Day is solemn, personal and deeply felt — a celebration of freedom won in 1917 and defended through hard decades since."],
    [
        ("h2", "A quiet national day"),
        ("p", "Until 1917 Finland was part of the Russian Empire. On 6 December 1917, the parliament declared independence. The day is observed with flags, church services and official events, but without boisterous street parties."),
        ("p", "The tone matches the national character: self-aware, respectful and reserved. People mark it at home, with family and reflection, rather than in crowds."),
        ("h2", "The presidential reception"),
        ("p", "Every 6 December, the President of Finland hosts the Independence Day reception at the Presidential Palace in Helsinki — famous as linnan juhlat, the Castle Ball."),
        ("p", "Broadcast nationwide, it shows the country’s honoured guests — from war veterans and artists to athletes and ordinary citizens who served their nation — walking through the halls in formal dress, watched by a captivated audience at home."),
        ("h2", "Candlelight at the graves"),
        ("p", "The most moving tradition is also the most Finnish: in the evening, families visit cemeteries to place two candles on the graves of their loved ones. Across the country, rows of flames glow in the darkness."),
        ("p", "This symbolises both remembrance and the small, steady flame of freedom kept burning through the night. It is dignity expressed in light."),
        ("h2", "What it means today"),
        ("p", "For Finns, the day is a quiet affirmation of independence, memory and national unity — a thing worth protecting but never boasting about."),
        ("p", "If you are invited to join an Independence Day gathering, expect candles, the national blue-and-white flag, baked food shared at home, and a thoughtful, warm evening rather than a party."),
    ],
    [
        ("Is fireworks a Finnish Independence Day tradition?", "Not really. Fireworks belong to New Year in Finland. Independence Day is candlelight, flags and quiet remembrance."),
        ("Can the public see the presidential reception?", "Not in person, but it is widely watched on television — it is something of a national ritual to follow the guests and their fashion and stories."),
        ("Is it a shop-closed public holiday?", "Yes, 6 December is a public holiday, so banks, shops and schools close. The atmosphere at home is warm and reflective."),
    ],
))

PAGES.append(page(
    "seasonal-rhythm", "Traditions & Celebrations",
    "The Seasonal Rhythm of Finnish Life",
    "The Seasonal Rhythm of Finnish Life",
    "How Finland’s four dramatic seasons — and the midnight sun, kaamos and nature’s calendar — shape daily life and culture.",
    ["In Finland, the calendar is not just a way to count days — it is a heartbeat. Each season rewrites the rhythm of food, work, sleep and social life.",
     "The extremes of light and dark, unique to this latitude, are the hidden engine behind many Finnish habits: the wintering, the summering, the coffee, the sauna and the joy of light."],
    [
        ("h2", "Four very different seasons"),
        ("p", "Finland has four genuinely distinct seasons, each with its own light, smell and etiquette. Winter is long, snowy and dark; spring arrives suddenly with light and melting; summer is open, warm and nearly sleepless; autumn brings berries, maples and a golden, melancholic glow."),
        ("p", "Seasonal food is still taken seriously: fresh potatoes and strawberries in summer, game and root vegetables in winter. Eating with the season is both tradition and good sense."),
        ("h2", "The midnight sun and kaamos"),
        ("p", "North of the Arctic Circle the sun does not set in summer — the midnight sun — and does not rise in winter, a dark period called kaamos. Even in the south, midsummer nights stay light all night in summer."),
        ("p", "This extreme light cycling is why Finns guard their vitamin D and their sleep. It also explains their intense love of both winter darkness and summer light: each gives the other meaning."),
        ("h2", "Nature’s calendar"),
        ("p", "The Finnish year is anchored to nature’s own events, which many follow closely: the return of migrating birds in spring, the ice breaking on lakes, the first berries and mushrooms, and the arrival of the first snow."),
        ("p", "Schools teach the natural year, and adults plan holidays around it — the berry season, the mushroom season and the winter swimming season all have their unofficial slots in the social calendar."),
        ("h2", "What flows from it"),
        ("ul", ["Winter: quiet, rest, indoors, dark cafés and warm food", "Spring: sudden public joy, walking outdoors, cleaning (kevät siivous)", "Summer: cottages, lakes, long days, all-night light", "Autumn: mushrooms, berries, candles, the return to routine"]),
        ("p", "This rhythm is why the same country can feel like four different places depending on the season — and why seasonal awareness is a real piece of cultural competence for anyone settling in."),
    ],
    [
        ("Which season do Finns love most?", "Summer, overwhelmingly. After the long dark, the light, warmth and lakeside freedom are treasured to an almost religious degree — despite all the love for winter sports and cosy dark."),
        ("Does the dark really affect people?", "Yes, many Finns feel the post-holiday winter lows, and the country takes light seriously — with bright indoor lighting, winter markets and the sauna year-round. Winter light therapy is common."),
        ("When is the best time to visit?", "If you want light and outdoor life, May to August. If you want the real winter — snow, northern lights, cosy dark — December to February. Each season has its own magic."),
    ],
))

# ---------------------------------------------------------------------------
# SAUNA & WELLBEING
# ---------------------------------------------------------------------------
PAGES.append(page(
    "sauna-culture", "Sauna & Wellbeing",
    "Sauna: The Soul of Finnish Culture",
    "Sauna: The Soul of Finnish Culture",
    "Why the sauna is much more than a room — the social equaliser, the ritual and the beating heart of Finnish culture.",
    ["Ask Finns what is most Finnish about Finland and many will not hesitate: sauna. It is not a luxury habit; it is as ordinary and essential as bread.",
     "There are roughly three million saunas in a country of about 5.5 million people. That fact, more than any statistic, tells you what the sauna really is."],
    [
        ("h2", "More than a room"),
        ("p", "The sauna is a small hot room of wood, heated by a stove over which water can be poured to create steam. It has existed in Finnish life for well over a thousand years — long before electricity or even chimneys."),
        ("p", "Originally a place to wash, warm and even give birth when water was scarce and winter was brutal, the sauna evolved into something cultural: a space for cleansing, healing, council and honesty."),
        ("h2", "A social equaliser"),
        ("p", "In the sauna everyone is equal. Hierarchies, titles and money are left at the door. Whether the President or the postman, all sit on the same wooden bench in the same heat."),
        ("p", "Because the sauna is naked and honest, it strips away pretense. Finns say that the best and most truthful conversations happen in the sauna — a place where people listen."),
        ("h2", "The sauna ritual"),
        ("p", "A proper Finnish sauna session has a rhythm: heat, löyly (steam), cool-down, rest, and repeat. Users throw water on the stove to raise the heat and humidity, sometimes whisk the skin softly with birch branches called vasta or vihta."),
        ("p", "Between rounds, bathers cool off — in fresh air, a cold shower, or, bravely, in a lake or a hole cut in the ice. The contrast is the point; the cycle warms and wakes the whole body."),
        ("h2", "Types of sauna"),
        ("ul", ["Smoke sauna (savusauna): the oldest, heated by a wood fire with no chimney, then aired — a soft, deep heat", "Continuous-heating sauna (kiuas): a classic wood-burning stove", "Electric sauna: the modern norm in apartments and public saunas", "Löyly-focused mobile saunas: increasingly found at festivals and lakes"]),
        ("p", "Whatever the type, the rules of calm apply: quiet respect, no phones, and great appreciation for heat honestly earned."),
    ],
    [
        ("Do Finns really sauna so often?", "Yes. Weekly sauna is the norm for many, and daily for some. It is a habit of cleanliness, relaxation and social connection — not an occasional treat."),
        ("Is the sauna a private or public thing?", "Both. Almost every home and apartment building has its own; public saunas and sauna bars are growing in popularity. Families often sauna together, with small children included."),
        ("Why do Finns say sauna is honest?", "Because everyone is equal and vulnerable in the heat, speech becomes plain. Many Finns report their deepest talks — with family, friends and even business partners — happen in the sauna."),
    ],
))

PAGES.append(page(
    "sauna-etiquette", "Sauna & Wellbeing",
    "Sauna Etiquette: The Unwritten Rules",
    "Sauna Etiquette: The Unwritten Rules",
    "The unwritten rules of the sauna, from nakedness to löyly, and how to behave so everyone feels comfortable.",
    ["The sauna has its own unspoken code, and while Finns are forgiving of newcomers, knowing the etiquette helps you relax instead of fumbling — which is exactly the point.",
     "Most of it comes down to two ideas: respect the heat, and respect the people."],
    [
        ("h2", "Nudity is normal"),
        ("p", "In a same-sex or family sauna, people are typically nude, and it is utterly normal — nobody stares, jokes or comments. A towel is often used to sit on, both for hygiene and comfort."),
        ("p", "Bringing a swimsuit is common in public mixed saunas and accepted in private ones if you prefer, though it may feel unusual to locals. Letting discomfort build is harder than simply getting used to the normal casualness."),
        ("h2", "How to behave"),
        ("p", "Keep your voice low. The sauna is a calm place, and loud chatter feels off. Sit or lie quietly, enjoy the heat, and follow the lead of the most experienced bather for how much steam and how long."),
        ("p", "Sit on a towel, be mindful of space, and never spray water around carelessly. If you are unsure about anything, simply ask — Finns are happy to explain their own tradition."),
        ("h2", "The löyly rule"),
        ("p", "Löyly — the steam thrown from a ladle over the hot stones — is an honour and a responsibility. It is usually the host or the most senior bather who throws it, and everyone else waits their turn."),
        ("p", "Do not create your own steam without invitation, and do not leave the sauna door open long enough to let the heat escape. The heat is communal property; treat it gently."),
        ("h2", "After the sauna"),
        ("p", "Shower or rinse before heading back in, especially in public saunas, where the Golden Rule is to be clean before you heat. Refreshments — water, juice or beer — are part of the session, enjoyed between rounds."),
        ("p", "Above all: the sauna is a judgement-free zone. Bodies, ages and levels of experience all belong in the heat, and the only failure is making anyone feel watched."),
    ],
    [
        ("Do I really have to go naked?", "In private and same-sex saunas, yes, that is the norm — and you will find it quickly feels natural. In mixed public saunas, swimsuits are now common, so choose the option you feel comfortable with."),
        ("Can I pour water on the stones myself?", "Wait until the host or an experienced bather does it first, then follow their lead. Uninvited löyly-throwing can feel pushy to traditionalists."),
        ("What if I find the heat too much?", "Sit lower (the heat rises), go outside or cool down, and rejoin when ready. Nobody will judge you for pacing yourself — sitting low is an art everyone uses."),
    ],
))

PAGES.append(page(
    "loyly", "Sauna & Wellbeing",
    "Löyly: The Art of Sauna Steam",
    "Löyly: The Art of Sauna Steam",
    "Löyly — the soul of the Finnish sauna: how steam is made, thrown and mastered, and why it means far more than heat.",
    ["Every sauna has heat, but only a Finnish sauna has löyly. The word is difficult to translate because it means the very essence of steam — and its spirit.",
     "When you pour water onto hot stones and the air blooms into soft, wet heat, that is löyly: at once a physics trick, an art form and a ritual."],
    [
        ("h2", "What löyly means"),
        ("p", "Löyly is not simply steam. It describes the steam as it rises toward the bathers — the humid, fragrant cloud that carries the sauna’s warmth deep into the air. In old Finnish belief, löyly was near-sacred, connected to cleansing and even health."),
        ("p", "The word even carries a hint of spirit: in ancient usage, löyly could mean the very breath or life of the sauna. That is why Finns speak of a good löyly with real respect."),
        ("h2", "Throwing the water"),
        ("p", "The classic tool is the kiuas: the stove covered in a pile of round stones. A wooden ladle (kauha) scoops water onto these stones, where it hisses instantly into steam."),
        ("p", "The technique matters. Too much water makes the heat scalding and thin; too little feels dry. Good löyly is a soft, enveloping warmth built in steady, modest doses that lap against the skin."),
        ("h2", "Managing the heat"),
        ("p", "Heat in a sauna is layered: it is hottest near the ceiling, cooler down low. Experienced bathers choose their bench by mood — high for a serious sweat, low for a gentle soak — and adjust with each round."),
        ("p", "The temperature usually sits between 70 and 100 °C, and humidity is controlled entirely by löyly. The result is a dry heat that becomes moist, deep and penetrating when the stones are wetted."),
        ("h2", "Why it matters"),
        ("ul", ["Löyly is the ritual of the sauna — the moment the whole room comes alive.", "It is shared: one person throws for everyone, and all receive it together.", "It is the difference between sweating and truly bathing — the experience Finns crave.", "It is best enjoyed slowly, in rounds, with calm, cool-downs and good company between."]),
        ("p", "Mastering löyly is not about technique alone. It is about patience — dosing, waiting, feeling — until the heat becomes something near spiritual. That is why Finns will gladly spend an evening perfecting it."),
    ],
    [
        ("What is the ideal sauna temperature?", "70–100 °C at the bench, with the exact level a matter of taste. Finns often say it is not the temperature that matters but the quality of the löyly."),
        ("What water should I use?", "Clean fresh water — preferably soft — is best. Hard or cloudy water leaves steam that feels coarser and can stain the stones."),
        ("Do I have to throw löyly at all?", "No, but in a Finnish sauna it is the normal, expected way of regulating the heat. Join in once you have watched and feel comfortable."),
    ],
))

PAGES.append(page(
    "ice-swimming", "Sauna & Wellbeing",
    "Avanto: Ice Swimming and Winter Wellness",
    "Avanto: Ice Swimming and Winter Wellness",
    "Avanto — ice swimming in a hole cut in a frozen lake: the tradition, the technique, the health benefits and the safety rules.",
    ["In winter, many Finns take a sauna — and then do something startling: they walk out into the cold and lower themselves into a hole cut through a metre of ice.",
     "This is avanto, ice swimming, a national pastime that mixes bravado with genuine calm. To the newcomer it looks extreme; to the Finn, it is a blissful, almost meditative reset."],
    [
        ("h2", "The winter tradition"),
        ("p", "Avanto has deep roots in the Nordic habit of alternating intense heat with intense cold. The classic Finnish version pairs ice swimming with the sauna: heat up, plunge in, repeat — the contrast pulsing energy through the whole body."),
        ("p", "Purpose-built facilities appear at lakes and seaside pools in winter, with changing cabins, a ladder into the hole and, always, the sauna nearby. It is social, organised and very much a community thing."),
        ("h2", "How it is done"),
        ("p", "The experienced approach is simple and safe: keep moving in the water, stay just a short time, and get out into the warmth quickly. Breathing steadily and staying calm is the whole art."),
        ("p", "Newcomers are always told: never swim alone, check the facility is professionally managed, and trust that you can leave after seconds if you wish — nobody is scoring your endurance."),
        ("h2", "Health benefits"),
        ("p", "Enthusiasts describe a remarkable afterglow: a deep calm, better sleep and a sense of clarity. Research points to benefits in circulation, mood and a general feeling of resilience in the cold."),
        ("p", "Regular practitioners often report lower stress and a cheerful tolerance of winter. But the effect is personal — some simply love the shiver that turns to warmth."),
        ("h2", "Safety rules"),
        ("ul", ["Never swim alone or in an unsupervised hole — always have help nearby", "Stay in no longer than you feel comfortable — seconds are a fine first dip", "Enter gradually and exit quickly to a warm place", "Let those with heart conditions or doubts consult a doctor — and let your body decide"]),
        ("p", "Done with respect, avanto is one of the most Finnish things there is: a small, brave act of self-care against the cold, rewarded with a warmth that no heater can match."),
    ],
    [
        ("Is ice swimming safe for beginners?", "Yes, if done properly: supervised, brief, with others, and entering gradually. The contrast is the thrill, not the length. Start with seconds, not minutes."),
        ("Do I need the sauna after?", "The sauna before and after is traditional and helps the body adjust to the cold. It also deepens the purifying ritual — heat, cold, heat."),
        ("Where can I try it?", "Municipal winter-swimming spots at lakes and seaside in Finland are common, with changing rooms and staff. Many welcome first-timers and will happily guide you through it."),
    ],
))

PAGES.append(page(
    "wellbeing-nature", "Sauna & Wellbeing",
    "Nature, Silence and Finnish Wellbeing",
    "Nature, Silence and Finnish Wellbeing",
    "Why Finns are among the world’s happiest: the forest, the silence, everyday wellbeing and the link to nature that shapes a nation.",
    ["Finland consistently ranks among the happiest countries on Earth, a fact that puzzles outsiders who picture grim winters and quiet people.",
     "The answer is not wealth or sunshine. It is a way of life built on nature, trust, simplicity and the quiet permission to rest — a recipe spelled out in everyday routines."],
    [
        ("h2", "The forest as a reset"),
        ("p", "Over 70 percent of Finland is forest, and it is woven into daily life. People walk, pick, ski and think there; the forest is a shared, open living room rather than a distant wilderness to be fenced off."),
        ("p", "Researchers call this effect green therapy. Even a short daily walk in the trees — listening, breathing, noticing — measurably lowers stress and lifts mood. Finns do it instinctively."),
        ("h2", "Silence as therapy"),
        ("p", "The Finnish comfort with silence, far from being a social weakness, is a strength for well-being. A quiet evening, a calm walk, a pause without a screen — these are treated as nourishment, not boredom."),
        ("p", "This is the flip side of the personal-space culture: Finns guard their ability to be still, and that stillness is part of why they stay level."),
        ("h2", "Everyday wellbeing"),
        ("ul", ["The daily sauna or weekly sauna ritual", "Regular time outdoors whatever the weather (there is no bad weather, only bad clothing)", "A strong coffee break as a genuine pause, not just a caffeine hit", "Trusting the state and each other lowers everyday stress", "Weekends at the cottage, in the forest or by the water"]),
        ("p", "These are not wellness trends to buy. They are ordinary habits, woven into work weeks and weekends, that add up to a steady, unglamorous well-being."),
        ("h2", "The happy-country clue"),
        ("p", "Gallup’s World Happiness Report, in which Finland tops the list, measures how people judge their lives — and Finns judge theirs highly despite cold and dark."),
        ("p", "The clue, say researchers and Finns alike: a society with high trust, free education, reliable safety nets and daily nature gives life quiet, dependable happiness — the kind that does not need to shout."),
    ],
    [
        ("Why is Finland the world’s happiest country?", "A combination of high social trust, strong public services, equality, safety and an everyday connection to nature. Happiness here is steady and unflashy rather than loud."),
        ("Does happiness mean Finns are smiley?", "No. Happiness is life satisfaction, not constant cheer. Finns are calm, reliable and content — which many would say is the more durable kind of happy."),
        ("Can I borrow the idea?", "Yes. Most of it is free: walk in nature, guard your quiet, share good tea or coffee with someone you trust, and let yourself rest. Rent it from Finnish life by spending time in Finland itself."),
    ],
))

# ---------------------------------------------------------------------------
# FOOD & DRINK
# ---------------------------------------------------------------------------
PAGES.append(page(
    "finnish-cuisine", "Food & Drink",
    "Finnish Cuisine: Simple, Honest and Fresh",
    "Finnish Cuisine: Simple, Honest and Fresh",
    "The principles of Finnish food: fresh naturals, simple honest flavours, everyday meals and seasonal eating from forest, lake and field.",
    ["Finnish cuisine does not try to impress with spice or spectacle. It aims for something older: honest ingredients, simple preparation and the flavours of a clean northern nature.",
     "Rye, fish, berries, mushrooms, wild game and potatoes form the quiet backbone of a food culture that has become rightly famous for its purity."],
    [
        ("h2", "From forest to table"),
        ("p", "Finland is a low, wide country of forests, thousands of lakes and a long, icy coast. That landscape writes the menu: lake fish like perch and vendace, Baltic herring, wild mushrooms, game and an abundance of berries."),
        ("p", "The tradition of going to pick and forage — still alive today — means much of the pantry is gathered, not grown. Everyman’s rights let anyone step into the forest and fill a basket."),
        ("h2", "Staple ingredients"),
        ("ul", ["Rye, in dark, moist sourdough breads", "Potatoes — new, waxy and beloved in summer", "Fish, especially salmon, vendace and herring", "Berries: lingonberry, blueberry, cloudberry, sea buckthorn", "Forest mushrooms, game and dairy, including the famous Finnish cheeses"]),
        ("p", "Salt is used with care, dill fresh and often, and butter a quiet hero. Fermenting, salting and preserving are old skills that still keep Nordic homes stocked through winter."),
        ("h2", "Everyday meals"),
        ("p", "The Finnish day usually starts with porridge or rye bread and coffee, moves through a warm lunch (often at school or work, where meals are free in schools), and ends with a simple home-cooked dinner: fish, meat or a vegetarian dish with salad and potatoes."),
        ("p", "Traditions like the everyday open sandwich — voileipä — keep meals unpretentious. But the standard of ingredients is high, because freshness is the real luxury."),
        ("h2", "Seasonal eating"),
        ("p", "Finns eat with the seasons by deep habit. Spring brings the first greens and silences; summer floods the table with strawberries, new potatoes and herbs; autumn offers mushrooms, game and berries; winter leans on stored root vegetables and preserved fish."),
        ("p", "The result is a cuisine that always tastes of now — simple, bright and honest, and a quietly proud answer to anyone who says northern food has no character."),
    ],
    [
        ("Is Finnish food bland?", "Not at all — it is honest. You taste the ingredients rather than the masking of them. Alongside plain favourites you will find bold flavours: strong rye, salted liquorice, fermented fish and sharp lingonberries."),
        ("What is a typical Finnish breakfast?", "Usually coffee with porridge or rye bread, sometimes with cheese, egg or cold cuts. It is quick, nourishing and built for a cold morning."),
        ("Do Finns eat reindeer everywhere?", "Reindeer is mainly a Lapland speciality, though widely available elsewhere. Everyday Finnish food is far more commonly fish, potatoes, rye and berries."),
    ],
))

PAGES.append(page(
    "rye-bread", "Food & Drink",
    "Rye Bread: The Staff of Finnish Life",
    "Rye Bread: The Staff of Finnish Life",
    "Why rye bread is the beloved staple of Finnish kitchens — the sourdough tradition, how it is eaten, and its modern renaissance.",
    ["If Finland has one national food, it is not fish or sausage — it is rye bread. Dark, dense, sour and chewy, ruisleipä has nourished Finns for over a thousand years.",
     "It appears at every meal, from school breakfasts to fine restaurant tables, and Finns hold fiercely strong opinions about which bakery makes the best."],
    [
        ("h2", "Why rye rules"),
        ("p", "Rye is demanding to grow in a short, cool, northern summer — which is exactly why it became Finland’s grain. It is hardy, feeds well and stores well, making it the dependable staff of life through long winters."),
        ("p", "Firmly rooted in this practical past, rye now carries deep cultural meaning: a thick slice of sour, dark bread is home, comfort and identity all at once."),
        ("h2", "The sourdough tradition"),
        ("p", "Finnish rye bread is traditionally fermented with a sourdough starter — never commercial yeast alone — sometimes handed down in families for generations. The result is a moist crumb and a tangy, complex flavour."),
        ("p", "The round flat loaf with a hole in the middle, reikäleipä, was born of practicality: it was threaded on poles and hung from the ceiling to dry and store. The shape survives as nostalgia and style alike."),
        ("h2", "How it is eaten"),
        ("ul", ["Fresh with butter and a slice of cheese", "Toast for the famous Finnish butter-and-cheese breakfast", "As a base for open-faced sandwiches — fish, egg or ham on top", "With soups, salads and the beloved “leipäjuusto” baked cheese"]),
        ("p", "A genuinely Finnish moment: a stack of dark rye, salted butter, and a boiled egg. Few things are more comforting."),
        ("h2", "Modern rye"),
        ("p", "The rye renaissance is real. Craft bakeries experiment with seeds, malt and long fermentation; top chefs plate rye bread alongside modern Nordic dishes; and Finns abroad hoard it in their suitcases."),
        ("p", "The health angle helps — rye’s wholegrain fibre is a celebrated part of the Finnish diet. But the real reason rye endures is simpler: it is simply, satisfyingly good."),
    ],
    [
        ("Where can I taste the best Finnish rye?", "Ask any Finn and they will name their local bakery or supermarket favourite — the debate is endless. For a gourmet version, look for a craft bakery making long-sourdough rye."),
        ("Why does Finnish rye taste sour?", "Because of slow sourdough fermentation, which gives the bread its characteristic tang and a moist, dense crumb. It is the same technique behind great sourdough everywhere."),
        ("Is rye healthier than white bread?", "Generally yes: it is dense with fibre, minerals and slow-digesting goodness that keeps you full longer. Its high fibre is part of why it is so prized in the Finnish diet."),
    ],
))

PAGES.append(page(
    "karelian-pies", "Food & Drink",
    "Karelian Pies and Savoury Classics",
    "Karelian Pies and Savoury Classics",
    "Karjalanpiirakka, the beloved Karelian pie, plus the savoury bake classics of Finland — and the egg butter that makes them complete.",
    ["Every conversation about Finnish food reaches the same golden moment: the Karelian pie. A thin rye crust folded around rice porridge (or mashed potato), baked golden and topped with egg butter.",
     "Its name honours its birthplace, the region of Karelia, and it has become the most cherished of all Finnish savoury pastries — humble, beautiful and utterly more-ish."],
    [
        ("h2", "The shape of home"),
        ("p", "The Karelian pie, karjalanpiirakka, is a small oval tart with a crimped, fluted rye edge that fans outward — a shape that looks hand-made even when machine-pressed, because it is meant to."),
        ("p", "Traditionally filled with rice porridge, and today also with potato, carrot or swede, it is the kind of food that carries the smell of real kitchens. It is eaten warm, still crisp, and is loved in ranks from school cafeterias to expensive buffets."),
        ("h2", "Making the pie"),
        ("p", "The true craft is the crust: a thin rye shell rolled almost transparently and folded into the classic crimped edge by hand. It takes patience and practice — which is why so many families buy theirs, and why the best hand-rolled ones are treasured."),
        ("p", "If you make them at home, the secret is rye flour, a steady hand, and baking hot enough to crisp the edge while the filling stays creamy. One tray is never enough."),
        ("h2", "Egg butter"),
        ("p", "The traditional accompaniment, munavoi, is simply finely chopped boiled eggs blended into soft salted butter. Spread on a warm Karelian pie it melts into a rich, savoury gloss — the classic Finnish pairing."),
        ("p", "Some add a scraping of cheese, herbs or lox for a modern twist, but purists hold that egg butter and rye are the whole point, and they are hard to argue with."),
        ("h2", "Where to find them"),
        ("ul", ["Fresh from any Finnish bakery — ask for the just-baked stack", "On breakfast buffets and at cafés across the country", "At modern restaurants plating new Nordic versions of the classic", "Frozen or fresh in supermarkets, ready to warm at home"]),
        ("p", "Wherever you get them, the honest test of a Karelian pie is simple: warm, crisp-edged, and gone before you have counted to five. That is the Finnish way to eat them."),
    ],
    [
        ("What does a Karelian pie taste like?", "A thin, slightly sour rye crust around a soft, creamy porridge filling, usually finished with the rich savoury hit of egg butter. Simple, comforting and satisfying."),
        ("Are all Karelian pies rice filled?", "Rice is the traditional filling, but potato, carrot and swede versions are all common and delicious today."),
        ("Do I eat them hot or cold?", "Warm, ideally — fresh from the oven or crisped in a pan. Cold Karelian pies are fine, but the warm ones are a different, much better dish."),
    ],
))

PAGES.append(page(
    "coffee-culture", "Food & Drink",
    "Coffee Culture: The World’s Caffeine Kings",
    "Coffee Culture: The World’s Caffeine Kings",
    "Finns drink more coffee per person than almost anyone on Earth — the coffee break, the culture and why it is a national ritual.",
    ["Finland drinks more coffee per person than any country on Earth — around 12 kilograms a year per adult. It is not a habit; it is a civilised ritual in two daily installments.",
     "Half life-saver, half social glue, the Finnish coffee break is a sacred pause built around one of the world’s great everyday drinks."],
    [
        ("h2", "The world’s heaviest coffee drinkers"),
        ("p", "Finland routinely tops the world ranking for coffee consumption per capita, ahead of Scandinavian neighbours and everyone else. The reason is cultural: coffee is rarely drunk alone or on the run — it is shared."),
        ("p", "The classic Finnish coffee is a light, medium roast, drunk black or with a little milk, brewed strong enough to taste but smooth enough to sip for an hour."),
        ("h2", "The proper coffee break"),
        ("p", "The daily kahvitauko (coffee pause) and the ritual fika-like break called kahvit on pillars of the working day. Twice a day, colleagues stop, sit, and talk over coffee — and often pulla, the cinnamon cardamom bun."),
        ("p", "The break is not a luxury; it is protected time, often meal-subsidised by employers, and skipping it entirely is rare. It is the most reliable social glue in Finnish working life."),
        ("h2", "Fika without the name"),
        ("p", "Sweden calls the coffee-and-cake pause fika; Finland simply lives it as kahvi ja pulla. A proper invitation — “come for coffee” — is a warm Finnish welcome, not a caffeine delivery."),
        ("p", "Coffee is offered on every visit, served with home baking, and understood as the natural centre of friendship, negotiation and ceremony from first dates to presidential visits."),
        ("h2", "What Finns drink today"),
        ("ul", ["Traditional filter coffee, light to medium roast, black", "Stronger dark roasts and espresso in newer café culture", "With pulla, cakes and open sandwiches on the social table", "Milky and cold variations among the next generation of coffee lovers"]),
        ("p", "Modern Finland has embraced espresso bars and specialty roasters, but the soul of its coffee culture remains the same: a strong, shared cup, slowly drunk among people who matter."),
    ],
    [
        ("Why do Finns drink so much coffee?", "It is deeply social — the coffee break is a twice-daily national ritual of connection and pause. And the light, smooth roast is built for sipping throughout the day."),
        ("What is pulla?", "A sweet, cardamom-scented braided bread or bun, beloved with coffee. It is the perfect companion to the strong Finnish cup."),
        ("Is coffee culture changing?", "Yes, a vibrant specialty scene is growing, but the classic coffee break remains central. Finns are adding craft espresso to their traditions, not replacing them."),
    ],
))

PAGES.append(page(
    "foraging-berries", "Food & Drink",
    "Foraging, Berries and the Forest Pantry",
    "Foraging, Berries and the Forest Pantry",
    "Everyman’s right to the forest: picking berries and mushrooms, the berry calendar, and the wild pantry that feeds Finnish kitchens.",
    ["Finns do not buy all their food. Vast numbers of them quietly step into the forest and pick — lingonberries, blueberries, cloudberries, chanterelles, porcini — a wild harvest that is free to anyone.",
     "Guaranteed by the historic everyman’s right, foraging is both a practical tradition and a beloved national pastime that ties the table directly to the landscape."],
    [
        ("h2", "Everyman’s right to the forest"),
        ("p", "In Finland, you may walk freely across forest and open land, and pick wild berries, mushrooms and flowers, regardless of who owns the land. This is the jokamiehenoikeus — everyman’s right — a national treasure."),
        ("p", "The rule comes with respect: no harm to nature, no entry to gardens or fenced fields, and no taking of protected species. But the berries themselves are a shared, abundant gift."),
        ("h2", "The berry calendar"),
        ("ul", ["Early summer: wild strawberries and the first blueberries", "Mid to late summer: blueberry (mustikka) in the forests", "Late summer: lingonberry (puolukka) and cranberry under the spruces", "Arctic north: the rare, golden cloudberry (lakka) in bogs"]),
        ("p", "Families return to their favourite picking patches year after year — jealously guarded spots passed down like recipes."),
        ("h2", "Mushrooms and edibles"),
        ("p", "The star mushrooms are the chanterelle (kantarelli) and the porcini (herkkutatti). Finns pick and cook them fresh in season and preserve the surplus — dried, salted or frozen — for the winter table."),
        ("p", "Safer, common and edible finds like the yellow milk cap and funnel chanterelle are also favourites. Beginners, of course, are always urged to learn from an experienced picker."),
        ("h2", "Preserving the harvest"),
        ("p", "The point of all that picking is winter. Lingonberries are made into jam to accompany everything from porridge to turkey; blueberries freeze for the winter baking; mushrooms dry and store beautifully."),
        ("p", "So the autumn harvest is a quiet act of planning ahead — the forest pantry stocked with June-to-September abundance, ready to warm Finnish kitchens all the way through the snow."),
    ],
    [
        ("Is foraging really legal everywhere in Finland?", "Yes, thanks to everyman’s right: you may pick wild berries, mushrooms and flowers on public and private land, with respect for nature and away from gardens and fenced areas. It is a cherished legal right."),
        ("When is the best berry-picking time?", "Blueberries peak in July and August, lingonberries from August into autumn, and cloudberries in the far north in July. Your local pickers will know the exact week."),
        ("Do I need to be an expert to forage safely?", "For mushrooms, yes, learn carefully from books or an experienced picker. Berries are far more forgiving, and the most common ones are easy to identify with certainty."),
    ],
))

# ---------------------------------------------------------------------------
# LANGUAGE & COMMUNICATION
# ---------------------------------------------------------------------------
PAGES.append(page(
    "finnish-language", "Language & Communication",
    "The Finnish Language: What to Know",
    "The Finnish Language: What to Know",
    "Finnish, a non-Indo-European language: the basics of its grammar, its loanwords and adaptation, and practical tips for learning.",
    ["Finnish is unlike most European languages, and its strangeness is precisely what makes it fascinating. It belongs to the Finno-Ugric family, with relatives like Estonian, Hungarian and the Sámi languages — not to the Indo-European family that includes English, German and Russian.",
     "For learners, Finnish is famously different but far from impossible; for visitors, even a handful of words and knowing their rhythms opens a warm door."],
    [
        ("h2", "A non-Indo-European language"),
        ("p", "Finnish runs on different bones than most of Europe. It has no grammatical gender, no articles, and builds meaning by adding suffixes to a word stem rather than rearranging word order."),
        ("p", "The many case endings (a dozen or more in daily use) and vowel harmony give the language its musical, precise character. Yet its spelling is beautifully faithful to its sound — words are nearly always written the way they are spoken."),
        ("h2", "Grammar at a glance"),
        ("ul", ["No gender: hän means both “he” and “she”", "No articles: talo is “a house”, “the house” or just “house”", "Rich case system: talo, talossa, talosta, talolla, talolta … (in, from, at the house)", "Vowel harmony: front and back vowels never mix within a word", "Long vowels and consonants are written double and change meaning: tuli (fire) vs. tuuli (wind) vs. tulli (customs)"]) ,
        ("p", "The key insight for English speakers: think in stems and endings, not word order. Finnish is remarkably logical once that clicks."),
        ("h2", "Loanwords and adaptation"),
        ("p", "Finnish borrows from many tongues — Swedish, Russian, German, English — and naturalises them fully: banaani (banana), politiikka (politics), juna (“train”, from the Swedish for young, as in the young railway carriages)."),
        ("p", "This loanword habit shows a culture open to the world that keeps its own grammatical engine, absorbing outside words and making them sound unmistakably Finnish."),
        ("h2", "Learning tips"),
        ("ul", ["Start with the sound: Finnish is spoken as it is written, so learning the pronunciation rules fast-tracks everything", "Learn phrases in context — travelling, shopping, saying thank you (kiitos)", "Respect the extra-long letters; doubling changes meaning completely", "Be patient: the case system takes time, but grammar is regular and there are few irregular verbs", "Use music, film and online Finnish media to meet the living language"]),
        ("p", "Above all, remember: Finns are endlessly charmed when newcomers try their language, and they will forgivingly switch to English with a smile the moment your Finnish runs out."),
    ],
    [
        ("Is Finnish really one of the hardest languages in the world?", "It is challenging for Indo-European speakers because of its different structure and case system, but its regular spelling and lack of irregular verbs make some things easier than in English, French or Russian."),
        ("Do Finns speak English?", "Very widely and well, especially among younger people. You can travel comfortably with English, but the effort to say a few Finnish words will delight people."),
        ("Does Finnish resemble any language I know?", "Closest to Estonian, then Hungarian and the Sámi languages. In the wider neighbourhood it is in a league of its own — which is part of its charm."),
    ],
))

PAGES.append(page(
    "finnish-humour", "Language & Communication",
    "Finnish Humour: Dry, Deadpan and Honest",
    "Finnish Humour: Dry, Deadpan and Honest",
    "Why Finnish humour is deadpan, self-deprecating and understated — the timing, the silence and where to find it.",
    ["Finnish humour is an acquired taste that, once acquired, is among the most beloved in the world — and it is almost the opposite of loud.",
     "It is dry, deadpan, self-deprecating, and delivered with a perfectly straight face. The punchline may be a pause, an understatement or a flat statement of the obvious."],
    [
        ("h2", "Understatement as comedy"),
        ("p", "The engine of Finnish humour is saying a great deal with very little. A Finn will describe a catastrophic blizzard as “a bit windy” and a terrible meal as “interesting” — the gap between the words and the reality is where the joke lives."),
        ("p", "Hyperbole is rare; restraint is king. The more serious the face, the funnier the line — and the audience knows to read between the syllables."),
        ("h2", "Self-deprecation"),
        ("p", "Finns laugh hard at themselves, their weather, their silence and their social awkwardness. The classic self-portrait — a quiet person, long pauses, no small talk — is a favourite target for jokes told proudly by Finns."),
        ("p", "This honesty about their own quirks is part of why Finnish humour feels so warm underneath the dry surface: it comes from a place of affectionate self-knowledge."),
        ("h2", "Timing and silence"),
        ("p", "Comfort with silence, that great Finnish skill, is the timing mechanism of the humour. A joke delivered into a thoughtful pause lands harder because of the beat before and after it."),
        ("p", "Stand-up comedians and Instagram accounts alike have spread this style worldwide, but to see it in full, watch Finns among themselves — the deadpan is contagious."),
        ("h2", "Where to hear it"),
        ("p", "Try Finnish stand-up (much of it now shared with English subtitles and captions online), classic shows, or simply sit with Finns over coffee. The humour is everywhere once you know to listen for the quiet line."),
        ("p", "Rule of thumb: if a Finn says something completely dry about how bad things are, and the room is smiling, that is comedy working exactly as intended."),
    ],
    [
        ("Why is Finnish humour so deadpan?", "Restraint and understatement are highly valued in Finnish culture. The humour lives in the quiet gap between words and reality, best told with a straight face."),
        ("Do Finns find their own silence funny?", "Yes, cheerfully so. Quietness and social awkwardness are the most beloved subjects of Finnish self-mockery."),
        ("Can a newcomer “get” Finnish humour?", "Absolutely, and preferably fast — dry humour translates well once you stop expecting the laugh to be loud. Deadpan is a global language."),
    ],
))

PAGES.append(page(
    "how-finns-communicate", "Language & Communication",
    "How Finns Communicate: Direct and Quiet",
    "How Finns Communicate: Direct and Quiet",
    "The Finnish communication style: say what you mean, value the pause, prefer text over chitchat, and listen properly.",
    ["If you want to know whether a Finn is annoyed, they will usually tell you. If you want to know whether they are happy, they may show it through quiet reliability instead of words.",
     "The Finnish communication style is direct, honest and comfortable with silence — a combination that sometimes confuses newcomers and is deeply appreciated once understood."],
    [
        ("h2", "Say what you mean"),
        ("p", "Finns value clarity over polish. A direct “no”, a clear opinion and an honest account of how a task went are all treated as respect, not bluntness. You will rarely be left guessing where you stand."),
        ("p", "This directness has limits: it is usually factual and calm rather than confrontational. Finns rarely raise their voices — they simply say what they think, then move on."),
        ("h2", "The joy of small talk (or not)"),
        ("p", "Small talk exists in Finland but is shorter, more practical and less performative than in many cultures. The weather, nature, sports and genuinely practical questions are safe, welcome topics."),
        ("p", "Forced chatter — complimenting everything, asking delicate personal questions — falls flat. Better to be sincere and brief than smooth and empty. Conversation speeds up once there is something real to say."),
        ("h2", "Written vs. spoken"),
        ("p", "Finns are famously comfortable with written communication. From official forms to heartfelt messages, the written word is an accepted, even preferred channel — it is clear and avoids the pressure of face-to-face timing."),
        ("p", "The flip side: in writing, Finns are often warmer and more open than they are in spoken small talk, because they can choose their words carefully."),
        ("h2", "Being a good listener"),
        ("p", "The pause is not a rejection; it is a Finn thinking. Silence in a conversation is actively polite — it shows you are considering what was said rather than rushing to fill the air."),
        ("p", "To communicate well with Finns: say what you mean, don’t be afraid of a pause, ask genuinely, and let them finish. You will be met with more warmth than their quiet suggests."),
    ],
    [
        ("Are Finns really as quiet as people say?", "Quiet, yes — in the sense of calm, brief and comfortable with silence — but not cold. Once trust builds, Finns are loyal, warm and surprisingly talkative within a small circle."),
        ("How do I get a Finn to open up?", "Share activities, be reliable, and respect their pace. Conversation deepens naturally over time — often in the sauna, at the cottage or over a slow coffee."),
        ("Is directness ever rude in Finland?", "Directness is normally neutral or positive here. Borne with honesty and calm, it is considered the respectful way to communicate — far better than silent resentment."),
    ],
))

PAGES.append(page(
    "dialects", "Language & Communication",
    "Finnish Dialects and Regional Identity",
    "Finnish Dialects and Regional Identity",
    "The many voices of Finnish: dialects east and west, standard versus colloquial language, and the pride regions take in their speech.",
    ["Finnish may be one language, but it speaks in many voices. Dialects — murteet — carry the history, humour and identity of regions from the Karelian east to the Ostrobothnian west.",
     "A Finn can often tell in seconds where another Finn comes from by their vowels, and that regional flavour is a source of affectionate pride, not shame."],
    [
        ("h2", "A language of many voices"),
        ("p", "The major dialect groups trace ancient settlement: western Finnish, influenced by Swedish and coastal trade, and eastern Finnish, rooted in Karelian and Savonian history. Within each, countless local shades exist."),
        ("p", "Some differences are vowel and rhythm, others vocabulary — a word for “you”, “now” or “with” can trip you from county to county. None are barriers; all are spice."),
        ("h2", "East vs. West"),
        ("p", "The eastern dialects, with their rounder vowels and Savonian drawl, are famously beloved on Finnish TV — comedies and folk comedy lean on them. The western dialects, spoken along the coast and in the south-west, are crisp and sometimes flavoured with Swedish loanwords."),
        ("p", "The far north adds the distinctive sound patterns of Lapland, and the Swedish-speaking coast keeps its own bilingual magic. Every region has its own laugh and its own endearments."),
        ("h2", "Standard vs. colloquial"),
        ("p", "Standard Finnish (kirjakieli, literally “book language”) is what is written, taught and read in official and formal speech. It is beautiful but can feel stiff in daily life."),
        ("p", "Spoken Finnish (puhekieli) is what people really say — shortened, relaxed and full of contractions and local words. The gap between them is larger than in most European languages."),
        ("h2", "Dialect pride"),
        ("p", "Finns are rarely embarrassed by their dialect; they are proud of it. Actors, musicians and comedy shows celebrate regional voices, and moving between standard and dialect is a skill many simply enjoy."),
        ("p", "For learners, one comfort: everyone understands standard Finnish, and meeting spoken Finnish is a gradual, delightful bridge from the classroom to the real street."),
    ],
    [
        ("Are Finnish dialects mutually understandable?", "Almost always, yes. Local words and accents differ enough to give away a speaker’s home region, but Finnish speakers understand one another without difficulty."),
        ("Which dialect is considered “standard”?", "Standard written and spoken Finnish is based largely on the southern/south-western dialects around Helsinki, now blended by decades of movement and media."),
        ("Must I learn a dialect to be understood?", "No. Standard Finnish works everywhere, and dialect is a welcome bonus colour, not a requirement."),
    ],
))

PAGES.append(page(
    "colloquial-finnish", "Language & Communication",
    "Colloquial Finnish: How Finns Actually Talk",
    "Colloquial Finnish: How Finns Actually Talk",
    "Puhekieli, the everyday spoken Finnish: shortened words, dropped endings and the friendly casual speech you meet in the street.",
    ["Textbooks teach beautiful standard Finnish. But step outside, and Finns are speaking puhekieli — colloquial Finnish — a faster, shorter, warmer version of the same language.",
     "Mastering a little of it means the difference between sounding like a page and sounding like a person."],
    [
        ("h2", "Puhekieli vs. kirjakieli"),
        ("p", "Kirjakieli (book language) is the careful, written standard. Puhekieli (spoken language) is the living, informal Finnish of everyday life — and nearly every Finn moves between the two all day long."),
        ("p", "The gap is striking. Where standard Finnish says the full, careful form of a word, spoken Finnish shortens, blends and relaxes it until the sound is friendlier and quicker."),
        ("h2", "Dropping and shortening"),
        ("ul", ["minä (I) becomes mä", "sinä (you) becomes sä", "minä olen (I am) becomes mä oon", "en minä tiedä (I don’t know) becomes en mä tiä", "tulla (to come) leaks into tuu, and passive “me” forms like mennään (let’s go) are everywhere"]),
        ("p", "Endings drop, vowels run together, and words like ei (no) soften the whole sentence. The pattern is consistent and, once you spot it, wonderfully friendly."),
        ("h2", "Everyday words"),
        ("p", "You will meet fillers like “joo” (yep/right), “niin” (as a warm agreement) and “just” or “justiinsa” meaning “exactly”. Greetings get shorter: “moi”, “hei” and “terve” replace the formal “hyvää päivää”."),
        ("p", "These words mark you as someone inside the conversation rather than outside it — a small vocabulary with a big effect on warmth."),
        ("h2", "Meeting it in the wild"),
        ("p", "You will hear puhekieli everywhere: the bus, the café, the office kitchen, the sauna. Scripted TV often uses it too, making series a perfect classroom."),
        ("p", "Do not be afraid to use it. Finns switch happily between standard and colloquial, understand both, and genuinely appreciate any visitor who has picked up a friendly “mä oon” or a casual “joo”."),
    ],
    [
        ("Is it rude to speak colloquial Finnish?", "No — among friends and in everyday settings it is completely natural. In very formal or official situations, standard Finnish is still expected, but spoken Finnish is not offensive anywhere."),
        ("Why is spoken Finnish so different from what I learned?", "Languages are like that: the written standard and the spoken everyday forms drift apart. For Finnish the drift is larger, but the good news is standard Finnish is understood by everyone."),
        ("Where should a beginner start?", "Learn standard Finnish properly, then add a few puhekieli touches (mä, sä, joo) as you gain confidence. Finns will smile at your effort either way."),
    ],
))

# ---------------------------------------------------------------------------
# ARTS & EVERYDAY LIFE
# ---------------------------------------------------------------------------
PAGES.append(page(
    "finnish-design", "Arts & Everyday Life",
    "Finnish Design: Function, Light and Simplicity",
    "Finnish Design: Function, Light and Simplicity",
    "Why Finnish design is world-famous: honest materials, functional clarity, the golden age and the icons that define a nation.",
    ["From the Alvar Aalto furniture studio to Marimekko patterns, Finnish design has a worldwide reputation out of all proportion to the country’s size.",
     "Its secret is a philosophy rather than a style: design should be beautiful, honest, useful and shaped by the northern light and landscape it comes from."],
    [
        ("h2", "Form follows honesty"),
        ("p", "Finnish design prizes truth in materials — the warm grain of birch, the honesty of cloth, the quiet dignity of plain functional shape. Nothing is decorated for its own sake; beauty emerges from purpose."),
        ("p", "This is the Aalto and modernist spirit: bring nature in, let function shape form, and make things people love to live with, not merely admire."),
        ("h2", "The golden age"),
        ("p", "After World War Two, Finnish design burst onto the world stage at exhibitions like the 1951 Milan Triennale, winning international prizes and attention with furniture, glass and textiles of startling elegance."),
        ("p", "Names from this era — Alvar Aalto, Tapio Wirkkala, Timo Sarpaneva, Eero Saarinen, Kaj Franck — became giants of mid-century design, their pieces still sought after worldwide."),
        ("h2", "Design icons"),
        ("ul", ["Alvar Aalto’s wooden furniture and the wave-shaped Savoy vase", "Marimekko’s bold printed textiles and its unmistakable patterns", "Iittala glassware — from the simple Aalto vase to everyday table glass", "Arabia ceramics, loved in Finnish homes for generations", "Urban contemporary pieces and the softer Nuutajärven glass atelier story"]),
        ("p", "These are not museum curiosities in Finland — they are used. Finns eat from Iittala, wear Marimekko, and sit on Aalto-inspired chairs daily."),
        ("h2", "Design in daily life"),
        ("p", "The point is that design is not a luxury layer but a daily companion. Good lighting for the dark season, a well-made wooden chair, a printed textile that lifts a room — these are considered essentials of a good Finnish life."),
        ("p", "This is why Finnish cities and homes feel calmly beautiful: design there is less about fashion and more about making everyday life better, one considered object at a time."),
    ],
    [
        ("What is Finnish design known for?", "Honest materials — especially wood, glass and textiles — functional simplicity, and a deep connection to nature and light. Think Aalto, Marimekko, Iittala and Arabia."),
        ("Why does Finnish design look so calm?", "Because it favours usefulness, restraint and good proportions over decoration. Calm is a design goal, not an accident."),
        ("Can I buy Finnish design on a budget?", "Yes. Everyday glass, ceramics, textiles and second-hand pieces of the golden age are widely affordable in Finland — and much of the charm is intended for daily use, not display only."),
    ],
))

PAGES.append(page(
    "nature-everymans-right", "Arts & Everyday Life",
    "Everyman’s Rights: Free Access to Nature",
    "Everyman’s Rights: Free Access to Nature",
    "Jokamiehenoikeus, Finland’s everyman’s right: what you may do freely in nature, where you may go, and what everyone must respect.",
    ["Few things define Finnish life more than jokamiehenoikeus — everyman’s right. It grants everyone, visitor and local alike, the freedom to roam, camp and forage across the vast Finnish landscape.",
     "It is not a law written in fine print; it is a birthright, taught to children and practised daily, rooted in respect for nature and for private property."],
    [
        ("h2", "What the right means"),
        ("p", "Everyman’s right lets you move freely on foot, ski, cycle and swim across forest and open land, and camp temporarily — regardless of ownership — as long as you do no harm. This is why Finland feels so wonderfully open."),
        ("p", "It also grants you to pick wild berries, mushrooms and flowers, and to use the local water. The right is enjoyed by everyone, which is why it is guarded with real care."),
        ("h2", "Where you may go"),
        ("ul", ["Walk, ski and cycle on forest and open land", "Camp overnight on any land, away from homes", "Swim in lakes and seas", "Pick berries, mushrooms and wildflowers", "Cross unfenced land and use established paths"]),
        ("p", "The freedom is breathtaking — but it comes with clear limits. You may not harm the environment, disturb the peace, cut growing trees, or use land in ways that trouble the owner."),
        ("h2", "What to respect"),
        ("p", "Everyman’s right has its mirror: everyman’s duty. Never enter gardens or yards, never camp beside someone’s house, never light a fire without permission or in the dry season, never litter, and never take more than you need."),
        ("p", "The right is a trust. Nature is treated as shared wealth — yours to enjoy, never yours to spoil."),
        ("h2", "Teaching at school"),
        ("p", "Finnish children learn everyman’s right at school, early and honestly, alongside lessons on nature, foraging and campcraft. By adulthood, respecting the land and the right is simply second nature."),
        ("p", "For visitors, the message is simple and joyful: step gently into the forest, take only what you will eat, and leave nothing but footprints. That is how the right stays sacred."),
    ],
    [
        ("Can I camp anywhere in Finland?", "Almost — you may camp overnight in most places, away from homes and gardens, leaving no trace. A simple, quiet overnight is the classic use of the right."),
        ("Can I make a campfire?", "Only where it is allowed and safe — never in the dry summer without permission. Many use portable stoves instead, which fall under the right more freely. When in doubt, ask."),
        ("Do I need permission to pick berries?", "No. That is the beauty of it: wild berries and mushrooms may be picked by anyone, anywhere, under everyman’s right."),
    ],
))

PAGES.append(page(
    "summer-cottage", "Arts & Everyday Life",
    "The Summer Cottage: A National Obsession",
    "The Summer Cottage: A National Obsession",
    "The Finnish kesämökki — a second home by the lake or forest — the simple rhythm, lakeside living and why it matters so much.",
    ["Somewhere out in the Finnish countryside, by a lake or in the forest, most Finnish families have a small piece of heaven: the kesämökki, the summer cottage.",
     "Over half a million cottages dot the country, and their importance rivals anything in Finnish culture. The cottage is where Finns go to live a simpler, quieter version of life."],
    [
        ("h2", "A second home in nature"),
        ("p", "The summer cottage usually has few comforts by modern standards: a wood stove, an outhouse, sometimes no electricity. That is the whole point — the cottage strips life back to its warm essentials."),
        ("p", "Weekends and summer weeks are spent there: swimming, fishing, sauna, berry-picking, reading, and simply being together. It is the antidote to the thinking, connected world."),
        ("h2", "The simple rhythm"),
        ("p", "The cottage day is slow on purpose. Morning coffee on the terrace, a row across the lake, a lunch of fresh fish or soup, an afternoon nap in a hammock, an evening sauna and a moonlit swim."),
        ("p", "Phones are often ignored, shops are far, and the gravitational pull of the city is wonderfully distant. Rest is treated as serious business — as it should be in a culture that prizes calm."),
        ("h2", "Lakeside living"),
        ("p", "Finland has around 188,000 lakes, and most cottages sit on a shore. The water is the heart of the experience: swimming, boating, and after the sauna, the traditional plunge into the cool lake."),
        ("p", "The sauna by the water is nearly mandatory at a proper mökki — heat, steam, a cold dip, repeat — a ritual that both cleans and deeply relaxes."),
        ("h2", "What it means"),
        ("ul", ["A return to nature and simple living", "Family time without screens and without hurry", "Roots and heritage, often passed down through generations", "The famous Finnish permission to be quiet and rest"]),
        ("p", "The cottage is not a holiday destination so much as a way of being. For Finns it is one of the clearest expressions of their bond with nature — and their best remedy for restoring it."),
    ],
    [
        ("Do I need to be invited to experience a cottage?", "Renting a cottage is common and easy — rental companies and municipal options offer every price range. A genuine “come to the mökki” invitation from a Finn is a high honour; accept it warmly."),
        ("What should I bring to a cottage?", "Practical things: warm clothes (even in summer the evenings cool), swimwear, a good book, food to share, and an open mind for simple living. The cottage provides the lake and the calm."),
        ("Why does the cottage matter so much in Finland?", "It is the place where Finns reconnect with nature, family and their own quiet — a deeply held national source of well-being and identity."),
    ],
))

PAGES.append(page(
    "music-and-arts", "Arts & Everyday Life",
    "Music, Film and the Arts in Finland",
    "Music, Film and the Arts in Finland",
    "From Sibelius to sauna metal: Finland’s music, cinema, literature and cultural life — and the festivals that bring a quiet nation alive.",
    ["Few small countries have punched so far above their weight in culture as Finland. Its classical heritage, cutting-edge music and distinctive film and literature have reached a global audience.",
     "The same calm, northern culture that values silence also produces some of the world’s most expressive and dramatic art — the two extremes feed one another."],
    [
        ("h2", "A sound identity"),
        ("p", "Jean Sibelius gave Finland its musical soul with works built from the landscape and national feeling — symphonies and the tone poem Finlandia that became a kind of aural national anthem. His house and his music remain pilgrimage sites."),
        ("p", "Finland’s classical scene is small but remarkably deep, producing conductors, orchestras and composers of world standing from a tiny population. Music education in schools is serious and inclusive."),
        ("h2", "From sauna metal to classical"),
        ("p", "Finland is famed for heavy metal — more bands per capita than almost anywhere — with an irony its people enjoy: the quietest country makes some of the loudest music."),
        ("p", "Beyond metal, Finns rule pop with world-conquering acts, produce cherished film, and run one of the world’s great design traditions. The range is the point: restraint and roar coexist comfortably."),
        ("h2", "Film and literature"),
        ("p", "Finnish cinema and literature tell the nation’s tales with dark humour, honesty and love of the landscape — from the beloved Moomins of author Tove Jansson to award-winning contemporary novels and films."),
        ("p", "The Moomins especially have crossed every border, charming children and adults alike with their quiet, kind, slightly melancholy world — a perfect cartoon of Finnish temperament."),
        ("h2", "Festivals and venues"),
        ("ul", ["Sibelius and chamber music festivals in the summer", "World-class opera and symphony seasons in Helsinki and Turku", "Rock, metal and pop festivals under the midnight sun", "Cinema festivals and literary events in the long, warm evenings"]),
        ("p", "The year is dotted with culture: outdoor concerts, festival tents, and summer theatres. For a nation known for quiet, Finns know how to gather — and when the music starts, they really listen."),
    ],
    [
        ("Why is Finland so strong in heavy metal?", "Theories abound — the dark winters, the low population density, a fierce do-it-yourself streak — but the simple fact stands: Finns love it and do it brilliantly. The irony with their quiet nature is part of the charm."),
        ("Who are the most famous Finnish artists?", "Sibelius in classical music, Tove Jansson (Moomin creator), award-winning directors like Aki Kaurismäki, and countless bands from Nightwish and HIM to Apocalyptica. The list is long for such a small country."),
        ("Is culture central to Finnish life?", "Very much so. Public libraries are heavily used, music is taught at school, museums are supported, and festivals are a national passion. Culture is treated as a public good."),
    ],
))

PAGES.append(page(
    "everyday-social-life", "Arts & Everyday Life",
    "Everyday Social Life in Finland",
    "Everyday Social Life in Finland",
    "How everyday social life works in Finland: work friendships, invitation etiquette, sports and clubs, and the guest rules to know.",
    ["Everyday social life in Finland is not a loud stage; it is built in small, reliable moments — the coffee break, the hobby club, the sauna invitation, the shared swim.",
     "Once you know where friendship lives here, the country opens up enormously. Connection grows from shared activities and trust, not from speed."],
    [
        ("h2", "Work and social life"),
        ("p", "The workplace is a genuine social arena in Finland. The twice-daily coffee break, staff lunches and occasional after-work activities (sauna nights, game evenings, weekend trips) build real bonds among colleagues."),
        ("p", "Work friendships may start reserved but deepen through reliability and shared tasks. A Finn who helps you without being asked is showing trust — a big signal."),
        ("h2", "Invitations and hosting"),
        ("p", "An invitation to a Finnish home is a real honour, and appearing on time with a small gift (flowers, wine or something local) is warmly received. Hosts take care of their guests; guests are expected simply to enjoy and be themselves."),
        ("p", "Shoes are left at the door, so bring warm socks — a small detail that wins immediate goodwill in a country of snowy, muddy winters."),
        ("h2", "Sports and clubs"),
        ("p", "A huge part of Finnish social life runs through communities of interest: sports clubs, choirs, book circles, cooking classes, walking groups, sailing and, of course, sauna societies."),
        ("p", "Joining one is famously the fastest and best way to make friends. In Finland, doing something together is far more natural than meeting just to talk — the activity is the social glue."),
        ("h2", "Guest etiquette"),
        ("ul", ["Arrive on time and remove shoes at the door", "Bring a small gift when invited to a home", "Bring your own towel and be ready for the sauna if offered", "Say thank you (kiitos) with feeling for the meal and the company", "Dress comfortable and casual — Finnish hosting rarely demands formal dress"]),
        ("p", "The golden rule is simple: be genuine, do your share, and respect a little quiet. Do that and Finns will quietly, reliably, and deeply welcome you into their world."),
    ],
    [
        ("How do I make Finnish friends?", "Through shared activities — a club, a sport, volunteering, a course — and through repeated, reliable presence. Friendships build slowly and last long once trust is earned."),
        ("Is it rude to arrive without a gift?", "Not rude, but a small gift is appreciated — flowers, wine, or something food-related are perfect. The thoughtfulness matters far more than the value."),
        ("Do Finns hug or kiss cheeks when greeting?", "Usually a firm handshake and eye contact, not hugging. Save hugs for genuinely close friends or occasions — proximity grows, it does not begin."),
    ],
))

# ---------------------------------------------------------------------------
# Homepage metadata (content is written by the generator directly, but keep
# the category listing authoritative here so the generator stays in sync).
# ---------------------------------------------------------------------------
HOMEPAGE = {
    "title": "Finnish Culture: A Guide to Values, Traditions and Everyday Life",
    "meta": "A practical guide to Finnish culture — sisu, values, traditions, sauna, food, language, design and everyday life.",
}