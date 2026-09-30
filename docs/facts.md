<!-- Generated from data/ by .tad/tools/render.py. Do not edit by hand. -->

# Facts

<a id="acid-mmc-barrier"></a>
### acid-mmc-barrier

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

Status
: confirmed

Quote
: excessive numbers of bacteria in the small bowel causing GI symptoms

Tags
: mechanism

Relations
: → belongs-to: [sibo-sifo-overview](topics.md#sibo-sifo-overview)

Sources
: [ACG Clinical Guideline: Small Intestinal Bacterial Overgrowth](https://doi.org/10.14309/ajg.0000000000000501)


<a id="breath-test-diagnosis"></a>
### breath-test-diagnosis

Status
: confirmed

Quote
: A positive breath test is defined as a >20-ppm increase of hydrogen

Tags
: diagnosis

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)

Sources
: [Small Intestinal Bacterial Overgrowth (SIBO) - Merck Manual Professional Edition](https://www.merckmanuals.com/professional/gastrointestinal-disorders/malabsorption-syndromes/small-intestinal-bacterial-overgrowth-sibo)


<a id="hydrogen-symptoms"></a>
### hydrogen-symptoms

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

Status
: mechanistic

Quote
: food moves too quickly from your stomach to your duodenum

Tags
: symptoms, timing, correction

Relations
: → belongs-to: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)
: → also-relevant-to: [protocol-prokinetics](topics.md#protocol-prokinetics)

Sources
: [Symptoms & Causes of Dumping Syndrome](https://www.niddk.nih.gov/health-information/digestive-diseases/dumping-syndrome/symptoms-causes)


<a id="supragastric-belching-mechanism"></a>
### supragastric-belching-mechanism

Status
: confirmed

Quote
: the supragastric air flow occurs more quickly and is independent of esophageal peristalsis

Tags
: belching

Relations
: → belongs-to: [belching-differential](topics.md#belching-differential)

Sources
: [AGA Clinical Practice Update on Evaluation and Management of Belching, Abdominal Bloating, and Distention: Expert Review](https://www.gastrojournal.org/article/S0016-5085(23)00823-5/fulltext)


<a id="belching-vs-aerophagia-vs-sibo-gas"></a>
### belching-vs-aerophagia-vs-sibo-gas

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

Status
: preliminary

Quote
: Nevertheless, intraluminal impedance measurement is required to distinguish supragastric from gastric belching

Tags
: belching

Relations
: → belongs-to: [belching-differential](topics.md#belching-differential)

Sources
: [Supragastric belching: Pathogenesis, diagnostic issues and treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC9212115/)


<a id="gas-odor-chemistry"></a>
### gas-odor-chemistry

Status
: confirmed

Quote
: characterized by its rotten eggs or blocked sewer smell

Tags
: smell, chemistry

Relations
: → belongs-to: [h2s-sibo-markers](topics.md#h2s-sibo-markers)

Sources
: [Epithelial Electrolyte Transport Physiology and the Gasotransmitter Hydrogen Sulfide](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4745330/)


<a id="h2s-flatline-diagnostic-clue"></a>
### h2s-flatline-diagnostic-clue

Status
: preliminary

Tags
: smell, diagnosis

Relations
: → belongs-to: [h2s-sibo-markers](topics.md#h2s-sibo-markers)


<a id="imo-reclassification"></a>
### imo-reclassification

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

Status
: confirmed

Quote
: methane is detected in 30%-50% of the healthy adult population worldwide

Tags
: imo, symptoms

Relations
: → belongs-to: [methane-imo-markers](topics.md#methane-imo-markers)
: → also-relevant-to: [h2s-sibo-markers](topics.md#h2s-sibo-markers)

Sources
: [Methanogens, Methane and Gastrointestinal Motility](https://pmc.ncbi.nlm.nih.gov/articles/PMC3895606/)


<a id="sifo-debated"></a>
### sifo-debated

Status
: disputed

Quote
: The existence and clinical relevance of SIFO as a distinct entity remain debated

Tags
: candida

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Small intestinal fungal overgrowth - AMBOSS](https://www.amboss.com/us/knowledge/small-intestinal-fungal-overgrowth)


<a id="sifo-candida-dominant"></a>
### sifo-candida-dominant

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

Status
: confirmed

Quote
: Intoxicating amounts of ethanol are produced through endogenous fermentation within the digestive system

Tags
: candida, smell

Relations
: → belongs-to: [sifo-candida-markers](topics.md#sifo-candida-markers)

Sources
: [Auto-brewery syndrome](https://en.wikipedia.org/wiki/Auto-brewery_syndrome)


<a id="systemic-permeability"></a>
### systemic-permeability

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

Status
: insufficient-evidence

Tags
: systemic, correction

Relations
: → belongs-to: [systemic-consequences](topics.md#systemic-consequences)


<a id="bile-deconjugation-mechanism"></a>
### bile-deconjugation-mechanism

Status
: confirmed

Quote
: deconjugation of bile acids by florid small bowel bacterial overgrowth defunctionalizes the bile acids

Tags
: malabsorption, fat

Relations
: → belongs-to: [cascade-fat-vitamins](topics.md#cascade-fat-vitamins)

Sources
: [Small and Large Intestine (I): Malabsorption of Nutrients](https://pmc.ncbi.nlm.nih.gov/articles/PMC8070135/)


<a id="vitamin-k-exception"></a>
### vitamin-k-exception

Status
: confirmed

Quote
: vitamin K is synthesized by luminal bacteria, deficiency of this vitamin is rarely seen

Tags
: malabsorption, fat

Relations
: → belongs-to: [cascade-fat-vitamins](topics.md#cascade-fat-vitamins)

Sources
: [Introduction to Small Intestinal Bacterial Overgrowth](https://med.virginia.edu/ginutrition/wp-content/uploads/sites/199/2015/11/zaidelarticle-July-03.pdf)


<a id="b12-bacterial-competition"></a>
### b12-bacterial-competition

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

Status
: mechanistic

Tags
: fatigue

Relations
: → belongs-to: [cascade-fatigue](topics.md#cascade-fatigue)


<a id="fatigue-inflammation-caveat"></a>
### fatigue-inflammation-caveat

Status
: insufficient-evidence

Tags
: fatigue, correction

Relations
: → belongs-to: [cascade-fatigue](topics.md#cascade-fatigue)


<a id="herx-reaction-origin"></a>
### herx-reaction-origin

Status
: confirmed

Quote
: The JHR occurs when large quantities of toxins are released

Tags
: die-off

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)

Sources
: [Recurrent Jarisch-Herxheimer reaction in a patient with Q fever pneumonia: a case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2621130/)


<a id="herx-extrapolation-gut"></a>
### herx-extrapolation-gut

Status
: insufficient-evidence

Tags
: die-off, correction

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)


<a id="binders-general-caution"></a>
### binders-general-caution

Status
: mechanistic

Tags
: die-off

Relations
: → belongs-to: [protocol-binders](topics.md#protocol-binders)


<a id="berberine-rct"></a>
### berberine-rct

Status
: preliminary

Quote
: the first clinical trial assessing the eradication effects of two weeks of berberine treatment

Tags
: eradication, berberine

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)

Sources
: [Berberine and rifaximin effects on small intestinal bacterial overgrowth: study protocol (BRIEF-SIBO)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9974661/)


<a id="herbal-vs-rifaximin-retrospective"></a>
### herbal-vs-rifaximin-retrospective

Status
: disputed

Quote
: Herbal therapies are at least as effective as rifaximin for resolution of SIBO

Tags
: eradication, correction

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)

Sources
: [Herbal Therapy Is Equivalent to Rifaximin for the Treatment of Small Intestinal Bacterial Overgrowth](https://pmc.ncbi.nlm.nih.gov/articles/PMC4030608/)


<a id="single-agent-evidence-gap"></a>
### single-agent-evidence-gap

Status
: insufficient-evidence

Tags
: eradication, correction

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)


<a id="allicin-methanogens-mechanism"></a>
### allicin-methanogens-mechanism

Status
: insufficient-evidence

Tags
: eradication, imo

Relations
: → belongs-to: [protocol-eradication](topics.md#protocol-eradication)


<a id="caprylic-acid-invitro"></a>
### caprylic-acid-invitro

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

Status
: confirmed

Quote
: structured communities of microbial cells embedded in an extracellular polymeric substance matrix

Tags
: biofilm

Relations
: → belongs-to: [protocol-biofilm](topics.md#protocol-biofilm)

Sources
: [Biofilm Disruption Enhances Antimicrobial Therapy for SIBO and Intestinal Methanogen Overgrowth](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12701763/)


<a id="biofilm-disruptor-evidence-gap"></a>
### biofilm-disruptor-evidence-gap

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

Status
: preliminary

Quote
: oral ginger improves gastroduodenal motility in the fasting state

Tags
: prokinetics, ginger

Relations
: → belongs-to: [protocol-prokinetics](topics.md#protocol-prokinetics)

Sources
: [Complementary and alternative treatment in functional dyspepsia](https://pmc.ncbi.nlm.nih.gov/articles/PMC5802680/)


<a id="artichoke-dyspepsia-not-sibo"></a>
### artichoke-dyspepsia-not-sibo

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

Status
: mechanistic

Tags
: healing

Relations
: → belongs-to: [protocol-healing](topics.md#protocol-healing)


<a id="pancreatic-enzyme-role"></a>
### pancreatic-enzyme-role

Status
: insufficient-evidence

Tags
: schedule, correction

Relations
: → belongs-to: [protocol-schedule](topics.md#protocol-schedule)


<a id="course-titration-caution"></a>
### course-titration-caution

Status
: mechanistic

Tags
: schedule

Relations
: → belongs-to: [protocol-schedule](topics.md#protocol-schedule)
