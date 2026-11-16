import random

def get_zoology_question(cls_num, chapter, subtopic, q_idx):
    diff = "easy" if q_idx % 4 == 0 else ("hard" if q_idx % 4 == 3 else "medium")
    q_type = "assertion_reason" if q_idx % 7 == 0 else ("match_columns" if q_idx % 9 == 0 else "standard_mcq")

    # =========================================================================
    # CLASS 11 ZOOLOGY
    # =========================================================================
    if "Animal Kingdom" in chapter:
        if "Non-Chordates" in subtopic:
            phyla = [
                ("Porifera (Sponges)", "Choanocytes (collar cells) lining the spongocoel and water canal system", "Flame cells", "Radula"),
                ("Cnidaria (Coelenterata)", "Cnidoblasts (stinging cells) with nematocysts and metagenesis in Obelia", "Comb plates", "Malpighian tubules"),
                ("Ctenophora (Comb jellies)", "Eight external rows of ciliated comb plates and bioluminescence", "Parapodia", "Choanocytes"),
                ("Platyhelminthes (Flatworms)", "Flame cells (solenocytes) for osmoregulation and excretion, acoelomate", "Pseudocoelom", "Radula"),
                ("Aschelminthes (Roundworms)", "Pseudocoelomate body plan with syncytial epidermis and muscular pharynx", "True coelom", "Canal system"),
                ("Echinodermata", "Water vascular system with tube feet, radial symmetry in adults and bilateral in larvae", "Nephridia", "Flame cells")
            ]
            item = phyla[q_idx % len(phyla)]
            return (
                f"Which unique anatomical feature is strictly diagnostic of phylum {item[0]}?",
                item[1],
                [f"Exclusively {item[2]} for locomotion and excretion", f"Possession of {item[3]} for respiration", "Open circulation with myogenic 4-chambered heart"],
                "Recall NCERT Table 4.2: Salient Features of Different Phyla.",
                "Taxonomic classification and diagnostic characters of invertebrate non-chordates.",
                f"Phylum {item[0]} is universally characterized by {item[1]}.",
                "Common trap is confusing flame cells (Platyhelminthes) with nephridia (Annelida).", diff, q_type
            )
        elif "Chordata" in subtopic:
            return (
                "Which four fundamental morphological characteristics define Phylum Chordata at some stage in their lifecycle?",
                "Notochord, dorsal hollow nerve cord, paired pharyngeal gill slits, and post-anal tail",
                ["Ventral solid nerve cord, open circulation, notochord, and gills", "Dorsal heart, notochord, absence of tail, and ventral nerve cord", "Cartilaginous vertebral column, scales, paired fins, and operculum"],
                "Recall the four cardinal diagnostic chordate features.",
                "Phylogenetic characteristics of Phylum Chordata.",
                "Chordates are characterized by a bilateral body plan possessing: 1. Notochord, 2. Dorsal tubular nerve cord, 3. Pharyngeal clefts, and 4. Post-anal tail.",
                "Option A describes non-chordates (ventral nerve cord).", diff, q_type
            )
        elif "Vertebrata" in subtopic:
            return (
                "Which anatomical characteristic distinguishes class Chondrichthyes (cartilaginous fishes) from class Osteichthyes (bony fishes)?",
                "Chondrichthyes have placoid scales, lack an operculum (exposed gill slits), and lack an air bladder (must swim constantly to avoid sinking)",
                ["Chondrichthyes have cycloid scales and an operculum covering their gills", "Chondrichthyes possess an air bladder for hydrostatic buoyancy", "Osteichthyes have cartilaginous vertebral columns and ventral mouths"],
                "Scale types, opercular covering, and air bladder presence in fish classes.",
                "Comparative anatomy and evolutionary adaptations in fish classes.",
                "Chondrichthyes possess cartilaginous endoskeletons, placoid scales, exposed gill slits without operculum, and no air bladder. Osteichthyes have bony skeletons, opercula, and air bladders.",
                "Option B attributes air bladder to Chondrichthyes, which is false.", diff, q_type
            )
        else: # Mammalia & Aves
            return (
                "Which set of anatomical features is unique and exclusive to Class Mammalia among all vertebrates?",
                "Mammary glands for nourishing young, hair on skin, external ear pinna, and 12 pairs of cranial nerves",
                ["Pneumatic hollow bones and four-chambered heart", "Presence of cloaca and epidermal scales", "Poikilothermic cold-blooded ectothermy"],
                "Mammary glands and external pinna are unique mammalian hallmarks.",
                "Taxonomic mammalian hallmarks and endothermic homeothermy.",
                "Mammals are uniquely diagnosed by functional mammary glands, hair/fur, and external ear pinnae. Pneumatic bones are unique to Aves (birds).",
                "Option A is characteristic of birds (Aves).", diff, q_type
            )

    elif "Structural Organisation" in chapter:
        if "Epithelial" in subtopic:
            return (
                "Which type of epithelial tissue forms the ultra-thin diffusion boundary in lung alveolar walls and capillary endothelium?",
                "Simple squamous epithelium",
                ["Simple cuboidal epithelium with brush border", "Simple ciliated columnar epithelium", "Stratified keratinized compound epithelium"],
                "Alveolar exchange requires minimal diffusion barrier thickness (< 1 mm).",
                "Histological organization of epithelial exchange surfaces.",
                "Simple squamous epithelium consists of a single thin layer of flattened cells with irregular boundaries, facilitating rapid passive gas diffusion.",
                "Option B lines proximal convoluted tubules (PCT) of kidneys for absorption.", diff, q_type
            )
        elif "Connective" in subtopic:
            return (
                "Tendons and Ligaments are classified under which category of connective tissue?",
                "Dense regular connective tissue (collagen fibers oriented in parallel bundles)",
                ["Loose areolar connective tissue", "Specialized vascular connective tissue", "Dense irregular connective tissue"],
                "Tendons connect muscle to bone; ligaments connect bone to bone.",
                "Histology and mechanical tensile properties of dense connective tissues.",
                "In dense regular connective tissue, collagen fibers are packed in parallel rows between bundles of fibers, resisting unidirectional tensile strain.",
                "Dense irregular tissue is found in the skin dermis.", diff, q_type
            )
        elif "Muscular" in subtopic:
            return (
                "Intercalated discs with gap junctions (communicating junctions for synchronized contraction) are unique to which muscle tissue?",
                "Cardiac muscle tissue",
                ["Skeletal striated voluntary muscle", "Smooth involuntary non-striated muscle", "Visceral smooth muscle of stomach"],
                "Intercalated discs allow cardiac myocytes to act as an electrical functional syncytium.",
                "Histological and electrophysiological specialization of cardiac muscle.",
                "Intercalated discs are communication junctions where plasma membranes fuse via desmosomes and gap junctions, allowing rapid action potential propagation across the myocardium.",
                "Skeletal muscle fibers are multinucleated syncytia without intercalated discs.", diff, q_type
            )
        else: # Cockroach Anatomy & Morphology
            return (
                "In the cockroach (Periplaneta americana), what is the anatomical position and function of Malpighian tubules?",
                "100 to 150 thin yellow tubules at the junction of midgut and hindgut; excretion of uric acid",
                ["6 to 8 blind tubules at the junction of foregut and midgut; secretion of digestive enzymes", "Paired structures in the head; secretion of salivary amylase", "Located in the 6th abdominal segment; pheromone secretion"],
                "Midgut-hindgut junction: Malpighian tubules (excretory). Foregut-midgut junction: Hepatic caeca (digestive).",
                "Internal organ architecture and uricotelic excretion in insects.",
                "Malpighian tubules extract potassium urate and wastes from hemolymph, converting them to uric acid eliminated with feces through the rectum.",
                "Option A describes hepatic caeca, not Malpighian tubules.", diff, q_type
            )

    elif "Biomolecules" in chapter:
        if "Carbohydrates" in subtopic:
            return (
                "Which carbohydrate polymer produces an intense blue color with iodine solution due to helical secondary structure holding iodine molecules?",
                "Starch (specifically amylose unbranched helical component)",
                ["Cellulose (linear rigid unbranched polymer)", "Glycogen (branches produce red-brown color)", "Inulin (polymer of fructose)"],
                "Starch forms secondary helical coils capable of trapping $\\text{I}_2$; cellulose cannot form helices.",
                "Polysaccharide conformational biochemistry and diagnostic iodine reaction.",
                "Amylose chains form a secondary helical spiral where iodine atoms fit into the central cavity, generating a charge-transfer complex with deep blue absorption. Cellulose forms linear chains lacking helices.",
                "Cellulose forms straight parallel chains without helices, giving no color with iodine.", diff, q_type
            )
        elif "Proteins" in subtopic:
            return (
                "Which level of protein structural organization is stabilized by covalent disulfide bonds ($-S-S-$) formed between cysteine residues alongside non-covalent hydrophobic interactions?",
                "Tertiary structure (yielding a biologically active 3D conformation)",
                ["Primary structure (linear amino acid sequence linked by peptide bonds only)", "Secondary structure (alpha-helix and beta-pleated sheets held by hydrogen bonds)", "Quaternary structure without subunits"],
                "Tertiary folding gives the overall 3D globular shape with active catalytic sites.",
                "Hierarchical protein architecture and stabilizing chemical bonds.",
                "Tertiary structure is maintained by disulfide bonds, hydrogen bonds, ionic bonds, and hydrophobic interactions between $R$-groups of amino acid residues, folding the polypeptide into an active 3D shape.",
                "Primary structure consists solely of peptide bonds; secondary structure is stabilized by regular peptide backbone hydrogen bonds.", diff, q_type
            )
        elif "Enzyme" in subtopic:
            return (
                "When a competitive enzyme inhibitor (e.g. Malonate inhibiting Succinate Dehydrogenase) binds to the active site, what happens to $K_m$ and $V_{\\max}$?",
                "$K_m$ increases (apparent substrate affinity decreases); $V_{\\max}$ remains unchanged (overcome by high substrate)",
                ["$K_m$ decreases; $V_{\\max}$ decreases", "$K_m$ remains unchanged; $V_{\\max}$ decreases (non-competitive pattern)", "Both $K_m$ and $V_{\\max}$ increase simultaneously"],
                "Competitive inhibitor competes for same active site; substrate excess outcompetes inhibitor.",
                "Michaelis-Menten enzyme kinetics and competitive inhibition mechanisms.",
                "Because inhibitor and substrate compete for the same catalytic active site, adding higher concentrations of substrate displaces the inhibitor, reaching original $V_{\\max}$. Hence $K_m$ increases while $V_{\\max}$ is unchanged.",
                "Option C describes non-competitive inhibition, where $V_{\\max}$ decreases while $K_m$ is unchanged.", diff, q_type
            )
        else: # Nucleic Acids & Watson-Crick Double Helix
            return (
                "According to the Watson-Crick model of standard B-DNA, what are the exact helical pitch and the distance between two consecutive base pairs?",
                "Pitch $= 3.4\\text{ nm}$ ($34\\text{ \\AA}$) and distance between base pairs $= 0.34\\text{ nm}$ ($3.4\\text{ \\AA}$ with 10 bp/turn)",
                ["Pitch $= 2.0\\text{ nm}$ and distance between base pairs $= 0.20\\text{ nm}$", "Pitch $= 4.5\\text{ nm}$ and distance between base pairs $= 0.45\\text{ nm}$", "Pitch $= 2.8\\text{ nm}$ and distance between base pairs $= 0.28\\text{ nm}$"],
                "One full helical turn is $3.4\\text{ nm}$ containing 10 base pairs; distance $= 3.4 / 10 = 0.34\\text{ nm}$.",
                "Watson-Crick B-form double helix geometrical parameters.",
                "Standard B-DNA has a helical pitch of $3.4\\text{ nm}$ ($34\\text{ \\AA}$) with roughly $10\\text{ base pairs}$ per helical turn, meaning adjacent base pairs are separated by $0.34\\text{ nm}$ ($3.4\\text{ \\AA}$).",
                "Option A confuses helical diameter ($2.0\\text{ nm}$) with pitch.", diff, q_type
            )

    elif "Breathing and Exchange" in chapter:
        if "Pulmonary" in subtopic or "Mechanism" in subtopic:
            return (
                "During quiet normal inspiration in humans, what mechanical event increases the volume of the thoracic cavity in the antero-posterior axis?",
                "Contraction of the diaphragm, flattening it downwards",
                ["Contraction of external intercostal muscles lifting ribs upwards", "Relaxation of the abdominal wall muscles", "Contraction of internal intercostal muscles pulling ribs down"],
                "Diaphragm contraction increases thoracic volume antero-posteriorly; intercostal contraction increases it dorso-ventrally.",
                "Mechanics of human pulmonary ventilation.",
                "Contraction of the phrenic muscle fibers flattens the dome-shaped diaphragm downward, increasing thoracic volume along the antero-posterior axis and reducing intrapulmonary pressure.",
                "Option B increases volume in the dorso-ventral axis.", diff, q_type
            )
        elif "Dissociation" in subtopic or "Oxygen-Haemoglobin" in subtopic:
            return (
                "Which physiological conditions in active skeletal muscle tissues cause a rightward shift of the Oxygen-Haemoglobin Dissociation Curve (Bohr effect)?",
                "High $p\\text{CO}_2$, high $[\\text{H}^+]$ (acidic pH), high temperature, and elevated 2,3-BPG",
                ["Low $p\\text{CO}_2$, alkaline pH, and cold temperature", "High $p\\text{O}_2$ and low $[\\text{H}^+]$", "Complete inhibition of carbonic anhydrase"],
                "Right shift indicates reduced affinity of haemoglobin for $\\text{O}_2$, facilitating unloading.",
                "Bohr effect and physiological regulation of oxygen delivery.",
                "In metabolically active tissues, cellular respiration generates $\\text{CO}_2$, lactic acid (lowering pH), and heat. These factors destabilize oxyhaemoglobin, shifting the dissociation curve right.",
                "Option A shifts the curve to the LEFT (increasing affinity, as in lung alveoli).", diff, q_type
            )
        elif "Chloride" in subtopic or "CO2" in subtopic:
            return (
                "During carbon dioxide transport from metabolizing tissues to systemic capillaries, the Hamburger phenomenon (Chloride Shift) involves:",
                "Diffusion of bicarbonate ions ($\\text{HCO}_3^-$) out of erythrocytes into plasma, accompanied by inward migration of chloride ions ($\\text{Cl}^-$) into erythrocytes",
                ["Efflux of $\\text{Cl}^-$ out of erythrocytes to balance hydrogen ion accumulation", "Active pumping of sodium ions out of RBCs by $\\text{Na}^+/\\text{K}^+$ ATPase", "Direct binding of $\\text{Cl}^-$ to the heme iron atoms of deoxyhemoglobin"],
                "Carbonic anhydrase converts $\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{HCO}_3^- + \\text{H}^+$. Electrical neutrality is preserved by $\\text{Cl}^-$ influx.",
                "Physiological erythrocyte ion exchange and bicarbonate buffering dynamics.",
                "RBC carbonic anhydrase produces $\\text{HCO}_3^-$ which diffuses down its gradient into plasma. To preserve electrostatic balance without changing membrane voltage, plasma $\\text{Cl}^-$ enters RBCs via the AE1 band 3 anion exchanger.",
                "Option A reverses the direction of chloride ion flux.", diff, q_type
            )
        else: # Respiratory Volumes & Capacities (Tidal, Vital)
            return (
                "What is the Vital Capacity ($VC$) of human lungs expressed in standard spirometric volume subdivisions?",
                "$VC = ERV + TV + IRV$ (Expiratory Reserve Volume + Tidal Volume + Inspiratory Reserve Volume)",
                ["$VC = TV + IRV$", "$VC = ERV + RV$", "$VC = TV + RV$"],
                "Vital capacity is the maximum volume expired after maximal inspiration. Excludes Residual Volume ($RV$).",
                "Spirometry and physiological pulmonary lung capacities.",
                "$$VC = ERV (1100\\text{ mL}) + TV (500\\text{ mL}) + IRV (3000\\text{ mL}) \\approx 4600\\text{ mL}.$$ Residual volume ($RV \\approx 1200\\text{ mL}$) remains in lungs.",
                "Option A is Inspiratory Capacity ($IC$); Option B is Functional Residual Capacity ($FRC$).", diff, q_type
            )

    elif "Body Fluids and Circulation" in chapter:
        if "Blood Groups" in subtopic or "Incompatibility" in subtopic:
            return (
                "In Erythroblastosis Foetalis (hemolytic disease of newborn), maternal-fetal incompatibility arises when:",
                "An $\\text{Rh}^-$ mother carries an $\\text{Rh}^+$ fetus, producing anti-Rh antibodies that attack fetal RBCs during subsequent pregnancies",
                ["An $\\text{Rh}^+$ mother carries an $\\text{Rh}^-$ fetus in her first gestation", "Both father and mother are $\\text{Rh}^-$ with an $\\text{Rh}^-$ fetus", "An ABO group O mother carries an AB fetus with maternal IgA anti-A"],
                "Maternal $\\text{Rh}^-$ immune system sensitized during first delivery develops anti-Rh IgG crossing placenta in later $\\text{Rh}^+$ pregnancies.",
                "Immunohaematology of Rh antigen sensitization and alloimmune hemolysis.",
                "During birth of first $\\text{Rh}^+$ baby, fetal blood mixes with maternal circulation, sensitizing $\\text{Rh}^-$ mother to produce anti-Rh antibodies. In subsequent $\\text{Rh}^+$ gestations, maternal IgG anti-D crosses placenta and destroys fetal erythrocytes.",
                "Option A has an $\\text{Rh}^+$ mother who recognizes Rh antigen as self.", diff, q_type
            )
        elif "ECG" in subtopic or "Cardiac Cycle" in subtopic:
            return (
                "During a normal human cardiac cycle ($75\\text{ beats/min}$, duration $0.8\\text{ s}$), what is the duration of ventricular systole, atrial systole, and joint diastole?",
                "Ventricular systole $= 0.3\\text{ s}$, Atrial systole $= 0.1\\text{ s}$, Joint diastole $= 0.4\\text{ s}$",
                ["Ventricular systole $= 0.5\\text{ s}$, Atrial systole $= 0.2\\text{ s}$, Joint diastole $= 0.1\\text{ s}$", "Ventricular systole $= 0.4\\text{ s}$, Atrial systole $= 0.4\\text{ s}$, Joint diastole $= 0.0\\text{ s}$", "Ventricular systole $= 0.1\\text{ s}$, Atrial systole $= 0.3\\text{ s}$, Joint diastole $= 0.4\\text{ s}$"],
                "Total cycle duration $= 60 / 75 = 0.8\\text{ s}$. Atria contract $0.1\\text{ s}$, ventricles contract $0.3\\text{ s}$.",
                "Cardiac cycle timing and hemodynamic chamber phases.",
                "Atrial systole lasts $0.1\\text{ s}$. Ventricular systole lasts $0.3\\text{ s}$. When both atria and ventricles relax simultaneously (joint diastole), it lasts $0.4\\text{ s}$. Total: $0.8\\text{ s}$.",
                "Option C inverts ventricular and atrial systolic intervals.", diff, q_type
            )
        elif "Double Circulation" in subtopic or "Portal" in subtopic:
            return (
                "What is the unique anatomical pathway and functional significance of the Hepatic Portal System in humans?",
                "It transports deoxygenated blood rich in absorbed nutrients from digestive tract capillaries directly to liver sinusoids before systemic return",
                ["It carries oxygenated arterial blood directly from aorta to liver parenchyma", "It drains renal capillaries directly into hepatic vein bypassing inferior vena cava", "It conducts venous drainage of cerebral hemispheres directly to pulmonary trunk"],
                "A portal system begins and ends in capillary beds without passing directly to heart.",
                "Vascular architecture of human splanchnic and hepatic microcirculation.",
                "The hepatic portal vein collects venous effluent from stomach, intestines, and spleen, delivering absorbed glucose and amino acids to hepatic sinusoids for first-pass metabolism and glycogen storage before entering systemic circulation.",
                "Option A describes the hepatic artery, which supplies oxygenated arterial blood.", diff, q_type
            )
        else: # Regulation of Cardiac Output
            return (
                "Sympathetic neural stimulation increases cardiac output through which neurochemical mechanism and cardiac target?",
                "Norepinephrine release at Sinoatrial Node (SAN) and ventricular myocardium, increasing heart rate and ventricular contractile force",
                ["Acetylcholine release via vagus nerve, hyperpolarizing pacemaker cells", "Histamine secretion inducing systemic arteriolar dilation without chronotropic effect", "Dopamine depletion within medulla oblongata slowing AV node conduction"],
                "Sympathetic stimulation speeds up pacemaker firing and ventricular contractility; Parasympathetic (vagus) slows it.",
                "Autonomic neurocardiac regulation and chronotropic/inotropic control.",
                "Sympathetic postganglionic terminals release norepinephrine acting on beta-1 adrenergic receptors on SAN and myocardium, accelerating pacemaker prepotential slope and enhancing $\\text{Ca}^{2+}$ influx to boost stroke volume and heart rate.",
                "Option A describes parasympathetic vagal stimulation, which reduces heart rate and cardiac output.", diff, q_type
            )

    elif "Excretory Products" in chapter:
        if "Nephron" in subtopic or "Malpighian" in subtopic:
            return (
                "In the human Malpighian body (renal corpuscle), what are the three microscopic filtration barrier layers through which blood is filtered under glomerular hydrostatic pressure?",
                "Glomerular capillary endothelium (fenestrated), acellular basement membrane, and visceral podocyte epithelium with filtration slits",
                ["Glomerular endothelium and tubular brush border epithelium only", "Parietal layer of Bowman capsule, mesangium, and peritubular capillaries", "Tunica adventitia, internal elastic lamina, and macula densa cells"],
                "Podocytes have pedicels creating filtration slits; basement membrane prevents albumin passage.",
                "Glomerular ultrafiltration barrier architecture and biophysics.",
                "Ultrafiltration traverses fenestrations of glomerular capillaries, negative-charge-rich basement membrane, and filtration slits between podocyte foot processes, excluding cells and large plasma proteins while yielding protein-free ultrafiltrate.",
                "Option B includes parietal Bowman layer, which does not contact glomerular capillaries.", diff, q_type
            )
        elif "Urine Formation" in subtopic or "Counter-Current" in subtopic:
            return (
                "The medullary hyperosmotic gradient ($300\\text{ mOsmol/L}$ in renal cortex up to $1200\\text{ mOsmol/L}$ in deep medulla) is established and maintained primarily by:",
                "Counter-current multiplier in Loop of Henle and counter-current exchanger in Vasa Recta (circulating $\\text{NaCl}$ and Urea)",
                ["Active glucose pumping across Proximal Convoluted Tubule brush borders", "Unidirectional filtration flow through Glomerular basement membrane", "Aldosterone secretion directly into the collecting ducts without medullary gradient"],
                "Opposite flow directions in Henle limbs and vasa recta multiply and preserve osmotic concentration gradient.",
                "Counter-current multiplier mechanism and urine concentration in juxtamedullary nephrons.",
                "Ascending Henle limb actively pumps $\\text{NaCl}$ into interstitium impermeable to water; descending limb passively loses water. Vasa recta hairpin blood flow removes absorbed water without washing away medullary $\\text{NaCl}$ and urea.",
                "Option A occurs in cortex and does not establish medullary gradient.", diff, q_type
            )
        elif "RAAS" in subtopic or "ANF" in subtopic:
            return (
                "When blood pressure or Glomerular Filtration Rate (GFR) drops, the Juxtaglomerular Apparatus (JGA) initiates which hormonal regulatory cascade?",
                "Renin-Angiotensin-Aldosterone System (RAAS), where renin converts angiotensinogen to angiotensin I",
                ["Atrial Natriuretic Factor (ANF) secretion from heart atria", "Immediate suppression of ADH release from hypothalamus", "Aldosterone secretion directly into kidney tubules"],
                "Fall in GFR stimulates JGA granular cells to secrete renin into blood.",
                "RAAS neuroendocrine regulation of blood pressure and renal hemodynamics.",
                "Renin converts plasma angiotensinogen to angiotensin I. ACE converts it to angiotensin II (potent vasoconstrictor stimulating adrenal cortex to secrete aldosterone, increasing sodium/water reabsorption).",
                "ANF is secreted when blood pressure is HIGH, antagonizing RAAS.", diff, q_type
            )
        else: # Micturition & Dialysis
            return (
                "During hemodialysis for patients with uremia, which chemical agent is added to blood before it enters the dialyzer, and what is added before returning it to the patient?",
                "Heparin (anticoagulant) is added before dialyzer; Anti-heparin (protamine sulfate) is added before blood return",
                ["Insulin before dialyzer; Glucagon before blood return", "EDTA before dialyzer; Calcium gluconate before blood return", "Antibiotics before dialyzer; Hydrocortisone before blood return"],
                "Heparin prevents clotting within artificial cellophane tubing; anti-heparin restores normal clotting.",
                "Clinical artificial kidney hemodialysis principles and safety anticoagulation.",
                "Blood pumped from a convenient artery is treated with heparin to prevent thrombosis inside dialyzer cellophane coils. Nitrogenous wastes diffuse into dialyzing fluid. Before returning cleared blood via a vein, anti-heparin neutralizes systemic bleeding risk.",
                "Option C omits anticoagulation, which would cause catastrophic tubing occlusion.", diff, q_type
            )

    # =========================================================================
    # CLASS 12 ZOOLOGY
    # =========================================================================
    elif "Human Reproduction" in chapter:
        if "Spermatogenesis" in subtopic:
            return (
                "In human male testes, what are the distinct endocrine functions and trophic hormone controllers of Leydig cells and Sertoli cells?",
                "Leydig cells secrete testosterone under LH stimulation; Sertoli cells nourish spermatogenic cells under FSH stimulation",
                ["Leydig cells secrete FSH; Sertoli cells secrete LH", "Leydig cells secrete progesterone; Sertoli cells secrete testosterone", "Both Leydig and Sertoli cells secrete adrenaline"],
                "LH acts on Leydig cells (L-L rule); FSH acts on Sertoli cells (S-S rule).",
                "Endocrine regulation of male spermatogenesis and testicular histology.",
                "Leydig (interstitial) cells produce testosterone stimulated by LH. Sertoli (nurse) cells provide metabolic support to germ cells and secrete androgen-binding protein under FSH influence.",
                "Option A inverts the hormone controllers.", diff, q_type
            )
        elif "Oogenesis" in subtopic:
            return (
                "At which stage of meiosis are human primary oocytes arrested from fetal life until puberty?",
                "Diplotene stage of Prophase I of Meiosis I",
                ["Metaphase II of Meiosis II", "Anaphase I of Meiosis I", "Telophase II"],
                "Primary oocytes begin meiosis I before birth and arrest in diplotene of prophase I until ovulation.",
                "Folliculogenesis and meiotic arrest in human oogenesis.",
                "Oogenesis initiates during embryonic development. No new oogonia form after birth. Primary oocytes enter prophase I and arrest at diplotene stage within primary follicles until puberty.",
                "Metaphase II arrest occurs in the secondary oocyte, released at ovulation.", diff, q_type
            )
        elif "Menstrual" in subtopic:
            return (
                "The LH surge (rapid, peak secretion of Luteinizing Hormone) occurring on day 14 of the human menstrual cycle triggers:",
                "Rupture of the Graafian follicle and release of the secondary oocyte (Ovulation)",
                ["Degeneration of corpus luteum into corpus albicans", "Immediate sloughing and shedding of uterine endometrium", "Formation of primary follicles from oogonia"],
                "High estrogen from mature Graafian follicle triggers positive feedback on anterior pituitary, causing LH peak.",
                "Neuroendocrine regulation of ovarian cycle and ovulatory dynamics.",
                "The mid-cycle LH surge induces final maturation and rupture of the mature Graafian follicle, releasing the secondary oocyte into the fallopian tube (ovulation).",
                "Option A occurs at days 26-28 when fertilisation fails to occur.", diff, q_type
            )
        else: # Fertilization, Cleavage & Implantation
            return (
                "In human development, implantation of the blastocyst into the uterine endometrium typically occurs at which embryonic stage and day post-fertilization?",
                "Blastocyst stage (with trophoblast attaching to endometrium) around day 7 post-fertilization",
                ["Morula stage (8-cell) around day 2", "Zygote stage within 24 hours in ampulla", "Gastrula stage around day 21"],
                "Blastocyst possesses outer trophoblast (attaches to uterine wall) and inner cell mass.",
                "Early human embryogenesis, cleavage divisions, and implantation.",
                "Cleavage in fallopian tube yields solid morula ($8\\text{-}16$ cells) $\\rightarrow$ hollow blastocyst ($64\\text{ cells}$) around day 5-6. Trophoblast attaches to secretory endometrium around day 7.",
                "Option A is premature; morula travels through fallopian tube.", diff, q_type
            )

    elif "Reproductive Health" in chapter:
        if "Contraceptive" in subtopic:
            return (
                "What is the mechanism of action of Copper-releasing Intrauterine Devices (such as CuT, Cu7, Multiload 375)?",
                "Released $\\text{Cu}^{2+}$ ions suppress sperm motility and fertilizing capacity, while promoting leukocyte phagocytosis of sperm",
                ["They prevent ovulation by destroying ovarian follicles", "They permanently scar fallopian tubes", "They destroy maternal red blood cells to induce menstruation"],
                "Copper ions act locally in uterine cavity; non-hormonal, reversible contraception.",
                "Mechanisms of Intrauterine Contraceptive Devices (IUDs).",
                "Copper-releasing IUDs stimulate sterile uterine inflammatory response increasing leukocyte phagocytosis of sperm, while released copper ions reduce sperm motility and viability.",
                "Option A describes oral hormonal pills; Option B describes surgical tubectomy.", diff, q_type
            )
        elif "MTP" in subtopic:
            return (
                "Under the Medical Termination of Pregnancy (MTP) Amendment Act, up to which stage of pregnancy is induced abortion considered safest with lowest maternal risk?",
                "First trimester (up to 12 weeks of pregnancy)",
                ["Second trimester (13 to 24 weeks)", "Third trimester (25 to 36 weeks)", "Any time before active labor begins"],
                "MTP is safest during first trimester; second trimester carries significant maternal hemorrhage risk.",
                "Reproductive health legislation and maternal safety in MTP.",
                "MTP performed during first 12 weeks is medically safest. Termination during second trimester ($12\\text{-}24\\text{ weeks}$) requires opinion of two registered medical practitioners.",
                "Option B carries substantially higher surgical risk.", diff, q_type
            )
        elif "STIs" in subtopic:
            return (
                "Which of the following Sexually Transmitted Infections (STIs) is completely non-curable with existing antimicrobial therapies?",
                "Hepatitis B, Genital Herpes, and HIV/AIDS",
                ["Gonorrhea and Syphilis", "Chlamydiasis and Trichomoniasis", "Candidiasis and Syphilis"],
                "Except for hepatitis B, genital herpes, and HIV infection, other STIs are completely curable if detected early.",
                "Epidemiology and clinical prognosis of sexually transmitted infections.",
                "Viral STIs like HIV, Hepatitis B, and Genital Herpes cannot be eradicated from host cells by antibiotics, requiring lifelong management.",
                "Bacterial STIs (Gonorrhea, Syphilis, Chlamydia) are curable with antibiotics.", diff, q_type
            )
        else: # Assisted Reproductive Technologies
            return (
                "In Assisted Reproductive Technology (ART), ZIFT (Zygote Intra-Fallopian Transfer) involves transferring:",
                "A zygote or early embryo up to 8 blastomeres into the Fallopian tube",
                ["An embryo with more than 8 blastomeres directly into the Uterus (IUT)", "Unfertilized ovum collected from a donor into the fallopian tube (GIFT)", "A single sperm injected directly into the cytoplasm of an ovum (ICSI)"],
                "ZIFT: up to 8 blastomeres into fallopian tube. IUT: > 8 blastomeres into uterus.",
                "Clinical protocols in assisted reproductive technologies.",
                "In IVF-ET: If embryo has up to 8 blastomeres, it is transferred into fallopian tube (ZIFT). Embryos with $> 8$ blastomeres are transferred into uterus (IUT).",
                "Option B describes IUT (Intra-Uterine Transfer); Option C describes ICSI.", diff, q_type
            )

    elif "Evolution" in chapter:
        if "Origin" in subtopic:
            return (
                "In the Miller-Urey experiment (1953) simulating prebiotic primitive Earth conditions, what gas mixture and energy source were used?",
                "$\\text{CH}_4, \\text{NH}_3, \\text{H}_2,$ and water vapor at $800^\\circ\\text{C}$ with electric spark discharge",
                ["$\\text{CO}_2, \\text{O}_2, \\text{N}_2,$ and water vapor with UV radiation", "$\\text{CH}_4, \\text{O}_2,$ and $\\text{H}_2\\text{S}$ with radioactive isotopes", "$\\text{NH}_3$ and $\\text{CO}_2$ with high hydrostatic pressure"],
                "Reducing atmosphere lacked free oxygen. Electric discharge simulated lightning.",
                "Experimental verification of Oparin-Haldane chemical evolution hypothesis.",
                "Miller circulated $\\text{CH}_4, \\text{NH}_3, \\text{H}_2$ ($2:1:2$) and boiling water vapor through tungsten electrodes generating electric sparks, producing amino acids (glycine, alanine, aspartic acid).",
                "Option A includes molecular $\\text{O}_2$, which was absent in primitive atmosphere.", diff, q_type
            )
        elif "Homologous" in subtopic:
            return (
                "Thorns of Bougainvillea and tendrils of Cucurbita represent which evolutionary phenomenon?",
                "Homologous organs arising from divergent evolution (both are modified axillary buds)",
                ["Analogous organs arising from convergent evolution", "Vestigial organs with no functional significance", "Atavism occurring in desert xerophytes"],
                "Homology: same embryonic origin and basic anatomy, modified for different functions.",
                "Comparative morphology and divergent adaptive evolution.",
                "Both thorns in Bougainvillea (defense) and tendrils in Cucurbita (climbing) develop from axillary buds. Common origin with divergent adaptation defines homology.",
                "Option A confuses homology with analogy (e.g. wings of bird and insect).", diff, q_type
            )
        elif "Hardy-Weinberg" in subtopic:
            return (
                "In a population in Hardy-Weinberg equilibrium, the frequency of recessive allele $a$ is $q = 0.4$. What is the frequency of heterozygous individuals ($Aa$)?",
                "$2pq = 2(0.6)(0.4) = 0.48$ ($48\\%$)",
                ["$p^2 = (0.6)^2 = 0.36$ ($36\\%$)", "$q^2 = (0.4)^2 = 0.16$ ($16\\%$)", "$p+q = 1.0$ ($100\\%$)"],
                "Hardy-Weinberg Equation: $p + q = 1 \\implies p = 0.6$. Heterozygotes $= 2pq$.",
                "Population genetics and Hardy-Weinberg equilibrium frequencies.",
                "$$p = 1 - 0.4 = 0.6 \\implies 2pq = 2(0.6)(0.4) = 0.48\\text{ (or } 48\\%\\text{)}.$$",
                "Option A calculates homozygous dominant frequency ($p^2 = 0.36$).", diff, q_type
            )
        else: # Human Evolution Lineage
            return (
                "Which human ancestor had a cranial capacity of approximately $900\\text{ cc}$ and showed evidence of eating meat?",
                "Homo erectus (Java Man)",
                ["Homo habilis (cranial capacity $650\\text{-}800\\text{ cc}$, vegetarian)", "Australopithecus (cranial capacity $500\\text{ cc}$)", "Neanderthal man (cranial capacity $1400\\text{ cc}$)"],
                "Homo habilis: 650-800 cc (did not eat meat). Homo erectus: 900 cc (ate meat). Neanderthal: 1400 cc.",
                "Paleoanthropological lineage of hominid brain evolution.",
                "Homo erectus fossils discovered in Java in 1891 date to $1.5\\text{ million years ago}$. They had $900\\text{ cc}$ cranial capacity and ate meat.",
                "Option A describes Homo habilis, the first tool-making hominid.", diff, q_type
            )

    elif "Human Health and Disease" in chapter:
        if "Innate" in subtopic:
            return (
                "Which of the following is classified under the Physiological Barriers of Innate Immunity in humans?",
                "Acid in stomach, saliva in mouth, and tears from eyes (containing lysozyme)",
                ["Skin and mucous membranes of respiratory tract (Physical barriers)", "Polymorphonuclear neutrophils and macrophages (Cellular barriers)", "Interferons produced by virus-infected cells (Cytokine barriers)"],
                "Four innate barrier types: Physical, Physiological, Cellular, and Cytokine.",
                "Innate non-specific immunity and host barrier defenses.",
                "Gastric $\\text{HCl}$ destroys swallowed microbes; tears and saliva contain bactericidal lysozyme that breaks bacterial peptidoglycan walls.",
                "Option B represents Cellular barriers; Option C represents Cytokine barriers.", diff, q_type
            )
        elif "Antibody" in subtopic:
            return (
                "An antibody molecule consists of four polypeptide chains ($H_2L_2$). Which immunoglobulin is primarily present in maternal colostrum, protecting the newborn's gut?",
                "Secretory IgA (dimeric immunoglobulin)",
                ["IgG (crosses placenta)", "IgM (pentameric, first responder)", "IgE (mediator of allergic responses)"],
                "Colostrum is yellowish milk secreted in early days of lactation, rich in IgA.",
                "Immunoglobulin isotypes and natural passive immunity.",
                "Secretory IgA protects neonate mucosa against gastrointestinal pathogen adhesion and invasion.",
                "IgG is the only antibody capable of crossing placental barrier, not colostrum.", diff, q_type
            )
        elif "Plasmodium" in subtopic:
            return (
                "In the lifecycle of Plasmodium (malaria parasite), sexual reproduction (syngamy of gametocytes) and formation of sporozoites occur in:",
                "Gut of the female Anopheles mosquito (forming ookinete and oocyst)",
                ["Human liver parenchymal hepatocytes", "Human erythrocytes (red blood cells)", "Human spleen sinusoids"],
                "Asexual schizogony occurs in humans; sexual cycle occurs in mosquito gut.",
                "Life cycle and parasitology of Plasmodium in human and dipteran hosts.",
                "Gametocytes fertilize in mosquito gut to form a motile ookinete, developing into an oocyst that produces sporozoites migrating to salivary glands.",
                "Human liver and RBCs are sites of asexual reproduction.", diff, q_type
            )
        else: # AIDS & Cancer
            return (
                "In human immunodeficiency virus (HIV) pathogenesis, the viral RNA is transcribed into viral DNA inside host cells by which enzyme?",
                "Reverse Transcriptase (RNA-dependent DNA Polymerase)",
                ["DNA-dependent RNA Polymerase", "DNA Ligase", "Topoisomerase II"],
                "HIV is a retrovirus possessing single-stranded RNA and reverse transcriptase.",
                "Retroviral molecular replication and pathogenesis in CD4+ T-helper cells.",
                "Reverse transcriptase synthesizes double-stranded viral DNA from viral RNA template. Integrase then incorporates viral DNA into host chromosome, directing viral assembly.",
                "Option A is cellular RNA polymerase.", diff, q_type
            )

    elif "Locomotion and Movement" in chapter:
        if "Types of Movement" in subtopic:
            return (
                "Amoeboid movement in human body cells (e.g. macrophages and neutrophils) is executed by:",
                "Pseudopodia formed by streaming of protoplasm and microfilament cytoskeletal dynamics",
                ["Ciliary beating of respiratory lining", "Skeletal muscle contractions", "Flagellar undulations"],
                "Macrophages and leucocytes move through tissues via amoeboid pseudopodial streaming.",
                "Cellular motility and actin microfilament dynamics.",
                "Actin microfilament assembly and cytoplasmic streaming produce pseudopodia, allowing phagocytes to squeeze through capillary walls (diapedesis).",
                "Option A is ciliary movement in trachea/fallopian tubes.", diff, q_type
            )
        elif "Sliding" in subtopic:
            return (
                "According to the Sliding Filament Theory of muscle contraction, what happens to the lengths of A-band, I-band, and H-zone?",
                "A-band length remains constant; I-band shortens; H-zone narrows or completely disappears",
                ["A-band shortens; I-band remains constant; H-zone expands", "Both A-band and I-band lengthen simultaneously", "All bands remain unchanged in length"],
                "Thin actin filaments slide inward past thick myosin filaments toward M-line.",
                "Ultrastructural molecular dynamics of sarcomere contraction.",
                "A-band length corresponds to physical length of myosin thick filaments and remains constant. Thin filaments slide over thick filaments, shortening I-band and obliterating central H-zone.",
                "Option A incorrectly asserts that myosin thick filaments shorten.", diff, q_type
            )
        elif "Human Skeletal" in subtopic:
            return (
                "The human axial skeleton comprises 80 bones. How many pairs of ribs are classified as 'true ribs' (vertebrosternal ribs attached directly to sternum)?",
                "First 7 pairs (pairs 1 to 7)",
                ["First 8 pairs", "Pairs 8, 9, and 10 (false ribs)", "Pairs 11 and 12 (floating ribs)"],
                "Ribs 1-7: True ribs; Ribs 8-10: False/vertebrochondral; Ribs 11-12: Floating ribs.",
                "Human axial osteology and thoracic cage anatomy.",
                "Ribs 1 to 7 attach dorsally to thoracic vertebrae and ventrally to sternum via hyaline costal cartilages. Pairs 8-10 attach to costal cartilage of 7th rib. Pairs 11-12 are floating.",
                "Option C describes floating ribs, which lack anterior attachment.", diff, q_type
            )
        else: # Joints & Disorders
            return (
                "Myasthenia gravis, an autoimmune neuromuscular disorder affecting skeletal muscle contraction, is caused by antibodies targeting:",
                "Acetylcholine (ACh) receptors on the post-synaptic neuromuscular sarcolemma",
                ["Voltage-gated calcium channels in presynaptic axon terminals", "Tropomyosin proteins on actin thin filaments", "Sarcoplasmic reticulum calcium ATPase pumps"],
                "Autoantibodies block and destroy nicotinic ACh receptors at motor end-plate.",
                "Pathophysiology of autoimmune neuromuscular junction disorders.",
                "Autoantibodies bind ACh receptors on motor end plates, impairing acetylcholine transmission and causing progressive muscle weakness, fatigue, and paralysis.",
                "Tetany is caused by hypocalcemia, not autoantibodies.", diff, q_type
            )

    else: # Neural Control and Chemical Coordination
        if "Generation & Conduction" in subtopic:
            return (
                "During generation of an Action Potential along an unmyelinated neuronal axon, the rapid Depolarisation phase is caused by:",
                "Rapid influx of $\\text{Na}^+$ ions through opened voltage-gated sodium channels into axoplasm",
                ["Rapid efflux of $\\text{K}^+$ ions out of axoplasm", "Active pumping of $3\\text{ Na}^+$ out and $2\\text{ K}^+$ in by $\\text{Na}^+/\\text{K}^+$ ATPase pump", "Influx of $\\text{Cl}^-$ ions making interior more negative"],
                "Resting potential is $-70\\text{ mV}$. Threshold stimulus opens voltage-gated $\\text{Na}^+$ channels.",
                "Biophysics of axonal resting membrane potential and action potential generation.",
                "Stimulus at threshold voltage opens activation gates of voltage-gated $\\text{Na}^+$ channels. Driven by concentration and electrical gradients, $\\text{Na}^+$ rushes inward, reversing polarity to $+30\\text{ mV}$.",
                "Option A describes Repolarisation, driven by $\\text{K}^+$ efflux.", diff, q_type
            )
        elif "Synaptic" in subtopic:
            return (
                "At a chemical synapse, release of neurotransmitter vesicles into the synaptic cleft is triggered by the influx of which ion into the presynaptic terminal?",
                "Calcium ions ($\\text{Ca}^{2+}$ through voltage-gated calcium channels)",
                ["Sodium ions ($\\text{Na}^+$) exclusively", "Chloride ions ($\\text{Cl}^-$)", "Potassium ions ($\\text{K}^+$)"],
                "Action potential arrival opens voltage-gated $\\text{Ca}^{2+}$ channels in terminal bouton.",
                "Electrophysiology and vesicle exocytosis in chemical synaptic transmission.",
                "Depolarization of axon terminal opens voltage-gated $\\text{Ca}^{2+}$ channels. Influx of $\\text{Ca}^{2+}$ triggers synaptotagmin, inducing synaptic vesicle fusion with presynaptic membrane and acetylcholine exocytosis.",
                "Option A maintains action potential propagation along axon, but does not directly mediate vesicle fusion.", diff, q_type
            )
        elif "Endocrine Glands" in subtopic:
            return (
                "Which endocrine hormone acts antagonistically to Parathyroid Hormone (PTH) in regulating systemic blood calcium ($\\text{Ca}^{2+}$) homeostasis?",
                "Thyrocalcitonin (TCT, a hypocalcemic peptide hormone secreted by thyroid parafollicular C-cells)",
                ["Thyroxine ($T_4$)", "Aldosterone", "Glucagon"],
                "PTH is hypercalcemic (raises blood calcium); TCT is hypocalcemic (lowers blood calcium).",
                "Endocrine control of mineral metabolism and calcium homeostasis.",
                "PTH raises blood $\\text{Ca}^{2+}$ by stimulating osteoclastic bone resorption and renal reabsorption. Thyrocalcitonin (TCT) lowers blood $\\text{Ca}^{2+}$ by inhibiting bone resorption and promoting bone calcium deposition.",
                "Option A ($T_4$) regulates basal metabolic rate, not calcium.", diff, q_type
            )
        else: # Mechanism of Hormone Action
            return (
                "Steroid hormones (such as Estrogen, Progesterone, and Cortisol) regulate cellular metabolism primarily by:",
                "Diffusing across target cell plasma membrane and binding to intracellular/intranuclear receptors to regulate gene expression",
                ["Binding to surface membrane-bound receptors and generating cyclic AMP (cAMP) second messenger", "Directly hydrolyzing cellular ATP in cytoplasm", "Blocking ribosomal peptidyl transferase"],
                "Lipid-soluble steroid hormones pass through lipid bilayer; peptide hormones act via cell surface receptors.",
                "Molecular mechanisms of steroid vs peptide hormone signaling.",
                "Being lipophilic, steroids cross the lipid bilayer and bind intracellular receptors. The hormone-receptor complex interacts with genome DNA to modulate transcription.",
                "Option A describes water-soluble peptide hormones (e.g. epinephrine, insulin, glucagon).", diff, q_type
            )
