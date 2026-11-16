import random

def get_botany_question(cls_num, chapter, subtopic, q_idx):
    diff = "easy" if q_idx % 4 == 0 else ("hard" if q_idx % 4 == 3 else "medium")
    q_type = "assertion_reason" if q_idx % 7 == 0 else ("match_columns" if q_idx % 9 == 0 else "standard_mcq")

    # =========================================================================
    # CLASS 11 BOTANY
    # =========================================================================
    if "Biological Classification" in chapter:
        if "Five Kingdom" in subtopic:
            return (
                "In Whittaker's Five Kingdom system, what was the primary phylogenetic criterion used to demarcate Kingdom Fungi from Kingdom Plantae?",
                "Mode of nutrition (heterotrophic absorptive vs autotrophic) and chitinous cell wall composition",
                ["Presence vs absence of a nuclear membrane", "Unicellularity vs multicellularity", "Presence of flagella in all vegetative stages"],
                "Whittaker used cell structure, body organization, mode of nutrition, reproduction, and phylogenetic relationships.",
                "Taxonomic criteria in modern five kingdom biological classification.",
                "Fungi possess heterotrophic absorptive nutrition and chitinous walls, whereas plants possess autotrophic photosynthetic nutrition and cellulosic walls.",
                "Option A is false because both fungi and plants are eukaryotic.", diff, q_type
            )
        elif "Monera" in subtopic:
            return (
                "Methanogens, which produce methane from ruminant dung, belong to which group and possess which distinctive adaptive characteristic?",
                "Archaebacteria; complex branched-chain lipid structure in cell membrane conferring extreme resistance",
                ["Eubacteria; peptidoglycan cell wall with teichoic acids", "Cyanobacteria; thick gelatinous sheath", "Mycoplasma; complete lack of a cell wall"],
                "Archaebacteria have branched lipid monolayers/bilayers conferring extreme heat/chemical resistance.",
                "Cell envelope adaptations in Archaebacteria extremophiles.",
                "Methanogens are obligate anaerobic archaebacteria. Their branched-chain ether lipids reduce membrane fluidity and prevent cell lysis in harsh anaerobic environments.",
                "Option B refers to true bacteria (Eubacteria).", diff, q_type
            )
        elif "Fungi" in subtopic:
            return (
                "Aseptate, coenocytic multinucleate mycelium and reproduction via endogenous asexual sporangiospores are diagnostic of which class of fungi?",
                "Phycomycetes (such as Mucor, Rhizopus, and Albugo)",
                ["Ascomycetes (sac fungi)", "Basidiomycetes (club fungi)", "Deuteromycetes (fungi imperfecti)"],
                "Phycomycetes possess coenocytic aseptate hyphae; all higher fungi (Asco, Basidio, Deutero) have septate hyphae.",
                "Mycelial morphological classification of fungi.",
                "Phycomycetes hyphae are continuous tubes filled with multinucleated cytoplasm without septa. Asexual spores are formed endogenously in sporangia.",
                "Ascomycetes produce exogenous conidia and endogenous ascospores.", diff, q_type
            )
        else: # Viruses, Viroids & Lichens
            return (
                "Viroids differ fundamentally from viruses in possessing which molecular characteristic?",
                "Free infectious RNA molecule of low molecular weight lacking a protein capsid coat",
                ["Double-stranded DNA enclosed in a protein capsid coat", "Abnormal infectious prion proteins lacking genetic material", "Both single-stranded RNA and reverse transcriptase enzymes"],
                "Discovered by T.O. Diener in 1971 as infectious agents causing potato spindle tuber disease.",
                "Structural virology and sub-viral infectious particles.",
                "Viroids consist solely of a short strand of circular, single-stranded RNA without any protein coat (capsid).",
                "Option C describes retroviruses like HIV.", diff, q_type
            )

    elif "Plant Kingdom" in chapter:
        if "Algae" in subtopic:
            algae = [
                ("Chlorophyceae (Green algae)", "Chlorophyll a and b", "Starch", "Cellulose and pectose"),
                ("Phaeophyceae (Brown algae)", "Chlorophyll a, c and Fucoxanthin", "Mannitol and laminarin", "Cellulose and algin"),
                ("Rhodophyceae (Red algae)", "Chlorophyll a, d and r-phycoerythrin", "Floridean starch", "Cellulose, pectin and polysulphate esters")
            ]
            item = algae[q_idx % len(algae)]
            return (
                f"Which major photosynthetic pigments, stored food reserve, and cell wall components are diagnostic of class {item[0]}?",
                f"Pigments: {item[1]}; Food: {item[2]}; Wall: {item[3]}",
                [f"Pigments: {algae[(q_idx+1)%3][1]}; Food: {algae[(q_idx+1)%3][2]}", f"Pigments: {algae[(q_idx+2)%3][1]}; Food: {item[2]}", f"Pigments: {item[1]}; Food: Glycogen"],
                "Table 3.1 in NCERT Plant Kingdom summarizes division of algae and their main characteristics.",
                "Phycological taxonomy and biochemical classification of algae.",
                f"{item[0]} are characterized by {item[1]} photosynthetic pigments and accumulate {item[2]} as their primary osmotic energy reserve.",
                "Mixing up fucoxanthin (brown) and r-phycoerythrin (red) is a very common NEET trap.", diff, q_type
            )
        elif "Bryophytes" in subtopic:
            return (
                "Why are Bryophytes classically termed the 'Amphibians of the Plant Kingdom'?",
                "They live in soil but require a thin film of external water for flagellated antherozoids to swim and fertilize the archegonium",
                ["They can respire using both lungs and moist vegetative surfaces", "They switch between autotrophic and heterotrophic modes of nutrition", "Their sporophyte is completely free-living and independent of gametophyte"],
                "Water is an absolute necessity for zooidogamous fertilization in bryophytes.",
                "Ecological and reproductive adaptations in non-vascular embryophytes.",
                "Bryophytes require external water to enable biflagellated male antherozoids to swim to the archegonium mouth to effect fertilization.",
                "Option D is false; the bryophyte sporophyte is physically attached to and parasitic on the photosynthetic gametophyte.", diff, q_type
            )
        elif "Pteridophytes" in subtopic:
            return (
                "Heterospory, a critical evolutionary precursor to the seed habit, is exhibited by which pteridophytes?",
                "Selaginella and Salvinia (producing microspores and megaspores)",
                ["Dryopteris and Pteris (strictly homosporous)", "Equisetum (horsetail) and Lycopodium", "Psilotum and Adiantum"],
                "Heterosporous pteridophytes produce distinct male microspores and female megaspores.",
                "Evolution of heterospory and origin of seed habit in vascular cryptogams.",
                "Selaginella and Salvinia produce small microspores and large megaspores, where female gametophytes are retained on the parent sporophytes.",
                "Most pteridophytes like Dryopteris, Pteris, and Equisetum are homosporous.", diff, q_type
            )
        else: # Gymnosperms & Cones
            return (
                "In Gymnosperms like Pinus and Cycas, the female gametophyte (endosperm) develops:",
                "Before fertilization and is strictly haploid ($n$)",
                ["After triple fusion and is triploid ($3n$)", "From the zygote and is diploid ($2n$)", "From nucellar tissue and is polyploid ($4n$)"],
                "Endosperm in gymnosperms is haploid ($n$) formed before fertilization; in angiosperms it is triploid ($3n$) formed post-fertilization.",
                "Comparative reproduction and endosperm ploidy in seed plants.",
                "The gymnosperm endosperm represents the vegetative tissue of the haploid female gametophyte developed directly from the functional megaspore before syngamy.",
                "Confusing gymnosperm endosperm ($n$) with angiosperm endosperm ($3n$) is a classic high-yield trap.", diff, q_type
            )

    elif "Morphology of Flowering Plants" in chapter:
        if "Root & Stem" in subtopic:
            return (
                "Pneumatophores (respiratory roots) that grow vertically upward above waterlogged marshy soil are adaptations found in:",
                "Rhizophora (halophytic mangrove vegetation)",
                ["Banyan tree (Ficus benghalensis, prop roots)", "Maize and sugarcane (stilt roots)", "Curcuma and sweet potato (tuberous adventitious roots)"],
                "Pneumatophores possess pneumathodes (lenticels) for oxygen uptake in anaerobic marshy soils.",
                "Morphological modifications of tap and adventitious root systems.",
                "In halophytes like Rhizophora growing in saline swamps, roots grow negative geotropically to obtain atmospheric oxygen for respiration.",
                "Option B and C represent mechanical support roots.", diff, q_type
            )
        elif "Leaf Venation" in subtopic:
            return (
                "Alternate, opposite, and whorled phyllotaxy (arrangement of leaves on stem) are classically exemplified by:",
                "China rose (alternate), Calotropis and Guava (opposite), Alstonia (whorled)",
                ["Alstonia (alternate), China rose (opposite), Calotropis (whorled)", "Calotropis (alternate), Alstonia (opposite), China rose (whorled)", "Mustard (opposite), Guava (alternate), Sunflower (whorled)"],
                "Phyllotaxy patterns: single leaf per node (alternate), pair at each node (opposite), multiple leaves in a whorl (whorled).",
                "Phyllotaxic classification in dicotyledonous shoots.",
                "In alternate phyllotaxy (China rose, mustard, sunflower), a single leaf arises at each node in an alternate manner. In opposite (Calotropis, guava), a pair of leaves arise. In whorled (Alstonia), more than two leaves arise at a node.",
                "Option D interchanges Calotropis and mustard patterns.", diff, q_type
            )
        elif "Inflorescence" in subtopic:
            return (
                "In an epigynous flower (such as Guava, Cucumber, and ray florets of Sunflower), the position of the ovary is:",
                "Inferior (margin of thalamus grows upward enclosing the ovary completely and getting fused with it)",
                ["Superior (hypogynous flower, as in Mustard and China rose)", "Half-inferior (perigynous flower, as in Plum, Rose, and Peach)", "Completely exposed and free above the perianth"],
                "Hypogynous = Superior ovary; Perigynous = Half-inferior; Epigynous = Inferior ovary.",
                "Floral morphology and ovary positional classification.",
                "In epigynous flowers, the thalamus completely encloses the ovary and fuses with its wall; sepals, petals, and stamens arise above the top of the ovary.",
                "Option B is Mustard/Brinjal; Option C is Rose/Peach.", diff, q_type
            )
        else: # Fruits & Seed
            return (
                "A mango fruit is classified as a drupe developed from a:",
                "Monocarpellary superior ovary with an edible fleshy mesocarp and stony hard endocarp",
                ["Multicarpellary inferior ovary with an edible endocarp", "Bicarpellary superior ovary with fleshy pericarp throughout", "Monocarpellary inferior ovary with fibrous epicarp"],
                "Drupes (mango, coconut) develop from monocarpellary superior ovaries and are one-seeded.",
                "Carpellary origin and pericarp zonation of drupaceous fruits.",
                "In mango, the pericarp is well differentiated into thin epicarp, fleshy edible mesocarp, and stony hard inner endocarp. In coconut, the mesocarp is fibrous.",
                "Option B describes berries like tomatoes.", diff, q_type
            )

    elif "Anatomy of Flowering Plants" in chapter:
        if "Meristematic" in subtopic:
            return (
                "Collenchyma tissue, which provides mechanical tensile support to growing petiole and young stems of dicots, is characterized by:",
                "Living cells with localized pectin, hemicellulose, and cellulose wall thickenings at corners, lacking intercellular spaces",
                ["Dead cells with uniform heavily lignified secondary cell walls and narrow lumens", "Living cells with thin cellulosic walls and prominent air cavities", "Non-nucleated enucleated conducting tubular cells with companion cells"],
                "Collenchyma has corner thickenings of pectin; sclerenchyma has uniform lignified walls.",
                "Histological characteristics of simple plant mechanical tissues.",
                "Collenchyma consists of living elongated cells with corners thickened by deposition of cellulose, hemicellulose, and pectin, providing flexibility without breaking.",
                "Option B describes sclerenchyma fibres and sclereids.", diff, q_type
            )
        elif "Vascular Bundles" in subtopic:
            return (
                "Radial vascular bundles, where xylem and phloem lie on alternating radii separated by non-vascular parenchyma, are typically found in:",
                "All roots (both dicot and monocot roots)",
                ["Dicot stems (conjoint open bundles)", "Monocot stems (conjoint closed scattered bundles)", "Isobilateral and dorsiventral leaves"],
                "Radial = Roots; Conjoint = Stems and Leaves.",
                "Stele architecture and vascular bundle orientation.",
                "In roots, xylem and phloem strands alternate along different radii (radial arrangement). In stems, xylem and phloem are conjointly arranged on the same radius.",
                "Option B and C have conjoint vascular bundles.", diff, q_type
            )
        elif "Anatomy of Dicot & Monocot" in subtopic:
            return (
                "Monocot roots differ anatomically from dicot roots in possessing:",
                "Polyarch xylem bundles (more than 6) and a large, well-developed pith",
                ["Diarch to hexarch xylem bundles and an inconspicuous pith", "Secondary growth with distinct cork cambium", "Ring-arranged open vascular bundles with cambium"],
                "Dicot roots have 2-6 (diarch to hexarch) xylem bundles; monocot roots have polyarch (>6) xylem bundles.",
                "Comparative internal anatomy of angiosperm roots.",
                "Monocot roots have numerous (usually >6) xylem patches (polyarch) and large central parenchymatous pith, completely lacking secondary growth.",
                "Option B is the diagnostic hallmark of dicot roots.", diff, q_type
            )
        else: # Secondary Growth
            return (
                "During secondary growth in a dicot stem, the active vascular cambium produces:",
                "Secondary xylem towards the interior (pith) in much greater amounts than secondary phloem towards the exterior",
                ["Equal amounts of secondary xylem and secondary phloem on both sides", "Secondary phloem towards the interior and secondary xylem towards the exterior", "Cork cells (phellem) towards the interior and phelloderm towards exterior"],
                "Cambium is more active on the inner side, generating 8-10 times more secondary xylem than phloem.",
                "Activity and bifacial production of secondary vascular tissues by the cambial ring.",
                "The vascular cambium ring cuts off secondary xylem cells inwards towards the pith and secondary phloem outwards towards the periphery, with xylem produced at a much higher rate.",
                "Option C reverses the orientation of secondary xylem/phloem.", diff, q_type
            )

    elif "Cell The Unit of Life" in chapter:
        if "Prokaryotic" in subtopic:
            return (
                "Mesosomes in prokaryotic bacteria represent specialized membranous invaginations that assist in which vital functions?",
                "Cell wall formation, DNA replication, daughter cell distribution, and respiration/secretion",
                ["Protein synthesis on 80S cytoplasmic ribosomes", "Phagocytosis of extracellular fluid particles", "Nuclear spindle apparatus assembly during mitosis"],
                "Mesosomes are formed by extensions of the plasma membrane into vesicles, tubules, and lamellae.",
                "Ultrastructure and physiological roles of prokaryotic plasma membrane derivatives.",
                "Mesosomes increase plasma membrane surface area, harbor respiratory electron transport enzymes, and assist in cell wall synthesis and chromosome partition.",
                "Bacteria have 70S ribosomes and lack mitotic spindle fibers.", diff, q_type
            )
        elif "Endomembrane" in subtopic:
            return (
                "Which sequence accurately maps the biosynthetic and modification pathway of secretory glycoproteins through the endomembrane system?",
                "Rough Endoplasmic Reticulum (RER) $\\rightarrow$ cis-face Golgi $\\rightarrow$ trans-face Golgi $\\rightarrow$ Secretory vesicles",
                ["Smooth Endoplasmic Reticulum $\\rightarrow$ Lysosome $\\rightarrow$ Peroxisome", "Golgi complex $\\rightarrow$ Rough ER $\\rightarrow$ Nucleus", "Chloroplast $\\rightarrow$ Vacuole $\\rightarrow$ Plasma membrane"],
                "Proteins synthesized on RER ribosomes are modified in Golgi cis/trans cisternae before targeted vesicle release.",
                "Endomembrane compartmentalization and vesicular trafficking.",
                "Proteins enter RER lumen, are packaged into transport vesicles fusing with the cis (forming) face of Golgi, undergo glycosylation, and exit from the trans (maturing) face.",
                "Option B starts from SER (lipid synthesis, not secretory protein synthesis).", diff, q_type
            )
        elif "Mitochondria" in subtopic:
            return (
                "Both mitochondria and chloroplasts are classified as semi-autonomous organelles because they possess:",
                "Their own circular double-stranded DNA, RNA, 70S ribosomes, and self-replicating capacity",
                ["A single outer membrane identical to eukaryotic plasma membrane", "Complete autonomy independent of nuclear gene expression", "80S ribosomes identical to the surrounding cytosol"],
                "Endosymbiotic hypothesis: evolved from engulfed prokaryotes.",
                "Organellar autonomy and prokaryotic endosymbiosis in eukaryotes.",
                "Both mitochondria and chloroplasts contain circular DNA molecules, RNA, and 70S ribosomes, allowing synthesis of some of their own structural and functional proteins.",
                "Option B is false; many organelle proteins are encoded by the cell nucleus.", diff, q_type
            )
        else: # Nucleus & Chromosome Structure
            return (
                "A chromosome with the centromere situated close to one end, forming one extremely short arm and one very long arm, is termed:",
                "Acrocentric chromosome",
                ["Metacentric chromosome (equal arms, median centromere)", "Sub-metacentric chromosome (slightly unequal arms)", "Telocentric chromosome (terminal centromere)"],
                "Chromosome morphology based on centromere position.",
                "Karyotypic chromosome classification and centromere positioning.",
                "Metacentric has centromere at center ($V$-shaped). Sub-metacentric has centromere near center ($L$-shaped). Acrocentric has centromere near end ($J$-shaped). Telocentric has terminal centromere ($i$-shaped).",
                "Option B describes slightly unequal arms, not an extremely short arm.", diff, q_type
            )

    elif "Cell Cycle and Cell Division" in chapter:
        if "Interphase" in subtopic:
            return (
                "During which phase of the eukaryotic cell cycle does genomic DNA replication and duplication of the cytoplasmic centriole occur?",
                "S phase (Synthesis phase), where DNA content per cell doubles from $2C$ to $4C$ while chromosome number remains $2n$",
                ["G1 phase, where chromosome number doubles from $2n$ to $4n$", "G2 phase, where chromosomal condensation initiates", "M phase, during equatorial metaphase alignment"],
                "DNA replicates strictly during the S phase of interphase.",
                "Cell cycle phases and genomic duplication kinetics.",
                "During S phase, DNA content per cell doubles ($2C \\rightarrow 4C$), but the ploidy and chromosome count remain strictly unchanged ($2n$). Centriole duplication also occurs in the cytoplasm.",
                "Students often mistakenly equate doubling of DNA content with doubling of chromosome number.", diff, q_type
            )
        elif "Mitosis" in subtopic:
            return (
                "The complete alignment of all chromosomes along the equatorial plate and attachment of spindle fibers to kinetochores is characteristic of:",
                "Metaphase (the optimal stage for studying chromosome morphology and karyotyping)",
                ["Prophase (chromatin condensation and aster formation)", "Anaphase (splitting of centromeres and sister chromatid separation)", "Telophase (nuclear envelope reformation around chromosome clusters)"],
                "Chromosomes align at the equatorial metaphase plate.",
                "Mitotic karyokinesis and spindle fiber-kinetochore interaction.",
                "In metaphase, spindle fibers attach to the disc-shaped kinetochores on centromeres, aligning sister chromatids at the equatorial metaphase plate.",
                "Anaphase involves centromere cleavage and poleward movement, not equatorial alignment.", diff, q_type
            )
        elif "Meiosis I Prophase" in subtopic:
            return (
                "Crossing over between non-sister chromatids of homologous chromosomes, mediated by the enzyme recombinase, occurs during which stage of Prophase I?",
                "Pachytene stage (recombination nodules visible under electron microscope)",
                ["Leptotene stage (beaded chromomeres appearance)", "Zygotene stage (synapsis and synaptonemal complex formation)", "Diplotene stage (dissolution of synaptonemal complex and chiasmata formation)"],
                "Crossing over occurs in Pachytene; synapsis occurs in Zygotene.",
                "Meiotic genetic recombination and homologous chromosome crossing over.",
                "Zygotene forms the synaptonemal complex. Pachytene exhibits crossing over via recombinase. Diplotene forms X-shaped chiasmata. Diakinesis shows terminalisation.",
                "Confusing Zygotene (pairing) with Pachytene (exchange) is a very frequent exam pitfall.", diff, q_type
            )
        else: # Significance of Meiosis & Synaptonemal Complex
            return (
                "Terminalisation of chiasmata and complete breakdown of the nucleolus and nuclear envelope mark the transition from which final prophase stage?",
                "Diakinesis, the concluding stage of Meiosis I Prophase I",
                ["Diplotene stage", "Pachytene stage", "Metaphase I"],
                "Terminalisation of chiasmata occurs in Diakinesis.",
                "Terminalisation and transition to meiotic metaphase.",
                "Diakinesis is marked by terminalisation of chiasmata, complete spindle assembly, and breakdown of nucleolus and nuclear envelope.",
                "Chiasmata become visible in Diplotene, but terminalise in Diakinesis.", diff, q_type
            )

    elif "Photosynthesis in Higher Plants" in chapter:
        if "Light Reactions" in subtopic:
            return (
                "In non-cyclic photophosphorylation (Z-scheme), the primary source of replacement electrons for the oxidized reaction center $P_{680}$ of PS II is:",
                "Photolysis (splitting) of water: $2\\text{H}_2\\text{O} \\rightarrow 4\\text{H}^+ + \\text{O}_2 + 4e^-$ at the Oxygen Evolving Complex",
                ["Oxidation of plastocyanin by cytochrome b6f", "Reduction of $\\text{NADP}^+$ by ferredoxin", "Cyclic electron flow returning from Photosystem I ($P_{700}$)"],
                "Water splitting occurs on the lumen side of the thylakoid membrane associated with PS II.",
                "Thylakoid electron transport and photolysis of water in Photosystem II.",
                "The water-splitting complex associated with PS II on the inner thylakoid membrane splits water into protons, electrons, and molecular oxygen. These electrons fill the hole in $P_{680}$.",
                "PS I receives electrons from PS II via plastocyanin, not direct water photolysis.", diff, q_type
            )
        elif "Calvin Cycle" in subtopic:
            return (
                "To synthesize one molecule of glucose via the Calvin cycle ($C_3$ pathway), how many molecules of $\\text{ATP}$ and $\\text{NADPH}$ are stoichiometrically required?",
                "$18\\text{ ATP}$ and $12\\text{ NADPH}$ ($3\\text{ ATP}$ and $2\\text{ NADPH}$ per $\\text{CO}_2$ fixed)",
                ["$12\\text{ ATP}$ and $18\\text{ NADPH}$", "$30\\text{ ATP}$ and $12\\text{ NADPH}$", "$36\\text{ ATP}$ and $24\\text{ NADPH}$"],
                "Each turn of Calvin cycle fixes $1\\text{ CO}_2$ using $3\\text{ ATP}$ and $2\\text{ NADPH}$. For glucose ($6\\text{ C}$), multiply by 6.",
                "Energetics of Calvin cycle carbon assimilation.",
                "For $6\\text{ CO}_2$: $6 \\times 3\\text{ ATP} = 18\\text{ ATP}$, and $6 \\times 2\\text{ NADPH} = 12\\text{ NADPH}$.",
                "Option C ($30\\text{ ATP}$) is the requirement for $C_4$ plants (which require $30\\text{ ATP}$ and $12\\text{ NADPH}$ per glucose).", diff, q_type
            )
        elif "Hatch-Slack" in subtopic:
            return (
                "In $C_4$ plants (e.g. Maize, Sugarcane), the primary $\\text{CO}_2$ acceptor and initial carboxylation enzyme located in mesophyll cells are:",
                "Phosphoenolpyruvate (PEP, $3\\text{C}$) and PEP carboxylase (PEPcase)",
                ["Ribulose-1,5-bisphosphate (RuBP, $5\\text{C}$) and RuBisCO", "Oxaloacetic acid (OAA, $4\\text{C}$) and Malic dehydrogenase", "Pyruvate ($3\\text{C}$) and Pyruvate kinase"],
                "Mesophyll cells in $C_4$ plants lack RuBisCO and possess PEPcase.",
                "Spatial compartmentalization and Kranz anatomy in $C_4$ dicarboxylic acid pathway.",
                "Primary carboxylation occurs in mesophyll via PEP carboxylase, forming $4\\text{C}$ OAA. Decarboxylation and Calvin cycle occur in bundle sheath cells containing RuBisCO.",
                "RuBisCO is located exclusively in bundle sheath cells in $C_4$ plants, not in mesophyll.", diff, q_type
            )
        else: # Photorespiration & Limiting Factors
            return (
                "Photorespiration ($C_2$ cycle) in $C_3$ plants is initiated when RuBisCO binds oxygen instead of $\\text{CO}_2$, sequentially involving which three cellular organelles?",
                "Chloroplast $\\rightarrow$ Peroxisome $\\rightarrow$ Mitochondria",
                ["Chloroplast $\\rightarrow$ Golgi apparatus $\\rightarrow$ Lysosome", "Mitochondria $\\rightarrow$ Peroxisome $\\rightarrow$ Vacuole", "Chloroplast $\\rightarrow$ Endoplasmic reticulum $\\rightarrow$ Ribosome"],
                "Organelle sequence for $C_2$ cycle: Chloroplast $\\to$ Peroxisome $\\to$ Mitochondria.",
                "Organellar sequence and wastefulness of $C_2$ photorespiratory glycolate pathway.",
                "RuBP oxygenation in chloroplast yields 3-PGA and 2-phosphoglycolate. Glycolate moves to peroxisome (forming glycine), which moves to mitochondria (releasing $\\text{CO}_2$ and forming serine).",
                "Photorespiration consumes ATP without producing sugar or ATP.", diff, q_type
            )

    elif "Respiration in Plants" in chapter:
        if "Glycolysis" in subtopic:
            return (
                "During glycolysis in the cytoplasm, what is the net yield of $\\text{ATP}$ and $\\text{NADH} + \\text{H}^+$ per molecule of glucose oxidized to two molecules of pyruvate?",
                "$2\\text{ ATP}$ (net) and $2\\text{ NADH} + \\text{H}^+$ ($4\\text{ ATP}$ formed $- 2\\text{ ATP}$ invested)",
                ["$4\\text{ ATP}$ and $4\\text{ NADH}$", "$2\\text{ ATP}$ and $0\\text{ NADH}$", "$36\\text{ ATP}$ and $10\\text{ NADH}$"],
                "Glycolysis invests $2\\text{ ATP}$ and produces $4\\text{ ATP}$ by substrate-level phosphorylation.",
                "Glycolytic pathway energetics and substrate-level phosphorylation.",
                "Investment phase: $2\\text{ ATP}$ used (hexokinase, PFK). Payoff phase: $4\\text{ ATP}$ formed, $2\\text{ NADH}$ generated. Net = $2\\text{ ATP} + 2\\text{ NADH}$.",
                "Gross ATP yield is 4, but net ATP is 2.", diff, q_type
            )
        elif "Citric Acid Cycle" in subtopic:
            return (
                "In the mitochondrial matrix Krebs cycle, substrate-level phosphorylation (formation of $\\text{GTP} / \\text{ATP}$) occurs during the conversion of:",
                "Succinyl-CoA to Succinic acid, catalyzed by succinyl-CoA synthetase",
                ["Isocitrate to $\\alpha$-ketoglutarate", "$\\alpha$-ketoglutarate to Succinyl-CoA", "Fumarate to Malate"],
                "Only one substrate-level phosphorylation step exists in Krebs cycle: Succinyl-CoA $\\to$ Succinate.",
                "Enzymatic steps and substrate-level phosphorylation in tricarboxylic acid (TCA) cycle.",
                "Cleavage of the high-energy thioester bond in succinyl-CoA drives GTP/ATP synthesis from GDP/ADP and inorganic phosphate.",
                "$\\alpha$-ketoglutarate to succinyl-CoA produces NADH, not GTP.", diff, q_type
            )
        elif "Electron Transport System" in subtopic:
            return (
                "In the mitochondrial inner membrane ETS, Complex IV (Cytochrome c oxidase) contains which metallic and cytochromic centers?",
                "Cytochrome $a$, Cytochrome $a_3$, and two copper centers ($\\text{Cu}_A$ and $\\text{Cu}_B$)",
                ["Cytochrome $b$, Cytochrome $c_1$, and Fe-S center", "NADH dehydrogenase and FMN", "Succinate dehydrogenase and FAD"],
                "Complex IV is cytochrome c oxidase, containing cyt $a, a_3$ and 2 copper centers.",
                "Mitochondrial respiratory complexes and terminal electron acceptor reduction.",
                "Complex IV passes electrons to molecular oxygen, reducing it to water ($2\\text{H}^+ + \\frac{1}{2}\\text{O}_2 + 2e^- \\to \\text{H}_2\\text{O}$).",
                "Complex III contains cytochrome $b$ and $c_1$.", diff, q_type
            )
        else: # Oxidative Phosphorylation & Respiratory Quotient
            return (
                "When tripalmitin (a triglyceride fatty acid, $\\text{C}_{51}\\text{H}_{98}\\text{O}_6$) is utilized as the respiratory substrate, its Respiratory Quotient (RQ) is:",
                "$0.7$ (less than $1.0$ because fats contain less oxygen and require more $\\text{O}_2$ for complete combustion)",
                ["$1.0$ (characteristic of carbohydrates like glucose)", "$0.9$ (characteristic of proteins)", "$\\infty$ (characteristic of anaerobic fermentation)"],
                "$\\text{RQ} = \\text{Volume of } \\text{CO}_2 \\text{ evolved} / \\text{Volume of } \\text{O}_2 \\text{ consumed}$.",
                "Respiratory quotient stoichiometry of metabolic substrates.",
                "$2\\text{C}_{51}\\text{H}_{98}\\text{O}_6 + 145\\text{O}_2 \\rightarrow 102\\text{CO}_2 + 98\\text{H}_2\\text{O}$. $\\text{RQ} = \\frac{102}{145} \\approx 0.7$.",
                "Glucose RQ is 1.0; oxalic acid RQ is > 1.0; fats RQ is ~0.7.", diff, q_type
            )

    elif "Plant Growth and Development" in chapter:
        if "Auxins and Gibberellins" in subtopic:
            return (
                "The phenomenon where the growing apical bud inhibits the growth of lateral axillary buds is caused by:",
                "Auxin produced in the shoot apex (apical dominance; decapitation promotes lateral branching)",
                ["Cytokinin accumulating in the root tips", "Gibberellic acid causing internodal elongation", "Abscisic acid promoting leaf abscission"],
                "Auxin causes apical dominance. Removing shoot apex (decapitation) allows lateral buds to grow.",
                "Hormonal control of apical dominance and branching architecture.",
                "Auxins synthesized at the shoot apex migrate basipetally and suppress axillary buds. Decapitation removes the auxin source, allowing cytokinins to trigger lateral growth (used in tea plucking and hedge-making).",
                "Cytokinin counteracts apical dominance.", diff, q_type
            )
        elif "Cytokinins and Ethylene" in subtopic:
            return (
                "Which gaseous phytohormone promotes horizontal seedling growth, swelling of the axis, apical hook formation in dicot seedlings, and accelerates climacteric fruit ripening?",
                "Ethylene ($\\text{C}_2\\text{H}_4$)",
                ["Abscisic Acid (ABA)", "Gibberellin ($GA_3$)", "Indole-3-Acetic Acid (IAA)"],
                "Ethylene is the only gaseous plant hormone that promotes fruit ripening.",
                "Physiological actions of gaseous plant growth regulator ethylene.",
                "Ethylene induces the classic 'triple response' in seedlings and triggers respiratory climacteric (sudden rise in respiration) during fruit ripening.",
                "ABA is the stress hormone; ethylene is the ripening and senescence hormone.", diff, q_type
            )
        elif "Abscisic Acid" in subtopic:
            return (
                "Why is Abscisic Acid (ABA) classically designated as the 'Stress Hormone' of plants?",
                "It stimulates stomatal closure during water deficit and induces seed dormancy to survive desiccation",
                ["It promotes rapid stem elongation during flood conditions", "It triggers premature flowering under high temperature stress", "It stimulates root hair formation under nutrient depletion"],
                "ABA closes stomata during drought and induces seed dormancy.",
                "Abscisic acid signaling under environmental stress.",
                "Under water deficit, ABA increases in leaves and acts on guard cell membranes to efflux $\\text{K}^+$ ions, causing loss of turgor and stomatal closure.",
                "Gibberellins break seed dormancy, whereas ABA promotes dormancy.", diff, q_type
            )
        else: # Photoperiodism & Vernalization
            return (
                "The site of perception of light/dark duration for photoperiodic floral induction is located in the:",
                "Leaves (where the hypothetical mobile flowering stimulus 'florigen' is synthesized)",
                ["Shoot apical meristem only", "Root tips", "Lateral buds"],
                "Leaves perceive the photoperiodic stimulus.",
                "Photoperiodic perception and hormonal flowering induction in angiosperms.",
                "Leaves perceive the relative duration of day and night via phytochromes. The floral hormone (florigen) then migrates through the phloem to the shoot apex.",
                "Shoot apex undergoes differentiation, but leaves perceive the light stimulus.", diff, q_type
            )

    # =========================================================================
    # CLASS 12 BOTANY
    # =========================================================================
    elif "Sexual Reproduction in Flowering" in chapter:
        if "Microsporogenesis" in subtopic:
            return (
                "Which innermost wall layer of the microsporangium (anther) provides nourishment to the developing pollen grains and possesses dense cytoplasm with multinucleate cells?",
                "Tapetum",
                ["Endothecium (with fibrous thickenings for dehiscence)", "Middle layers", "Epidermis"],
                "Anther wall layers: Epidermis $\\rightarrow$ Endothecium $\\rightarrow$ Middle layers $\\rightarrow$ Tapetum.",
                "Microsporangium wall layers and tapetal nutritive specialization.",
                "The tapetum is the innermost nutritive layer nourishing developing microspore tetrads. It also synthesizes callase and sporopollenin precursors.",
                "Option B (Endothecium) aids in anther dehiscence, not microspore nourishment.", diff, q_type
            )
        elif "Megasporogenesis" in subtopic:
            return (
                "A typical mature monosporic (Polygonum-type) angiosperm female gametophyte (embryo sac) is structurally organized as:",
                "7-celled and 8-nucleate (3 antipodals, 2 synergids, 1 egg cell, and 1 central cell with 2 polar nuclei)",
                ["8-celled and 8-nucleate", "7-celled and 7-nucleate", "6-celled and 8-nucleate"],
                "Derived from 1 functional megaspore undergoing 3 successive mitotic nuclear divisions.",
                "Megagametogenesis and monosporic embryo sac architecture.",
                "Three mitotic divisions of the functional megaspore produce 8 nuclei. Cellularization produces 3 antipodal cells at the chalaza, an egg apparatus (1 egg + 2 synergids) at the micropyle, and a large central cell containing 2 polar nuclei (7 cells, 8 nuclei).",
                "Students commonly mistake it for 8-celled because there are 8 nuclei.", diff, q_type
            )
        elif "Double Fertilization" in subtopic:
            return (
                "Double fertilization, a unique defining hallmark of angiosperms, consists of which two simultaneous syngamic events?",
                "Syngamy (male gamete + egg $\\rightarrow$ diploid zygote) AND Triple Fusion (male gamete + 2 polar nuclei $\\rightarrow$ triploid PEN)",
                ["Syngamy (male gamete + synergid) and Apomixis", "Triple fusion between two male gametes and one vegetative nucleus", "Parthenogenesis and adventive embryony"],
                "Discovered by S.G. Nawaschin in Lilium and Fritillaria.",
                "Syngamy and triple fusion dynamics in angiospermic fertilization.",
                "One male gamete fuses with the egg cell nucleus to form a diploid ($2n$) zygote. The second male gamete fuses with the two polar nuclei in the central cell to produce the triploid ($3n$) Primary Endosperm Nucleus (PEN).",
                "Option B is nonsense; apomixis is asexual seed formation without fertilization.", diff, q_type
            )
        else: # Endosperm & Apomixis
            return (
                "Apomixis, observed in some species of Asteraceae and grasses, is defined biologically as:",
                "A form of asexual reproduction that mimics sexual reproduction by producing seeds without fertilization",
                ["Development of fruit without fertilization (parthenocarpy)", "Formation of embryos directly from unreduced microspores in anthers", "Fusion of two vegetative somatic cells to form a polyploid zygote"],
                "Apomixis produces viable seeds without syngamy or meiosis.",
                "Genetics and reproductive biology of agamospermy and apomixis.",
                "Apomictic seeds develop without syngamy, such as when a diploid egg cell forms without reduction division and develops into an embryo without fertilization, or through nucellar adventive embryony (Citrus, Mango).",
                "Option B describes Parthenocarpy (seedless fruits like banana), not Apomixis.", diff, q_type
            )

    elif "Principles of Inheritance" in chapter:
        if "Mendel's Monohybrid" in subtopic:
            return (
                "In a classical Mendelian dihybrid cross ($RrYy \\times RrYy$), what is the expected phenotypic ratio in the $F_2$ generation assuming independent assortment?",
                "$9:3:3:1$ (9 Round Yellow, 3 Round Green, 3 Wrinkled Yellow, 1 Wrinkled Green)",
                ["$1:2:1:2:4:2:1:2:1$ (this is the genotypic ratio)", "$9:3:4$ (recessive epistasis)", "$12:3:1$ (dominant epistasis)"],
                "Phenotypic dihybrid ratio is $(3:1) \\times (3:1) = 9:3:3:1$.",
                "Mendel's Law of Independent Assortment and dihybrid inheritance.",
                "The $F_2$ generation exhibits 4 distinct phenotypic classes: parental combinations ($9/16$ and $1/16$) and recombinant combinations ($3/16$ and $3/16$).",
                "Option B is the GENOTYPIC ratio of the dihybrid cross.", diff, q_type
            )
        elif "Incomplete Dominance" in subtopic:
            return (
                "In Antirrhinum majus (snapdragon), a cross between red-flowered ($RR$) and white-flowered ($rr$) plants yields all pink ($Rr$) $F_1$. In $F_2$, the phenotypic and genotypic ratios are:",
                "Both phenotypic and genotypic ratios are identical: $1:2:1$ (1 Red : 2 Pink : 1 White)",
                ["Phenotypic ratio is $3:1$; genotypic ratio is $1:2:1$", "Phenotypic ratio is $9:7$; genotypic ratio is $1:1$", "Phenotypic ratio is $1:1$; genotypic ratio is $1:2:1$"],
                "In incomplete dominance, heterozygote has intermediate phenotype, making phenotypic ratio equal genotypic ratio ($1:2:1$).",
                "Allelic interactions and incomplete dominance in flower pigmentation.",
                "Because allele $R$ is not completely dominant over $r$, $Rr$ produces half as much pigment, appearing pink. Hence $RR$ (Red), $Rr$ (Pink), and $rr$ (White) produce a $1:2:1$ ratio.",
                "Option A is classical complete dominance.", diff, q_type
            )
        elif "Chromosomal Theory" in subtopic:
            return (
                "In his Drosophila experiments, why did T.H. Morgan observe a significant deviation from the expected $9:3:3:1$ $F_2$ ratio for eye color and body color?",
                "The two genes were physically linked on the same X chromosome and did not assort independently",
                ["The genes underwent lethal mutations during gametogenesis", "Eye color in Drosophila is governed by multiple alleles with maternal inheritance", "Drosophila chromosomes undergo complete non-disjunction in females"],
                "Morgan established that linked genes on the same chromosome assort together unless recombination occurs.",
                "Physical gene linkage, recombination frequency, and chromosomal mapping.",
                "When genes are located on the same chromosome (linkage), parental gene combinations occur at a much higher frequency than non-parental recombinant combinations.",
                "Option B is irrelevant; linkage is physical association on a chromosome.", diff, q_type
            )
        else: # Genetic Disorders
            return (
                "Sickle-cell anemia is an autosomal recessive disorder caused by which specific point mutation in the $\\beta$-globin gene?",
                "A transversion point mutation converting GAG codon to GUG codon at the 6th position, substituting Glutamic acid with Valine",
                ["Deletion of 3 consecutive codons encoding phenylalanine", "Frame-shift mutation in the $\\alpha$-globin locus", "Substitution of Valine by Glutamic acid at the 12th codon"],
                "Position 6 of $\\beta$-globin: GAG (Glutamic acid, hydrophilic) $\\rightarrow$ GUG (Valine, hydrophobic).",
                "Molecular basis of point mutations and hemoglobinopathy.",
                "The hydrophobic valine causes sickle-cell hemoglobin ($HbS$) to polymerize under low oxygen tension, distorting biconcave RBCs into rigid sickle shapes.",
                "Option C inverts the substitution direction (it is Glutamic acid to Valine).", diff, q_type
            )

    elif "Molecular Basis of Inheritance" in chapter:
        if "Structure of DNA" in subtopic:
            return (
                "According to the Watson-Crick B-DNA double helix model, what are the pitch of the helix and the distance between adjacent base pairs?",
                "Pitch $= 3.4\\text{ nm}$ ($34\\text{ \\AA}$), with $10\\text{ bp}$ per turn and $0.34\\text{ nm}$ distance between adjacent base pairs",
                ["Pitch $= 2.0\\text{ nm}$, with $12\\text{ bp}$ per turn and $0.20\\text{ nm}$ distance", "Pitch $= 34\\text{ nm}$, with $100\\text{ bp}$ per turn and $3.4\\text{ nm}$ distance", "Pitch $= 1.54\\text{ nm}$, with $8\\text{ bp}$ per turn and $0.54\\text{ nm}$ distance"],
                "One complete turn has 10 base pairs over $3.4\\text{ nm}$.",
                "Spatial helical parameters and stereochemistry of B-form duplex DNA.",
                "B-DNA is a right-handed helix with diameter $2.0\\text{ nm}$, pitch $3.4\\text{ nm}$, and axial rise per base pair $= 3.4/10 = 0.34\\text{ nm}$.",
                "Confusing nanometers ($3.4\\text{ nm}$) with Angstroms ($34\\text{ \\AA}$) is a common unit trap.", diff, q_type
            )
        elif "Meselson-Stahl" in subtopic:
            return (
                "In the Meselson-Stahl experiment using $^{15}\\text{N}$ and $^{14}\\text{N}$ density gradient centrifugation in $\\text{CsCl}$, what was the isotopic distribution of DNA molecules after two generations ($40\\text{ minutes}$) in $^{14}\\text{NH}_4\\text{Cl}$?",
                "$50\\%$ Hybrid ($^{15}\\text{N}-^{14}\\text{N}$) DNA and $50\\%$ Light ($^{14}\\text{N}-^{14}\\text{N}$) DNA",
                ["$100\\%$ Hybrid ($^{15}\\text{N}-^{14}\\text{N}$) DNA", "$25\\%$ Heavy ($^{15}\\text{N}-^{15}\\text{N}$) and $75\\%$ Light ($^{14}\\text{N}-^{14}\\text{N}$) DNA", "$100\\%$ Light ($^{14}\\text{N}-^{14}\\text{N}$) DNA"],
                "Generation 0: $100\\%\\ ^{15}\\text{N}$. Gen 1 ($20\\text{ min}$): $100\\%$ Hybrid. Gen 2 ($40\\text{ min}$): $50\\%$ Hybrid, $50\\%$ Light.",
                "Semiconservative replication proof using equilibrium density gradient sedimentation.",
                "Each parental strand serves as a template. In Gen 2, 4 DNA duplexes are present: 2 hybrid duplexes and 2 fully light duplexes ($1:1$ ratio).",
                "Option A is the result after Generation 1 ($20\\text{ minutes}$).", diff, q_type
            )
        elif "Transcription" in subtopic:
            return (
                "In eukaryotic post-transcriptional processing of hnRNA, the addition of 7-methylguanosine triphosphate and adenylate residues ($200-300$) correspond to:",
                "Capping at the $5'$-end and Tailing (polyadenylation) at the $3'$-end, respectively",
                ["Tailing at the $5'$-end and Capping at the $3'$-end", "Splicing at both $5'$ and $3'$ ends simultaneously", "Methylation at the $3'$-end and dephosphorylation at the $5'$-end"],
                "Capping $= 5'$ end (m7Gppp); Tailing $= 3'$ end (poly-A tail).",
                "Eukaryotic pre-mRNA processing, 5'-capping, and 3'-polyadenylation.",
                "hnRNA undergoes 5'-capping with an unusual nucleotide (7-methylguanosine triphosphate) and 3'-tailing where 200-300 adenylate residues are added template-independently to protect mRNA from exonucleases.",
                "Option B reverses the $5'$ and $3'$ orientations.", diff, q_type
            )
        else: # Genetic Code & Translation
            return (
                "Which codon serves the dual function of initiating translation and coding for the amino acid Methionine?",
                "AUG codon",
                ["UAA codon (Ochre stop codon)", "UAG codon (Amber stop codon)", "UGA codon (Opal stop codon)"],
                "AUG codes for Methionine and is the initiator codon; UAA, UAG, and UGA are non-sense stop codons.",
                "Genetic code degeneracy, universality, and punctuation codons.",
                "AUG acts as the start codon recognized by initiator tRNA ($tRNA_i^{\\text{Met}}$) in ribosomal P-site. UAA, UAG, and UGA signal termination.",
                "Options B, C, and D are nonsense/stop termination codons.", diff, q_type
            )

    elif "Microbes in Human Welfare" in chapter:
        if "Food Processing" in subtopic:
            return (
                "The large holes in Swiss cheese are produced by which bacterium through which metabolic activity?",
                "Propionibacterium shermanii, producing large amounts of carbon dioxide ($\text{CO}_2$) gas during fermentation",
                ["Lactobacillus acidophilus, producing lactic acid", "Saccharomyces cerevisiae, producing ethanol", "Penicillium roqueforti, producing protease enzymes"],
                "Swiss cheese holes are due to $\text{CO}_2$ gas produced by Propionibacterium shermanii.",
                "Microbial fermentation in dairy food processing.",
                "Propionibacterium shermanii ferments lactic acid to propionic acid, acetic acid, and large bubbles of $\text{CO}_2$ gas that form the characteristic eyes/holes of Swiss cheese.",
                "Option C (Penicillium roqueforti) is used for ripening Roquefort cheese for flavor, not large holes.", diff, q_type
            )
        elif "Sewage Treatment" in subtopic:
            return (
                "During secondary biological sewage treatment in aeration tanks, the significant reduction of which parameter indicates purified effluent?",
                "Biochemical Oxygen Demand (BOD), indicating reduced organic matter pollution load",
                ["Dissolved oxygen content", "Total inorganic nitrogen and heavy metals", "Temperature and pH"],
                "BOD measures the rate of oxygen uptake by microorganisms; lower BOD indicates cleaner water.",
                "Aerobic flocs and biochemical oxygen demand kinetics in wastewater treatment.",
                "Vigorous aeration allows aerobic microbes to form 'flocs' (masses of bacteria associated with fungal filaments), which rapidly consume organic matter, dramatically decreasing effluent BOD.",
                "BOD is an indirect measure of organic matter, not toxic heavy metals.", diff, q_type
            )
        elif "Biogas" in subtopic:
            return (
                "The primary gas component in biogas produced by anaerobic digestion of cellulosic waste by Methanobacterium is:",
                r"Methane ($\text{CH}_4$, $50-70\%$), accompanied by $\text{CO}_2$ ($30-40\%$) and trace $\text{H}_2\text{S}$",
                [r"Carbon monoxide ($\text{CO}$, $80\%$)", r"Pure Oxygen ($\text{O}_2$, $90\%$)", r"Nitrogen dioxide ($\text{NO}_2$, $60\%$)"],
                "Biogas consists predominantly of methane ($\text{CH}_4$).",
                "Methanogenesis and anaerobic biogas digestor dynamics.",
                "Methanogens (anaerobic archaebacteria) break down cellulosic plant material anaerobically, producing a combustible mixture predominantly composed of methane and carbon dioxide.",
                "Option A is dangerous carbon monoxide (water gas), not biogas.", diff, q_type
            )
        else: # Biocontrol & Biofertilizers
            return (
                "Baculoviruses (genus Nucleopolyhedrovirus) are acclaimed biocontrol agents in Integrated Pest Management (IPM) because they:",
                "Possess narrow-spectrum, species-specific insecticidal action with no negative impacts on non-target plants, mammals, birds, or beneficial insects",
                ["Eradicate all soil invertebrates and microbes indiscriminately", "Produce broad-spectrum organophosphate toxins", "Infect only pollinating bees and earthworms"],
                "Nucleopolyhedroviruses have zero negative impact on non-target organisms.",
                "Biological control and ecological safety of viral bio-insecticides.",
                "Baculoviruses are pathogen specific, targeting exclusively harmful arthropod pests while preserving beneficial predators, parasites, and honeybees.",
                "Option B describes synthetic chemical insecticides.", diff, q_type
            )

    elif "Biotechnology Principles" in chapter:
        if "Restriction" in subtopic:
            return (
                "Restriction endonuclease EcoRI cleaves double-stranded DNA specifically at which palindromic recognition sequence and creates which type of ends?",
                "$5'\\text{-GAATTC-3'}$, cutting between G and A to produce staggered, cohesive 'sticky ends'",
                ["$5'\\text{-GGATCC-3'}$, producing blunt ends", "$5'\\text{-AAGCTT-3'}$, producing non-complementary single-stranded tails", "$5'\\text{-CTGCAG-3'}$, producing blunt phosphorylated ends"],
                "EcoRI recognizes GAATTC: cuts between G and A on both antiparallel strands.",
                "Palindromic sequence recognition and enzymatic cleavage by type II restriction endonucleases.",
                "EcoRI binds to $5'\\text{-G}\\downarrow\\text{AATTC-3'}$ and $3'\\text{-CTTAA}\\uparrow\\text{G-5'}$, leaving overhanging single-stranded sticky ends that readily form hydrogen bonds with complementary vector DNA.",
                "Option B is BamHI; Option C is HindIII.", diff, q_type
            )
        elif "pBR322" in subtopic:
            return (
                "In cloning vector pBR322, insertional inactivation of the $\\beta$-galactosidase gene (lacZ) or tetracycline resistance gene ($tet^R$) enables:",
                "One-step visual or phenotypic selection of recombinant transformants from non-recombinant colonies",
                ["Increased replication copy number of the foreign plasmid", "Lysis of host bacterial cells to release cloned gene products", "Formation of high-density competent cell membranes"],
                "Insertional inactivation of a selectable marker distinguishes recombinants from non-recombinants.",
                "Selectable markers and insertional inactivation principles.",
                "Insertion of foreign DNA into the coding region of a marker gene disrupts its expression. Recombinants lose tetracycline resistance or fail to produce blue color on X-gal media (appearing as white colonies).",
                "Option A is controlled by the 'ori' (origin of replication) and rop protein.", diff, q_type
            )
        elif "Polymerase Chain Reaction" in subtopic:
            return (
                "The enzyme Taq polymerase, essential for automated thermocycling in PCR, is isolated from which thermophilic organism and why?",
                "Thermus aquaticus; it remains stable and active at high denaturation temperatures ($94-95^\\circ\\text{C}$)",
                ["Escherichia coli; it exhibits ultra-high replication fidelity", "Bacillus thuringiensis; it synthesizes crystalline inclusion bodies", "Agrobacterium tumefaciens; it integrates T-DNA into plant genomes"],
                "Taq polymerase withstands repeated denaturation cycles at $94^\\circ\\text{C}$.",
                "Thermal kinetics of DNA amplification by Polymerase Chain Reaction.",
                "Standard DNA polymerases denature at $>65^\\circ\\text{C}$. Taq polymerase isolated from hot spring bacterium Thermus aquaticus retains full enzymatic activity across denaturation ($94^\\circ\\text{C}$), annealing ($54^\\circ\\text{C}$), and extension ($72^\\circ\\text{C}$).",
                "E. coli DNA polymerase denatures rapidly during the first denaturation step.", diff, q_type
            )
        else: # Bioreactors
            return (
                "Stirred-tank bioreactors are engineered with spargers and agitator impellers primarily to achieve:",
                "Optimal oxygen transfer, homogeneous mixing of nutrients, and precise temperature/pH control throughout the vessel",
                ["High-speed centrifugation to separate microbial pellets continuously", "Complete anaerobic sealing with zero gas exchange", "Ultrafiltration of intracellular enzymes under hydrostatic vacuum"],
                "Stirred-tank bioreactors ensure even aeration and agitation for maximum microbial biomass yield.",
                "Bioprocess engineering and downstream mass transfer in industrial fermenters.",
                "The curved base and motor-driven impellers facilitate even mixing and gas bubble dispersion, maximizing the surface area for oxygen dissolution required by aerobic production strains.",
                "Option B is false; aerobic production strains require continuous sterile oxygen sparging.", diff, q_type
            )

    elif "Biotechnology and its Applications" in chapter:
        if "Bt Cotton" in subtopic:
            return (
                "How does the inactive protoxin Cry protein from Bacillus thuringiensis kill sensitive lepidopteran insect larvae (e.g. bollworms)?",
                "The protoxin is solubilized by the alkaline pH of the insect midgut, cleaved by proteases into active toxin, and creates pores causing midgut cell lysis",
                ["It produces acidic burns in the larval foregut upon contact", "It binds irreversibly to acetylcholine receptors in the insect brain", "It inhibits cuticular chitin synthesis during larval molting"],
                "Alkaline gut pH solubilizes the inactive crystal protoxin.",
                "Mechanism of action of Bt crystalline Cry endotoxins.",
                "The crystalline Cry protein is an inactive protoxin. Once ingested, the alkaline pH of the insect midgut dissolves the crystals. Midgut proteases cleave it into an active toxin that binds epithelial cells, creating pores, causing swelling, lysis, and death.",
                "Option B describes organophosphate nerve poisons.", diff, q_type
            )
        elif "RNA Interference" in subtopic:
            return (
                "In RNA interference (RNAi) used to confer nematode resistance (Meloidogyne incognita) in tobacco roots, gene silencing is achieved by:",
                "Double-stranded RNA (dsRNA) triggering targeted enzymatic cleavage of specific nematode mRNA",
                ["Inhibition of DNA replication by synthetic nucleotide analogs", "Blocking protein transport across the nuclear pore complex", "Promoting hypermethylation of bacterial ribosomal subunits"],
                "RNAi involves targeted silencing of specific mRNA by complementary dsRNA.",
                "Post-transcriptional gene silencing via RNA-induced silencing complex (RISC).",
                "Using Agrobacterium vectors, both sense and anti-sense RNA are introduced into the host plant. They anneal to form dsRNA, which triggers Dicer and RISC to recognize and degrade the nematode's complementary mRNA.",
                "Option A describes antiviral chemotherapy, not endogenous RNAi.", diff, q_type
            )
        elif "Insulin & Gene Therapy" in subtopic:
            return (
                "In 1983, Eli Lilly company produced genetically engineered human insulin (Humulin) by:",
                "Synthesizing two separate DNA sequences for insulin chains A and B in E. coli, extracting them, and linking them via disulfide bonds",
                ["Cloning pro-insulin containing C-peptide and chemically removing it in vitro", "Extracting active insulin directly from transgenic sheep milk", "Transforming yeast with bovine pancreatic mRNA"],
                "Chains A and B were synthesized separately in E. coli and combined with disulfide bridges.",
                "Recombinant DNA technology in therapeutic peptide manufacturing.",
                "Human insulin consists of chain A (21 amino acids) and chain B (30 amino acids) linked by disulfide bonds. Synthesizing chains A and B separately eliminated the requirement to enzymatically excise the C-peptide from proinsulin.",
                "Human insulin does not contain C-peptide; proinsulin does.", diff, q_type
            )
        else: # Transgenic Animals & Biopiracy
            return (
                "The first transgenic cow, Rosie (produced in 1997), was genetically modified to produce humanized milk enriched in:",
                "Human $\\alpha$-lactalbumin ($2.4\\text{ g/L}$), making it nutritionally superior and balanced for human babies",
                ["Human growth hormone and recombinant clotting factor VIII", "Bovine somatotropin to double dairy yield", "Therapeutic monoclonal antibodies against hepatitis B"],
                "Rosie cow milk contained human $\\alpha$-lactalbumin at $2.4\\text{ g/L}$.",
                "Transgenic animal bioreactors and molecular pharming.",
                "Rosie's milk contained human $\\alpha$-lactalbumin ($2.4\\text{ g per litre}$), providing a nutritionally balanced product for infants who cannot tolerate cow's milk.",
                "Option B is a pituitary hormone, not a milk nutrient.", diff, q_type
            )

    elif "Organisms and Populations" in chapter:
        if "Abiotic Adaptations" in subtopic:
            return (
                "According to Allen's Rule in ecological adaptation, mammals inhabiting colder polar climates tend to possess:",
                "Shorter ears and shorter limbs to minimize surface area and reduce metabolic heat loss",
                ["Longer ears and longer limbs to dissipate heat", "Thinner subcutaneous blubber layers", "Absence of fur covering"],
                "Allen's Rule: extremities of endothermic animals are shorter in cold climates.",
                "Morphological thermoregulatory adaptations in endotherms.",
                "Reducing body extremity dimensions minimizes surface-area-to-volume ratio, decreasing conductive and radiative heat loss in sub-zero polar habitats.",
                "Option A is true for desert mammals like the fennec fox (heat dissipation).", diff, q_type
            )
        elif "Population Growth" in subtopic:
            return (
                "In the Verhulst-Pearl Logistic Growth equation $\\frac{dN}{dt} = rN\\left(\\frac{K - N}{K}\\right)$, when population density $N$ equals carrying capacity $K$ ($N = K$), growth rate $\\frac{dN}{dt}$ is:",
                "Zero (population reaches steady-state carrying capacity plateau)",
                ["Equal to intrinsic rate of increase $r$", "Infinitely large (exponential explosion)", "Negative infinity leading to instant extinction"],
                "When $N = K$, $\\frac{K - N}{K} = \\frac{0}{K} = 0$.",
                "Logistic population growth models and resource limitation.",
                "Environmental resistance curtails population increase as resources become limiting, yielding a sigmoid (S-shaped) curve where growth rate approaches zero as $N \\rightarrow K$.",
                "Option B describes exponential growth where resources are assumed infinite.", diff, q_type
            )
        elif "Predation" in subtopic:
            return (
                "Gause's Competitive Exclusion Principle states that:",
                "Two closely related species competing for the exact same limiting resources cannot coexist indefinitely; the inferior competitor will eventually be eliminated",
                ["Predators always drive their prey species to complete extinction", "Parasites never harm their host organisms", "Competing species always undergo mutual hybridisation"],
                "Gause's principle: complete competitors cannot coexist in the same ecological niche.",
                "Interspecific competition and ecological niche partitioning.",
                "When resources are limiting, competitive superior utilizes resource more efficiently, driving inferior competitor to extinction unless resource partitioning occurs.",
                "Option A is false; prudent predators maintain prey populations sustainably.", diff, q_type
            )
        else: # Mutualism & Commensalism
            return (
                "The ecological interaction between an orchid growing as an epiphyte on a mango tree branch is classified as:",
                "Commensalism ($+/0$, orchid benefits from physical support while mango tree is neither harmed nor benefited)",
                ["Mutualism ($+/+$, both derive essential metabolic nutrients)", "Parasitism ($+/-$, orchid derives water and minerals from mango xylem)", "Amensalism ($-/0$, mango tree is inhibited by orchid exudates)"],
                "Commensalism: one species benefits while the other is unaffected.",
                "Interspecific population interactions and commensalism.",
                "The epiphyte gains physical canopy access to sunlight and air moisture without penetrating mango tissue or extracting sap ($+/0$).",
                "Option B describes parasitic plants like Cuscuta (dodder).", diff, q_type
            )

    elif "Ecosystem" in chapter:
        if "Structure" in subtopic:
            return (
                "The rate of biomass production by autotrophic green plants per unit area over a time period is termed Primary Productivity. Net Primary Productivity (NPP) is mathematically expressed as:",
                "$\\text{NPP} = \\text{GPP} - R$ (Gross Primary Productivity minus Respiration losses)",
                ["$\\text{NPP} = \\text{GPP} + R$", "$\\text{NPP} = \\text{GPP} \\times R$", "$\\text{NPP} = \\frac{\\text{GPP}}{R}$"],
                "Net Primary Productivity is the biomass available to heterotrophs after plant respiration.",
                "Primary productivity thermodynamics in terrestrial and aquatic biomes.",
                "Gross Primary Productivity (GPP) is the total rate of organic matter synthesis during photosynthesis. A considerable amount is utilized by plants in respiration ($R$), leaving NPP available to primary consumers.",
                "Option B adds respiration, which violates mass balance.", diff, q_type
            )
        elif "Decomposition" in subtopic:
            return (
                "The process where water-soluble inorganic nutrients percolate deep into the soil horizon and get precipitated as unavailable salts during decomposition is termed:",
                "Leaching",
                ["Fragmentation (breakdown of detritus into smaller particles by earthworms)", "Catabolism (enzymatic degradation by bacteria and fungi)", "Humification (accumulation of dark amorphous humus)"],
                "Leaching removes water-soluble nutrients from the topsoil into lower horizons.",
                "Decomposition steps of plant and animal detritus.",
                "Decomposition comprises fragmentation, leaching, catabolism, humification, and mineralization. In leaching, water-soluble nutrients descend into deeper soil horizons.",
                "Option B is fragmentation; Option C is catabolism.", diff, q_type
            )
        elif "Pyramids" in subtopic:
            return (
                "Why is an ecological pyramid of energy ALWAYS upright and can never be inverted in any ecosystem?",
                "Energy transfer strictly obeys the Second Law of Thermodynamics, with only $\\sim 10\\%$ of energy transferred to the next trophic level while $90\\%$ is lost as metabolic heat",
                ["Carnivores always possess greater total biomass than herbivores", "Decomposers generate energy independently from soil minerals", "Top carnivores consume equal calories as primary producers"],
                "Lindeman's 10% law dictates that energy always decreases at successive trophic levels.",
                "Trophic thermodynamics and Lindeman's ten percent energy law.",
                "Energy flows unidirectionally from producers to apex consumers. Heat dissipation at each step means energy available at a higher trophic level is always less than at lower levels.",
                "Biomass pyramids can be inverted (e.g. phytoplankton < zooplankton in sea), but energy pyramids are ALWAYS upright.", diff, q_type
            )
        else: # Succession
            return (
                "In primary ecological succession on bare rocks (xerarch succession), which organisms serve as the pioneer species and how do they pave the way for higher plants?",
                "Lichens; they secrete organic acids that weather rock minerals into initial soil particles",
                ["Bryophytes; they develop woody stems directly on dry bare granite", "Submerged rooted hydrophytes; they retain silt runoff", "Forest hardwood climax trees; they sprout from subterranean rootstocks"],
                "Lichens are pioneer species in xerarch succession; phytoplankton in hydrarch.",
                "Ecological succession kinetics and soil pedogenesis.",
                "Crustose and foliose lichens colonize bare rock surfaces, producing carbonic and lichenic acids that etch and weather rocks, accumulating the first thin layer of soil suitable for mosses.",
                "Option C is the pioneer in aquatic (hydrarch) succession.", diff, q_type
            )

    else: # Biodiversity and Conservation
        if "Levels" in subtopic:
            return (
                "Why does species diversity and biodiversity decrease progressively as we move from the equator towards the polar regions (latitudinal gradient)?",
                "Tropical environments are older, climatically more stable and predictable, and receive higher solar energy fostering greater speciation rates",
                ["Poles receive higher solar insolation causing excessive mutational lethality", "Tropical rainforests undergo frequent glaciations promoting rapid extinction", "Polar oceans have higher salinity prohibiting marine invertebrate growth"],
                "Latitudinal gradient: Tropics harbor far higher species diversity than temperate or polar zones.",
                "Biogeographical patterns and evolutionary drivers of latitudinal biodiversity gradients.",
                "Unlike temperate regions subjected to frequent glaciations in the past, tropical latitudes have remained relatively undisturbed for millions of years, allowing prolonged evolutionary diversification.",
                "Option B is false; glaciations occurred repeatedly in temperate/polar regions, not the tropics.", diff, q_type
            )
        elif "Loss of Biodiversity" in subtopic:
            return (
                "Which driver among the 'Evil Quartet' is recognized by conservation biologists as the SINGLE MOST IMPORTANT cause driving animal and plant species to extinction?",
                "Habitat loss and fragmentation (e.g. destruction of Amazon rainforest for soybean cultivation)",
                ["Co-extinction of obligate mutualists", "Invasion of alien weed species", "Over-exploitation for commercial trade"],
                "Habitat destruction is the number one cause of global biodiversity loss.",
                "Anthropogenic causes of sixth mass extinction (The Evil Quartet).",
                "The Evil Quartet comprises: 1) Habitat loss & fragmentation, 2) Over-exploitation, 3) Alien species invasions, and 4) Co-extinctions. Habitat loss is quantitatively the most devastating.",
                "Option C and D are significant, but habitat destruction is the primary cause.", diff, q_type
            )
        elif "In-Situ" in subtopic:
            return (
                "Which conservation strategy exemplifies in-situ (on-site) biodiversity preservation?",
                "Biosphere Reserves, National Parks, and Sacred Groves (protecting endangered species within their natural intact ecosystem)",
                ["Botanical Gardens and Zoological Parks", "Cryopreservation of gametes at $-196^\\circ\\text{C}$ in liquid nitrogen", "Seed banks and pollen storage facilities"],
                "In-situ = on-site in natural habitat; Ex-situ = off-site in artificial enclosure.",
                "In-situ versus ex-situ ecological conservation paradigms.",
                "In-situ conservation protects species in their native wild ecosystem (e.g. 14 Biosphere Reserves, 90+ National Parks in India). Botanical gardens and seed banks are ex-situ.",
                "Options B, C, and D are all examples of EX-SITU conservation.", diff, q_type
            )
        else: # Ex-Situ
            return (
                "Cryopreservation of gametes of threatened and endangered species in viable and fertile conditions is carried out at:",
                "$-196^\\circ\\text{C}$ in liquid nitrogen (advanced ex-situ conservation)",
                ["$0^\\circ\\text{C}$ in refrigerated saline ice", "$-20^\\circ\\text{C}$ in commercial blast freezers", "$-80^\\circ\\text{C}$ in solid dry ice chambers"],
                "Cryopreservation uses liquid nitrogen at $-196^\\circ\\text{C}$.",
                "Biocryogenics and long-term germplasm preservation.",
                "Ultra-low temperature ($-196^\\circ\\text{C}$) in liquid nitrogen stops all cellular metabolic and enzymatic activities, preserving gamete DNA integrity indefinitely without degradation.",
                "Option B and C do not arrest enzymatic decomposition over extended decades.", diff, q_type
            )
