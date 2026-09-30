<!-- Generated from data/ by .tad/tools/render.py. Do not edit by hand. -->

# Facts

<a id="acid-mmc-barrier"></a>
### acid-mmc-barrier

Name ru
: Кислотный барьер и ММК

Name en
: Acid barrier and the MMC

Statement ru
: Желудочная кислота и мигрирующий моторный комплекс (ММК) — два основных механизма, ограничивающих количество бактерий в тонкой кишке; их нарушение (подавление кислотности, нарушения моторики, диабет, склеродермия, спайки после операций) — признанный фактор риска СИБР.

Statement en
: Gastric acid and the migrating motor complex (MMC) are the two principal mechanisms limiting bacterial numbers in the small intestine; their disruption (acid suppression, motility disorders, diabetes, scleroderma, post-surgical adhesions) is a recognised SIBO risk factor.

Status
: confirmed

Tags
: mechanism

Relations
: → belongs-to: [sibo-sifo-overview](topics.md#sibo-sifo-overview)

Sources
: [Small Intestinal Bacterial Overgrowth (SIBO) - Merck Manual Professional Edition](https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/small-intestinal-bacterial-overgrowth-sibo)


<a id="acg-definition"></a>
### acg-definition

Name ru
: Официальное определение СИБР

Name en
: The formal definition of SIBO

Statement ru
: СИБР официально определяется как избыточное количество бактерий в тонкой кишке, вызывающее симптомы со стороны ЖКТ; преобладают грамотрицательные бактерии, ферментирующие углеводы с образованием газа.

Statement en
: SIBO is formally defined as excessive numbers of bacteria in the small bowel causing GI symptoms; gram-negative, carbohydrate-fermenting, gas-producing organisms predominate.

Quote
: excessive numbers of bacteria in the small bowel causing GI symptoms

Quote ru
: избыточное количество бактерий в тонкой кишке, вызывающее симптомы со стороны ЖКТ

Status
: confirmed

Tags
: mechanism

Relations
: → belongs-to: [sibo-sifo-overview](topics.md#sibo-sifo-overview)

Sources
: [ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth](https://doi.org/10.14309/ajg.0000000000000501)


<a id="breath-test-diagnosis"></a>
### breath-test-diagnosis

Name ru
: Критерий положительного водородного теста

Name en
: Positive hydrogen-test criterion

Statement ru
: Диагноз ставится дыхательным тестом: подъём водорода на ≥20 ppm от исходного уровня в первые 90 минут после приёма глюкозы или лактулозы — признанный критерий положительного результата (ACG, 2020).

Statement en
: Diagnosis is made by breath test: a rise in hydrogen of ≥20 ppm from baseline within the first 90 minutes after glucose or lactulose ingestion is the accepted positive criterion (ACG, 2020).

Quote
: A positive breath test is defined as a >20-ppm increase of hydrogen

Quote ru
: положительным тестом считается прирост водорода более чем на 20 ppm

Status
: confirmed

Tags
: diagnosis

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)

Sources
: [Small Intestinal Bacterial Overgrowth (SIBO) - Merck Manual Professional Edition](https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/small-intestinal-bacterial-overgrowth-sibo)


<a id="hydrogen-symptoms"></a>
### hydrogen-symptoms

Name ru
: Симптомы водородного варианта

Name en
: Hydrogen-variant symptoms

Statement ru
: Вздутие, боль в животе, газообразование и/или диарея после еды — стандартный, признанный в гастроэнтерологии симптомокомплекс, ассоциированный с положительным водородным тестом.

Statement en
: Bloating, abdominal pain, gas and/or diarrhoea after eating form the standard symptom cluster gastroenterology associates with a positive hydrogen test.

Status
: confirmed

Tags
: symptoms

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)

Sources
: [ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth](https://doi.org/10.14309/ajg.0000000000000501)


<a id="rapid-onset-diagnostic-logic"></a>
### rapid-onset-diagnostic-logic

Name ru
: Почему именно быстрая реакция считается специфичной

Name en
: Why a fast reaction specifically counts as specific

Statement ru
: У здорового человека путь еды до толстой кишки занимает в среднем 70–90 минут; поэтому ранний, а не поздний подъём водорода/метана в дыхательном тесте и считается признаком брожения в тонкой, а не толстой кишке. Быстрый (15–30 минут), стабильно повторяющийся отклик именно на определённые продукты воспроизводит эту же логику на уровне самонаблюдения, а не по одним ощущениям без физиологической опоры.

Statement en
: In a healthy person, food takes 70-90 minutes on average to reach the colon; that is exactly why an early, not a late, rise in breath hydrogen/methane is taken as a sign of fermentation in the small rather than the large intestine. A fast (15-30 minute), consistently repeating response to specific foods reproduces that same logic at the level of self-observation, not a feeling without physiological grounding.

Status
: mechanistic

Tags
: symptoms, timing

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)

Sources
: [Critical appraisal of the SIBO hypothesis and breath testing: a clinical practice update endorsed by ESNM and ANMS](https://onlinelibrary.wiley.com/doi/10.1111/nmo.14817)


<a id="orocecal-transit-confound"></a>
### orocecal-transit-confound

Name ru
: Два разных сценария за одним и тем же ранним подъёмом

Name en
: Two different scenarios behind the same early rise

Statement ru
: Клинический разбор 2024 года (ESNM/ANMS) указывает: формально тест не отличает «бактерий много в тонкой кишке» от «содержимое просто быстрее обычного доехало целиком до толстой». Но на практике это не тупик, а вопрос сопутствующих ощущений. У целого, ускоренного транзита через все 5-7 метров тонкой кишки (классически — демпинг-синдром после операций на желудке) есть собственная, узнаваемая картина: потливость, приливы, учащённое сердцебиение, головокружение вплоть до желания лечь — реакция всего тела на резкий сброс жидкости и гормональный всплеск, а не только кишечный дискомфорт. Изолированное вздутие, урчание и срочный позыв в туалет без этих системных симптомов гораздо больше говорит именно о локальном перепроизводстве газа, а не о разогнавшемся насквозь транзите.

Есть и более простое объяснение самой скорости: при типичном (не тотальном) СИБР бактерии разрастаются не по всей длине тонкой кишки, а ближе к её началу, сразу за желудком. Пище в таком случае не нужно нестись все 5-7 метров за 15 минут — достаточно доехать до близко расположенной колонии, а это в разы короче стандартного маршрута до толстой кишки. «Подозрительно быстро» тут означает не сверхскорость целиком, а просто короткое расстояние до источника брожения.

Statement en
: A 2024 clinical practice update (ESNM/ANMS) points out: formally, the test cannot tell "too many bacteria in the small intestine" apart from "contents simply reached the colon faster than usual, whole distance included." In practice, though, this isn't a dead end - it's a question of accompanying sensations. Truly accelerated transit through the entire 5-7 metres of small intestine (classically, dumping syndrome after stomach surgery) has its own, recognisable picture: sweating, flushing, a racing heart, dizziness to the point of needing to lie down - a whole-body reaction to a sudden fluid shift and hormone surge, not just gut discomfort. Isolated bloating, gurgling, and an urgent need for the toilet without those systemic symptoms points far more toward local gas overproduction than toward transit accelerated end to end.

There's also a simpler explanation for the speed itself: in typical (non-total) SIBO, bacteria don't overgrow along the whole length of the small intestine - they cluster near its start, right after the stomach. Food doesn't need to race the full 5-7 metres in 15 minutes; it only has to reach a colony sitting close by, a fraction of the standard distance to the colon. "Suspiciously fast" here doesn't mean superhuman overall speed - it means a short distance to the source of fermentation.

Quote
: food moves too quickly from your stomach to your duodenum

Quote ru
: еда слишком быстро проходит из желудка в двенадцатиперстную кишку

Status
: mechanistic

Tags
: symptoms, timing, correction

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)

Sources
: [Symptoms & Causes of Dumping Syndrome](https://www.niddk.nih.gov/health-information/digestive-diseases/dumping-syndrome/symptoms-causes)


<a id="supragastric-belching-mechanism"></a>
### supragastric-belching-mechanism

Name ru
: Механизм супрагастральной отрыжки

Name en
: The supragastric belching mechanism

Statement ru
: При супрагастральной отрыжке воздух засасывается в пищевод и почти сразу выталкивается обратно, не доходя ни до желудка, ни до кишечника; это, по сути, мышечный паттерн пищевода, а не пищеварительный процесс и не бактериальное брожение.

Statement en
: In supragastric belching, air is sucked into the oesophagus and pushed straight back out without reaching the stomach or intestine; it is essentially an oesophageal muscular pattern, not a digestive process and not bacterial fermentation.

Quote
: the supragastric air flow occurs more quickly and is independent of esophageal peristalsis

Quote ru
: поток воздуха при супрагастральной отрыжке возникает быстрее и не зависит от перистальтики пищевода

Status
: confirmed

Tags
: belching

Relations
: → belongs-to: [belching-differential](topics.md#belching-differential)

Sources
: [AGA Clinical Practice Update on Evaluation and Management of Belching, Abdominal Bloating, and Distention: Expert Review](https://www.gastrojournal.org/article/S0016-5085(23)00823-5/fulltext)


<a id="belching-vs-aerophagia-vs-sibo-gas"></a>
### belching-vs-aerophagia-vs-sibo-gas

Name ru
: Отрыжка, аэрофагия и кишечный газ — разные картины

Name en
: Belching, aerophagia and gut gas - different pictures

Statement ru
: При аэрофагии воздух всё же доходит до кишечника, и главные симптомы — вздутие и флатуленция, а не отрыжка. При бактериальном брожении (водородном или метановом варианте) газ тоже движется преимущественно вниз. Картина, где именно отрыжка — основная и доминирующая жалоба, а не вздутие или изменения стула, статистически смещена в сторону супрагастрального механизма, а не кишечного.

Statement en
: In aerophagia, air does reach the intestine, and the main symptoms are bloating and flatulence, not belching. In bacterial fermentation (hydrogen or methane variant), gas also moves mostly downward. A picture where belching itself is the main, dominant complaint, not bloating or altered stools, is statistically weighted toward a supragastric mechanism rather than a gut one.

Status
: mechanistic

Tags
: belching, correction

Relations
: → belongs-to: [belching-differential](topics.md#belching-differential)

Sources
: [AGA Clinical Practice Update on Evaluation and Management of Belching, Abdominal Bloating, and Distention: Expert Review](https://www.gastrojournal.org/article/S0016-5085(23)00823-5/fulltext)


<a id="belching-anxiety-formal-dx"></a>
### belching-anxiety-formal-dx

Name ru
: Связь с тревожностью и формальная диагностика

Name en
: The anxiety link and formal diagnosis

Statement ru
: Супрагастральная отрыжка чаще встречается у людей с тревожностью и официально диагностируется только импедансометрией пищевода, а не по одним ощущениям - в этом смысле она, как и остальные пункты этой темы, требует объективного теста для окончательного подтверждения, а не только характерной клинической картины.

Statement en
: Supragastric belching is more common in people with anxiety and is formally diagnosed only by oesophageal impedance monitoring, not by sensation alone - in that sense, like everything else in this topic, it needs an objective test for final confirmation, not just a characteristic clinical picture.

Quote
: Nevertheless, intraluminal impedance measurement is required to distinguish supragastric from gastric belching

Quote ru
: тем не менее, для различения супрагастральной и желудочной отрыжки требуется импедансометрия

Status
: preliminary

Tags
: belching

Relations
: → belongs-to: [belching-differential](topics.md#belching-differential)

Sources
: [Supragastric belching: Pathogenesis, diagnostic issues and treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC9212115/)


<a id="gas-odor-chemistry"></a>
### gas-odor-chemistry

Name ru
: Почему одни газы пахнут, а другие нет

Name en
: Why some gases smell and others don't

Statement ru
: Сами по себе водород и метан ничем не пахнут; характерный запах кишечных газов дают следовые серосодержащие соединения (сероводород — запах тухлых яиц) и продукты бактериального расщепления белка (индол и скатол — тяжёлый, фекальный запах). Поэтому «просто много газов без резкого запаха» и «отчётливо зловонные газы» — по составу разные, отдельно диагностически значимые картины, а не варианты одного и того же.

Statement en
: Hydrogen and methane have no smell of their own; the characteristic odour of gut gas comes from trace sulfur compounds (hydrogen sulfide - a rotten-egg smell) and from bacterial protein breakdown products (indole and skatole - a heavy, faecal smell). "Just a lot of gas with no sharp smell" and "distinctly foul-smelling gas" are therefore compositionally different, separately meaningful pictures, not variants of the same thing.

Quote
: characterized by its rotten eggs or blocked sewer smell

Quote ru
: характеризуется запахом тухлых яиц или засорившейся канализации

Status
: confirmed

Tags
: smell, chemistry

Relations
: → belongs-to: [h2s-sibo-markers](topics.md#h2s-sibo-markers)

Sources
: [Epithelial Electrolyte Transport Physiology and the Gasotransmitter Hydrogen Sulfide](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4745330/)


<a id="h2s-flatline-diagnostic-clue"></a>
### h2s-flatline-diagnostic-clue

Name ru
: «Ровный» тест на фоне явных симптомов

Name en
: A 'flat' test despite obvious symptoms

Statement ru
: Сероводородные бактерии перехватывают водород, который иначе ушёл бы в выдох, поэтому у части пациентов с этим типом СИБР стандартный водородный/метановый тест выглядит подозрительно нормальным при явных, стабильных симптомах — сам по себе такой разрыв между картиной и результатом теста является узнаваемым косвенным признаком именно сероводородного варианта.

Statement en
: Hydrogen-sulfide bacteria intercept the hydrogen that would otherwise be exhaled, so in some patients with this SIBO type the standard hydrogen/methane test looks suspiciously normal despite clear, consistent symptoms - that gap between the clinical picture and the test result is itself a recognisable indirect clue pointing to the hydrogen-sulfide variant.

Status
: preliminary

Tags
: smell, diagnosis

Relations
: → belongs-to: [h2s-sibo-markers](topics.md#h2s-sibo-markers)


<a id="imo-reclassification"></a>
### imo-reclassification

Name ru
: Метан образуют археи, не бактерии

Name en
: Methane comes from archaea, not bacteria

Statement ru
: Избыточный метан производят не бактерии, а археи-метаногены; поэтому ACG использует термин IMO (intestinal methanogen overgrowth) вместо «метановый СИБР». Порог положительного теста — метан ≥10 ppm.

Statement en
: Excess methane is produced by methanogenic archaea, not bacteria; ACG therefore prefers the term IMO (intestinal methanogen overgrowth) over "methane SIBO". The positive-test threshold is methane ≥10 ppm.

Status
: confirmed

Tags
: diagnosis, imo

Relations
: → belongs-to: [methane-imo-markers](topics.md#methane-imo-markers)

Sources
: [ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth](https://doi.org/10.14309/ajg.0000000000000501)


<a id="imo-constipation-link"></a>
### imo-constipation-link

Name ru
: IMO и запор

Name en
: IMO and constipation

Statement ru
: ACG (2020) прямо рекомендует тестирование на метан/IMO у пациентов с запором — связь между избыточным метаном и замедленным транзитом признана на уровне клинической рекомендации, хотя качество доказательств оценено как очень низкое.

Statement en
: ACG (2020) explicitly recommends methane/IMO testing in patients with constipation - the link between excess methane and slow transit is recognised at guideline level, though the evidence is graded very low quality.

Status
: confirmed

Tags
: diagnosis, imo

Relations
: → belongs-to: [methane-imo-markers](topics.md#methane-imo-markers)

Sources
: [ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth](https://doi.org/10.14309/ajg.0000000000000501)


<a id="methane-reduces-gas-volume"></a>
### methane-reduces-gas-volume

Name ru
: Почему метановый вариант «тише» водородного

Name en
: Why the methane variant is 'quieter' than the hydrogen one

Statement ru
: На производство одной молекулы метана метаногены расходуют четыре молекулы водорода, поэтому итоговый объём газа в кишечнике при метановом варианте физически меньше, чем был бы при том же брожении без них — отсюда более тихая, но тяжёлая, распирающая картина, а не частое громкое отхождение газов.

Statement en
: Methanogens consume four hydrogen molecules to produce one methane molecule, so the resulting gas volume in the gut is physically smaller than it would be from the same fermentation without them - hence a quieter but heavier, more distending picture rather than frequent, loud gas.

Quote
: methane is detected in 30%-50% of the healthy adult population worldwide

Quote ru
: метан обнаруживается у 30-50% здоровых взрослых людей в мире

Status
: confirmed

Tags
: imo, symptoms

Relations
: → belongs-to: [methane-imo-markers](topics.md#methane-imo-markers)

Sources
: [Methanogens, Methane and Gastrointestinal Motility](https://pmc.ncbi.nlm.nih.gov/articles/PMC3895606/)


<a id="sifo-debated"></a>
### sifo-debated

Name ru
: Существование СИФО как диагноза оспаривается

Name en
: SIFO's status as a diagnosis is disputed

Statement ru
: Существование СИФО как отдельной клинической единицы и его значимость до сих пор являются предметом дискуссии; общепринятого стандартизированного протокола диагностики нет.

Statement en
: The existence and clinical relevance of SIFO as a distinct entity remain debated in the literature, and there is no standardised diagnostic protocol.

Quote
: The existence and clinical relevance of SIFO as a distinct entity remain debated

Quote ru
: существование и клиническая значимость СИФО как отдельной единицы остаются предметом дискуссии

Status
: disputed

Tags
: candida

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Small intestinal fungal overgrowth - AMBOSS](https://www.amboss.com/us/knowledge/small-intestinal-fungal-overgrowth)


<a id="sifo-candida-dominant"></a>
### sifo-candida-dominant

Name ru
: 97% случаев СИФО — Candida

Name en
: 97% of SIFO cases are Candida

Statement ru
: В исследованиях пациентов с необъяснёнными жалобами ЖКТ около 97% выявленных при СИФО грибков относились к роду Candida, чаще всего Candida albicans.

Statement en
: In studies of patients with unexplained GI complaints, roughly 97% of fungi identified in SIFO cases belonged to the genus Candida, most often Candida albicans.

Status
: preliminary

Tags
: candida

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Small Intestinal Bacterial and Fungal Overgrowth: Health Implications and Management Perspectives](https://pmc.ncbi.nlm.nih.gov/articles/PMC12030604/)


<a id="sifo-symptom-overlap"></a>
### sifo-symptom-overlap

Name ru
: Симптомы СИФО совпадают с СИБР

Name en
: SIFO symptoms overlap with SIBO

Statement ru
: Клинические проявления СИФО (боль, вздутие, газ, диарея) во многом совпадают с симптомами бактериального СИБР, что затрудняет разграничение без специфической диагностики (посев аспирата тонкой кишки).

Statement en
: SIFO's clinical picture (pain, bloating, gas, diarrhoea) largely overlaps with bacterial SIBO, which makes the two hard to tell apart without specific testing (small-bowel aspirate culture).

Status
: preliminary

Tags
: candida, diagnosis

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Small Intestinal Bacterial and Fungal Overgrowth: Health Implications and Management Perspectives](https://pmc.ncbi.nlm.nih.gov/articles/PMC12030604/)


<a id="auto-brewery-marker"></a>
### auto-brewery-marker

Name ru
: Редкий, но абсолютно однозначный маркер: опьянение без алкоголя

Name en
: A rare but completely unambiguous marker: intoxication without alcohol

Statement ru
: В редких, но хорошо задокументированных случаях дрожжи (включая виды Candida) в тонкой кишке ферментируют съеденные углеводы в этанол прямо в кишечнике, вызывая настоящее алкогольное опьянение после богатой углеводами еды без единой капли спиртного — синдром аутоброжения. Это не самый частый симптом СИФО, но там, где он есть, спутать его с чем-то другим практически невозможно.

Statement en
: In rare but well-documented cases, yeast (including Candida species) in the small intestine ferments ingested carbohydrates into ethanol right there in the gut, producing genuine alcohol intoxication after a carb-heavy meal without a drop of alcohol consumed - auto-brewery syndrome. It isn't the most common SIFO symptom, but where it occurs, it is almost impossible to mistake for anything else.

Quote
: Intoxicating amounts of ethanol are produced through endogenous fermentation within the digestive system

Quote ru
: опьяняющие количества этанола образуются в результате эндогенного брожения внутри пищеварительной системы

Status
: confirmed

Tags
: candida, smell

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Auto-brewery syndrome](https://en.wikipedia.org/wiki/Auto-brewery_syndrome)


<a id="systemic-permeability"></a>
### systemic-permeability

Name ru
: Проницаемость: механизм правдоподобен, цепочка не доказана

Name en
: Permeability: plausible mechanism, unproven chain

Statement ru
: Цепочка «перерастяжение газом / биоплёнка → повреждение слизистого барьера → повышенная проницаемость → новые пищевые реакции» обсуждается в литературе как механизм, но убедительных клинических доказательств того, что она реализуется у типичного пациента с СИБР, недостаточно.

Statement en
: The chain "gas distension / biofilm -> damaged mucosal barrier -> increased permeability -> new food reactions" is discussed in the literature as a mechanism, but solid clinical evidence that it plays out in a typical SIBO patient is lacking.

Status
: mechanistic

Tags
: systemic

Relations
: → belongs-to: [systemic-consequences](topics.md#systemic-consequences)

Sources
: [Small Intestinal Bacterial and Fungal Overgrowth: Health Implications and Management Perspectives](https://pmc.ncbi.nlm.nih.gov/articles/PMC12030604/)


<a id="systemic-sphincter-oddi-claim"></a>
### systemic-sphincter-oddi-claim

Name ru
: Спазм сфинктера Одди / панкреатит — не подтверждено

Name en
: Sphincter of Oddi spasm / pancreatitis - unsupported

Statement ru
: Утверждение, что вздутие при СИБР регулярно вызывает спазм сфинктера Одди и вторичный панкреатит, не нашло подтверждения в проверенной нами гастроэнтерологической литературе; это не признанное осложнение СИБР, а, судя по всему, непроверяемая экстраполяция.

Statement en
: The claim that SIBO-related bloating routinely causes sphincter of Oddi spasm and secondary pancreatitis found no support in the gastroenterology literature we checked; it is not a recognised SIBO complication, and appears to be an unsourced extrapolation.

Status
: insufficient-evidence

Tags
: systemic, correction

Relations
: → belongs-to: [systemic-consequences](topics.md#systemic-consequences)


<a id="bile-deconjugation-mechanism"></a>
### bile-deconjugation-mechanism

Name ru
: Деконъюгация желчи и мицеллы

Name en
: Bile deconjugation and micelles

Statement ru
: Бактерии деконъюгируют желчные кислоты, добывая из них энергию; деконъюгированная желчь не может формировать мицеллы, необходимые для растворения и всасывания жира.

Statement en
: Bacteria deconjugate bile acids to harvest energy from them; deconjugated bile can no longer form the micelles needed to dissolve and absorb fat.

Quote
: deconjugation of bile acids by florid small bowel bacterial overgrowth defunctionalizes the bile acids

Quote ru
: деконъюгация желчных кислот избыточной бактериальной флорой тонкой кишки делает эти кислоты функционально непригодными

Status
: confirmed

Tags
: malabsorption, fat

Relations
: → belongs-to: [cascade-fat-vitamins](topics.md#cascade-fat-vitamins)

Sources
: [Small and Large Intestine (I): Malabsorption of Nutrients](https://pmc.ncbi.nlm.nih.gov/articles/PMC8070135/)


<a id="vitamin-k-exception"></a>
### vitamin-k-exception

Name ru
: Витамин K — исключение из правила

Name en
: Vitamin K - the exception to the rule

Statement ru
: В отличие от A, D и E, дефицит витамина K при СИБР встречается редко, потому что те же кишечные бактерии, что мешают усвоению жира, сами же его синтезируют.

Statement en
: Unlike A, D and E, vitamin K deficiency is uncommon in SIBO, because the same gut bacteria that impair fat absorption also synthesise the vitamin themselves.

Quote
: vitamin K is synthesized by luminal bacteria, deficiency of this vitamin is rarely seen

Quote ru
: витамин K синтезируется просветной микрофлорой, поэтому его дефицит встречается редко

Status
: confirmed

Tags
: malabsorption, fat

Relations
: → belongs-to: [cascade-fat-vitamins](topics.md#cascade-fat-vitamins)

Sources
: [Introduction to Small Intestinal Bacterial Overgrowth](https://med.virginia.edu/ginutrition/wp-content/uploads/sites/199/2015/11/zaidelarticle-July-03.pdf)


<a id="b12-bacterial-competition"></a>
### b12-bacterial-competition

Name ru
: Как бактерии перехватывают B12

Name en
: How bacteria intercept B12

Statement ru
: Бактерии напрямую потребляют витамин B12 для собственных нужд и производят неактивные аналоги, которые конкурентно занимают рецепторы всасывания B12 в подвздошной кишке.

Statement en
: Bacteria directly consume vitamin B12 for their own use and produce inactive analogues that competitively occupy the B12 absorption receptors in the ileum.

Status
: confirmed

Tags
: malabsorption, b12

Relations
: → belongs-to: [cascade-b12-folate](topics.md#cascade-b12-folate)

Sources
: [Small and Large Intestine (I): Malabsorption of Nutrients](https://pmc.ncbi.nlm.nih.gov/articles/PMC8070135/)


<a id="b12-folate-lab-pattern"></a>
### b12-folate-lab-pattern

Name ru
: Низкий B12 при нормальной или высокой фолиевой кислоте

Name en
: Low B12 with normal or high folate

Statement ru
: В отличие от B12, часть кишечных бактерий синтезируют фолиевую кислоту и выделяют её в просвет кишки, поэтому типичная лабораторная картина при СИБР — сниженный B12 на фоне нормальной или повышенной фолиевой кислоты.

Statement en
: Unlike B12, many gut bacteria synthesise folate and release it into the gut lumen, so a typical SIBO lab pattern is low B12 alongside normal or elevated folate.

Status
: confirmed

Tags
: malabsorption, b12, diagnosis

Relations
: → belongs-to: [cascade-b12-folate](topics.md#cascade-b12-folate)

Sources
: [Comprehensive Review - Small Intestinal Bacterial Overgrowth (SIBO)](https://iihoms.org/PediatricGastroenterology/SIBO-review.html)


<a id="bacterial-caloric-theft"></a>
### bacterial-caloric-theft

Name ru
: Бактерии как конкурент за калории

Name en
: Bacteria as a calorie competitor

Statement ru
: Избыточные бактерии потребляют часть съеденных углеводов для собственной энергии раньше, чем те успевают всосаться кишечными клетками, что ведёт к потере калорий и труднообъяснимой потере веса.

Statement en
: Excess bacteria consume part of ingested carbohydrates for their own energy before intestinal cells can absorb them, leading to caloric loss and hard-to-explain weight loss.

Status
: confirmed

Tags
: malabsorption, calories

Relations
: → belongs-to: [cascade-carb-calories](topics.md#cascade-carb-calories)

Sources
: [Small Intestinal Bacterial Overgrowth (SIBO) - Merck Manual Professional Edition](https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/small-intestinal-bacterial-overgrowth-sibo)


<a id="secondary-lactose-intolerance"></a>
### secondary-lactose-intolerance

Name ru
: Вторичная непереносимость лактозы

Name en
: Secondary lactose intolerance

Statement ru
: Повреждение щёточной каймы тонкой кишки на фоне СИБР может снижать выработку лактазы; клиническое исследование показало, что у пациентов с подтверждённой биопсией лактазной недостаточностью положительный тест на СИБР встречался значимо чаще.

Statement en
: Brush-border damage from ongoing SIBO can reduce lactase output; a clinical study found that patients with biopsy-confirmed lactase deficiency tested positive for SIBO significantly more often.

Status
: confirmed

Tags
: malabsorption, lactose

Relations
: → belongs-to: [cascade-carb-calories](topics.md#cascade-carb-calories)

Sources
: [Lactase Deficiency Diagnosed by Endoscopic Biopsy-based Method Is Associated With Positivity to Glucose Breath Test](https://pmc.ncbi.nlm.nih.gov/articles/PMC9837539)


<a id="fatigue-anemia-link"></a>
### fatigue-anemia-link

Name ru
: Анемия как прямая причина усталости

Name en
: Anaemia as a direct cause of fatigue

Statement ru
: Дефицит B12 (реже — железа) снижает способность крови переносить кислород, что напрямую проявляется постоянной усталостью независимо от количества сна.

Statement en
: B12 deficiency (less often, iron) reduces blood's oxygen-carrying capacity, which shows up directly as constant fatigue regardless of how much sleep a person gets.

Status
: confirmed

Tags
: fatigue, b12

Relations
: → belongs-to: [cascade-fatigue](topics.md#cascade-fatigue)

Sources
: [Comprehensive Review - Small Intestinal Bacterial Overgrowth (SIBO)](https://iihoms.org/PediatricGastroenterology/SIBO-review.html)


<a id="fatigue-caloric-sleep"></a>
### fatigue-caloric-sleep

Name ru
: Калории и сон складываются в то же ощущение

Name en
: Calories and sleep add up to the same feeling

Statement ru
: Потеря части калорий бактериям и нарушение сна из-за ночного вздутия/рефлюкса/позывов — два независимых, чисто механических вклада в усталость, дополняющих эффект анемии.

Statement en
: Calories lost to bacteria and sleep disruption from nighttime bloating/reflux/urgency are two independent, purely mechanical contributors to fatigue, on top of the anaemia effect.

Status
: mechanistic

Tags
: fatigue

Relations
: → belongs-to: [cascade-fatigue](topics.md#cascade-fatigue)


<a id="fatigue-inflammation-caveat"></a>
### fatigue-inflammation-caveat

Name ru
: Хроническое воспаление как причина — менее доказано

Name en
: Chronic inflammation as a cause - less proven

Statement ru
: Идея о хроническом вялотекущем воспалении от постоянного присутствия бактерий как отдельной причине усталости правдоподобна и изучается для дисбиоза в целом, но для СИБР конкретно доказательная база тоньше, чем для анемии, потери калорий и нарушения сна.

Statement en
: The idea of chronic low-grade inflammation from ongoing bacterial presence as a separate fatigue cause is plausible and studied for dysbiosis broadly, but for SIBO specifically the evidence is thinner than for anaemia, caloric loss, and sleep disruption.

Status
: insufficient-evidence

Tags
: fatigue, correction

Relations
: → belongs-to: [cascade-fatigue](topics.md#cascade-fatigue)


<a id="herx-reaction-origin"></a>
### herx-reaction-origin

Name ru
: Классическая реакция Яриша-Герксгеймера

Name en
: The classic Jarisch-Herxheimer reaction

Statement ru
: Реакция Яриша-Герксгеймера описана и подтверждена для антибиотикотерапии спирохетозных и близких инфекций (сифилис, болезнь Лайма, лептоспироз, Ку-лихорадка) — острая воспалительная реакция на массовый распад бактерий, обычно в первые 24 часа.

Statement en
: The Jarisch-Herxheimer reaction is described and confirmed for antibiotic treatment of spirochaetal and related infections (syphilis, Lyme disease, leptospirosis, Q fever) - an acute inflammatory reaction to mass bacterial lysis, usually within the first 24 hours.

Quote
: The JHR occurs when large quantities of toxins are released

Quote ru
: реакция возникает, когда в организм высвобождается большое количество токсинов

Status
: confirmed

Tags
: die-off

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)

Sources
: [Recurrent Jarisch-Herxheimer reaction in a patient with Q fever pneumonia: a case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2621130/)


<a id="herx-extrapolation-gut"></a>
### herx-extrapolation-gut

Name ru
: Перенос на СИБР/кандиду не подтверждён исследованиями

Name en
: The extension to SIBO/candida is not research-backed

Statement ru
: Перенос этой концепции на приём растительных антимикробных добавок при СИБР/кандиде («детокс-реакция») — устоявшийся термин в интегративной медицине, но контролируемых клинических исследований именно этого механизма в контексте пищевых добавок нам найти не удалось; относитесь к нему как к правдоподобному, но не доказанному объяснению недомогания в начале курса.

Statement en
: Extending this concept to herbal antimicrobial supplements for SIBO/candida (a "detox reaction") is an established term in integrative medicine, but we could not find controlled clinical studies of this specific mechanism in a supplement context; treat it as a plausible, not a proven, explanation for early-course malaise.

Status
: insufficient-evidence

Tags
: die-off, correction

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)


<a id="binders-general-caution"></a>
### binders-general-caution

Name ru
: Сорбенты связывают неизбирательно

Name en
: Binders bind non-selectively

Statement ru
: Сорбенты вроде цеолита или активированного угля физически связывают вещества в просвете кишки неизбирательно — это касается не только «токсинов», но и лекарств и части нутриентов, поэтому их разносят по времени с едой и другими препаратами минимум на 1.5-2 часа; это общее фармакологическое свойство адсорбентов, а не доказательство пользы именно при «die-off».

Statement en
: Binders such as zeolite or activated charcoal adsorb substances in the gut lumen non-selectively - this affects not just "toxins" but medications and some nutrients too, which is why they are timed at least 1.5-2 hours from food and other supplements; this is a general property of adsorbents, not evidence of benefit specifically for "die-off".

Status
: mechanistic

Tags
: die-off

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)


<a id="berberine-rct"></a>
### berberine-rct

Name ru
: Берберин против рифаксимина: идёт РКИ

Name en
: Berberine vs rifaximin: an RCT is underway

Statement ru
: Берберин напрямую сравнивается с рифаксимином в зарегистрированном рандомизированном клиническом исследовании (BRIEF-SIBO, Пекинский университет); опубликован протокол исследования, гипотеза — берберин не уступает рифаксимину по эффективности эрадикации.

Statement en
: Berberine is being directly compared with rifaximin in a registered randomised controlled trial (BRIEF-SIBO, Peking University); the trial protocol has been published, with the hypothesis that berberine is non-inferior to rifaximin for eradication.

Quote
: the first clinical trial assessing the eradication effects of two weeks of berberine treatment

Quote ru
: первое клиническое испытание, оценивающее эффект двухнедельного приёма берберина

Status
: preliminary

Tags
: eradication, berberine

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)

Sources
: [Berberine and rifaximin effects on small intestinal bacterial overgrowth: study protocol (BRIEF-SIBO)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9974661/)


<a id="herbal-vs-rifaximin-retrospective"></a>
### herbal-vs-rifaximin-retrospective

Name ru
: «46% против 34%» — из ретроспективного, не рандомизированного исследования

Name en
: "46% vs 34%" is from a retrospective, non-randomised study

Statement ru
: Часто цитируемое сравнение «46% против 34%» в пользу трав против рифаксимина получено в ретроспективном анализе историй болезни (не в рандомизированном исследовании): пациенты сами выбирали лечение, разница статистически не значима (p=.24), а использовались запатентованные комбинированные формулы (Dysbiocide/FC-Cidal, Candibactin-AR/BR), а не отдельно орегано или берберин.

Statement en
: The widely cited "46% vs 34%" comparison favouring herbs over rifaximin comes from a retrospective chart review (not a randomised trial): patients self-selected their treatment, the difference was not statistically significant (p=.24), and the herbal arm used proprietary combination formulas (Dysbiocide/FC-Cidal, Candibactin-AR/BR), not standalone oregano or berberine.

Quote
: Herbal therapies are at least as effective as rifaximin for resolution of SIBO

Quote ru
: травяная терапия по меньшей мере не уступает рифаксимину в разрешении СИБР

Status
: disputed

Tags
: eradication, correction

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)

Sources
: [Herbal Therapy Is Equivalent to Rifaximin for the Treatment of Small Intestinal Bacterial Overgrowth](https://pmc.ncbi.nlm.nih.gov/articles/PMC4030608/)


<a id="single-agent-evidence-gap"></a>
### single-agent-evidence-gap

Name ru
: Отдельных испытаний одного агента почти нет

Name en
: Almost no single-agent trials exist

Statement ru
: Прямых клинических испытаний одного только масла орегано, только берберина вне BRIEF-SIBO или только аллицина против СИБР у людей практически нет; доступные данные получены либо на комбинированных формулах, либо in vitro / на животных.

Statement en
: Direct human clinical trials of oregano oil alone, of berberine alone outside BRIEF-SIBO, or of allicin alone against SIBO are essentially absent; the available data come either from combination formulas or from in vitro / animal work.

Status
: insufficient-evidence

Tags
: eradication, correction

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)


<a id="allicin-methanogens-mechanism"></a>
### allicin-methanogens-mechanism

Name ru
: Аллицин против метаногенов — данные из животноводства, не медицины

Name en
: Allicin vs methanogens - livestock data, not clinical data

Statement ru
: Аллицин (из чеснока) подавляет рост метаногенных архей в исследованиях, посвящённых снижению метана у жвачных животных; прямых клинических испытаний аллицина против IMO у людей найти не удалось — перенос эффекта на человека остаётся предположением, а не установленным фактом.

Statement en
: Allicin (from garlic) does suppress methanogenic archaea in research aimed at reducing ruminant methane emissions; we could not find direct human clinical trials of allicin against IMO - extrapolating the effect to people remains an assumption, not an established fact.

Status
: insufficient-evidence

Tags
: eradication, imo

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)


<a id="caprylic-acid-invitro"></a>
### caprylic-acid-invitro

Name ru
: Каприловая кислота: доказательства только in vitro

Name en
: Caprylic acid: in-vitro evidence only

Statement ru
: Противогрибковое действие каприловой кислоты в отношении Candida показано преимущественно in vitro; контролируемых клинических испытаний у людей с диагностированным СИФО не найдено. При подтверждённом СИФО стандартом остаются рецептурные антимикотики (например, флуконазол).

Statement en
: Caprylic acid's antifungal action against Candida has mainly been shown in vitro; no controlled human trials in diagnosed SIFO were found. Where SIFO is confirmed, prescription antifungals (e.g. fluconazole) remain the standard of care.

Status
: insufficient-evidence

Tags
: eradication, candida

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)

Sources
: [Small intestinal fungal overgrowth - AMBOSS](https://www.amboss.com/us/knowledge/small-intestinal-fungal-overgrowth)


<a id="nac-biofilm-definition"></a>
### nac-biofilm-definition

Name ru
: Что такое биоплёнка

Name en
: What a biofilm is

Statement ru
: Биоплёнка — структурированное сообщество микробных клеток во внеклеточном полисахаридном матриксе; её присутствие называют одним из факторов, затрудняющих лечение СИБР/IMO антимикробными средствами.

Statement en
: A biofilm is a structured community of microbial cells embedded in an extracellular polysaccharide matrix; its presence is cited as one factor that makes SIBO/IMO harder to treat with antimicrobials.

Quote
: structured communities of microbial cells embedded in an extracellular polymeric substance matrix

Quote ru
: структурированные сообщества микробных клеток во внеклеточном полимерном матриксе

Status
: confirmed

Tags
: biofilm

Relations
: → belongs-to: [protocol-biofilm](topics.md#protocol-biofilm)

Sources
: [Biofilm Disruption Enhances Antimicrobial Therapy for SIBO and Intestinal Methanogen Overgrowth](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12701763/)


<a id="biofilm-disruptor-evidence-gap"></a>
### biofilm-disruptor-evidence-gap

Name ru
: Разрушать биоплёнку до эрадикации — рационально, но не доказано на людях

Name en
: Disrupt-then-treat is rational but not human-proven

Statement ru
: Идея «сначала разрушить биоплёнку (например, NAC), потом убивать патоген» механистически рациональна и обсуждается в свежих обзорах по СИБР/IMO, но клинических испытаний, доказывающих, что именно эта последовательность улучшает исходы у людей по сравнению с однократным приёмом антимикробных средств, пока мало.

Statement en
: The idea of "disrupt the biofilm first (e.g. with NAC), then kill the pathogen" is mechanistically rational and discussed in recent SIBO/IMO reviews, but there are still few clinical trials proving this sequence improves human outcomes compared with antimicrobials alone.

Status
: insufficient-evidence

Tags
: biofilm, correction

Relations
: → belongs-to: [protocol-biofilm](topics.md#protocol-biofilm)

Sources
: [Biofilm Disruption Enhances Antimicrobial Therapy for SIBO and Intestinal Methanogen Overgrowth](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12701763/)


<a id="prokinetic-mmc-rationale"></a>
### prokinetic-mmc-rationale

Name ru
: Зачем нужны прокинетики после эрадикации

Name en
: Why prokinetics matter after eradication

Statement ru
: Риск рецидива СИБР во многом связан с тем, восстановилась ли моторика: ММК в фазе покоя «выметает» остатки пищи и бактерий из тонкой кишки между приёмами пищи.

Statement en
: SIBO relapse risk is closely tied to whether motility has recovered: the fasting-phase MMC "sweeps" residual food and bacteria out of the small intestine between meals.

Status
: confirmed

Tags
: prokinetics

Relations
: → belongs-to: [protocol-prokinetics](topics.md#protocol-prokinetics)

Sources
: [Complementary and alternative treatment in functional dyspepsia](https://pmc.ncbi.nlm.nih.gov/articles/PMC5802680/)


<a id="ginger-mmc-evidence"></a>
### ginger-mmc-evidence

Name ru
: Имбирь и III фаза ММК: подтверждено в малых исследованиях

Name en
: Ginger and MMC phase III: shown in small studies

Statement ru
: В небольших исследованиях экстракт имбиря достоверно усиливал антральную моторику именно в III фазе ММК натощак — механизм действия имеет прямое клиническое подтверждение, хотя выборки небольшие.

Statement en
: In small studies, ginger extract reliably increased antral motility specifically during fasting-state MMC phase III - the mechanism has direct clinical support, though sample sizes are small.

Quote
: oral ginger improves gastroduodenal motility in the fasting state

Quote ru
: приём имбиря улучшает гастродуоденальную моторику в состоянии натощак

Status
: preliminary

Tags
: prokinetics, ginger

Relations
: → belongs-to: [protocol-prokinetics](topics.md#protocol-prokinetics)

Sources
: [Complementary and alternative treatment in functional dyspepsia](https://pmc.ncbi.nlm.nih.gov/articles/PMC5802680/)


<a id="artichoke-dyspepsia-not-sibo"></a>
### artichoke-dyspepsia-not-sibo

Name ru
: Артишок доказан при диспепсии, не при СИБР

Name en
: Artichoke is proven for dyspepsia, not SIBO

Statement ru
: Экстракт артишока (Cynara scolymus) имеет РКИ-подтверждение эффективности при функциональной диспепсии, но отдельных испытаний именно для профилактики рецидива СИБР после эрадикации найти не удалось - это перенос с смежного показания.

Statement en
: Artichoke leaf extract (Cynara scolymus) has RCT support for functional dyspepsia, but no dedicated trials for preventing SIBO relapse after eradication were found - this is a carry-over from an adjacent indication.

Status
: mechanistic

Tags
: prokinetics, correction

Relations
: → belongs-to: [protocol-prokinetics](topics.md#protocol-prokinetics)

Sources
: [Complementary and alternative treatment in functional dyspepsia](https://pmc.ncbi.nlm.nih.gov/articles/PMC5802680/)


<a id="glutamine-mixed-evidence"></a>
### glutamine-mixed-evidence

Name ru
: L-глутамин: доказан в других контекстах, не в этом

Name en
: L-glutamine: proven elsewhere, not here

Statement ru
: L-глутамин изучен как топливо для энтероцитов и применяется у пациентов в критическом состоянии или с синдромом короткой кишки; доказательств именно для «заживления» кишечника при бытовом СИБР и повышенной проницаемости у в остальном здоровых людей значительно меньше.

Statement en
: L-glutamine is studied as an enterocyte fuel and used in critically ill patients or those with short-bowel syndrome; evidence specifically for gut "healing" in everyday SIBO and increased permeability in otherwise healthy people is considerably thinner.

Status
: mechanistic

Tags
: healing

Relations
: → belongs-to: [protocol-healing](topics.md#protocol-healing)


<a id="pancreatic-enzyme-role"></a>
### pancreatic-enzyme-role

Name ru
: Ферменты «на весь курс» — практика функциональной медицины, не гайдлайн

Name en
: Enzymes "for the whole course" is functional-medicine practice, not a guideline

Statement ru
: Ферментные препараты (панкреатин) — стандартное лечение при подтверждённой экзокринной недостаточности поджелудочной железы; их профилактическое применение «на время курса эрадикации СИБР» у людей без диагностированной недостаточности — практика функциональной медицины, не показание, закреплённое в гастроэнтерологических гайдлайнах.

Statement en
: Pancreatic enzyme products (pancreatin) are standard treatment for confirmed exocrine pancreatic insufficiency; using them prophylactically "for the duration of a SIBO eradication course" in people without diagnosed insufficiency is functional-medicine practice, not an indication set out in gastroenterology guidelines.

Status
: insufficient-evidence

Tags
: schedule, correction

Relations
: → belongs-to: [protocol-schedule](topics.md#protocol-schedule)


<a id="course-titration-caution"></a>
### course-titration-caution

Name ru
: Постепенное введение агентов — разумно, но не протестировано как протокол

Name en
: Staggered introduction is sensible, but untested as a protocol

Statement ru
: Постепенное введение агентов по одному, с паузами в 1-2 дня, — разумная практика (легче связать реакцию с конкретным веществом), но конкретный график «5 этапов за N дней» как таковой в исследованиях не тестировался; сроки индивидуальны.

Statement en
: Introducing agents one at a time with 1-2 day gaps is sensible practice (it makes a reaction easier to attribute to a specific substance), but no study has tested this specific "5 stages over N days" schedule as such; timing is individual.

Status
: mechanistic

Tags
: schedule

Relations
: → belongs-to: [protocol-schedule](topics.md#protocol-schedule)
