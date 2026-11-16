import math, random

def get_chemistry_question(cls_num, chapter, subtopic, q_idx):
    diff = "easy" if q_idx % 4 == 0 else ("hard" if q_idx % 4 == 3 else "medium")
    q_type = "assertion_reason" if q_idx % 7 == 0 else ("match_columns" if q_idx % 9 == 0 else "standard_mcq")

    # =========================================================================
    # CLASS 11 CHEMISTRY
    # =========================================================================
    if "Some Basic Concepts" in chapter:
        if "Mole Concept" in subtopic:
            solutes = [("NaOH", 40, 4, 250), ("NaOH", 40, 8, 500), ("H2SO4", 98, 9.8, 500), ("KOH", 56, 5.6, 250)]
            s_name, mw, g, vol = solutes[q_idx % len(solutes)]
            molarity = round((g * 1000) / (mw * vol), 2)
            return (
                f"What is the molarity of an aqueous solution prepared by dissolving ${g}\\text{{ g}}$ of $\\text{{{s_name}}}$ (Molar mass $= {mw}\\text{{ g/mol}}$) in water to make ${vol}\\text{{ mL}}$ of solution?",
                f"${molarity}\\text{{ M}}$",
                [f"${round(molarity * 2, 2)}\\text{{ M}}$", f"${round(molarity / 2, 2)}\\text{{ M}}$", f"${round(g / vol, 3)}\\text{{ M}}$"],
                f"Molarity $M = \\frac{{w \\times 1000}}{{M_w \\times V_{{\\text{{mL}}}}}}$.",
                "Molar concentration and volumetric stoichiometry.",
                f"$$\\text{{Moles}} = \\frac{{{g}\\text{{ g}}}}{{{mw}\\text{{ g/mol}}}} = {g/mw:.3f}\\text{{ mol}}.$$<br>$$M = \\frac{{{g/mw:.3f} \\times 1000}}{{{vol}}} = {molarity}\\text{{ M}}.$$",
                "Option D divides mass by volume, ignoring molecular weight.", diff, q_type
            )
        elif "Limiting" in subtopic:
            return (
                "In the reaction $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightarrow 2\\text{NH}_3(g)$, $28\\text{ g}$ of $\\text{N}_2$ ($1\\text{ mol}$) reacts with $6\\text{ g}$ of $\\text{H}_2$ ($3\\text{ mol}$). What is the limiting reagent and mass of $\\text{NH}_3$ produced?",
                "Neither reagent is limiting (stoichiometrically balanced); $34\\text{ g}$ of $\\text{NH}_3$ is produced",
                ["$\\text{N}_2$ is limiting; $17\\text{ g}$ of $\\text{NH}_3$ is produced", "$\\text{H}_2$ is limiting; $34\\text{ g}$ of $\\text{NH}_3$ is produced", "$\\text{N}_2$ is limiting; $34\\text{ g}$ of $\\text{NH}_3$ is produced"],
                "Compare molar ratio of reactants with stoichiometric coefficients.",
                "Limiting reagent and stoichiometric mass conservation.",
                "$$\\text{Moles of } \\text{N}_2 = 1\\text{ mol}, \\quad \\text{Moles of } \\text{H}_2 = 3\\text{ mol}.$$ Exactly matches $1 : 3$. Mass $= 2 \\times 17 = 34\\text{ g}$.",
                "Option A incorrectly assumes $\\text{N}_2$ is limiting.", diff, q_type
            )
        elif "Empirical" in subtopic:
            return (
                "An organic compound contains $40.0\\%$ Carbon, $6.67\\%$ Hydrogen, and $53.33\\%$ Oxygen. If molecular weight is $180\\text{ g/mol}$, empirical and molecular formulas are:",
                "Empirical: $\\text{CH}_2\\text{O}$; Molecular: $\\text{C}_6\\text{H}_{12}\\text{O}_6$",
                ["Empirical: $\\text{CHO}$; Molecular: $\\text{C}_6\\text{H}_6\\text{O}_6$", "Empirical: $\\text{CH}_2\\text{O}$; Molecular: $\\text{C}_3\\text{H}_6\\text{O}_3$", "Empirical: $\\text{C}_2\\text{H}_4\\text{O}_2$; Molecular: $\\text{C}_6\\text{H}_{12}\\text{O}_6$"],
                "Calculate atomic mole ratios: $C:H:O = 40/12 : 6.67/1 : 53.33/16 = 1 : 2 : 1$.",
                "Empirical vs molecular formula determination.",
                "Empirical formula $= \\text{CH}_2\\text{O}$ (Mass $= 30$). Ratio $n = 180 / 30 = 6 \\implies \\text{C}_6\\text{H}_{12}\\text{O}_6$.",
                "Option B computes $n = 3$, giving triose sugar.", diff, q_type
            )
        else: # Equivalent Weight & Normality
            return (
                "What is the normality ($N$) of a $0.5\\text{ M}$ aqueous solution of sulfuric acid ($\\text{H}_2\\text{SO}_4$, a dibasic acid)?",
                "$1.0\\text{ N}$ (Normality $= \\text{Molarity} \\times \\text{Basicity} = 0.5 \\times 2$)",
                ["$0.5\\text{ N}$", "$0.25\\text{ N}$", "$2.0\\text{ N}$"],
                "Normality $N = M \\times n$-factor (for $\\text{H}_2\\text{SO}_4$, $n = 2$).",
                "Equivalent weight and normality of polyprotic acids.",
                "$$\\text{Normality} = 0.5\\text{ M} \\times 2\\text{ eq/mol} = 1.0\\text{ N}.$$",
                "Option A equates normality with molarity, forgetting dibasic nature.", diff, q_type
            )

    elif "Structure of Atom" in chapter:
        if "Bohr" in subtopic:
            return (
                "In Bohr's model of the hydrogen atom, radius of $n^{\\text{th}}$ orbit $r_n$ and total electron energy $E_n$ scale with principal quantum number $n$ as:",
                "$r_n \\propto n^2, \\quad E_n \\propto -\\frac{1}{n^2}$",
                ["$r_n \\propto n, \\quad E_n \\propto -\\frac{1}{n}$", "$r_n \\propto n^2, \\quad E_n \\propto -n^2$", "$r_n \\propto \\frac{1}{n^2}, \\quad E_n \\propto -\\frac{1}{n^2}$"],
                "$r_n = 0.529 n^2/Z\\text{ \\AA}$ and $E_n = -13.6 Z^2/n^2\\text{ eV}$.",
                "Bohr's quantization postulates and atomic orbits.",
                "Quantization $mvr = nh/(2\\pi)$ yields $r_n \\propto n^2$ and $E_n \\propto -1/n^2$.",
                "Option A assumes linear radius scaling.", diff, q_type
            )
        elif "De Broglie" in subtopic:
            return (
                "According to Heisenberg's Uncertainty Principle, if uncertainty in the position of an electron is $\\Delta x = 0$, what is the uncertainty in its momentum $\\Delta p$?",
                "$\\Delta p = \\infty$ (Infinite uncertainty, physically impossible to determine simultaneously)",
                ["$\\Delta p = 0$", "$\\Delta p = h / (4\\pi)$", "$\\Delta p = h$"],
                "Heisenberg Principle: $\\Delta x \\cdot \\Delta p \\ge \\frac{h}{4\\pi}$.",
                "Fundamental limits of simultaneous quantum measurements.",
                "$$\\Delta p \\ge \\frac{h}{4\\pi \\Delta x}.$$ If $\\Delta x \\rightarrow 0$, $\\Delta p \\rightarrow \\infty$.",
                "Option A assumes both can be determined simultaneously with zero error.", diff, q_type
            )
        elif "Quantum Numbers" in subtopic:
            return (
                "Which set of quantum numbers ($n, l, m_l, m_s$) is NOT permissible for an electron in an isolated ground-state atom?",
                "$n = 3, l = 3, m_l = 0, m_s = +1/2$",
                ["$n = 4, l = 2, m_l = -1, m_s = -1/2$", "$n = 2, l = 1, m_l = 0, m_s = +1/2$", "$n = 3, l = 0, m_l = 0, m_s = -1/2$"],
                "Rules: Azimuthal quantum number $l$ can take values from $0$ to $n-1$.",
                "Quantum numbers and orbital boundary conditions.",
                "For $n = 3$, $l$ can only be $0, 1,$ or $2$ ($s, p, d$). A value of $l = 3$ is forbidden.",
                "Other options adhere to all quantum rules.", diff, q_type
            )
        else: # Photoelectric Effect in Atoms
            return (
                "When ultraviolet light of frequency $\\nu$ strikes a metal surface with work function $\\phi_0$, the stopping potential $V_0$ is given by:",
                "$e V_0 = h\\nu - \\phi_0$",
                ["$e V_0 = h\\nu + \\phi_0$", "$V_0 = h\\nu - \\phi_0$", "$e V_0 = \\phi_0 - h\\nu$"],
                "Einstein's photoelectric equation: $K_{\\max} = e V_0 = h\\nu - \\phi_0$.",
                "Photoelectric emission and energy conservation.",
                "Incident photon energy $h\\nu$ supplies work function $\\phi_0$ and kinetic energy $eV_0$.",
                "Option B forgets the electronic charge $e$ on stopping potential.", diff, q_type
            )

    elif "Classification of Elements" in chapter:
        if "Radii" in subtopic:
            return (
                "Among the isoelectronic ions $\\text{N}^{3-}, \\text{O}^{2-}, \\text{F}^-, \\text{Na}^+, \\text{Mg}^{2+}$, what is the correct decreasing order of ionic radii?",
                "$\\text{N}^{3-} > \\text{O}^{2-} > \\text{F}^- > \\text{Na}^+ > \\text{Mg}^{2+}$",
                ["$\\text{Mg}^{2+} > \\text{Na}^+ > \\text{F}^- > \\text{O}^{2-} > \\text{N}^{3-}$", "$\\text{F}^- > \\text{O}^{2-} > \\text{N}^{3-} > \\text{Na}^+ > \\text{Mg}^{2+}$", "All have identical radii because they possess 10 electrons"],
                "In isoelectronic species, radius decreases with increasing nuclear charge ($Z$).",
                "Effective nuclear charge and ionic radii of isoelectronic species.",
                "All have 10 electrons. Nuclear charge increases from $\\text{N}$ ($Z=7$) to $\\text{Mg}$ ($Z=12$). Higher $Z_{\\text{eff}}$ contracts electron cloud.",
                "Option A inverts the order.", diff, q_type
            )
        elif "Ionization" in subtopic:
            return (
                "Which Period 2 element possesses higher first ionization enthalpy than Nitrogen?",
                "Neon and Fluorine (Nitrogen exceeds Oxygen due to stable half-filled $2p^3$ subshell)",
                ["Oxygen", "Carbon", "Boron"],
                "First ionization enthalpy: $\\text{Li} < \\text{B} < \\text{Be} < \\text{C} < \\text{O} < \\text{N} < \\text{F} < \\text{Ne}$.",
                "Periodic anomalies in ionization enthalpy across Period 2.",
                "Nitrogen ($1s^2 2s^2 2p^3$) has extra exchange stability from half-filled $2p$ subshell, higher than Oxygen ($1402$ vs $1314\\text{ kJ/mol}$). Only $\\text{F}$ and $\\text{Ne}$ exceed it.",
                "Option A is the classic trap: Oxygen is lower than Nitrogen.", diff, q_type
            )
        elif "Electronegativity" in subtopic:
            return (
                "On the Pauling electronegativity scale, which element is the most electronegative in the periodic table?",
                "Fluorine (value $4.0$)",
                ["Chlorine", "Oxygen", "Nitrogen"],
                "Pauling scale: $\\text{F} (4.0) > \\text{O} (3.5) > \\text{N} \\approx \\text{Cl} (3.0)$.",
                "Periodic trends in Pauling electronegativity.",
                "Fluorine has the smallest atomic radius and highest effective nuclear attraction for bonded electrons in Period 2.",
                "Option A confuses electron affinity (where $\\text{Cl} > \\text{F}$) with electronegativity.", diff, q_type
            )
        else: # Valency & Anomalous Properties
            return (
                "Why does Lithium exhibit anomalous behavior compared to other alkali metals (forming oxide $\\text{Li}_2\\text{O}$ rather than superoxide)?",
                "Exceptionally small atomic and ionic size and high polarizing power ($e/r$ ratio)",
                ["Presence of vacant d-orbitals in its valence shell", "Low ionization enthalpy compared to Cesium", "Complete inability to form covalent bonds"],
                "Anomalous properties of Period 2 elements arise from small size, high charge density, and absence of d-orbitals.",
                "Diagonal relationships and anomalous second-period chemistry.",
                "Lithium's small cation $\\text{Li}^+$ polarizes small oxide ion $\\text{O}^{2-}$ stably, preventing formation of larger superoxides.",
                "Option A is false because Period 2 elements lack d-orbitals.", diff, q_type
            )

    elif "Chemical Bonding" in chapter:
        if "VSEPR" in subtopic:
            cases = [
                ("XeF4", "sp^3d^2", "Square planar", "4 bond pairs + 2 lone pairs"),
                ("SF4", "sp^3d", "See-saw", "4 bond pairs + 1 lone pair"),
                ("ClF3", "sp^3d", "T-shaped", "3 bond pairs + 2 lone pairs"),
                ("PCl5", "sp^3d", "Trigonal bipyramidal", "5 bond pairs + 0 lone pairs")
            ]
            c_name, hyb, geom, desc = cases[q_idx % len(cases)]
            return (
                f"According to VSEPR theory, hybridization of central atom and molecular geometry of $\\text{{{c_name}}}$ are:",
                f"${hyb}$, {geom}",
                [f"${hyb}$, Tetrahedral", f"sp^3, Octahedral", f"sp^3d, Planar"],
                f"Count steric number: {desc}.",
                "VSEPR electron pair repulsion geometry.",
                f"In $\\text{{{c_name}}}$, central atom has {desc}. Hybridization is ${hyb}$ and lone pair repulsions minimize potential energy into {geom} geometry.",
                "Option A confuses electron pair arrangement with molecular shape.", diff, q_type
            )
        elif "Hybridization" in subtopic:
            return (
                "In ethyne (acetylene, $\\text{H-C}\\equiv\\text{C-H}$), the hybridization of carbon atoms and the number of $\\sigma$ and $\\pi$ bonds are:",
                "sp hybridized; $3\\sigma$ bonds and $2\\pi$ bonds",
                ["sp^2 hybridized; $4\\sigma$ bonds and $1\\pi$ bond", "sp^3 hybridized; $5\\sigma$ bonds and $0\\pi$ bonds", "sp hybridized; $2\\sigma$ bonds and $3\\pi$ bonds"],
                "Triple bond consists of $1\\sigma + 2\\pi$. Linear geometry corresponds to sp hybridization.",
                "Orbital hybridization and covalent bond counting.",
                "Each Carbon forms $2\\sigma$ bonds (one $\\text{C-H}$ and one $\\text{C-C}$) $\\implies$ sp hybridization. Total: $2\\text{ C-H }\\sigma + 1\\text{ C-C }\\sigma = 3\\sigma$, plus $2\\pi$ bonds.",
                "Option A describes ethene ($\text{H}_2\text{C}=\text{CH}_2$).", diff, q_type
            )
        elif "MOT" in subtopic:
            return (
                "According to Molecular Orbital Theory (MOT), what is the bond order and magnetic nature of $\\text{O}_2$?",
                "Bond order $= 2$, Paramagnetic (2 unpaired electrons in $\\pi^* 2p_x$ and $\\pi^* 2p_y$ orbitals)",
                ["Bond order $= 2$, Diamagnetic (all electrons paired)", "Bond order $= 1.5$, Paramagnetic", "Bond order $= 2.5$, Diamagnetic"],
                "Configuration: $\\dots \\pi^* 2p_x^1 \\pi^* 2p_y^1$. Bond order $= (N_b - N_a)/2$.",
                "Molecular orbital theory and paramagnetism of $\\text{O}_2$.",
                "$$\\text{Bond Order} = \\frac{10 - 6}{2} = 2.$$ Two antibonding $\\pi^*$ degenerate orbitals each hold one unpaired electron.",
                "Option A is the valence bond theory failure that motivated MOT.", diff, q_type
            )
        else: # Dipole Moment & Hydrogen Bonding
            return (
                "Why does $\\text{NH}_3$ possess a higher net dipole moment ($1.47\\text{ D}$) than $\\text{NF}_3$ ($0.24\\text{ D}$)?",
                "In $\\text{NH}_3$, orbital dipole of lone pair points in same direction as resultant $\\text{N-H}$ bond dipoles; in $\\text{NF}_3$, highly electronegative Fluorine opposes lone pair dipole",
                ["Nitrogen is more electronegative than Fluorine in $\\text{NF}_3$", "$\\text{NH}_3$ is planar while $\\text{NF}_3$ is pyramidal", "$\\text{NF}_3$ contains no lone pairs on Nitrogen"],
                "Vector addition of lone pair dipole and individual polar bond dipoles.",
                "Molecular polarity and vector dipole summation.",
                "In $\\text{NH}_3$, $\\text{N-H}$ bond dipoles point toward $\\text{N}$, reinforcing lone pair dipole. In $\\text{NF}_3$, $\\text{N-F}$ bond dipoles point away toward $\\text{F}$, partially canceling lone pair dipole.",
                "Option A is false; Fluorine is the most electronegative element.", diff, q_type
            )

    elif "Chemical Thermodynamics" in chapter:
        if "First Law" in subtopic:
            return (
                "In an isothermal reversible expansion of an ideal gas, what are the values of $\\Delta U, \\Delta H,$ and $q$?",
                "$\\Delta U = 0, \\Delta H = 0, q = -w = nRT\\ln(V_2/V_1)$",
                ["$\\Delta U > 0, \\Delta H > 0, q = 0$", "$\\Delta U = q, \\Delta H = w, q = 0$", "$\\Delta U = -w, \\Delta H = q, q = 0$"],
                "Internal energy and enthalpy of an ideal gas depend only on temperature ($T = \\text{const}$).",
                "First law of thermodynamics applied to isothermal processes.",
                "Since $\\Delta T = 0$, $\\Delta U = n C_v \\Delta T = 0$ and $\\Delta H = n C_p \\Delta T = 0$. By First Law, $q = -w$.",
                "Option A is true for adiabatic compression.", diff, q_type
            )
        elif "Hess" in subtopic:
            return (
                "According to Hess's Law of Constant Heat Summation, the total enthalpy change of a chemical reaction depends on:",
                "Initial reactants and final products only, independent of intermediate pathway steps",
                ["Number of steps in the pathway", "Rate at which reaction is conducted", "Presence of homogeneous catalysts"],
                "Enthalpy $H$ is a state function; $\\Delta H = H_{\\text{products}} - H_{\\text{reactants}}$.",
                "Hess's law and thermodynamic state functions.",
                "Since enthalpy is a state function, overall $\\Delta H$ is identical whether reaction occurs in one step or a series of steps.",
                "Option B confuses thermodynamic enthalpy with kinetic rates.", diff, q_type
            )
        elif "Entropy" in subtopic:
            return (
                r"In which of the following physical or chemical processes does entropy ($\Delta S$) DECREASE?",
                "Crystallization of liquid water into solid ice ($H_2O(l) \\rightarrow H_2O(s)$)",
                ["Sublimation of solid dry ice ($CO_2(s) \\rightarrow CO_2(g)$)", "Dissolution of table salt in water", "Thermal dissociation of $PCl_5(g) \\rightarrow PCl_3(g) + Cl_2(g)$"],
                "Entropy measures molecular disorder: $\\text{gas} > \\text{liquid} > \\text{solid}$.",
                "Second law of thermodynamics and entropy variations.",
                "Freezing liquid water into crystalline ice locks molecules into an ordered lattice, decreasing entropy ($\\Delta S < 0$).",
                "Options B, C, and D increase molecular randomness ($\\Delta S > 0$).", diff, q_type
            )
        else: # Gibbs Free Energy & Equilibrium
            return (
                "The criterion for spontaneous feasibility of a process at constant $T$ and $P$ is:",
                "$\\Delta G = \\Delta H - T\\Delta S < 0$",
                ["$\\Delta H < 0$ strictly", "$\\Delta S_{\\text{system}} > 0$ strictly", "$\\Delta G > 0$"],
                "Gibbs-Helmholtz: $\\Delta G_{\\text{sys}} = -T\\Delta S_{\\text{total}} < 0$.",
                "Thermodynamic spontaneity and Gibbs free energy.",
                "Spontaneity requires $\\Delta S_{\\text{total}} > 0$, equivalent to $\\Delta G < 0$ at constant $T, P$. Endothermic reactions can be spontaneous if $T\\Delta S > \\Delta H$.",
                "Option A is false because endothermic reactions with positive entropy can be spontaneous.", diff, q_type
            )

    elif "Equilibrium" in chapter:
        if "Law of Chemical" in subtopic:
            return (
                "For the gaseous reaction $2\\text{SO}_2(g) + \\text{O}_2(g) \\rightleftharpoons 2\\text{SO}_3(g)$, what is the relationship between $K_p$ and $K_c$?",
                "$K_p = K_c (RT)^{-1}$ (since $\\Delta n_g = 2 - 3 = -1$)",
                ["$K_p = K_c (RT)^{+1}$", "$K_p = K_c$", "$K_p = K_c (RT)^{-2}$"],
                "$K_p = K_c (RT)^{\\Delta n_g}$ where $\\Delta n_g = \\sum n_{g,\\text{products}} - \\sum n_{g,\\text{reactants}}$.",
                "Relationship between gaseous equilibrium constants $K_p$ and $K_c$.",
                "$$\\Delta n_g = 2 - (2 + 1) = -1 \\implies K_p = K_c (RT)^{-1} = \\frac{K_c}{RT}.$$",
                "Option A calculates $\\Delta n_g = +1$ by inverting reactants and products.", diff, q_type
            )
        elif "Le Chatelier" in subtopic:
            return (
                "For the exothermic reaction $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g) \\quad (\\Delta H = -92.4\\text{ kJ/mol})$, equilibrium yield of $\\text{NH}_3$ is maximized by:",
                "Low temperature and High pressure",
                ["High temperature and Low pressure", "High temperature and High pressure", "Low temperature and Low pressure"],
                "Le Chatelier: Lower temperature favors exothermic direction; Higher pressure favors fewer gas moles ($4 \\rightarrow 2$).",
                "Dynamic chemical equilibrium response to physical stress.",
                "Lowering $T$ shifts equilibrium forward (exothermic). Increasing $P$ shifts equilibrium forward ($4 \\rightarrow 2$ moles).",
                "Option B shifts equilibrium backward.", diff, q_type
            )
        elif "pH" in subtopic:
            return (
                "What is the pH of a $10^{-8}\\text{ M}$ aqueous hydrochloric acid ($\\text{HCl}$) solution at $25^\\circ\\text{C}$?",
                "$\\text{pH} \\approx 6.96$ (considering $[\\text{H}^+]$ from autoionization of water $10^{-7}\\text{ M}$)",
                ["$\\text{pH} = 8.0$", "$\\text{pH} = 7.0$", "$\\text{pH} = 6.0$"],
                "Total $[\\text{H}^+] = [\\text{H}^+]_{\\text{acid}} + [\\text{H}^+]_{\\text{water}} = 10^{-8} + 10^{-7} = 1.1 \\times 10^{-7}\\text{ M}$.",
                "Acid-base equilibria in ultra-dilute strong acid solutions.",
                "An acidic solution cannot have $\\text{pH} \\ge 7$. Autoionization of water supplies $[\\text{H}^+] \\approx 10^{-7}$. $\\text{pH} = -\\log(1.05 \\times 10^{-7}) \\approx 6.96$.",
                "Option A is the classic student trap ($-\\log 10^{-8} = 8$), which is alkaline.", diff, q_type
            )
        else: # Buffer Solutions & Solubility Product (Ksp)
            return (
                "If the solubility product of a sparingly soluble salt $\\text{Ag}_2\\text{CrO}_4$ ($A_2B$ type) is $K_{\\text{sp}}$, its molar solubility $s$ in pure water is:",
                "$s = \\left(\\frac{K_{\\text{sp}}}{4}\\right)^{1/3}$",
                ["$s = \\sqrt{K_{\\text{sp}}}$", "$s = \\left(\\frac{K_{\\text{sp}}}{27}\\right)^{1/4}$", "$s = \\frac{K_{\\text{sp}}}{2}$"],
                "$\\text{Ag}_2\\text{CrO}_4 \\rightleftharpoons 2\\text{Ag}^+ + \\text{CrO}_4^{2-} \\implies K_{\\text{sp}} = (2s)^2(s) = 4s^3$.",
                "Solubility equilibria and $K_{\\text{sp}}$ stoichiometric relations.",
                "$$K_{\\text{sp}} = [\\text{Ag}^+]^2 [\\text{CrO}_4^{2-}] = (2s)^2(s) = 4s^3 \\implies s = \\left(\\frac{K_{\\text{sp}}}{4}\\right)^{1/3}.$$",
                "Option A is for $AB$ type salts like $\\text{AgCl}$ ($K_{\\text{sp}} = s^2$).", diff, q_type
            )

    elif "Redox Reactions" in chapter:
        if "Oxidation Number" in subtopic:
            return (
                "What is the oxidation state of Chromium in Potassium Dichromate ($\\text{K}_2\\text{Cr}_2\\text{O}_7$)?",
                "$+6$",
                ["$+7$", "$+3$", "$+12$"],
                "Sum of oxidation numbers $= 0$. Potassium is $+1$, Oxygen is $-2$.",
                "Oxidation number assignment in polyatomic anions.",
                "$$2(+1) + 2x + 7(-2) = 0 \\implies 2x = 12 \\implies x = +6.$$",
                "Option C computes $2x = +12$ without dividing by $2$.", diff, q_type
            )
        elif "Balancing" in subtopic:
            return (
                "In the balanced redox reaction in acidic medium: $\\text{MnO}_4^- + 8\\text{H}^+ + n e^- \\rightarrow \\text{Mn}^{2+} + 4\\text{H}_2\\text{O}$, how many electrons $n$ are transferred?",
                "$n = 5\\text{ electrons}$ (Manganese is reduced from $+7$ to $+2$)",
                ["$n = 3$", "$n = 6$", "$n = 1$"],
                "Change in oxidation state: $\\text{Mn}(+7) \\rightarrow \\text{Mn}(+2) \\implies \\Delta = 5$.",
                "Ion-electron half-reaction balancing in acidic media.",
                "$$+7 + n(-1) = +2 \\implies n = 5\\text{ electrons}.$$",
                "Option A ($n=3$) occurs in neutral or weakly alkaline medium ($+7 \\rightarrow +4$ in $\\text{MnO}_2$).", diff, q_type
            )
        elif "Electrochemical Series" in subtopic:
            return (
                "Given standard reduction potentials: $E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = -0.76\\text{ V}$ and $E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$. Which statement is correct?",
                "Zinc is a stronger reducing agent than Copper and can displace $\\text{Cu}^{2+}$ from solution",
                ["Copper is a stronger reducing agent than Zinc", "Copper can displace Zinc from $\\text{ZnSO}_4$ solution", "Zinc ion $\\text{Zn}^{2+}$ is a stronger oxidizing agent than $\\text{Cu}^{2+}$"],
                "More negative $E^\\circ$ indicates greater tendency to lose electrons (stronger reducing agent).",
                "Electrochemical series and spontaneous single displacement reactions.",
                "Zinc has lower reduction potential ($-0.76\\text{ V}$), oxidizing spontaneously: $\\text{Zn} + \\text{Cu}^{2+} \\rightarrow \\text{Zn}^{2+} + \\text{Cu}$.",
                "Option B is false; Copper has higher reduction potential.", diff, q_type
            )
        else: # Redox Titrations
            return (
                "In redox titrations using standard Potassium Permanganate ($\\text{KMnO}_4$), why is no external indicator required?",
                "$\\text{KMnO}_4$ acts as a self-indicator; deep purple color discharges to colorless, with first excess drop imparting permanent faint pink color",
                ["It produces starch which changes color", "Reaction produces bubbles that signal equivalence", "Methyl orange is permanently incorporated in $\\text{KMnO}_4$ crystals"],
                "$\\text{KMnO}_4$ self-indicator mechanism in acidic redox titrations.",
                "Volumetric redox titration endpoints and self-indicating reagents.",
                "$\\text{MnO}_4^-$ (deep purple) is reduced to $\\text{Mn}^{2+}$ (nearly colorless). At equivalence point, single excess drop of $\\text{MnO}_4^-$ colors solution pink.",
                "Option A confuses permanganometry with iodometry.", diff, q_type
            )

    elif "Organic Chemistry Basics" in chapter:
        if "IUPAC" in subtopic:
            return (
                "What is the correct IUPAC name of $\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}_2-\\text{CO}-\\text{CH}_3$?",
                "4-Methylpentan-2-one",
                ["2-Methylpentan-4-one", "4,4-Dimethylbutan-2-one", "Isopropylacetone"],
                "Ketone functional group receives lowest locant (number from right).",
                "IUPAC nomenclature rules for branched aliphatic ketones.",
                "Principal functional group is ketone at C-2; methyl substituent is at C-4. Name is 4-methylpentan-2-one.",
                "Option A numbers from the wrong end, assigning higher locant to the carbonyl.", diff, q_type
            )
        elif "Inductive" in subtopic:
            return (
                "Which substituent exerts the strongest $-I$ (electron-withdrawing inductive) effect?",
                "$-\\text{NO}_2$",
                ["$-\\text{COOH}$", "$-\\text{OCH}_3$", "$-\\text{CH}_3$"],
                "$-I$ strength order: $-\\text{NO}_2 > -\\text{CN} > -\\text{COOH} > -\\text{F} > -\\text{Cl} > -\\text{Br} > -\\text{I} > -\\text{OH} > -\\text{OCH}_3$.",
                "Electronic inductive displacements and electronegative groups.",
                "The nitro group possesses formal positive charge on Nitrogen, exerting the strongest $-I$ effect.",
                "Option D exerts a $+I$ (electron-donating) inductive effect.", diff, q_type
            )
        elif "Carbocations" in subtopic:
            return (
                "Which carbocation exhibits the highest thermodynamic stability?",
                "Tertiary butyl carbocation ($(\\text{CH}_3)_3\\text{C}^+$, stabilized by 9 hyperconjugative $\\alpha$-hydrogens)",
                ["Isopropyl carbocation ($(\\text{CH}_3)_2\\text{CH}^+$)", "Ethyl carbocation ($\\text{CH}_3\\text{CH}_2^+$)", "Methyl carbocation ($\\text{CH}_3^+$)"],
                "Stability: $3^\\circ > 2^\\circ > 1^\\circ > \\text{methyl}$ governed by hyperconjugation and $+I$ effects.",
                "Hyperconjugation and carbocation intermediate stabilization.",
                "Tertiary butyl carbocation has 9 $\\alpha$-hydrogens providing 9 hyperconjugative canonical forms delocalizing positive charge.",
                "Option B has only 6 $\\alpha$-hydrogens.", diff, q_type
            )
        else: # Isomerism
            return (
                "How many structural isomers (chain and positional) are possible for the molecular formula $\\text{C}_5\\text{H}_{12}$ (pentane)?",
                "3 structural isomers (n-pentane, isopentane, and neopentane)",
                ["4 structural isomers", "5 structural isomers", "2 structural isomers"],
                "Isomers of $\\text{C}_5\\text{H}_{12}$: Pentane, 2-Methylbutane, 2,2-Dimethylpropane.",
                "Structural chain isomerism in saturated acyclic alkanes.",
                "1. n-Pentane: $\\text{CH}_3(\\text{CH}_2)_3\\text{CH}_3$.<br>2. Isopentane: $(\\text{CH}_3)_2\\text{CHCH}_2\\text{CH}_3$.<br>3. Neopentane: $(\\text{CH}_3)_4\\text{C}$. Exactly 3 isomers.",
                "Option B confuses carbon atom count with isomer count.", diff, q_type
            )

    elif "Hydrocarbons" in chapter:
        if "Alkanes" in subtopic:
            return (
                "In the free-radical chlorination of alkanes, what is the reactivity order of hydrogen atoms?",
                "Tertiary ($3^\\circ$) > Secondary ($2^\\circ$) > Primary ($1^\\circ$)",
                ["Primary ($1^\\circ$) > Secondary ($2^\\circ$) > Tertiary ($3^\\circ$)", "Secondary ($2^\\circ$) > Tertiary ($3^\\circ$) > Primary ($1^\\circ$)", "All hydrogens react at identical rates"],
                "Rate-determining hydrogen abstraction forms alkyl radical; stability is $3^\\circ > 2^\\circ > 1^\\circ$.",
                "Free radical halogenation mechanism and C-H bond dissociation energies.",
                "Tertiary C-H bond has the lowest bond dissociation energy, forming the most stable tertiary free radical ($3^\\circ > 2^\\circ > 1^\\circ$).",
                "Option A inverts the stability order.", diff, q_type
            )
        elif "Alkenes" in subtopic:
            return (
                "Ozonolysis of an alkene produces Acetone ($(\\text{CH}_3)_2\\text{CO}$) and Formaldehyde ($\\text{HCHO}$). What is the structure of the original alkene?",
                "2-Methylpropene ($(\\text{CH}_3)_2\\text{C}=\\text{CH}_2$)",
                ["But-2-ene", "2-Methylbut-2-ene", "Propene"],
                "Join the two carbonyl fragments at oxygen atoms to reconstruct the double bond.",
                "Reductive ozonolysis and double bond position identification.",
                "$$(\\text{CH}_3)_2\\text{C}=\\text{O} + \\text{O}=\\text{CH}_2 \\implies (\\text{CH}_3)_2\\text{C}=\\text{CH}_2\\text{ (2-methylpropene)}.$$",
                "Option B produces acetone and acetaldehyde.", diff, q_type
            )
        elif "Alkynes" in subtopic:
            return (
                "Why is ethyne (acetylene, $\\text{H-C}\\equiv\\text{C-H}$) acidic enough to react with sodium amide ($\\text{NaNH}_2$) while ethene and ethane are not?",
                "Carbon in ethyne is sp hybridized with $50\\%$ s-character, making it highly electronegative and stabilizing the carbanion",
                ["Ethyne possesses delocalized $\\pi$-electron aromatic cloud", "Ethyne undergoes spontaneous resonance into an allenic anion", "Carbon in ethyne is sp^3 hybridized"],
                "Higher s-character ($50\\%$ in sp vs $33\\%$ in $sp^2$ vs $25\\%$ in $sp^3$) increases electronegativity.",
                "Acidity of terminal alkynes and hybridization of carbon.",
                "Higher s-character pulls electrons closer to carbon nucleus, stabilizing conjugate acetylide base $\\text{H-C}\\equiv\\text{C}^-$.",
                "Option A incorrectly attributes aromaticity to acyclic ethyne.", diff, q_type
            )
        else: # Aromaticity & Electrophilic Substitution
            return (
                "According to Huckel's rule, a cyclic planar conjugated molecule is aromatic if it contains:",
                "$(4n + 2)\\;\\pi\\text{ electrons (where } n = 0, 1, 2, 3, \\dots)$",
                ["$4n\\;\\pi\\text{ electrons}$", "$(2n + 1)\\;\\pi\\text{ electrons}$", "$(4n + 4)\\;\\pi\\text{ electrons}$"],
                "Huckel's rule: Planar, cyclic, completely conjugated with $(4n+2)\\pi$ electrons.",
                "Criteria for aromaticity and electronic delocalization.",
                "Benzene ($n=1$, $6\\pi$ electrons), cyclooctatetraene dianion ($n=2$, $10\\pi$ electrons), and cyclopentadienyl anion ($n=1$, $6\\pi$) satisfy $(4n+2)$.",
                "Option A ($4n$) defines antiaromatic systems (e.g. cyclobutadiene).", diff, q_type
            )

    # =========================================================================
    # CLASS 12 CHEMISTRY
    # =========================================================================
    elif "Solutions" in chapter:
        if "Raoult" in subtopic:
            return (
                "Which binary liquid mixture exhibits NEGATIVE deviation from Raoult's Law with maximum boiling azeotrope?",
                "Chloroform and Acetone (forming intermolecular hydrogen bonds between $\\text{CHCl}_3$ and carbonyl oxygen)",
                ["Ethanol and Acetone", "Benzene and Toluene", "Carbon tetrachloride and Chloroform"],
                "Negative deviation occurs when solute-solvent interactions ($A-B$) are stronger than $A-A$ and $B-B$.",
                "Thermodynamics of non-ideal solutions and azeotropic mixtures.",
                "Hydrogen bonding between chloroform hydrogen and acetone oxygen strengthens $A-B$ attraction, decreasing vapor pressure below Raoult's ideal value.",
                "Option A exhibits positive deviation due to breaking of ethanol hydrogen bonds.", diff, q_type
            )
        elif "Boiling" in subtopic:
            return (
                "What is the elevation in boiling point ($\\Delta T_b$) of a $1\\text{ molal}$ aqueous solution of $\\text{NaCl}$ ($K_b = 0.52\\text{ K kg/mol}$, assuming $100\\%$ dissociation)?",
                "$\\Delta T_b = 1.04\\text{ K}$ (Van 't Hoff factor $i = 2$)",
                ["$\\Delta T_b = 0.52\\text{ K}$", "$\\Delta T_b = 1.56\\text{ K}$", "$\\Delta T_b = 0.26\\text{ K}$"],
                "$\\Delta T_b = i K_b m$. For $\\text{NaCl} \\rightarrow \\text{Na}^+ + \\text{Cl}^-$, $i = 2$.",
                "Colligative properties and boiling point elevation.",
                "$$\\Delta T_b = (2)(0.52)(1) = 1.04\\text{ K}.$$",
                "Option A forgets Van 't Hoff factor ($i=1$).", diff, q_type
            )
        elif "Freezing" in subtopic:
            return (
                "Ethylene glycol is used as an antifreeze in automobile radiators because it:",
                "Lowers the freezing point of water and raises its boiling point",
                ["Raises the freezing point of water to prevent ice crystal formation", "Acts as an electrical electrolyte conductor", "Permanently solidifies cooling fluid"],
                "Colligative depression in freezing point: $\\Delta T_f = K_f m$.",
                "Depression in freezing point and practical antifreeze applications.",
                "Adding non-volatile ethylene glycol depresses water's freezing point below $0^\\circ\\text{C}$ while elevating boiling point above $100^\\circ\\text{C}$.",
                "Option A asserts freezing point increases, which is physically false.", diff, q_type
            )
        else: # Osmotic Pressure & Van't Hoff Factor
            return (
                "A $0.1\\text{ M}$ solution of potassium ferrocyanide $\\text{K}_4[\\text{Fe(CN)}_6]$ with $100\\%$ dissociation has a Van 't Hoff factor $i$ equal to:",
                "$i = 5$ (dissociates into $4\\text{ K}^+ + 1\\;[\\text{Fe(CN)}_6]^{4-}$)",
                ["$i = 4$", "$i = 1$", "$i = 6$"],
                "Van 't Hoff factor for complete dissociation $i = n$. Total ions $= 4 + 1 = 5$.",
                "Van 't Hoff factor and coordination compound ionic dissociation.",
                "Complex ion $[\\text{Fe(CN)}_6]^{4-}$ remains intact as a single entity; potassium counter-ions dissociate into $4\\text{ K}^+$. Total ions $= 5$.",
                "Option A counts only potassium ions.", diff, q_type
            )

    elif "Electrochemistry" in chapter:
        if "Nernst" in subtopic:
            return (
                "In a Daniell cell: $\\text{Zn}(s) + \\text{Cu}^{2+}(aq) \\rightarrow \\text{Zn}^{2+}(aq) + \\text{Cu}(s)$, given $E^\\circ_{\\text{Zn}^{2+}/\\text{Zn}} = -0.76\\text{ V}$ and $E^\\circ_{\\text{Cu}^{2+}/\\text{Cu}} = +0.34\\text{ V}$. Standard cell EMF $E^\\circ_{\\text{cell}}$ is:",
                "$E^\\circ_{\\text{cell}} = +1.10\\text{ V}$",
                ["$E^\\circ_{\\text{cell}} = +0.42\\text{ V}$", "$E^\\circ_{\\text{cell}} = -1.10\\text{ V}$", "$E^\\circ_{\\text{cell}} = +0.76\\text{ V}$"],
                "$E^\\circ_{\\text{cell}} = E^\\circ_{\\text{cathode}} - E^\\circ_{\\text{anode}} = +0.34 - (-0.76)$.",
                "Standard reduction potentials and galvanic cell EMF.",
                "$$E^\\circ_{{\\text{{cell}}}} = +0.34\\text{{ V}} - (-0.76\\text{{ V}}) = +1.10\\text{{ V}}.$$",
                "Option A subtracts magnitudes without respecting the negative sign of zinc.", diff, q_type
            )
        elif "Kohlrausch" in subtopic:
            return (
                "According to Kohlrausch's Law of Independent Migration of Ions, the limiting molar conductivity of an electrolyte is:",
                "The sum of individual limiting molar conductivities of its constituent cations and anions",
                ["The product of ionic charges and temperature", "Independent of concentration and solvent viscosity", "Zero at infinite dilution"],
                "$\\Lambda_m^\\circ = \\nu_+ \\lambda_+^\\circ + \\nu_- \\lambda_-^\\circ$.",
                "Kohlrausch's law and limiting molar conductivities.",
                "At infinite dilution, each ion migrates independently of co-ions, contributing a definite value to total molar conductivity.",
                "Option C is false; molar conductivity reaches maximum finite limit $\\Lambda_m^\\circ$ at infinite dilution.", diff, q_type
            )
        elif "Faraday" in subtopic:
            return (
                "How many Faradays ($F$) of electricity are required to reduce $1\\text{ mole}$ of $\\text{Al}^{3+}$ ions to metallic aluminum ($\\text{Al}$)?",
                "$3\\text{ F}$ (reduction reaction: $\\text{Al}^{3+} + 3e^- \\rightarrow \\text{Al}$)",
                ["$1\\text{ F}$", "$2\\text{ F}$", "$6\\text{ F}$"],
                "Faraday's Law: $1\\text{ mol}$ of electrons $= 1\\text{ Faraday} \\approx 96,500\\text{ C}$.",
                "Faraday's laws of electrolysis and charge stoichiometry.",
                "Reducing $1\\text{ mol}$ of trivalent $\\text{Al}^{3+}$ requires $3\\text{ moles of electrons} = 3\\text{ F}$.",
                "Option A calculates for monovalent ion like $\\text{Na}^+$.", diff, q_type
            )
        else: # Lead Storage Battery & Fuel Cells
            return (
                "During the discharging of a lead storage battery, what chemical transformation occurs at both the anode and cathode?",
                "Both electrodes are converted into lead sulfate ($\\text{PbSO}_4$) while sulfuric acid is consumed",
                ["Anode produces $\\text{PbO}_2$ while cathode produces $\\text{Pb}$", "Concentration of $\\text{H}_2\\text{SO}_4$ increases", "Lead metal is deposited at both electrodes"],
                "Discharge reaction: $\\text{Pb} + \\text{PbO}_2 + 2\\text{H}_2\\text{SO}_4 \\rightarrow 2\\text{PbSO}_4 + 2\\text{H}_2\\text{O}$.",
                "Secondary galvanic cells and lead-acid battery electrochemistry.",
                "Anode ($\\text{Pb}$) oxidizes to $\\text{PbSO}_4$; Cathode ($\\text{PbO}_2$) reduces to $\\text{PbSO}_4$. Density of $\\text{H}_2\\text{SO}_4$ drops.",
                "Option B is the process occurring during RECHARGING.", diff, q_type
            )

    elif "Chemical Kinetics" in chapter:
        if "Rate Law" in subtopic:
            return (
                "For reaction $A + B \\rightarrow \\text{Products}$, doubling $[A]$ quadruples the rate, while doubling $[B]$ doubles the rate. The overall order of reaction is:",
                "Order $= 3$ (second order in $A$ and first order in $B$; $\\text{Rate} = k [A]^2 [B]$)",
                ["Order $= 2$", "Order $= 1$", "Order $= 4$"],
                "$\\text{Rate} \\propto [A]^x [B]^y$. If doubling $[A]$ gives $4\\times$, $x=2$. If doubling $[B]$ gives $2\\times$, $y=1$. Overall $= x+y$.",
                "Rate laws and reaction order determination from initial rates.",
                "$$2^x = 4 \\implies x = 2; \\quad 2^y = 2 \\implies y = 1. \\quad \\text{Overall Order} = 2 + 1 = 3.$$",
                "Option A assumes first order in each reactant.", diff, q_type
            )
        elif "Half-life" in subtopic:
            k = 2.303e-3
            t12 = round(0.693 / k, 1)
            t75 = round(2 * t12, 1)
            return (
                f"A first-order reaction has rate constant $k = {k:.3e}\\text{{ s}}^{{-1}}$. Time required for $75\\%$ decomposition of reactant is:",
                f"$t_{{75\\%}} = {t75}\\text{{ s}}$",
                [f"$t_{{75\\%}} = {t12}\\text{{ s}}$", f"$t_{{75\\%}} = {round(t75 * 1.5, 1)}\\text{{ s}}$", f"$t_{{75\\%}} = {round(t12 / 2, 1)}\\text{{ s}}$"],
                "First-order: $t_{75\\%} = 2 \\times t_{1/2} = 2 \\times \\frac{0.693}{k}$.",
                "Integrated rate equations and half-life relations.",
                f"$$t_{{1/2}} = \\frac{{0.693}}{{{k:.3e}}} = {t12}\\text{{ s}} \\implies t_{{75\\%}} = 2 \\times {t12} = {t75}\\text{{ s}}.$$",
                "Option A is the time for $50\\%$ completion (one half-life).", diff, q_type
            )
        elif "Arrhenius" in subtopic:
            return (
                "According to the Arrhenius equation $k = A e^{-E_a / (RT)}$, a plot of $\\ln k$ versus $1/T$ yields a straight line with slope equal to:",
                "$\\text{Slope} = -\\frac{E_a}{R}$",
                ["$\\text{Slope} = +\\frac{E_a}{R}$", "$\\text{Slope} = -E_a$", "$\\text{Slope} = \\ln A$"],
                "$\\ln k = \\ln A - \\frac{E_a}{R}\\left(\\frac{1}{T}\\right)$. Form $y = c + mx$.",
                "Arrhenius activation energy and temperature dependence of rates.",
                "Plotting $\\ln k$ ($y$) against $1/T$ ($x$) gives a negative linear slope $m = -E_a / R$ and intercept $\\ln A$.",
                "Option A omits the negative sign.", diff, q_type
            )
        else: # Collision Theory & Pseudo First Order
            return (
                "The acid-catalyzed hydrolysis of ethyl acetate: $\\text{CH}_3\\text{COOC}_2\\text{H}_5 + \\text{H}_2\\text{O} \\xrightarrow{\\text{H}^+} \\text{CH}_3\\text{COOH} + \\text{C}_2\\text{H}_5\\text{OH}$ is classified as:",
                "Pseudo-first-order reaction (water is present in large excess, so its concentration remains practically constant)",
                ["True second-order bimolecular reaction", "Zero-order reaction", "Third-order reaction"],
                "When one reactant is present in large excess, its concentration does not alter noticeably.",
                "Pseudo-molecularity and pseudo-first-order reaction kinetics.",
                "Rate $= k' [\\text{ester}][\\text{H}_2\\text{O}]$. Because $[\\text{H}_2\\text{O}]$ is constant, Rate $= k[\\text{ester}]$, behaving as first-order.",
                "Option A considers molecularity rather than apparent kinetic order.", diff, q_type
            )

    elif "d and f Block" in chapter:
        if "Configurations" in subtopic:
            return (
                "The anomalous electronic configuration of Chromium atom ($Z = 24$) is correctly represented as:",
                "$[\\text{Ar}]\\;3d^5 4s^1$ (due to symmetrical half-filled d-subshell exchange stability)",
                ["$[\\text{Ar}]\\;3d^4 4s^2$", "$[\\text{Ar}]\\;3d^6 4s^0$", "$[\\text{Ar}]\\;3d^3 4s^2 4p^1$"],
                "Half-filled ($d^5$) and fully-filled ($d^{10}$) subshells have extra exchange energy stability.",
                "Electronic configurations of 3d transition series elements.",
                "Transferring an electron from $4s$ to $3d$ gives a stable spherically symmetric half-filled $3d^5$ subshell with maximum exchange energy.",
                "Option A represents the expected Aufbau configuration without exchange stabilization.", diff, q_type
            )
        elif "Magnetic" in subtopic:
            return (
                "What is the spin-only magnetic moment ($\\mu$) of a $\\text{Fe}^{2+}$ ion ($3d^6$, $4$ unpaired electrons)?",
                "$\\mu = \\sqrt{4(4 + 2)} = \\sqrt{24} \\approx 4.90\\text{ BM}$",
                ["$\\mu = \\sqrt{6(6 + 2)} = \\sqrt{48} \\approx 6.93\\text{ BM}$", "$\\mu = \\sqrt{2(2 + 2)} = \\sqrt{8} \\approx 2.83\\text{ BM}$", "$\\mu = 0\\text{ BM}$ (Diamagnetic)"],
                "Spin-only formula: $\\mu = \\sqrt{n(n + 2)}\\text{ BM}$ where $n$ is number of unpaired electrons.",
                "Magnetic moments and paramagnetism of transition metal ions.",
                "$\\text{Fe}^{2+}$ has $3d^6$ configuration. By Hund's rule, there are $4$ unpaired electrons $\\implies \\mu = \\sqrt{4 \\times 6} = 4.90\\text{ BM}$.",
                "Option A uses total d-electrons ($6$) instead of unpaired electrons ($4$).", diff, q_type
            )
        elif "Lanthanoid" in subtopic:
            return (
                "What causes the nearly identical atomic radii of $\\text{Zr}$ ($4d$, $160\\text{ pm}$) and $\\text{Hf}$ ($5d$, $159\\text{ pm}$)?",
                "Lanthanoid Contraction (poor shielding by intervening $4f$ electrons)",
                ["Diagonal relationship", "Actinoid contraction", "Identical number of valence shells"],
                "$4f$ electrons shield nuclear charge poorly, causing steady decrease in atomic radii.",
                "Lanthanoid contraction and post-lanthanoid transition elements.",
                "Between $\\text{La}$ and $\\text{Hf}$, $14$ lanthanoid elements fill the diffuse $4f$ subshell. Imperfect shielding allows high nuclear charge to pull outer electrons inward.",
                "Option B refers to the $5f$ series elements.", diff, q_type
            )
        else: # Potassium Dichromate & Permanganate
            return (
                "In acidic medium, Potassium Permanganate ($\\text{KMnO}_4$) acts as a powerful oxidizing agent. Its equivalent weight is:",
                "$\\text{Equivalent Weight} = \\frac{M}{5}$ (Manganese is reduced from $+7$ to $+2$)",
                ["$\\text{Equivalent Weight} = \\frac{M}{3}$", "$\\text{Equivalent Weight} = M$", "$\\text{Equivalent Weight} = \\frac{M}{6}$"],
                "Equivalent weight $= \\frac{\\text{Molar Mass}}{n\\text{-factor}}$ ($n$-factor $= 5$ in acid, $3$ in neutral, $1$ in alkaline).",
                "Equivalent weight of oxidizing agents in varying pH media.",
                "$$\\text{MnO}_4^- + 8\\text{H}^+ + 5e^- \\rightarrow \\text{Mn}^{2+} + 4\\text{H}_2\\text{O} \\implies n = 5 \\implies \\text{Eq. Wt.} = M / 5.$$",
                "Option A ($M/3$) is the equivalent weight in neutral or weakly alkaline medium.", diff, q_type
            )

    elif "Coordination Compounds" in chapter:
        if "Werner" in subtopic:
            return (
                "According to Werner's theory, when excess silver nitrate ($\\text{AgNO}_3$) is added to $1\\text{ mole}$ of $\\text{CoCl}_3 \\cdot 5\\text{NH}_3$, how many moles of $\\text{AgCl}$ precipitate?",
                "$2\\text{ moles of AgCl}$ (formulated as $[\\text{Co(NH}_3)_5\\text{Cl}]\\text{Cl}_2$ with 2 ionizable chloride ions)",
                ["$3\\text{ moles of AgCl}$", "$1\\text{ mole of AgCl}$", "$0\\text{ moles of AgCl}$"],
                "Primary valencies (outside coordination sphere) ionize; secondary valencies (inside sphere) do not.",
                "Werner's coordination theory and primary vs secondary valency.",
                "Coordination number of Cobalt is 6. Complex is $[\\text{Co(NH}_3)_5\\text{Cl}]\\text{Cl}_2$. The two chloride counter-ions outside the sphere precipitate as $\\text{AgCl}$.",
                "Option A assumes all three chlorides are ionizable.", diff, q_type
            )
        elif "Isomerism" in subtopic:
            return (
                "Which coordination complex exhibits optical isomerism (enantiomer pairs)?",
                "cis-$[\\text{Pt(en)}_2\\text{Cl}_2]^{2+}$ (asymmetrical cis isomer lacking plane of symmetry)",
                ["trans-$[\\text{Pt(en)}_2\\text{Cl}_2]^{2+}$ (possessing inversion center/plane of symmetry)", "$[\\text{Co(NH}_3)_6]^{3+}$", "Square planar $[\\text{Pt(NH}_3)_2\\text{Cl}_2]$"],
                "Optical isomerism requires non-superimposable mirror images lacking plane of symmetry.",
                "Optical and geometrical stereoisomerism in coordination complexes.",
                "cis-$[\\text{Pt(en)}_2\\text{Cl}_2]^{2+}$ is chiral with no plane of symmetry. Its trans isomer has a plane of symmetry and is optically inactive.",
                "Option B is the trans isomer, which is optically inactive.", diff, q_type
            )
        elif "CFT" in subtopic:
            return (
                "In an octahedral complex $[\\text{CoF}_6]^{3-}$ with weak-field fluoride ligand ($\\Delta_o < P$), the $d^6$ electronic configuration is:",
                "$t_{2g}^4 e_g^2$ (High spin, 4 unpaired electrons)",
                ["$t_{2g}^6 e_g^0$ (Low spin, diamagnetic)", "$t_{2g}^3 e_g^3$", "$t_{2g}^5 e_g^1$"],
                "Weak field: $\\Delta_o < P$ (pairing energy). Electrons obey Hund's rule and populate $e_g$ before pairing in $t_{2g}$.",
                "Crystal field splitting and spectrochemical ligand strength.",
                "Because pairing energy exceeds crystal field splitting, electrons occupy $t_{2g}^3 e_g^2$ singly first, then the 6th electron pairs in $t_{2g}$, yielding $t_{2g}^4 e_g^2$.",
                "Option A is the low-spin configuration formed by strong-field ligands like $\\text{CN}^-$.", diff, q_type
            )
        else: # Valence Bond Theory
            return (
                "According to Valence Bond Theory, the complex ion $[\\text{Fe(CN)}_6]^{3-}$ involves which hybridization and geometry?",
                "$d^2sp^3$ hybridization (Inner orbital octahedral complex, paramagnetic with 1 unpaired electron)",
                ["$sp^3d^2$ hybridization (Outer orbital octahedral complex)", "$sp^3$ tetrahedral", "$dsp^2$ square planar"],
                "Cyanide ($\\text{CN}^-$) is a strong-field ligand that forces pairing of $3d$ electrons, leaving two $3d$ orbitals vacant for $d^2sp^3$.",
                "Valence bond theory and inner vs outer orbital complexes.",
                "$\\text{Fe}^{3+}$ ($d^5$) electrons pair up under strong $\\text{CN}^-$ ligand field to leave two inner $3d$ orbitals free, giving $d^2sp^3$ octahedral hybridization.",
                "Option B occurs with weak-field ligands like $[\\text{FeF}_6]^{3-}$.", diff, q_type
            )

    elif "Haloalkanes" in chapter:
        if "SN1" in subtopic:
            return (
                "Which alkyl halide undergoes nucleophilic substitution via $\\text{S}_\\text{N}1$ mechanism at the fastest rate?",
                "Tertiary butyl chloride ($(\\text{CH}_3)_3\\text{C-Cl}$)",
                ["Isopropyl chloride ($(\\text{CH}_3)_2\\text{CH-Cl}$)", "Ethyl chloride ($\\text{CH}_3\\text{CH}_2\\text{Cl}$)", "Methyl chloride ($\\text{CH}_3\\text{Cl}$)"],
                "$\\text{S}_\\text{N}1$ rate is governed by carbocation intermediate stability: $3^\\circ > 2^\\circ > 1^\\circ > \\text{methyl}$.",
                "Carbocation stability and unimolecular nucleophilic substitution kinetics.",
                "Ionization yields the tertiary carbocation, stabilized by 9 hyperconjugative $\\alpha$-hydrogens. Hence it reacts fastest by $\\text{S}_\\text{N}1$.",
                "Option D reacts fastest by $\\text{S}_\\text{N}2$ mechanism due to minimal steric hindrance.", diff, q_type
            )
        elif "Elimination" in subtopic:
            return (
                "According to Saytzeff's Rule, dehydrohalogenation of 2-bromobutane with alcoholic $\\text{KOH}$ yields which major product?",
                "But-2-ene (more substituted, thermodynamically more stable alkene)",
                ["But-1-ene (less substituted alkene)", "Butan-2-ol", "But-1-yne"],
                "Saytzeff's Rule: Elimination favors the alkene having greatest number of alkyl substituents on double-bonded carbons.",
                "$\beta$-elimination mechanism and Saytzeff regioselectivity.",
                "Elimination of $\\text{H}$ from C-3 produces but-2-ene (6 hyperconjugative hydrogens, $81\\%$ major). Elimination from C-1 yields but-1-ene ($19\\%$ minor).",
                "Option B is the substitution product formed with aqueous $\\text{KOH}$.", diff, q_type
            )
        elif "Chlorobenzene" in subtopic:
            return (
                "Why is Chlorobenzene significantly less reactive toward nucleophilic substitution than Chloroethane?",
                "Resonance gives the $\\text{C-Cl}$ bond partial double bond character, and the $sp^2$ hybridized carbon is more electronegative",
                ["Chlorine is easily protonated in benzene ring", "Benzene ring undergoes spontaneous ring cleavage", "The $\\text{C-Cl}$ bond length is longer in chlorobenzene"],
                "Partial double bond character from resonance + $sp^2$ carbon holding electrons tightly.",
                "Nucleophilic aromatic substitution resistance in aryl halides.",
                "Delocalization of chlorine lone pair into benzene ring shortens and strengthens $\\text{C-Cl}$ bond ($169\\text{ pm}$ vs $177\\text{ pm}$ in haloalkanes), resisting cleavage.",
                "Option C is false; resonance makes the bond shorter, not longer.", diff, q_type
            )
        else: # Grignard Reagents
            return (
                "Why must Grignard reagents ($R\\text{MgX}$) be prepared in strictly anhydrous (dry ether) conditions?",
                "Grignard reagents are highly reactive bases and react with traces of water to form alkanes ($R\\text{MgX} + \\text{H}_2\\text{O} \\rightarrow R\\text{H} + \\text{Mg(OH)X}$)",
                ["Water oxidizes magnesium to magnesium oxide", "Ether acts as a nucleophile displacing magnesium", "Water permanently polymerizes alkyl radicals"],
                "Strongly basic carbanion character of $R^-$ abstracts proton from any protic source.",
                "Organometallic Grignard chemistry and moisture sensitivity.",
                "The carbon-magnesium bond is strongly polar covalent ($R^{\\delta-}-\\text{Mg}^{\\delta+}\\text{X}$). Even trace moisture protonates $R^-$, decomposing reagent into alkane.",
                "Option A is incorrect; the primary destruction is carbanion protonation.", diff, q_type
            )

    elif "Alcohols" in chapter:
        if "Hydroboration" in subtopic:
            return (
                "Hydroboration-oxidation of propene ($\\text{CH}_3\\text{CH}=\\text{CH}_2$) with $(\\text{BH}_3)_2$ followed by alkaline $\\text{H}_2\\text{O}_2$ yields:",
                "Propan-1-ol (Anti-Markownikoff hydration product)",
                ["Propan-2-ol (Markownikoff product)", "Propanoic acid", "Acetone"],
                "Hydroboration-oxidation adds $\\text{H}_2\\text{O}$ across double bond in Anti-Markownikoff orientation with syn-stereospecificity.",
                "Electrophilic organoborane additions and regioselective hydration.",
                "Boron attacks terminal carbon to minimize steric hindrance, giving trialkylborane. Oxidation by alkaline $\\text{H}_2\\text{O}_2$ yields propan-1-ol.",
                "Option A is the product of acid-catalyzed hydration or oxymercuration-demercuration.", diff, q_type
            )
        elif "Reimer" in subtopic:
            return (
                "In the Reimer-Tiemann reaction, Phenol is heated with $\\text{CHCl}_3$ and aqueous $\\text{NaOH}$. Reactive intermediate and major product are:",
                "Intermediate: Dichlorocarbene ($:\\text{CCl}_2$); Product: Salicylaldehyde (o-hydroxybenzaldehyde)",
                ["Intermediate: Carbocation; Product: Benzaldehyde", "Intermediate: Free radical; Product: Benzoic acid", "Intermediate: Dichlorocarbene; Product: Picric acid"],
                "Reaction: Phenol $+ \\text{CHCl}_3 + 3\\text{NaOH} \\rightarrow \\text{Salicylaldehyde}$.",
                "Electrophilic aromatic substitution of phenoxide by carbenes.",
                "Base abstracts proton from $\\text{CHCl}_3$ followed by $\\alpha$-elimination of $\\text{Cl}^-$, producing neutral electrophilic dichlorocarbene intermediate.",
                "Option A mistakes the electrophile for an alkyl carbocation.", diff, q_type
            )
        elif "Williamson" in subtopic:
            return (
                "To prepare tert-butyl ethyl ether via Williamson's Ether Synthesis, which reactant combination must be employed?",
                "Sodium tert-butoxide ($(\\text{CH}_3)_3\\text{C-ONa}$) + Ethyl bromide ($\\text{CH}_3\\text{CH}_2\\text{Br}$)",
                ["Sodium ethoxide ($\\text{CH}_3\\text{CH}_2\\text{ONa}$) + tert-Butyl bromide ($(\\text{CH}_3)_3\\text{C-Br}$)", "tert-Butanol + Ethanol with dilute $\\text{HCl}$", "Sodium tert-butoxide + Acetone"],
                "Williamson synthesis operates via $\\text{S}_\\text{N}2$ mechanism; alkyl halide MUST be primary ($1^\\circ$) to avoid E2 elimination.",
                "Williamson ether synthesis mechanism and steric limitations.",
                "If tert-butyl bromide ($3^\\circ$) is used with alkoxide, strong basicity causes exclusive E2 elimination yielding isobutylene rather than ether. Hence primary alkyl halide must be used.",
                "Option A yields isobutylene ($99\\%$) via E2 elimination.", diff, q_type
            )
        else: # Acidic Character of Phenols vs Alcohols
            return (
                "Why are phenols significantly more acidic than aliphatic alcohols ($\\text{p}K_a \\approx 10$ vs $16$)?",
                "Phenoxide ion is stabilized by delocalization of negative charge across the aromatic ring resonance structures",
                ["Aliphatic alkoxide ions possess stronger resonance stabilization", "Phenol contains an acidic carboxylic acid moiety", "Phenol cannot form intermolecular hydrogen bonds"],
                "Acidity depends on conjugate base stability. Phenoxide is resonance-stabilized; alkoxide has no resonance.",
                "Resonance stabilization of phenoxide anion.",
                "In phenoxide, negative charge on oxygen is delocalized over ortho and para positions of benzene ring. In alkoxide ($R\\text{O}^-$), $+I$ alkyl group destabilizes negative charge.",
                "Option A is false; alkoxide has no resonance delocalization.", diff, q_type
            )

    elif "Aldehydes" in chapter:
        if "Nucleophilic" in subtopic:
            return (
                "What is the correct reactivity order of carbonyl compounds toward nucleophilic addition reactions (e.g. addition of $\\text{HCN}$)?",
                "$\\text{HCHO} > \\text{CH}_3\\text{CHO} > \\text{CH}_3\\text{COCH}_3$",
                ["$\\text{CH}_3\\text{COCH}_3 > \\text{CH}_3\\text{CHO} > \\text{HCHO}$", "$\\text{CH}_3\\text{CHO} > \\text{HCHO} > \\text{CH}_3\\text{COCH}_3$", "All react at identical rates"],
                "Nucleophilic addition is favored by low steric hindrance and high electrophilicity on carbonyl carbon.",
                "Steric and electronic factors in carbonyl nucleophilic additions.",
                "Aldehydes are more reactive than ketones due to steric hindrance of alkyl groups and $+I$ electron donation reducing carbonyl positive charge.",
                "Option A is inverted.", diff, q_type
            )
        elif "Aldol" in subtopic:
            return (
                "Which carbonyl compound undergoes the Cannizzaro reaction when treated with concentrated ($50\\%$) aqueous $\\text{NaOH}$?",
                "Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$, lacking $\\alpha$-hydrogen atoms)",
                ["Acetaldehyde ($\\text{CH}_3\\text{CHO}$)", "Acetone ($\\text{CH}_3\\text{COCH}_3$)", "Propanal ($\\text{CH}_3\\text{CH}_2\\text{CHO}$)"],
                "Cannizzaro reaction occurs strictly in aldehydes lacking $\\alpha$-hydrogen atoms.",
                "Disproportionation (self-redox) of non-enolizable aldehydes.",
                "Benzaldehyde has no $\\alpha$-hydrogen, undergoing self-redox to yield benzyl alcohol and sodium benzoate. Compounds with $\\alpha$-hydrogens undergo Aldol condensation.",
                "Options B, C, and D undergo Aldol condensation.", diff, q_type
            )
        elif "Tollens" in subtopic:
            return (
                "Which of the following reduces Tollens' reagent ($[\\text{Ag(NH}_3)_2]^+$) to form a shiny silver mirror?",
                "Acetaldehyde and Glucose (all aldehydes and reducing sugars)",
                ["Acetone", "Acetophenone", "Benzophenone"],
                "Tollens' reagent is reduced by aliphatic and aromatic aldehydes, and $\\alpha$-hydroxy ketones.",
                "Diagnostic chemical tests for carbonyl differentiation.",
                "Aldehydes are easily oxidized to carboxylates by mild oxidant $[\\text{Ag(NH}_3)_2]^+$, precipitating silver mirror $\\text{Ag}(s)$. Ketones do not react.",
                "Options B, C, and D are ketones which do not reduce Tollens' reagent.", diff, q_type
            )
        else: # HVZ Reaction & Decarboxylation
            return (
                "In the Hell-Volhard-Zelinsky (HVZ) reaction, carboxylic acids are treated with $\\text{Br}_2$ in the presence of red phosphorus to form:",
                "$\\alpha$-Bromo carboxylic acids (selective halogenation at the $\\alpha$-carbon)",
                ["$\beta$-Bromo carboxylic acids", "Acid bromides with loss of $\\text{CO}_2$", "Perbromo alkanes"],
                "HVZ reaction selectively replaces $\\alpha$-hydrogen of carboxylic acid with halogen.",
                "$\alpha$-Halogenation of aliphatic carboxylic acids.",
                "Red phosphorus reacts with $\\text{Br}_2$ to form $\\text{PBr}_3$, converting acid to enolizable acyl bromide which brominates at $\\alpha$-position.",
                "Option B confuses HVZ with Hunsdiecker decarboxylation.", diff, q_type
            )

    elif "Amines and Diazonium Salts" in chapter:
        if "Hoffmann" in subtopic:
            return (
                "In the Hoffmann Bromamide Degradation reaction, an amide is treated with $\\text{Br}_2$ and aqueous $\\text{KOH}$. The amine product contains:",
                "One carbon atom LESS than the parent amide ($R\\text{CONH}_2 \\rightarrow R\\text{NH}_2$)",
                ["Same number of carbon atoms as parent amide", "One carbon atom more than parent amide", "Two amine groups on adjacent carbons"],
                "Reaction: $R\\text{CONH}_2 + \\text{Br}_2 + 4\\text{KOH} \\rightarrow R\\text{NH}_2 + \\text{K}_2\\text{CO}_3 + 2\\text{KBr} + 2\\text{H}_2\\text{O}$.",
                "Hoffmann degradation of amides and carbon-chain stepping down.",
                "Carbonyl carbon is eliminated as carbonate ion ($\\text{K}_2\\text{CO}_3$) through an isocyanate ($R\\text{-N=C=O}$) intermediate, yielding amine with one less carbon.",
                "Option A is true for reduction with $\\text{LiAlH}_4$, not Hoffmann degradation.", diff, q_type
            )
        elif "Basicity" in subtopic:
            return (
                "In aqueous solution, what is the correct order of basic strength of methyl-substituted aliphatic amines?",
                "Secondary > Primary > Tertiary > Ammonia ($(\\text{CH}_3)_2\\text{NH} > \\text{CH}_3\\text{NH}_2 > (\\text{CH}_3)_3\\text{N} > \\text{NH}_3$)",
                ["Tertiary > Secondary > Primary > Ammonia", "Primary > Secondary > Tertiary > Ammonia", "Ammonia > Primary > Secondary > Tertiary"],
                "Combined effect of $+I$ inductive effect, steric hindrance, and hydration of conjugate cation.",
                "Aqueous basicity and solvation stabilization of alkylammonium cations.",
                "In aqueous solution for methyl amines, basic strength order is $2^\\circ > 1^\\circ > 3^\\circ > \\text{NH}_3$ (213 order). For ethyl amines, order is $2^\\circ > 3^\\circ > 1^\\circ > \\text{NH}_3$ (231 order).",
                "Option A represents gas phase basicity ($3^\\circ > 2^\\circ > 1^\\circ$), ignoring hydration stabilization.", diff, q_type
            )
        elif "Carbylamine" in subtopic or "Hinsberg" in subtopic:
            return (
                "The Carbylamine reaction (heating with $\\text{CHCl}_3$ and alcoholic $\\text{KOH}$) is a diagnostic test given exclusively by:",
                "Primary aliphatic and primary aromatic amines, producing foul-smelling isocyanides ($R\\text{-NC}$)",
                ["Secondary amines only", "Tertiary amines only", "All classes of amines and amides"],
                "Carbylamine test: $R\\text{-NH}_2 + \\text{CHCl}_3 + 3\\text{KOH} \\rightarrow R\\text{-NC} + 3\\text{KCl} + 3\\text{H}_2\\text{O}$.",
                "Electrophilic dichlorocarbene intermediate and isocyanide test.",
                "Only primary amines possess two nitrogen hydrogens required to eliminate water with dichlorocarbene ($\\text{:CCl}_2$), forming extremely foul-smelling isocyanides.",
                "Secondary and tertiary amines do not react.", diff, q_type
            )
        else: # Diazonium Salts & Sandmeyer
            return (
                "Treatment of freshly prepared benzenediazonium chloride ($\\text{C}_6\\text{H}_5\\text{N}_2^+\\text{Cl}^-$) with cuprous chloride in $\\text{HCl}$ (Sandmeyer reaction) yields:",
                "Chlorobenzene ($\\text{C}_6\\text{H}_5\\text{Cl}$) with nitrogen gas evolution ($\\text{N}_2$)",
                ["Phenol ($\\text{C}_6\\text{H}_5\\text{OH}$)", "Benzene ($\\text{C}_6\\text{H}_6$)", "Aniline ($\\text{C}_6\\text{H}_5\\text{NH}_2$)"],
                "Sandmeyer reaction: $\\text{ArN}_2^+\\text{Cl}^- \\xrightarrow{\\text{Cu}_2\\text{Cl}_2/\\text{HCl}} \\text{ArCl} + \\text{N}_2$.",
                "Radical substitution of aryl diazonium groups.",
                "Copper(I) ion catalyzes one-electron transfer to the diazonium cation, releasing $\\text{N}_2$ gas and generating aryl radical which captures chlorine to give chlorobenzene.",
                "Option B is obtained by reduction with $\\text{H}_3\\text{PO}_2$.", diff, q_type
            )

    else: # Biomolecules
        if "Glucose" in subtopic or "Carbohydrates" in subtopic:
            return (
                "The $\\alpha$-D-glucopyranose and $\\beta$-D-glucopyranose forms of glucose are classified as:",
                "Anomers (epimers differing in configuration only at the C-1 anomeric hemiacetal carbon)",
                ["Enantiomers", "Geometrical isomers", "Structural chain isomers"],
                "Anomers are stereoisomers differing in configuration strictly at the hemiacetal carbon.",
                "Cyclic pyranose structures and mutarotation of monosaccharides.",
                "During intramolecular hemiacetal formation between C-1 carbonyl and C-5 hydroxyl, C-1 becomes chiral, producing $\\alpha$ ($-\\text{OH}$ axial/down) and $\\beta$ ($-\\text{OH}$ equatorial/up) anomers.",
                "Option A refers to non-superimposable mirror images across all chiral centers.", diff, q_type
            )
        elif "Amino Acids" in subtopic or "Zwitterions" in subtopic:
            return (
                "In neutral aqueous solution, an amino acid exists predominantly as a dipolar ion termed a Zwitterion because:",
                "The basic amino group ($-\\text{NH}_2$) accepts a proton to become $-\\text{NH}_3^+$, while the acidic carboxyl group ($-\\text{COOH}$) loses a proton to become $-\\text{COO}^-$",
                ["It carries zero net charge in any non-polar solvent", "The amino acid polymerizes into peptide chains spontaneously", "The alpha carbon undergoes spontaneous inversion of stereochemistry"],
                "Zwitterion: dipolar ion carrying both positive ($-\\text{NH}_3^+$) and negative ($-\\text{COO}^-$) formal charges.",
                "Isoelectric point and amphoteric equilibria of amino acids.",
                "Because of intramolecular acid-base neutralization, amino acids exist as neutral dipolar zwitterions. At their characteristic isoelectric point ($pI$), they do not migrate in an electric field.",
                "Option B describes peptide synthesis, requiring ATP/ribosomes.", diff, q_type
            )
        elif "Protein" in subtopic:
            return (
                "During denaturation of a globular protein (by heat, heavy metals, or extreme pH), which structural level remains strictly intact?",
                "Primary structure (covalent peptide bonds are not broken)",
                ["Secondary structure ($\\alpha$-helix and $\\beta$-pleated sheets)", "Tertiary three-dimensional folded conformation", "Quaternary subunit assembly"],
                "Denaturation disrupts hydrogen bonds, ionic salt bridges, and hydrophobic interactions, but not covalent peptide linkages.",
                "Protein conformational stability and denaturation mechanisms.",
                "Denaturation unfolds tertiary and secondary structures, causing loss of biological activity, but linear sequence of amino acids joined by peptide bonds (primary structure) remains intact.",
                "Options B, C, and D are destroyed during denaturation.", diff, q_type
            )
        else: # Nucleic Acids & Enzyme
            return (
                "In DNA and RNA polynucleotide chains, consecutive nucleotides are covalently linked together by:",
                "$3'-5'$ phosphodiester linkages between the phosphate group and sugars",
                ["$1'-4'$ glycosidic bonds", "Hydrogen bonds between nitrogenous base pairs", "Disulfide covalent cross-bridges"],
                "Nucleotides polymerize via $3'-5'$ phosphodiester bonds.",
                "Phosphodiester backbone and primary structure of nucleic acids.",
                "The 3'-OH group of the sugar of one nucleotide connects to the 5'-phosphate group of the adjacent nucleotide via an ester bond, forming a continuous alternating sugar-phosphate backbone.",
                "Option B is found in glycogen/starch.", diff, q_type
            )

        if "Hoffmann" in subtopic:
            return (
                "In the Hoffmann Bromamide Degradation reaction, an amide is treated with $\\text{Br}_2$ and aqueous $\\text{KOH}$. The amine product contains:",
                "One carbon atom LESS than the parent amide ($R\\text{CONH}_2 \\rightarrow R\\text{NH}_2$)",
                ["Same number of carbon atoms as parent amide", "One carbon atom more than parent amide", "Two amine groups on adjacent carbons"],
                "Reaction: $R\\text{CONH}_2 + \\text{Br}_2 + 4\\text{KOH} \\rightarrow R\\text{NH}_2 + \\text{K}_2\\text{CO}_3 + 2\\text{KBr} + 2\\text{H}_2\\text{O}$.",
                "Hoffmann degradation of amides and carbon-chain stepping down.",
                "Carbonyl carbon is eliminated as carbonate ion ($\\text{K}_2\\text{CO}_3$) through an isocyanate ($R\\text{-N=C=O}$) intermediate, yielding amine with one less carbon.",
                "Option A is true for reduction with $\\text{LiAlH}_4$, not Hoffmann degradation.", diff, q_type
            )
        elif "Gabriel" in subtopic:
            return (
                "Gabriel Phthalimide synthesis is used exclusively for preparation of which class of amines?",
                "Pure primary aliphatic amines ($R\\text{NH}_2$)",
                ["Aromatic primary amines (Aniline)", "Secondary amines ($R_2\\text{NH}$)", "Tertiary amines ($R_3\\text{N}$)"],
                "Aryl halides cannot undergo nucleophilic $\\text{S}_\\text{N}2$ substitution with phthalimide anion.",
                "Gabriel phthalimide synthesis and substrate specificity.",
                "Phthalimide anion displaces halide from primary alkyl halide. Aryl halides cannot react due to partial double bond character of $\\text{C-X}$ bond; hence aniline cannot be prepared.",
                "Option B is an exam trap: aniline CANNOT be synthesized via Gabriel reaction.", diff, q_type
            )
        elif "Carbohydrates" in subtopic:
            return (
                "The $\\alpha$-D-glucopyranose and $\\beta$-D-glucopyranose forms of glucose are classified as:",
                "Anomers (epimers differing in configuration only at the C-1 anomeric hemiacetal carbon)",
                ["Enantiomers", "Geometrical isomers", "Structural chain isomers"],
                "Anomers are stereoisomers differing in configuration strictly at the hemiacetal carbon.",
                "Cyclic pyranose structures and mutarotation of monosaccharides.",
                "During intramolecular hemiacetal formation between C-1 carbonyl and C-5 hydroxyl, C-1 becomes chiral, producing $\\alpha$ ($-\\text{OH}$ axial/down) and $\\beta$ ($-\\text{OH}$ equatorial/up) anomers.",
                "Option A refers to non-superimposable mirror images across all chiral centers.", diff, q_type
            )
        else: # Proteins
            return (
                "During denaturation of a globular protein (by heat or extreme pH change), which level of protein structural organization remains INTACT?",
                "Primary structure (covalent peptide bonds are not broken)",
                ["Secondary structure ($\alpha$-helix and $\beta$-pleated sheets)", "Tertiary three-dimensional folded conformation", "Quaternary subunit assembly"],
                "Denaturation disrupts hydrogen bonds, ionic salt bridges, and hydrophobic interactions, but not covalent peptide linkages.",
                "Protein conformational stability and denaturation mechanisms.",
                "Denaturation unfolds tertiary and secondary structures, causing loss of biological activity, but linear sequence of amino acids joined by peptide bonds (primary structure) remains intact.",
                "Options B, C, and D are destroyed during denaturation.", diff, q_type
            )
