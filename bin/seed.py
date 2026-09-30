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
]
for id_, title, url, author, year in SOURCES:
    con.execute("INSERT INTO sources VALUES (?,?,?,?,?)", [id_, title, url, author, year])

# ---------------------------------------------------------------- topics
# id, name_ru, name_en, summary_ru, summary_en, order_key, tags
TOPICS = [
    ("sibo-sifo-overview", "Обзор: СИБР и СИФО", "Overview: SIBO and SIFO",
     "Механизм, из-за которого бактерии и грибки толстой кишки заселяют обычно малонаселённую тонкую кишку, и почему это меняет то, что происходит с едой.",
     "The mechanism by which colon-dwelling bacteria and fungi colonise the normally sparsely populated small intestine, and why that changes what happens to food.",
     10, ["gi", "overview"]),
    ("hydrogen-sibo-markers", "Маркеры водородного СИБР", "Hydrogen-dominant SIBO markers",
     "Что именно диагностируется как «водородный СИБР» и на какие самонаблюдения это похоже.",
     "What is actually diagnosed as hydrogen-dominant SIBO, and what it tends to feel like day to day.",
     20, ["gi", "diagnosis"]),
    ("methane-imo-markers", "Маркеры метанового СИБР (IMO)", "Methane / IMO markers",
     "Почему метановый вариант официально переименован в IMO и чем он отличается от водородного.",
     "Why the methane variant was formally renamed IMO, and how it differs from the hydrogen variant.",
     30, ["gi", "diagnosis"]),
    ("sifo-candida-markers", "Маркеры СИФО (грибковый перерост)", "SIFO (fungal overgrowth) markers",
     "Наименее устоявшийся из трёх диагнозов: что о нём известно и что остаётся спорным.",
     "The least settled of the three diagnoses: what is known about it and what remains disputed.",
     40, ["gi", "diagnosis", "candida"]),
    ("systemic-consequences", "Системные последствия", "Systemic consequences",
     "Какие claims о вторичных эффектах (проницаемость, панкреатит, аллергии) подтверждены, а какие нет.",
     "Which claims about downstream effects (permeability, pancreatitis, new allergies) are supported, and which are not.",
     50, ["gi", "systemic"]),
    ("protocol-overview", "Протокол эрадикации: обзор этапов", "Eradication protocol: stage overview",
     "Общая структура пятиэтапного фито-протокола и то, насколько каждый этап клинически обоснован.",
     "The overall structure of the five-stage phytotherapy protocol, and how well-evidenced each stage actually is.",
     60, ["gi", "protocol"]),
    ("protocol-biofilm", "Этап 1 — разрушение биоплёнки", "Stage 1 - biofilm disruption",
     "Что такое биоплёнка в этом контексте и насколько доказана польза от её целенаправленного разрушения.",
     "What a biofilm is in this context, and how well-proven the benefit of deliberately disrupting it actually is.",
     61, ["gi", "protocol"]),
    ("protocol-eradication", "Этап 2 — эрадикация", "Stage 2 - eradication agents",
     "Доказательная база берберина, орегано, аллицина и каприловой кислоты по отдельности и в комбинациях.",
     "The evidence base for berberine, oregano oil, allicin and caprylic acid, individually and in combination.",
     62, ["gi", "protocol"]),
    ("protocol-binders", "Этап 3 — сорбенты и реакция на распад", "Stage 3 - binders & die-off",
     "Что известно о реакции Яриша-Герксгеймера и насколько уместно это понятие здесь.",
     "What is known about the Jarisch-Herxheimer reaction, and how appropriate that concept is here.",
     63, ["gi", "protocol"]),
    ("protocol-prokinetics", "Этап 4 — прокинетики", "Stage 4 - prokinetics",
     "Имбирь и артишок: где доказательства действительно есть, а где это перенос с другого диагноза.",
     "Ginger and artichoke: where the evidence genuinely applies, and where it is carried over from a different diagnosis.",
     64, ["gi", "protocol"]),
    ("protocol-healing", "Этап 5 — заживление слизистой", "Stage 5 - mucosal healing",
     "L-глутамин: физиологическая роль против доказательств именно для этого случая.",
     "L-glutamine: its physiological role versus the evidence for this specific use case.",
     65, ["gi", "protocol"]),
    ("protocol-schedule", "Порядок приёма и правила курса", "Dosing schedule & course rules",
     "Практические правила курса и то, что в них является клинической практикой, а что — предположением.",
     "Practical course rules, and which of them are established clinical practice versus a reasonable guess.",
     66, ["gi", "protocol"]),
]
for id_, nr, ne, sr, se, ok, tags in TOPICS:
    con.execute("INSERT INTO topics VALUES (?,?,?,?,?,?,?)", [id_, nr, ne, sr, se, ok, tags])

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

con.execute(f"EXPORT DATABASE 'data' (FORMAT json)")
print("exported.")
print("sources:", con.execute("SELECT count(*) FROM sources").fetchone()[0])
print("topics:", con.execute("SELECT count(*) FROM topics").fetchone()[0])
print("facts:", con.execute("SELECT count(*) FROM facts").fetchone()[0])
print("relations:", con.execute("SELECT count(*) FROM relations").fetchone()[0])
print("fact_sources:", con.execute("SELECT count(*) FROM fact_sources").fetchone()[0])
