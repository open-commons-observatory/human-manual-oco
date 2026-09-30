#!/usr/bin/env python3
"""seed.py - one-off content loader for the SIBO/SIFO first topic. Not part of the TAD engine
(.tad/): this is repo-local content-authoring tooling, run once, then discarded/reused for the
next topic. Builds data/ from data/schema.sql + the Python literals below, via the exact same
DuckDB IMPORT/EXPORT DATABASE mechanism .tad/tools/dc.py canon uses, so the result is byte-
identical to what `make canon` would produce from equivalent INSERT statements.
"""
import duckdb

con = duckdb.connect()
con.execute(open("data/schema.sql").read())

# ---------------------------------------------------------------- sources
SOURCES = [
    # id, title, url, author, year
    ("acg-sibo-2020", "ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth",
     "https://doi.org/10.14309/ajg.0000000000000501", "Pimentel M, Saad RJ, Long MD, Rao SSC", 2020),
    ("merck-sibo", "Small Intestinal Bacterial Overgrowth (SIBO) - Merck Manual Professional Edition",
     "https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/small-intestinal-bacterial-overgrowth-sibo",
     "Merck Manual Professional Edition", None),
    ("amboss-sifo", "Small intestinal fungal overgrowth - AMBOSS",
     "https://www.amboss.com/us/knowledge/small-intestinal-fungal-overgrowth", "AMBOSS", None),
    ("nutrients-2025-sibo-sifo", "Small Intestinal Bacterial and Fungal Overgrowth: Health Implications and Management Perspectives",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC12030604/", None, 2025),
    ("chedid-2014-herbal", "Herbal Therapy Is Equivalent to Rifaximin for the Treatment of Small Intestinal Bacterial Overgrowth",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC4030608/",
     "Chedid V, Dhalla S, Clarke JO, Roland BC, Dunbar KB, Koh J, Justino E, Tomakin E, Mullin GE", 2014),
    ("brief-sibo-protocol", "Berberine and rifaximin effects on small intestinal bacterial overgrowth: study protocol (BRIEF-SIBO)",
     "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9974661/", "Guo H, Lu S, Zhang J, Chen C, Du Y, Wang K, Duan L", 2023),
    ("dyspepsia-cam-review", "Complementary and alternative treatment in functional dyspepsia",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC5802680/", None, None),
    ("biofilm-disruption-2025", "Biofilm Disruption Enhances Antimicrobial Therapy for SIBO and Intestinal Methanogen Overgrowth",
     "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12701763/", None, 2025),
    ("jhr-classic", "Recurrent Jarisch-Herxheimer reaction in a patient with Q fever pneumonia: a case report",
     "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2621130/", "Aloizos S, Gourgiotis S, Oikonomou K, Stakia P", 2008),
    ("sibo-critical-appraisal-2024", "Critical appraisal of the SIBO hypothesis and breath testing: a clinical practice update endorsed by ESNM and ANMS",
     "https://onlinelibrary.wiley.com/doi/10.1111/nmo.14817", "Kashyap PC, et al.", 2024),
    ("aga-belching-2023", "AGA Clinical Practice Update on Evaluation and Management of Belching, Abdominal Bloating, and Distention: Expert Review",
     "https://www.gastrojournal.org/article/S0016-5085(23)00823-5/fulltext", None, 2023),
    ("sgb-pathogenesis-review", "Supragastric belching: Pathogenesis, diagnostic issues and treatment",
     "https://pmc.ncbi.nlm.nih.gov/articles/PMC9212115/", None, None),
]
for id_, title, url, author, year in SOURCES:
    con.execute("INSERT INTO sources VALUES (?,?,?,?,?)", [id_, title, url, author, year])

# ---------------------------------------------------------------- topics
# id, name_ru, name_en, summary_ru, summary_en, narrative_ru, narrative_en, order_key, tags
# narrative_* is long-form flowing prose (the "story" reading path); summary_* stays short, for
# nav lists. Same underlying facts, two independently-editable views - narrative paragraphs link
# out to the topic's own fact page with {{ "..." | relative_url }} the same way render_manual.py
# links elsewhere, since these strings get written verbatim into rendered .md and pass through
# Jekyll's Liquid processing on-site.
TOPICS = [
    ("sibo-sifo-overview", "Обзор: СИБР и СИФО", "Overview: SIBO and SIFO",
     "Механизм, из-за которого бактерии и грибки толстой кишки заселяют обычно малонаселённую тонкую кишку, и почему это меняет то, что происходит с едой.",
     "The mechanism by which colon-dwelling bacteria and fungi colonise the normally sparsely populated small intestine, and why that changes what happens to food.",
     "Наверное, вы замечали за собой что-то из этого. Живот раздувается почти сразу после еды — будто внутри надули шарик. Изжога возвращается снова и снова, хотя вы вроде бы не ели ничего «такого». То запор на несколько дней, то, наоборот, внезапный жидкий стул через полчаса после завтрака. А иногда к этому добавляются вещи, которые на первый взгляд вообще ни при чём: скачки сахара без видимой причины, новая аллергия на еду, которую вы всю жизнь ели без проблем, туман в голове, который списывают на «стресс» и «недосып».\n\nСтандартный маршрут в такой ситуации — это хождение по разным кабинетам. Гастроэнтеролог смотрит на изжогу отдельно, аллерголог — на новую аллергию отдельно, эндокринолог — на сахар отдельно, и каждый честно лечит свой кусочек, потому что именно из его кабинета проблема выглядит изолированной. На выходе — набор диагнозов, которые не складываются в одну картину.\n\nЗаметная часть этой связки объясняется одним физиологическим узлом: избыточным ростом микроорганизмов там, где их в норме почти нет — в тонкой кишке. Толстая кишка населена бактериями плотно и намеренно, это нормальная часть пищеварения. Тонкая — совсем другое дело: у здорового человека там почти пусто, и держат её такой два барьера. Первый — кислотность желудка, которая обеззараживает всё, что идёт дальше (и да, это тот самый ирония: длительный приём препаратов от изжоги подавляет именно этот барьер). Второй — [мигрирующий моторный комплекс]({{ \"/ru/protocol-prokinetics.html\" | relative_url }}) (ММК), волна сокращений, которая между приёмами пищи выметает из тонкой кишки всё лишнее.\n\nЕсли один из этих барьеров ослаблен — подавлена кислотность, нарушена моторика, есть спайки после операций, диабет или другие факторы риска, — бактерии и грибки из толстой кишки постепенно заселяют тонкую. И еда, которая должна всасываться вами, начинает частично сбраживаться ими же.",
     "You've probably noticed some of this in yourself. Your stomach bloats almost right after eating, like a balloon inflating inside you. Heartburn keeps coming back even though you haven't eaten anything unusual. Constipation for days, then, just as suddenly, urgent loose stools half an hour after breakfast. And sometimes things that seem entirely unrelated pile on top: blood-sugar swings with no obvious cause, a new allergy to a food you'd eaten your whole life without trouble, brain fog that gets written off as \"stress\" or \"not enough sleep\".\n\nThe standard route from here is a tour of specialists. A gastroenterologist looks at the heartburn on its own, an allergist at the new allergy on its own, an endocrinologist at the sugar on its own - and each of them treats their own slice honestly, because from their chair the problem genuinely looks isolated. What you end up with is a pile of diagnoses that never quite add up to one picture.\n\nA meaningful part of that cluster is explained by one physiological hinge: an overgrowth of microorganisms somewhere that's normally almost empty - the small intestine. The colon is densely, deliberately populated with bacteria; that's a normal part of digestion. The small intestine is a different story: in a healthy person it's nearly sterile, kept that way by two barriers. The first is stomach acid, which sterilises whatever passes further down (and here's the irony worth sitting with: long-term use of heartburn medication suppresses exactly this barrier). The second is the [migrating motor complex]({{ \"/en/protocol-prokinetics.html\" | relative_url }}) (MMC), a wave of contractions that sweeps the small intestine clean between meals.\n\nWhen either barrier weakens - acid suppressed, motility disrupted, post-surgical adhesions, diabetes, or other risk factors - bacteria and fungi from the colon gradually colonise the small intestine. And food that should be absorbed by you starts being partly fermented by them instead.",
     10, ["gi", "overview"]),
    ("hydrogen-sibo-markers", "Маркеры водородного СИБР", "Hydrogen-dominant SIBO markers",
     "Что именно диагностируется как «водородный СИБР» и на какие самонаблюдения это похоже.",
     "What is actually diagnosed as hydrogen-dominant SIBO, and what it tends to feel like day to day.",
     "Ближе всего к описанию из первого абзаца — вариант с преобладанием водородобразующих бактерий. Классическая картина: съели яблоко, кусок хлеба или что-то ещё, богатое ферментируемыми углеводами — и через 15–30 минут живот заметно раздуло. Дальше — активное, иногда болезненное газообразование и нередко резкий, срочный позыв в туалет: стенки кишки перерастянуты газом, и организм торопится всё сбросить.\n\nДиагностируется это дыхательным тестом: пациент выпивает раствор глюкозы или лактулозы, и если водород в выдыхаемом воздухе поднимается достаточно резко в первые полтора часа — это и есть искомый маркер. Симптомокомплекс (вздутие, боль, газы, диарея после еды) настолько устойчиво с этим ассоциируется, что вошёл в официальные гастроэнтерологические рекомендации, а не только в блоги о питании.\n\nСама скорость реакции здесь не случайна и не преувеличена — она прямо отражает то, что и измеряет тест. У здорового человека путь еды до толстой кишки, где бактерий много и они интенсивно бродят, занимает в среднем 70–90 минут; поэтому именно ранний, а не поздний подъём водорода/метана и считается признаком того, что брожение произошло раньше срока — то есть ещё в тонкой кишке. Стабильно повторяющийся день за днём быстрый (15–30 минут) отклик именно на определённые продукты, с одним и тем же характером ощущений — это не «размытый» симптом, а сигнал с понятной физиологической логикой за собой.\n\nОднако у этой логики есть важная и совсем свежая оговорка. Авторитетный клинический разбор 2024 года (одобренный европейским и американским обществами нейрогастроэнтерологии) указывает: тот же самый ранний подъём водорода можно объяснить не только избытком бактерий в тонкой кишке, но и попросту быстрым транзитом — если еда добралась до толстой кишки быстрее обычных 70–90 минут, брожение там начнётся раньше при полностью нормальном количестве бактерий в самой тонкой кишке. Отличить «бактерий много» от «транзит быстрый» по одним ощущениям, и даже по стандартному дыхательному тесту, не всегда возможно — это признанная методологическая проблема, а не придирка. Устойчивость и специфичность паттерна по-прежнему говорит в пользу того, что процесс реальный и понятный, но окончательно определить именно его причину без теста (а иногда и с тестом) непросто. [Подробнее о критериях и источниках →]({{ \"/ru/hydrogen-sibo-markers.html\" | relative_url }})",
     "Closest to the picture in the opening paragraph is the hydrogen-dominant variant. The classic pattern: you eat an apple, a slice of bread, anything rich in fermentable carbohydrate - and 15-30 minutes later your stomach is visibly distended. What follows is active, sometimes painful gas production and often a sudden, urgent need for the toilet: the gut wall is overstretched by gas, and the body rushes to empty itself.\n\nThis is diagnosed with a breath test: the patient drinks a glucose or lactulose solution, and if exhaled hydrogen rises sharply enough within the first ninety minutes, that's the marker being looked for. The symptom cluster - bloating, pain, gas, diarrhoea after eating - is consistently enough associated with it to have made it into formal gastroenterology guidelines, not just nutrition blogs.\n\nThe speed of the reaction itself isn't incidental or exaggerated - it directly reflects what the test measures. In a healthy person, food normally takes 70-90 minutes to reach the colon, where bacteria are dense and ferment actively; that's exactly why an early, not a late, rise in hydrogen or methane is taken as a sign that fermentation happened ahead of schedule - still in the small intestine. A fast (15-30 minute) response to specific foods, recurring day after day with the same character of sensation, isn't a vague symptom - it's a signal with real physiological logic behind it.\n\nBut that logic comes with an important, very recent caveat. An authoritative 2024 clinical practice update (endorsed by the European and American neurogastroenterology societies) points out that the same early hydrogen rise can also be explained not by bacterial excess in the small intestine but simply by fast transit - if food reaches the colon faster than the usual 70-90 minutes, fermentation there starts early even with a completely normal bacterial count in the small intestine itself. Telling \"too many bacteria\" apart from \"fast transit\" by feel alone, or even with a standard breath test, isn't always possible - that's a recognised methodological problem, not nitpicking. The consistency and specificity of the pattern still argues that something real and identifiable is going on; pinning down exactly which cause it is, without testing (and sometimes even with it), is the harder part. [More on the criteria and sources →]({{ \"/en/hydrogen-sibo-markers.html\" | relative_url }})",
     20, ["gi", "diagnosis"]),
    ("methane-imo-markers", "Маркеры метанового СИБР (IMO)", "Methane / IMO markers",
     "Почему метановый вариант официально переименован в IMO и чем он отличается от водородного.",
     "Why the methane variant was formally renamed IMO, and how it differs from the hydrogen variant.",
     "Прямая противоположность по симптому — не понос, а стойкий запор, часто с ощущением тяжести в животе даже натощак и характерным «туманом в голове» по утрам. Долгое время это называли «метановым СИБР», но название оказалось неточным: газ действительно метан, но производят его не бактерии, а совсем другой домен жизни — археи-метаногены. Поэтому современные гайдлайны используют более точный термин — IMO, избыточный рост метаногенов, — и это не игра в слова: раз источник другой, логично, что и подход к лечению может отличаться. Связь между избыточным метаном и замедленным транзитом признана достаточно, чтобы тестирование на метан официально рекомендовали именно пациентам с хроническим запором. [Подробнее →]({{ \"/ru/methane-imo-markers.html\" | relative_url }})",
     "The mirror image, symptom-wise: not diarrhoea but persistent constipation, often with a heavy feeling in the stomach even on an empty one, and a characteristic morning brain fog. This was long called \"methane SIBO\", but the name turned out to be imprecise: the gas really is methane, but it's produced not by bacteria but by an entirely different domain of life - methanogenic archaea. Modern guidelines therefore use the more accurate term IMO, intestinal methanogen overgrowth - and that's not just semantics: a different source reasonably means a different treatment logic. The link between excess methane and slow transit is recognised enough that methane testing is formally recommended specifically for patients with chronic constipation. [More →]({{ \"/en/methane-imo-markers.html\" | relative_url }})",
     30, ["gi", "diagnosis"]),
    ("sifo-candida-markers", "Маркеры СИФО (грибковый перерост)", "SIFO (fungal overgrowth) markers",
     "Наименее устоявшийся из трёх диагнозов: что о нём известно и что остаётся спорным.",
     "The least settled of the three diagnoses: what is known about it and what remains disputed.",
     "Третий, самый спорный участник этой троицы — грибковый перерост, чаще всего дрожжами рода Candida. Узнаваемая картина: почти наркотическая тяга к сладкому и выпечке, белый налёт на языке по утрам, отрыжка без запаха, вздутие в самом низу живота. Проблема в том, что само существование этого диагноза как отдельной клинической единицы — предмет открытого спора: единого протокола диагностики нет, а симптомы почти полностью перекрываются с обычным бактериальным СИБР, так что отличить одно от другого без специфического анализа по одним ощущениям невозможно. Это не значит, что явления не существует — скорее что доказательная база здесь заметно тоньше, чем у первых двух пунктов. [Подробнее →]({{ \"/ru/sifo-candida-markers.html\" | relative_url }})",
     "The third and most disputed member of the trio: fungal overgrowth, usually Candida yeasts. The recognisable picture: an almost compulsive craving for sugar and baked goods, a white coating on the tongue in the morning, odourless burping, bloating low in the abdomen. The catch is that the existence of this diagnosis as its own clinical entity is genuinely disputed: there's no standardised diagnostic protocol, and the symptoms overlap almost completely with ordinary bacterial SIBO, so the two can't be told apart by feel alone without specific testing. That doesn't mean the phenomenon doesn't exist - just that the evidence base here is noticeably thinner than for the first two. [More →]({{ \"/en/sifo-candida-markers.html\" | relative_url }})",
     40, ["gi", "diagnosis", "candida"]),
    ("belching-differential", "Отрыжка без запаха — чаще другой механизм", "Odorless belching - usually a different mechanism",
     "Почему повторяющаяся весь день отрыжка воздухом без запаха обычно объясняется не бактериями кишечника, а отдельным пищеводным механизмом.",
     "Why all-day, odorless air belching is usually explained not by gut bacteria but by a separate oesophageal mechanism.",
     "Второй симптом стоит разобрать отдельно, потому что интуитивно он кажется частью той же картины, а по механизму обычно ей не является. Отрыжка воздухом без запаха, повторяющаяся весь день и усиливающаяся через 20–30 минут после еды, — это не типичный портрет бактериального брожения. У брожения (что водородного, что метанового) газ движется вниз и наружу — вздутие, флатуленция, при водородном варианте нередко диарея; путь газа вверх и через рот при этом не главный.\n\nПовторяющаяся отрыжка — отдельно классифицированный в современной гастроэнтерологии феномен, супрагастральная отрыжка: воздух засасывается в пищевод и тут же выталкивается обратно, не успевая дойти ни до желудка, ни тем более до кишечника. Это не переваривание и не брожение — это, по сути, мышечный паттерн пищевода, который может закрепляться как привычка и чаще встречается у людей с тревожностью. От истинного заглатывания воздуха (аэрофагии, при которой воздух всё же доходит до кишечника и даёт вздутие и флатуленцию, а не отрыжку как главный симптом) и тем более от бактериального брожения это отличается и по ощущению, и по происхождению, хотя со стороны выглядит похоже. Официально отличить одно от другого можно только импедансометрией пищевода, но сам факт, что жалоба — преимущественно отрыжка, а не вздутие и не изменения стула, — уже смещает вероятность в сторону этого, а не кишечного механизма. [Подробнее →]({{ \"/ru/belching-differential.html\" | relative_url }})",
     "This second symptom deserves separate treatment, because intuitively it feels part of the same picture, but mechanistically it usually isn't. Odorless air belching, recurring all day and picking up 20-30 minutes after eating, isn't a typical portrait of bacterial fermentation. With fermentation (hydrogen or methane variant alike), gas moves down and out - bloating, flatulence, often diarrhoea in the hydrogen variant; the route up and out through the mouth isn't the main one.\n\nRecurring belching is its own, separately classified phenomenon in current gastroenterology: supragastric belching. Air is sucked into the oesophagus and pushed straight back out, without ever really reaching the stomach, let alone the intestine. It isn't digestion or fermentation at all - it's essentially an oesophageal muscular pattern that can become a learned habit, more common in people with anxiety. It differs, both in how it feels and in where it comes from, from true air-swallowing (aerophagia, where the air does reach the intestine and produces bloating and flatulence rather than belching as the main symptom) and even more so from bacterial fermentation, even though from the outside they can look alike. Formally telling them apart requires oesophageal impedance monitoring, but the fact that the complaint is mainly belching, not bloating or altered stools, already shifts the odds toward this mechanism rather than a gut one. [More →]({{ \"/en/belching-differential.html\" | relative_url }})",
     45, ["gi", "diagnosis", "differential"]),
    ("systemic-consequences", "Системные последствия", "Systemic consequences",
     "Какие claims о вторичных эффектах (проницаемость, панкреатит, аллергии) подтверждены, а какие нет.",
     "Which claims about downstream effects (permeability, pancreatitis, new allergies) are supported, and which are not.",
     "Именно на этом уровне и начинают появляться те самые «несвязанные» жалобы из хождения по врачам. Логика, которую можно встретить в популярных источниках: перерастянутая газом и колониями бактерий стенка кишки повреждается, становится более проницаемой, недопереваренные фрагменты белка попадают в кровоток — и иммунная система реагирует на них как на чужеродные, отсюда внезапные пищевые реакции и гистаминовая непереносимость. Механизм правдоподобен и активно изучается, но нужно быть честными: убедительных доказательств того, что именно эта цепочка реализуется у типичного человека с СИБР, пока недостаточно — это скорее гипотеза, чем установленный факт.\n\nЕщё жёстче стоит сказать про одно конкретное утверждение: что вздутие регулярно вызывает спазм особого клапана между желчными протоками и кишечником (сфинктера Одди) и вторичный панкреатит. Мы специально искали подтверждение этому в проверенной гастроэнтерологической литературе — и не нашли. Как регулярное, ожидаемое осложнение СИБР это утверждение ничем не подкреплено. [Подробнее и источники →]({{ \"/ru/systemic-consequences.html\" | relative_url }})",
     "This is where those \"unrelated\" complaints from your tour of specialists start to make sense. The logic you'll find in popular sources runs like this: a gut wall overstretched by gas and bacterial colonies gets damaged, becomes more permeable, undigested protein fragments enter the bloodstream, and the immune system reacts to them as foreign - hence sudden food reactions and histamine intolerance. The mechanism is plausible and actively studied, but honestly: solid evidence that this exact chain plays out in a typical SIBO patient is still lacking - it's a hypothesis, not an established fact.\n\nOne specific claim deserves a firmer word: that bloating routinely causes spasm of the valve between the bile ducts and the intestine (the sphincter of Oddi) and secondary pancreatitis. We specifically looked for support for this in the gastroenterology literature we could verify - and found none. As a routine, expected SIBO complication, this claim is unsupported. [More and sources →]({{ \"/en/systemic-consequences.html\" | relative_url }})",
     50, ["gi", "systemic"]),
    ("protocol-overview", "Протокол эрадикации: обзор этапов", "Eradication protocol: stage overview",
     "Общая структура пятиэтапного фито-протокола и то, насколько каждый этап клинически обоснован.",
     "The overall structure of the five-stage phytotherapy protocol, and how well-evidenced each stage actually is.",
     "Если картина выше показалась знакомой — логичный следующий вопрос: что с этим вообще можно сделать. Распространённый в интегративной и функциональной медицине ответ — пятиэтапный фито-протокол: сначала разрушить защитную биоплёнку патогенов, затем эрадицировать их растительными антимикробными средствами, справиться с реакцией организма на их массовую гибель, восстановить моторику кишечника прокинетиками и, наконец, залечить саму слизистую. Структура внутренне логичная и последовательная. Вопрос, который стоит задавать на каждом этапе, — не «звучит ли это разумно», а «что именно из этого подтверждено исследованиями на людях, а что — экстраполяция из смежной области». Дальше — по каждому этапу отдельно, без сглаживания в обе стороны.",
     "If the picture above felt familiar, the obvious next question is what can actually be done about it. A common answer in integrative and functional medicine is a five-stage phytotherapy protocol: first disrupt the pathogens' protective biofilm, then eradicate them with herbal antimicrobials, manage the body's reaction to their mass die-off, restore gut motility with prokinetics, and finally heal the mucosa itself. The structure is internally logical and sequential. The question worth asking at every stage isn't \"does this sound reasonable\" but \"what part of this is backed by human trials, and what's an extrapolation from an adjacent field\". What follows goes stage by stage, without softening in either direction.",
     60, ["gi", "protocol"]),
    ("protocol-biofilm", "Этап 1 — разрушение биоплёнки", "Stage 1 - biofilm disruption",
     "Что такое биоплёнка в этом контексте и насколько доказана польза от её целенаправленного разрушения.",
     "What a biofilm is in this context, and how well-proven the benefit of deliberately disrupting it actually is.",
     "Биоплёнка — это не метафора, а вполне конкретная структура: сообщество микробных клеток, укрытое общим полисахаридным матриксом, как городом под одной крышей. Идея в том, что пока эта «крыша» цела, антимикробным веществам труднее добраться до клеток внутри, поэтому логично сперва её разрушить — например, N-ацетилцистеином, — а уже потом переходить к уничтожению патогенов. Механически рассуждение убедительное, и оно действительно обсуждается в свежих научных обзорах по СИБР и IMO. Но между «звучит логично» и «доказано, что улучшает результат у людей» есть разница: исследований, которые бы напрямую сравнили эту последовательность с обычным приёмом антимикробных средств без неё, пока попросту мало. [Подробнее →]({{ \"/ru/protocol-biofilm.html\" | relative_url }})",
     "A biofilm isn't a metaphor, it's a fairly literal structure: a community of microbial cells sheltered under a shared polysaccharide matrix, like a city under one roof. The idea is that while that \"roof\" is intact, antimicrobials have a harder time reaching the cells inside, so it's logical to disrupt it first - with N-acetylcysteine, for instance - before moving on to killing the pathogens. Mechanistically the reasoning is sound, and it's genuinely discussed in recent SIBO/IMO reviews. But there's a gap between \"sounds logical\" and \"proven to improve human outcomes\": trials directly comparing this sequence against antimicrobials alone are still simply scarce. [More →]({{ \"/en/protocol-biofilm.html\" | relative_url }})",
     61, ["gi", "protocol"]),
    ("protocol-eradication", "Этап 2 — эрадикация", "Stage 2 - eradication agents",
     "Доказательная база берберина, орегано, аллицина и каприловой кислоты по отдельности и в комбинациях.",
     "The evidence base for berberine, oregano oil, allicin and caprylic acid, individually and in combination.",
     "Здесь находится самое популярное сравнение из всей темы — что травяная терапия (берберин, масло орегано и другие) якобы не уступает рифаксимину, стандартному антибиотику при СИБР. Источник этого утверждения стоит знать точно: это ретроспективный анализ историй болезни 2014 года, а не рандомизированное исследование. Пациенты сами выбирали, чем лечиться, разница между группами оказалась статистически не значима, а «травяная» группа принимала запатентованные комбинированные формулы из нескольких растений сразу — не отдельно орегано или отдельно берберин, как это обычно подаётся в пересказах.\n\nОтдельная история — берберин: прямо сейчас идёт настоящее рандомизированное исследование, сравнивающее его с рифаксимином один на один, но на момент написания опубликован только протокол исследования, а не итоговые результаты. Аллицин из чеснока действительно подавляет архей-метаногенов — но в исследованиях о снижении метана у коров и овец, а не в клинических испытаниях на людях с IMO. Каприловая кислота против кандиды показала эффект преимущественно в пробирке. Иначе говоря: почти для каждого отдельного растительного компонента этой части протокола прямых испытаний именно на людях с СИБР либо нет, либо они пока не завершены. [Все источники по каждому пункту →]({{ \"/ru/protocol-eradication.html\" | relative_url }})",
     "This is where the single most-cited comparison in the whole topic lives: that herbal therapy (berberine, oregano oil, and others) supposedly matches rifaximin, the standard SIBO antibiotic. The source of that claim is worth knowing precisely: a 2014 retrospective chart review, not a randomised trial. Patients self-selected their treatment, the difference between groups wasn't statistically significant, and the \"herbal\" arm took proprietary multi-herb combination formulas - not standalone oregano or standalone berberine, as it's usually retold.\n\nBerberine has its own, more promising story: a genuine randomised trial comparing it head-to-head with rifaximin is under way right now, though at the time of writing only the trial protocol is published, not the results. Garlic-derived allicin does suppress methanogenic archaea - but in research on reducing cattle and sheep methane emissions, not in human IMO trials. Caprylic acid against candida has mostly shown an effect in a test tube. In short: for nearly every individual herbal component of this stage, direct human SIBO trials either don't exist yet or haven't concluded. [All sources, item by item →]({{ \"/en/protocol-eradication.html\" | relative_url }})",
     62, ["gi", "protocol"]),
    ("protocol-binders", "Этап 3 — сорбенты и реакция на распад", "Stage 3 - binders & die-off",
     "Что известно о реакции Яриша-Герксгеймера и насколько уместно это понятие здесь.",
     "What is known about the Jarisch-Herxheimer reaction, and how appropriate that concept is here.",
     "Идея о том, что при массовой гибели патогенов возникает временное ухудшение самочувствия — головная боль, ломота, тошнота, — заимствована из реальной, хорошо задокументированной реакции Яриша-Герксгеймера. Это действительно подтверждённый феномен, только относится он к антибиотикотерапии спирохетозных инфекций вроде сифилиса, болезни Лайма или лептоспироза: массовый распад бактерий определённого типа выбрасывает в кровь достаточно токсинов, чтобы вызвать острую воспалительную реакцию, обычно в первые сутки лечения. Перенос этого понятия на приём растительных антимикробных добавок при СИБР — устоявшийся в интегративной медицине термин, но контролируемых исследований именно этого механизма именно в этом контексте найти не удалось.\n\nСорбенты вроде цеолита или активированного угля в такой ситуации действительно используют, и физически они работают — связывают вещества в просвете кишки. Но связывают неизбирательно, включая часть лекарств и нутриентов, поэтому их и разносят по времени с едой на полтора-два часа — это общее свойство любого адсорбента, а не специфическое доказательство пользы именно при «детоксе». [Подробнее →]({{ \"/ru/protocol-binders.html\" | relative_url }})",
     "The idea that mass pathogen die-off causes temporary malaise - headache, body aches, nausea - is borrowed from a real, well-documented phenomenon: the Jarisch-Herxheimer reaction. It's genuinely confirmed, but it applies to antibiotic treatment of spirochaetal infections like syphilis, Lyme disease, or leptospirosis: mass lysis of that specific kind of bacteria releases enough toxins into the blood to trigger an acute inflammatory reaction, usually within the first day of treatment. Extending this concept to herbal antimicrobial supplements for SIBO is an established term in integrative medicine, but controlled studies of this exact mechanism in this exact context couldn't be found.\n\nBinders like zeolite or activated charcoal are genuinely used here, and physically they do work - they adsorb substances in the gut lumen. But non-selectively, including some medications and nutrients, which is why they're timed 1.5-2 hours from food - a general property of any adsorbent, not specific evidence of benefit for \"detox\" as such. [More →]({{ \"/en/protocol-binders.html\" | relative_url }})",
     63, ["gi", "protocol"]),
    ("protocol-prokinetics", "Этап 4 — прокинетики", "Stage 4 - prokinetics",
     "Имбирь и артишок: где доказательства действительно есть, а где это перенос с другого диагноза.",
     "Ginger and artichoke: where the evidence genuinely applies, and where it is carried over from a different diagnosis.",
     "После того как патогенов стало меньше, встаёт следующий вопрос: почему они вообще там оказались и что помешает им вернуться. Ответ обычно упирается в тот самый мигрирующий моторный комплекс из самого начала: если он ослаблен, тонкая кишка перестаёт «выметать» остатки пищи и бактерий между приёмами пищи, и почва для рецидива остаётся та же. Здесь неожиданно хорошо выглядит имбирь: в небольших исследованиях его экстракт действительно усиливал моторику именно в нужной, «уборочной» фазе ММК натощак — один из немногих пунктов протокола с прямым, а не косвенным клиническим подтверждением, пусть и на небольших выборках. Артишок доказан хуже: у него есть солидная доказательная база, но при функциональной диспепсии, а не при профилактике рецидива СИБР — это соседний диагноз, и перенос эффекта отсюда туда остаётся предположением, а не фактом. [Подробнее →]({{ \"/ru/protocol-prokinetics.html\" | relative_url }})",
     "Once pathogen numbers have come down, the next question is why they got there in the first place, and what stops them coming back. The answer usually comes back to that same migrating motor complex from the very start: if it's weak, the small intestine stops \"sweeping out\" leftover food and bacteria between meals, and the ground for relapse stays the same. Ginger looks surprisingly good here: in small studies its extract genuinely increased motility specifically in the fasting-state \"housekeeping\" phase of the MMC - one of the few stages of the protocol with direct, not just indirect, clinical support, even if the samples were small. Artichoke is proven for a different thing: it has a solid evidence base, but for functional dyspepsia, not for preventing SIBO relapse - a neighbouring diagnosis, and carrying the effect over remains an assumption, not a fact. [More →]({{ \"/en/protocol-prokinetics.html\" | relative_url }})",
     64, ["gi", "protocol"]),
    ("protocol-healing", "Этап 5 — заживление слизистой", "Stage 5 - mucosal healing",
     "L-глутамин: физиологическая роль против доказательств именно для этого случая.",
     "L-glutamine: its physiological role versus the evidence for this specific use case.",
     "Последний по порядку, но не по значению вопрос — что происходит со слизистой оболочкой тонкой кишки после того, как её какое-то время раздражали газ, бактерии и продукты их жизнедеятельности. L-глутамин здесь выступает как топливо для энтероцитов, клеток, которые эту слизистую и образуют, — это реальная, изученная роль, но изучена она в основном на пациентах в критическом состоянии или с синдромом короткой кишки, а не на в целом здоровых людях с бытовым СИБР. Эффект правдоподобен — аминокислота действительно нужна этим клеткам для работы, — но это не то же самое, что доказанная польза именно в этой ситуации. [Подробнее →]({{ \"/ru/protocol-healing.html\" | relative_url }})",
     "Last but not least: what happens to the small intestine's mucosal lining after being irritated by gas, bacteria, and their by-products for a while. L-glutamine's role here is as fuel for enterocytes, the cells that make up that lining - a real, studied role, but studied mainly in critically ill patients or those with short-bowel syndrome, not in otherwise healthy people with everyday SIBO. The effect is plausible - the amino acid genuinely is needed by these cells - but that's not the same as proven benefit in this specific situation. [More →]({{ \"/en/protocol-healing.html\" | relative_url }})",
     65, ["gi", "protocol"]),
    ("protocol-schedule", "Порядок приёма и правила курса", "Dosing schedule & course rules",
     "Практические правила курса и то, что в них является клинической практикой, а что — предположением.",
     "Practical course rules, and which of them are established clinical practice versus a reasonable guess.",
     "И в конце — практические правила самого курса, где стоит развести то, что является общей клинической осторожностью, и то, что специфично именно для этого протокола. Вводить новые вещества по одному, с паузами в день-два, чтобы при плохой реакции было понятно, на что именно она возникла, — это просто разумная фармаконадзорная практика, применимая к чему угодно, а не проверенный в исследованиях конкретно этот пятиэтапный график. Ферментные препараты вроде панкреатина — настоящее, одобренное лечение, но при подтверждённой ферментной недостаточности поджелудочной железы; профилактический приём «на весь курс эрадикации» у человека без такого диагноза — это практика функциональной медицины, а не показание, закреплённое в гастроэнтерологических гайдлайнах. [Подробнее →]({{ \"/ru/protocol-schedule.html\" | relative_url }})",
     "Finally, the practical rules of the course itself, where it's worth separating general clinical caution from what's specific to this protocol. Introducing new substances one at a time, a day or two apart, so a bad reaction can be traced to its actual cause, is just sensible pharmacovigilance practice, applicable to anything - not a specifically tested five-stage schedule. Enzyme products like pancreatin are real, approved treatment, but for confirmed pancreatic enzyme insufficiency; taking them prophylactically \"for the whole eradication course\" without that diagnosis is functional-medicine practice, not an indication set out in gastroenterology guidelines. [More →]({{ \"/en/protocol-schedule.html\" | relative_url }})",
     66, ["gi", "protocol"]),
]
for id_, nr, ne, sr, se, nar_r, nar_e, ok, tags in TOPICS:
    con.execute("INSERT INTO topics VALUES (?,?,?,?,?,?,?,?,?)",
                [id_, nr, ne, sr, se, nar_r, nar_e, ok, tags])

# ---------------------------------------------------------------- facts
# id, name_ru, name_en, statement_ru, statement_en, quote, quote_ru, status, tags, topic_id, source_id_or_None
FACTS = [
    ("acid-mmc-barrier", "Кислотный барьер и ММК", "Acid barrier and the MMC",
     "Желудочная кислота и мигрирующий моторный комплекс (ММК) — два основных механизма, ограничивающих количество бактерий в тонкой кишке; их нарушение (подавление кислотности, нарушения моторики, диабет, склеродермия, спайки после операций) — признанный фактор риска СИБР.",
     "Gastric acid and the migrating motor complex (MMC) are the two principal mechanisms limiting bacterial numbers in the small intestine; their disruption (acid suppression, motility disorders, diabetes, scleroderma, post-surgical adhesions) is a recognised SIBO risk factor.",
     None, None, "confirmed", ["mechanism"], "sibo-sifo-overview", "merck-sibo"),
    ("acg-definition", "Официальное определение СИБР", "The formal definition of SIBO",
     "СИБР официально определяется как избыточное количество бактерий в тонкой кишке, вызывающее симптомы со стороны ЖКТ; преобладают грамотрицательные бактерии, ферментирующие углеводы с образованием газа.",
     "SIBO is formally defined as excessive numbers of bacteria in the small bowel causing GI symptoms; gram-negative, carbohydrate-fermenting, gas-producing organisms predominate.",
     "excessive numbers of bacteria in the small bowel causing GI symptoms",
     "избыточное количество бактерий в тонкой кишке, вызывающее симптомы со стороны ЖКТ",
     "confirmed", ["mechanism"], "sibo-sifo-overview", "acg-sibo-2020"),
    ("breath-test-diagnosis", "Критерий положительного водородного теста", "Positive hydrogen-test criterion",
     "Диагноз ставится дыхательным тестом: подъём водорода на ≥20 ppm от исходного уровня в первые 90 минут после приёма глюкозы или лактулозы — признанный критерий положительного результата (ACG, 2020).",
     "Diagnosis is made by breath test: a rise in hydrogen of ≥20 ppm from baseline within the first 90 minutes after glucose or lactulose ingestion is the accepted positive criterion (ACG, 2020).",
     "A positive breath test is defined as a >20-ppm increase of hydrogen",
     "положительным тестом считается прирост водорода более чем на 20 ppm",
     "confirmed", ["diagnosis"], "hydrogen-sibo-markers", "merck-sibo"),
    ("hydrogen-symptoms", "Симптомы водородного варианта", "Hydrogen-variant symptoms",
     "Вздутие, боль в животе, газообразование и/или диарея после еды — стандартный, признанный в гастроэнтерологии симптомокомплекс, ассоциированный с положительным водородным тестом.",
     "Bloating, abdominal pain, gas and/or diarrhoea after eating form the standard symptom cluster gastroenterology associates with a positive hydrogen test.",
     None, None, "confirmed", ["symptoms"], "hydrogen-sibo-markers", "acg-sibo-2020"),
    ("rapid-onset-diagnostic-logic", "Почему именно быстрая реакция считается специфичной", "Why a fast reaction specifically counts as specific",
     "У здорового человека путь еды до толстой кишки занимает в среднем 70–90 минут; поэтому ранний, а не поздний подъём водорода/метана в дыхательном тесте и считается признаком брожения в тонкой, а не толстой кишке. Быстрый (15–30 минут), стабильно повторяющийся отклик именно на определённые продукты воспроизводит эту же логику на уровне самонаблюдения, а не по одним ощущениям без физиологической опоры.",
     "In a healthy person, food takes 70-90 minutes on average to reach the colon; that is exactly why an early, not a late, rise in breath hydrogen/methane is taken as a sign of fermentation in the small rather than the large intestine. A fast (15-30 minute), consistently repeating response to specific foods reproduces that same logic at the level of self-observation, not a feeling without physiological grounding.",
     None, None, "mechanistic", ["symptoms", "timing"], "hydrogen-sibo-markers", "sibo-critical-appraisal-2024"),
    ("orocecal-transit-confound", "Оговорка 2024: быстрый транзит даёт тот же паттерн", "2024 caveat: fast transit gives the same pattern",
     "Клинический разбор 2024 года (ESNM/ANMS) указывает, что тот же ранний подъём водорода объясним не только избытком бактерий в тонкой кишке, но и просто быстрым транзитом: если содержимое доходит до богатой бактериями толстой кишки раньше обычного, брожение там начинается раньше при нормальном количестве бактерий в самой тонкой кишке. Отличить один сценарий от другого по одним симптомам, а иногда и по самому тесту, не всегда возможно.",
     "A 2024 clinical practice update (ESNM/ANMS) points out that the same early hydrogen rise is explainable not only by bacterial excess in the small intestine but simply by fast transit: if contents reach the bacteria-rich colon earlier than usual, fermentation there starts early with a normal small-intestine bacterial count. Telling the two scenarios apart by symptoms alone, and sometimes even by the test itself, is not always possible.",
     "wide variation in transit time through the stomach and small intestine to the cecum",
     "существенный разброс во времени прохождения пищи через желудок и тонкую кишку до слепой кишки",
     "disputed", ["symptoms", "timing", "correction"], "hydrogen-sibo-markers", "sibo-critical-appraisal-2024"),
    ("supragastric-belching-mechanism", "Механизм супрагастральной отрыжки", "The supragastric belching mechanism",
     "При супрагастральной отрыжке воздух засасывается в пищевод и почти сразу выталкивается обратно, не доходя ни до желудка, ни до кишечника; это, по сути, мышечный паттерн пищевода, а не пищеварительный процесс и не бактериальное брожение.",
     "In supragastric belching, air is sucked into the oesophagus and pushed straight back out without reaching the stomach or intestine; it is essentially an oesophageal muscular pattern, not a digestive process and not bacterial fermentation.",
     "the supragastric air flow occurs more quickly and is independent of esophageal peristalsis",
     "поток воздуха при супрагастральной отрыжке возникает быстрее и не зависит от перистальтики пищевода",
     "confirmed", ["belching"], "belching-differential", "aga-belching-2023"),
    ("belching-vs-aerophagia-vs-sibo-gas", "Отрыжка, аэрофагия и кишечный газ — разные картины", "Belching, aerophagia and gut gas - different pictures",
     "При аэрофагии воздух всё же доходит до кишечника, и главные симптомы — вздутие и флатуленция, а не отрыжка. При бактериальном брожении (водородном или метановом варианте) газ тоже движется преимущественно вниз. Картина, где именно отрыжка — основная и доминирующая жалоба, а не вздутие или изменения стула, статистически смещена в сторону супрагастрального механизма, а не кишечного.",
     "In aerophagia, air does reach the intestine, and the main symptoms are bloating and flatulence, not belching. In bacterial fermentation (hydrogen or methane variant), gas also moves mostly downward. A picture where belching itself is the main, dominant complaint, not bloating or altered stools, is statistically weighted toward a supragastric mechanism rather than a gut one.",
     None, None, "mechanistic", ["belching", "correction"], "belching-differential", "aga-belching-2023"),
    ("belching-anxiety-formal-dx", "Связь с тревожностью и формальная диагностика", "The anxiety link and formal diagnosis",
     "Супрагастральная отрыжка чаще встречается у людей с тревожностью и официально диагностируется только импедансометрией пищевода, а не по одним ощущениям - в этом смысле она, как и остальные пункты этой темы, требует объективного теста для окончательного подтверждения, а не только характерной клинической картины.",
     "Supragastric belching is more common in people with anxiety and is formally diagnosed only by oesophageal impedance monitoring, not by sensation alone - in that sense, like everything else in this topic, it needs an objective test for final confirmation, not just a characteristic clinical picture.",
     "Nevertheless, intraluminal impedance measurement is required to distinguish supragastric from gastric belching",
     "тем не менее, для различения супрагастральной и желудочной отрыжки требуется импедансометрия",
     "preliminary", ["belching"], "belching-differential", "sgb-pathogenesis-review"),
    ("imo-reclassification", "Метан образуют археи, не бактерии", "Methane comes from archaea, not bacteria",
     "Избыточный метан производят не бактерии, а археи-метаногены; поэтому ACG использует термин IMO (intestinal methanogen overgrowth) вместо «метановый СИБР». Порог положительного теста — метан ≥10 ppm.",
     "Excess methane is produced by methanogenic archaea, not bacteria; ACG therefore prefers the term IMO (intestinal methanogen overgrowth) over \"methane SIBO\". The positive-test threshold is methane ≥10 ppm.",
     None, None, "confirmed", ["diagnosis", "imo"], "methane-imo-markers", "acg-sibo-2020"),
    ("imo-constipation-link", "IMO и запор", "IMO and constipation",
     "ACG (2020) прямо рекомендует тестирование на метан/IMO у пациентов с запором — связь между избыточным метаном и замедленным транзитом признана на уровне клинической рекомендации, хотя качество доказательств оценено как очень низкое.",
     "ACG (2020) explicitly recommends methane/IMO testing in patients with constipation - the link between excess methane and slow transit is recognised at guideline level, though the evidence is graded very low quality.",
     None, None, "confirmed", ["diagnosis", "imo"], "methane-imo-markers", "acg-sibo-2020"),
    ("sifo-debated", "Существование СИФО как диагноза оспаривается", "SIFO's status as a diagnosis is disputed",
     "Существование СИФО как отдельной клинической единицы и его значимость до сих пор являются предметом дискуссии; общепринятого стандартизированного протокола диагностики нет.",
     "The existence and clinical relevance of SIFO as a distinct entity remain debated in the literature, and there is no standardised diagnostic protocol.",
     "The existence and clinical relevance of SIFO as a distinct entity remain debated",
     "существование и клиническая значимость СИФО как отдельной единицы остаются предметом дискуссии",
     "disputed", ["candida"], "sifo-candida-markers", "amboss-sifo"),
    ("sifo-candida-dominant", "97% случаев СИФО — Candida", "97% of SIFO cases are Candida",
     "В исследованиях пациентов с необъяснёнными жалобами ЖКТ около 97% выявленных при СИФО грибков относились к роду Candida, чаще всего Candida albicans.",
     "In studies of patients with unexplained GI complaints, roughly 97% of fungi identified in SIFO cases belonged to the genus Candida, most often Candida albicans.",
     None, None, "preliminary", ["candida"], "sifo-candida-markers", "nutrients-2025-sibo-sifo"),
    ("sifo-symptom-overlap", "Симптомы СИФО совпадают с СИБР", "SIFO symptoms overlap with SIBO",
     "Клинические проявления СИФО (боль, вздутие, газ, диарея) во многом совпадают с симптомами бактериального СИБР, что затрудняет разграничение без специфической диагностики (посев аспирата тонкой кишки).",
     "SIFO's clinical picture (pain, bloating, gas, diarrhoea) largely overlaps with bacterial SIBO, which makes the two hard to tell apart without specific testing (small-bowel aspirate culture).",
     None, None, "preliminary", ["candida", "diagnosis"], "sifo-candida-markers", "nutrients-2025-sibo-sifo"),
    ("systemic-permeability", "Проницаемость: механизм правдоподобен, цепочка не доказана", "Permeability: plausible mechanism, unproven chain",
     "Цепочка «перерастяжение газом / биоплёнка → повреждение слизистого барьера → повышенная проницаемость → новые пищевые реакции» обсуждается в литературе как механизм, но убедительных клинических доказательств того, что она реализуется у типичного пациента с СИБР, недостаточно.",
     "The chain \"gas distension / biofilm -> damaged mucosal barrier -> increased permeability -> new food reactions\" is discussed in the literature as a mechanism, but solid clinical evidence that it plays out in a typical SIBO patient is lacking.",
     None, None, "mechanistic", ["systemic"], "systemic-consequences", "nutrients-2025-sibo-sifo"),
    ("systemic-sphincter-oddi-claim", "Спазм сфинктера Одди / панкреатит — не подтверждено", "Sphincter of Oddi spasm / pancreatitis - unsupported",
     "Утверждение, что вздутие при СИБР регулярно вызывает спазм сфинктера Одди и вторичный панкреатит, не нашло подтверждения в проверенной нами гастроэнтерологической литературе; это не признанное осложнение СИБР, а, судя по всему, непроверяемая экстраполяция.",
     "The claim that SIBO-related bloating routinely causes sphincter of Oddi spasm and secondary pancreatitis found no support in the gastroenterology literature we checked; it is not a recognised SIBO complication, and appears to be an unsourced extrapolation.",
     None, None, "insufficient-evidence", ["systemic", "correction"], "systemic-consequences", None),
    ("herx-reaction-origin", "Классическая реакция Яриша-Герксгеймера", "The classic Jarisch-Herxheimer reaction",
     "Реакция Яриша-Герксгеймера описана и подтверждена для антибиотикотерапии спирохетозных и близких инфекций (сифилис, болезнь Лайма, лептоспироз, Ку-лихорадка) — острая воспалительная реакция на массовый распад бактерий, обычно в первые 24 часа.",
     "The Jarisch-Herxheimer reaction is described and confirmed for antibiotic treatment of spirochaetal and related infections (syphilis, Lyme disease, leptospirosis, Q fever) - an acute inflammatory reaction to mass bacterial lysis, usually within the first 24 hours.",
     "The JHR occurs when large quantities of toxins are released",
     "реакция возникает, когда в организм высвобождается большое количество токсинов",
     "confirmed", ["die-off"], "protocol-binders", "jhr-classic"),
    ("herx-extrapolation-gut", "Перенос на СИБР/кандиду не подтверждён исследованиями", "The extension to SIBO/candida is not research-backed",
     "Перенос этой концепции на приём растительных антимикробных добавок при СИБР/кандиде («детокс-реакция») — устоявшийся термин в интегративной медицине, но контролируемых клинических исследований именно этого механизма в контексте пищевых добавок нам найти не удалось; относитесь к нему как к правдоподобному, но не доказанному объяснению недомогания в начале курса.",
     "Extending this concept to herbal antimicrobial supplements for SIBO/candida (a \"detox reaction\") is an established term in integrative medicine, but we could not find controlled clinical studies of this specific mechanism in a supplement context; treat it as a plausible, not a proven, explanation for early-course malaise.",
     None, None, "insufficient-evidence", ["die-off", "correction"], "protocol-binders", None),
    ("binders-general-caution", "Сорбенты связывают неизбирательно", "Binders bind non-selectively",
     "Сорбенты вроде цеолита или активированного угля физически связывают вещества в просвете кишки неизбирательно — это касается не только «токсинов», но и лекарств и части нутриентов, поэтому их разносят по времени с едой и другими препаратами минимум на 1.5-2 часа; это общее фармакологическое свойство адсорбентов, а не доказательство пользы именно при «die-off».",
     "Binders such as zeolite or activated charcoal adsorb substances in the gut lumen non-selectively - this affects not just \"toxins\" but medications and some nutrients too, which is why they are timed at least 1.5-2 hours from food and other supplements; this is a general property of adsorbents, not evidence of benefit specifically for \"die-off\".",
     None, None, "mechanistic", ["die-off"], "protocol-binders", None),
    ("berberine-rct", "Берберин против рифаксимина: идёт РКИ", "Berberine vs rifaximin: an RCT is underway",
     "Берберин напрямую сравнивается с рифаксимином в зарегистрированном рандомизированном клиническом исследовании (BRIEF-SIBO, Пекинский университет); опубликован протокол исследования, гипотеза — берберин не уступает рифаксимину по эффективности эрадикации.",
     "Berberine is being directly compared with rifaximin in a registered randomised controlled trial (BRIEF-SIBO, Peking University); the trial protocol has been published, with the hypothesis that berberine is non-inferior to rifaximin for eradication.",
     "the first clinical trial assessing the eradication effects of two weeks of berberine treatment",
     "первое клиническое испытание, оценивающее эффект двухнедельного приёма берберина",
     "preliminary", ["eradication", "berberine"], "protocol-eradication", "brief-sibo-protocol"),
    ("herbal-vs-rifaximin-retrospective", "«46% против 34%» — из ретроспективного, не рандомизированного исследования", "\"46% vs 34%\" is from a retrospective, non-randomised study",
     "Часто цитируемое сравнение «46% против 34%» в пользу трав против рифаксимина получено в ретроспективном анализе историй болезни (не в рандомизированном исследовании): пациенты сами выбирали лечение, разница статистически не значима (p=.24), а использовались запатентованные комбинированные формулы (Dysbiocide/FC-Cidal, Candibactin-AR/BR), а не отдельно орегано или берберин.",
     "The widely cited \"46% vs 34%\" comparison favouring herbs over rifaximin comes from a retrospective chart review (not a randomised trial): patients self-selected their treatment, the difference was not statistically significant (p=.24), and the herbal arm used proprietary combination formulas (Dysbiocide/FC-Cidal, Candibactin-AR/BR), not standalone oregano or berberine.",
     "Herbal therapies are at least as effective as rifaximin for resolution of SIBO",
     "травяная терапия по меньшей мере не уступает рифаксимину в разрешении СИБР",
     "disputed", ["eradication", "correction"], "protocol-eradication", "chedid-2014-herbal"),
    ("single-agent-evidence-gap", "Отдельных испытаний одного агента почти нет", "Almost no single-agent trials exist",
     "Прямых клинических испытаний одного только масла орегано, только берберина вне BRIEF-SIBO или только аллицина против СИБР у людей практически нет; доступные данные получены либо на комбинированных формулах, либо in vitro / на животных.",
     "Direct human clinical trials of oregano oil alone, of berberine alone outside BRIEF-SIBO, or of allicin alone against SIBO are essentially absent; the available data come either from combination formulas or from in vitro / animal work.",
     None, None, "insufficient-evidence", ["eradication", "correction"], "protocol-eradication", None),
    ("allicin-methanogens-mechanism", "Аллицин против метаногенов — данные из животноводства, не медицины", "Allicin vs methanogens - livestock data, not clinical data",
     "Аллицин (из чеснока) подавляет рост метаногенных архей в исследованиях, посвящённых снижению метана у жвачных животных; прямых клинических испытаний аллицина против IMO у людей найти не удалось — перенос эффекта на человека остаётся предположением, а не установленным фактом.",
     "Allicin (from garlic) does suppress methanogenic archaea in research aimed at reducing ruminant methane emissions; we could not find direct human clinical trials of allicin against IMO - extrapolating the effect to people remains an assumption, not an established fact.",
     None, None, "insufficient-evidence", ["eradication", "imo"], "protocol-eradication", None),
    ("caprylic-acid-invitro", "Каприловая кислота: доказательства только in vitro", "Caprylic acid: in-vitro evidence only",
     "Противогрибковое действие каприловой кислоты в отношении Candida показано преимущественно in vitro; контролируемых клинических испытаний у людей с диагностированным СИФО не найдено. При подтверждённом СИФО стандартом остаются рецептурные антимикотики (например, флуконазол).",
     "Caprylic acid's antifungal action against Candida has mainly been shown in vitro; no controlled human trials in diagnosed SIFO were found. Where SIFO is confirmed, prescription antifungals (e.g. fluconazole) remain the standard of care.",
     None, None, "insufficient-evidence", ["eradication", "candida"], "protocol-eradication", "amboss-sifo"),
    ("nac-biofilm-definition", "Что такое биоплёнка", "What a biofilm is",
     "Биоплёнка — структурированное сообщество микробных клеток во внеклеточном полисахаридном матриксе; её присутствие называют одним из факторов, затрудняющих лечение СИБР/IMO антимикробными средствами.",
     "A biofilm is a structured community of microbial cells embedded in an extracellular polysaccharide matrix; its presence is cited as one factor that makes SIBO/IMO harder to treat with antimicrobials.",
     "structured communities of microbial cells embedded in an extracellular polymeric substance matrix",
     "структурированные сообщества микробных клеток во внеклеточном полимерном матриксе",
     "confirmed", ["biofilm"], "protocol-biofilm", "biofilm-disruption-2025"),
    ("biofilm-disruptor-evidence-gap", "Разрушать биоплёнку до эрадикации — рационально, но не доказано на людях", "Disrupt-then-treat is rational but not human-proven",
     "Идея «сначала разрушить биоплёнку (например, NAC), потом убивать патоген» механистически рациональна и обсуждается в свежих обзорах по СИБР/IMO, но клинических испытаний, доказывающих, что именно эта последовательность улучшает исходы у людей по сравнению с однократным приёмом антимикробных средств, пока мало.",
     "The idea of \"disrupt the biofilm first (e.g. with NAC), then kill the pathogen\" is mechanistically rational and discussed in recent SIBO/IMO reviews, but there are still few clinical trials proving this sequence improves human outcomes compared with antimicrobials alone.",
     None, None, "insufficient-evidence", ["biofilm", "correction"], "protocol-biofilm", "biofilm-disruption-2025"),
    ("prokinetic-mmc-rationale", "Зачем нужны прокинетики после эрадикации", "Why prokinetics matter after eradication",
     "Риск рецидива СИБР во многом связан с тем, восстановилась ли моторика: ММК в фазе покоя «выметает» остатки пищи и бактерий из тонкой кишки между приёмами пищи.",
     "SIBO relapse risk is closely tied to whether motility has recovered: the fasting-phase MMC \"sweeps\" residual food and bacteria out of the small intestine between meals.",
     None, None, "confirmed", ["prokinetics"], "protocol-prokinetics", "dyspepsia-cam-review"),
    ("ginger-mmc-evidence", "Имбирь и III фаза ММК: подтверждено в малых исследованиях", "Ginger and MMC phase III: shown in small studies",
     "В небольших исследованиях экстракт имбиря достоверно усиливал антральную моторику именно в III фазе ММК натощак — механизм действия имеет прямое клиническое подтверждение, хотя выборки небольшие.",
     "In small studies, ginger extract reliably increased antral motility specifically during fasting-state MMC phase III - the mechanism has direct clinical support, though sample sizes are small.",
     "oral ginger improves gastroduodenal motility in the fasting state",
     "приём имбиря улучшает гастродуоденальную моторику в состоянии натощак",
     "preliminary", ["prokinetics", "ginger"], "protocol-prokinetics", "dyspepsia-cam-review"),
    ("artichoke-dyspepsia-not-sibo", "Артишок доказан при диспепсии, не при СИБР", "Artichoke is proven for dyspepsia, not SIBO",
     "Экстракт артишока (Cynara scolymus) имеет РКИ-подтверждение эффективности при функциональной диспепсии, но отдельных испытаний именно для профилактики рецидива СИБР после эрадикации найти не удалось - это перенос с смежного показания.",
     "Artichoke leaf extract (Cynara scolymus) has RCT support for functional dyspepsia, but no dedicated trials for preventing SIBO relapse after eradication were found - this is a carry-over from an adjacent indication.",
     None, None, "mechanistic", ["prokinetics", "correction"], "protocol-prokinetics", "dyspepsia-cam-review"),
    ("glutamine-mixed-evidence", "L-глутамин: доказан в других контекстах, не в этом", "L-glutamine: proven elsewhere, not here",
     "L-глутамин изучен как топливо для энтероцитов и применяется у пациентов в критическом состоянии или с синдромом короткой кишки; доказательств именно для «заживления» кишечника при бытовом СИБР и повышенной проницаемости у в остальном здоровых людей значительно меньше.",
     "L-glutamine is studied as an enterocyte fuel and used in critically ill patients or those with short-bowel syndrome; evidence specifically for gut \"healing\" in everyday SIBO and increased permeability in otherwise healthy people is considerably thinner.",
     None, None, "mechanistic", ["healing"], "protocol-healing", None),
    ("pancreatic-enzyme-role", "Ферменты «на весь курс» — практика функциональной медицины, не гайдлайн", "Enzymes \"for the whole course\" is functional-medicine practice, not a guideline",
     "Ферментные препараты (панкреатин) — стандартное лечение при подтверждённой экзокринной недостаточности поджелудочной железы; их профилактическое применение «на время курса эрадикации СИБР» у людей без диагностированной недостаточности — практика функциональной медицины, не показание, закреплённое в гастроэнтерологических гайдлайнах.",
     "Pancreatic enzyme products (pancreatin) are standard treatment for confirmed exocrine pancreatic insufficiency; using them prophylactically \"for the duration of a SIBO eradication course\" in people without diagnosed insufficiency is functional-medicine practice, not an indication set out in gastroenterology guidelines.",
     None, None, "insufficient-evidence", ["schedule", "correction"], "protocol-schedule", None),
    ("course-titration-caution", "Постепенное введение агентов — разумно, но не протестировано как протокол", "Staggered introduction is sensible, but untested as a protocol",
     "Постепенное введение агентов по одному, с паузами в 1-2 дня, — разумная практика (легче связать реакцию с конкретным веществом), но конкретный график «5 этапов за N дней» как таковой в исследованиях не тестировался; сроки индивидуальны.",
     "Introducing agents one at a time with 1-2 day gaps is sensible practice (it makes a reaction easier to attribute to a specific substance), but no study has tested this specific \"5 stages over N days\" schedule as such; timing is individual.",
     None, None, "mechanistic", ["schedule"], "protocol-schedule", None),
]

for f in FACTS:
    (id_, nr, ne, sr, se, quote, quote_ru, status, tags, topic_id, source_id) = f
    con.execute("INSERT INTO facts VALUES (?,?,?,?,?,?,?,?,?)",
                [id_, nr, ne, sr, se, quote, quote_ru, status, tags])
    con.execute("INSERT INTO relations VALUES (?,?,?,?)", [id_, topic_id, "belongs-to", None])
    if source_id:
        con.execute("INSERT INTO fact_sources VALUES (?,?)", [id_, source_id])

# ---------------------------------------------------------------- topic hierarchy
SUBTOPIC_OF = [
    ("hydrogen-sibo-markers", "sibo-sifo-overview"),
    ("methane-imo-markers", "sibo-sifo-overview"),
    ("sifo-candida-markers", "sibo-sifo-overview"),
    ("belching-differential", "sibo-sifo-overview"),
    ("systemic-consequences", "sibo-sifo-overview"),
    ("protocol-overview", "sibo-sifo-overview"),
    ("protocol-biofilm", "protocol-overview"),
    ("protocol-eradication", "protocol-overview"),
    ("protocol-binders", "protocol-overview"),
    ("protocol-prokinetics", "protocol-overview"),
    ("protocol-healing", "protocol-overview"),
    ("protocol-schedule", "protocol-overview"),
]
for child, parent in SUBTOPIC_OF:
    con.execute("INSERT INTO relations VALUES (?,?,?,?)", [child, parent, "subtopic-of", None])

# ---------------------------------------------------------------- backlog & session_log
con.execute("INSERT INTO backlog VALUES (?,?,?,?,?)",
            ["expand-manual-sections", "Добавить следующие разделы мануала (за пределами СИБР/СИФО)",
             "open", "Тема и структура задаются пользователем по мере выбора следующих тем.", "2026-09-30"])
con.execute("INSERT INTO backlog VALUES (?,?,?,?,?)",
            ["verify-brief-sibo-results", "Проверить опубликованные результаты BRIEF-SIBO, когда исследование завершится",
             "open", "На момент написания (2026) в открытом доступе есть только протокол исследования, не итоговые результаты.", "2026-09-30"])

con.execute("INSERT INTO session_log VALUES (?,?,?,?,?,?)", [
    "sibo-sifo-launch", "2026-09-30", "Запуск мануала: тема SIBO/SIFO",
    "Репозиторий создан из шаблона creation-guidelines/text-as-data-template. Схема расширена под "
    "мануал: topics (иерархия через relations/subtopic-of), facts (statement + короткая цитата "
    "+ перевод + статус доказательности), sources, fact_sources (цитирование). Присланный пользователем "
    "текст по СИБР/СИФО проверен по первоисточникам (ACG 2020, Merck Manual, AMBOSS, Nutrients 2025, "
    "Chedid 2014, BRIEF-SIBO protocol, обзор по функциональной диспепсии, обзор по биоплёнкам, JHR case "
    "report) и переписан с явными статусами: confirmed / preliminary / mechanistic / disputed / "
    "insufficient-evidence.",
    "Единая англоязычная схема с _ru/_en колонками вместо раздельных таблиц per-locale - проще "
    "поддерживать consistency и проще генерировать оба языка одним проходом рендера.",
    "Не стал трогать .tad/tools/render.py (даёт только плоские per-table страницы) - вместо этого "
    "двуязычный рендер с хлебными крошками сделан отдельным скриптом bin/render_manual.py, чтобы "
    "не терять возможность git subrepo pull обновлений движка.",
])
con.execute("INSERT INTO session_log VALUES (?,?,?,?,?,?)", [
    "narrative-and-pager", "2026-09-30", "Сквозная статья и book-style пейджер",
    "topics получил narrative_ru/narrative_en (длинные абзацы, отдельные от терсе summary_*). "
    "bin/render_manual.py: render_story() собирает /ru|en/story.md конкатенацией narrative_* "
    "всех topics в порядке обхода дерева (тот же порядок, что и в оглавлении), с оглавлением-"
    "якорями и ссылками 'подробнее' на страницу каждого раздела. На каждой странице раздела внизу "
    "добавлен prev/next пейджер по тому же линейному порядку (READING_ORDER).",
    "Хранить нарратив как отдельные абзацы по фактам (narrative на уровне facts, не topics) - "
    "отклонено: факты специально терсе и атомарны для переиспользования в карточках/цитатах; "
    "нарратив - это связующая проза МЕЖДУ фактами, ей место на уровне topic, не factов.",
    "Не стал делать единый глобальный markdown-файл со статьёй вручную - тогда правка стала бы "
    "второй копией того же контента, а не тем же полем, что и в разделе; смысл TAD в этом и был.",
])
con.execute("INSERT INTO session_log VALUES (?,?,?,?,?,?)", [
    "symptom-specificity-review", "2026-09-30", "Специфичность тайминга симптомов + новый раздел про отрыжку",
    "По запросу пользователя перепроверена специфичность двух конкретных паттернов: быстрое "
    "(15-30 мин) газообразование после ферментируемых продуктов и весь день повторяющаяся отрыжка "
    "без запаха. Добавлены facts rapid-onset-diagnostic-logic и orocecal-transit-confound в "
    "hydrogen-sibo-markers (со ссылкой на критический разбор ESNM/ANMS 2024 - Kashyap et al., "
    "который ставит под вопрос, отличим ли ранний подъём водорода от просто быстрого транзита). "
    "Добавлен новый topic belching-differential: повторяющаяся отрыжка без запаха по Rome IV чаще "
    "объясняется супрагастральной отрыжкой (пищеводный, не кишечный механизм), а не бактериальным "
    "брожением - три facts со ссылками на AGA 2023 и обзор по супрагастральной отрыжке.",
    "Понизить статус acg-definition/breath-test-diagnosis с confirmed - отклонено: это по-прежнему "
    "официально принятый клинический стандарт; критика ESNM/ANMS 2024 добавлена отдельными fact-ами "
    "рядом, а не заменой существующего статуса - контроверза показана, а не одна сторона стёрта "
    "другой.",
])

con.execute(f"EXPORT DATABASE 'data' (FORMAT json)")
print("exported.")
print("sources:", con.execute("SELECT count(*) FROM sources").fetchone()[0])
print("topics:", con.execute("SELECT count(*) FROM topics").fetchone()[0])
print("facts:", con.execute("SELECT count(*) FROM facts").fetchone()[0])
print("relations:", con.execute("SELECT count(*) FROM relations").fetchone()[0])
print("fact_sources:", con.execute("SELECT count(*) FROM fact_sources").fetchone()[0])
