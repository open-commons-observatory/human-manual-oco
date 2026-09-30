<!-- Generated from data/ by .tad/tools/render.py. Do not edit by hand. -->

# Topics

<a id="sibo-sifo-overview"></a>
### sibo-sifo-overview

Order key
: 10

Tags
: gi, overview

Relations
: ← belongs-to: [acid-mmc-barrier](facts.md#acid-mmc-barrier)
: ← belongs-to: [acg-definition](facts.md#acg-definition)
: ← subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← subtopic-of: [systemic-consequences](topics.md#systemic-consequences)
: ← subtopic-of: [malabsorption-cascades](topics.md#malabsorption-cascades)
: ← subtopic-of: [protocol-overview](topics.md#protocol-overview)


<a id="self-observation-markers"></a>
### self-observation-markers

Order key
: 15

Tags
: gi, markers

Relations
: → subtopic-of: [sibo-sifo-overview](topics.md#sibo-sifo-overview)
: ← subtopic-of: [hydrogen-sibo-markers](topics.md#hydrogen-sibo-markers)
: ← subtopic-of: [methane-imo-markers](topics.md#methane-imo-markers)
: ← subtopic-of: [h2s-sibo-markers](topics.md#h2s-sibo-markers)
: ← subtopic-of: [sifo-candida-markers](topics.md#sifo-candida-markers)
: ← subtopic-of: [belching-differential](topics.md#belching-differential)


<a id="hydrogen-sibo-markers"></a>
### hydrogen-sibo-markers

Order key
: 20

Tags
: gi, diagnosis

Relations
: → subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← belongs-to: [breath-test-diagnosis](facts.md#breath-test-diagnosis)
: ← belongs-to: [hydrogen-symptoms](facts.md#hydrogen-symptoms)
: ← belongs-to: [rapid-onset-diagnostic-logic](facts.md#rapid-onset-diagnostic-logic)
: ← belongs-to: [orocecal-transit-confound](facts.md#orocecal-transit-confound)


<a id="methane-imo-markers"></a>
### methane-imo-markers

Order key
: 30

Tags
: gi, diagnosis

Relations
: → subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← belongs-to: [imo-reclassification](facts.md#imo-reclassification)
: ← belongs-to: [imo-constipation-link](facts.md#imo-constipation-link)
: ← belongs-to: [methane-reduces-gas-volume](facts.md#methane-reduces-gas-volume)


<a id="h2s-sibo-markers"></a>
### h2s-sibo-markers

Order key
: 35

Tags
: gi, diagnosis, smell

Relations
: → subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← belongs-to: [gas-odor-chemistry](facts.md#gas-odor-chemistry)
: ← belongs-to: [h2s-flatline-diagnostic-clue](facts.md#h2s-flatline-diagnostic-clue)
: ← also-relevant-to: [methane-reduces-gas-volume](facts.md#methane-reduces-gas-volume)


<a id="sifo-candida-markers"></a>
### sifo-candida-markers

Order key
: 40

Tags
: gi, diagnosis, candida

Relations
: → subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← belongs-to: [sifo-debated](facts.md#sifo-debated)
: ← belongs-to: [sifo-candida-dominant](facts.md#sifo-candida-dominant)
: ← belongs-to: [sifo-symptom-overlap](facts.md#sifo-symptom-overlap)
: ← belongs-to: [auto-brewery-marker](facts.md#auto-brewery-marker)


<a id="belching-differential"></a>
### belching-differential

Order key
: 45

Tags
: gi, diagnosis, differential

Relations
: → subtopic-of: [self-observation-markers](topics.md#self-observation-markers)
: ← belongs-to: [supragastric-belching-mechanism](facts.md#supragastric-belching-mechanism)
: ← belongs-to: [belching-vs-aerophagia-vs-sibo-gas](facts.md#belching-vs-aerophagia-vs-sibo-gas)
: ← belongs-to: [belching-anxiety-formal-dx](facts.md#belching-anxiety-formal-dx)


<a id="systemic-consequences"></a>
### systemic-consequences

Order key
: 50

Tags
: gi, systemic

Relations
: → subtopic-of: [sibo-sifo-overview](topics.md#sibo-sifo-overview)
: ← belongs-to: [systemic-permeability](facts.md#systemic-permeability)
: ← belongs-to: [systemic-sphincter-oddi-claim](facts.md#systemic-sphincter-oddi-claim)


<a id="malabsorption-cascades"></a>
### malabsorption-cascades

Order key
: 55

Tags
: gi, systemic, malabsorption

Relations
: → subtopic-of: [sibo-sifo-overview](topics.md#sibo-sifo-overview)
: ← subtopic-of: [cascade-fat-vitamins](topics.md#cascade-fat-vitamins)
: ← subtopic-of: [cascade-b12-folate](topics.md#cascade-b12-folate)
: ← subtopic-of: [cascade-carb-calories](topics.md#cascade-carb-calories)
: ← subtopic-of: [cascade-fatigue](topics.md#cascade-fatigue)


<a id="cascade-fat-vitamins"></a>
### cascade-fat-vitamins

Order key
: 56

Tags
: gi, malabsorption

Relations
: → subtopic-of: [malabsorption-cascades](topics.md#malabsorption-cascades)
: ← belongs-to: [bile-deconjugation-mechanism](facts.md#bile-deconjugation-mechanism)
: ← belongs-to: [vitamin-k-exception](facts.md#vitamin-k-exception)


<a id="cascade-b12-folate"></a>
### cascade-b12-folate

Order key
: 57

Tags
: gi, malabsorption

Relations
: → subtopic-of: [malabsorption-cascades](topics.md#malabsorption-cascades)
: ← belongs-to: [b12-bacterial-competition](facts.md#b12-bacterial-competition)
: ← belongs-to: [b12-folate-lab-pattern](facts.md#b12-folate-lab-pattern)


<a id="cascade-carb-calories"></a>
### cascade-carb-calories

Order key
: 58

Tags
: gi, malabsorption

Relations
: → subtopic-of: [malabsorption-cascades](topics.md#malabsorption-cascades)
: ← belongs-to: [bacterial-caloric-theft](facts.md#bacterial-caloric-theft)
: ← belongs-to: [secondary-lactose-intolerance](facts.md#secondary-lactose-intolerance)


<a id="cascade-fatigue"></a>
### cascade-fatigue

Order key
: 59

Tags
: gi, malabsorption, fatigue

Relations
: → subtopic-of: [malabsorption-cascades](topics.md#malabsorption-cascades)
: ← belongs-to: [fatigue-anemia-link](facts.md#fatigue-anemia-link)
: ← belongs-to: [fatigue-caloric-sleep](facts.md#fatigue-caloric-sleep)
: ← belongs-to: [fatigue-inflammation-caveat](facts.md#fatigue-inflammation-caveat)


<a id="protocol-overview"></a>
### protocol-overview

Order key
: 60

Tags
: gi, protocol

Relations
: → subtopic-of: [sibo-sifo-overview](topics.md#sibo-sifo-overview)
: ← subtopic-of: [protocol-biofilm](topics.md#protocol-biofilm)
: ← subtopic-of: [protocol-eradication](topics.md#protocol-eradication)
: ← subtopic-of: [protocol-binders](topics.md#protocol-binders)
: ← subtopic-of: [protocol-prokinetics](topics.md#protocol-prokinetics)
: ← subtopic-of: [protocol-healing](topics.md#protocol-healing)
: ← subtopic-of: [protocol-schedule](topics.md#protocol-schedule)


<a id="protocol-biofilm"></a>
### protocol-biofilm

Order key
: 61

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [nac-biofilm-definition](facts.md#nac-biofilm-definition)
: ← belongs-to: [biofilm-disruptor-evidence-gap](facts.md#biofilm-disruptor-evidence-gap)


<a id="protocol-eradication"></a>
### protocol-eradication

Order key
: 62

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [berberine-rct](facts.md#berberine-rct)
: ← belongs-to: [herbal-vs-rifaximin-retrospective](facts.md#herbal-vs-rifaximin-retrospective)
: ← belongs-to: [single-agent-evidence-gap](facts.md#single-agent-evidence-gap)
: ← belongs-to: [allicin-methanogens-mechanism](facts.md#allicin-methanogens-mechanism)
: ← belongs-to: [caprylic-acid-invitro](facts.md#caprylic-acid-invitro)


<a id="protocol-binders"></a>
### protocol-binders

Order key
: 63

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [herx-reaction-origin](facts.md#herx-reaction-origin)
: ← belongs-to: [herx-extrapolation-gut](facts.md#herx-extrapolation-gut)
: ← belongs-to: [binders-general-caution](facts.md#binders-general-caution)


<a id="protocol-prokinetics"></a>
### protocol-prokinetics

Order key
: 64

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [prokinetic-mmc-rationale](facts.md#prokinetic-mmc-rationale)
: ← belongs-to: [ginger-mmc-evidence](facts.md#ginger-mmc-evidence)
: ← belongs-to: [artichoke-dyspepsia-not-sibo](facts.md#artichoke-dyspepsia-not-sibo)
: ← also-relevant-to: [orocecal-transit-confound](facts.md#orocecal-transit-confound)


<a id="protocol-healing"></a>
### protocol-healing

Order key
: 65

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [glutamine-mixed-evidence](facts.md#glutamine-mixed-evidence)


<a id="protocol-schedule"></a>
### protocol-schedule

Order key
: 66

Tags
: gi, protocol

Relations
: → subtopic-of: [protocol-overview](topics.md#protocol-overview)
: ← belongs-to: [pancreatic-enzyme-role](facts.md#pancreatic-enzyme-role)
: ← belongs-to: [course-titration-caution](facts.md#course-titration-caution)
