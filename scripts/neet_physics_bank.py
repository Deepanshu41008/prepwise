import math, random

def get_physics_question(cls_num, chapter, subtopic, q_idx):
    diff = "easy" if q_idx % 4 == 0 else ("hard" if q_idx % 4 == 3 else "medium")
    q_type = "assertion_reason" if q_idx % 7 == 0 else ("match_columns" if q_idx % 9 == 0 else "standard_mcq")
    
    # =========================================================================
    # CLASS 11 PHYSICS
    # =========================================================================
    if "Units and Measurements" in chapter:
        if "SI Units" in subtopic:
            consts = [
                ("Universal Gravitational Constant ($G$)", "$[M^{-1} L^3 T^{-2}]$", ["$[M L^2 T^{-2}]$", "$[M^{-1} L^2 T^{-1}]$", "$[M L^3 T^{-2}]$"],
                 "From $F = \\frac{G m_1 m_2}{r^2} \\implies [G] = \\frac{[F][r^2]}{[m^2]} = [M^{-1} L^3 T^{-2}]$.", "Option B is energy; Option C is angular momentum."),
                ("Planck's Constant ($h$)", "$[M L^2 T^{-1}]$", ["$[M L^2 T^{-2}]$", "$[M L T^{-1}]$", "$[M^{-1} L^2 T^{-1}]$"],
                 "From $E = h\\nu \\implies [h] = \\frac{[M L^2 T^{-2}]}{[T^{-1}]} = [M L^2 T^{-1}]$. It matches dimensions of angular momentum.", "Option A is work; Option B is linear momentum."),
                ("Coefficient of Viscosity ($\\eta$)", "$[M L^{-1} T^{-1}]$", ["$[M L T^{-1}]$", "$[M L^2 T^{-2}]$", "$[M^{-1} L^{-1} T^{-1}]$"],
                 "From Stokes' law $F = 6\\pi\\eta r v \\implies [\\eta] = \\frac{[M L T^{-2}]}{[L][L T^{-1}]} = [M L^{-1} T^{-1}]$.", "Option A is momentum; Option B is energy."),
                ("Permeability of Free Space ($\\mu_0$)", "$[M L T^{-2} A^{-2}]$", ["$[M L^2 T^{-2} A^{-1}]$", "$[M^{-1} L^3 T^{-2} A^2]$", "$[M L T^{-1} A^{-2}]$"],
                 "From force between parallel currents $\\frac{F}{l} = \\frac{\\mu_0 I_1 I_2}{2\\pi d} \\implies [\\mu_0] = [M L T^{-2} A^{-2}]$.", "Option B is magnetic flux; Option C is permittivity $\\varepsilon_0$.")
            ]
            item = consts[q_idx % len(consts)]
            return (
                f"The dimensional formula of {item[0]} in base SI dimensions is:",
                item[1], item[2], "Relate to fundamental equations of motion/electromagnetism.",
                "Dimensional analysis of physical constants from defining dynamical laws.",
                item[3], item[4], diff, q_type
            )
        elif "Significant Figures" in subtopic:
            a_err = (q_idx % 3 + 1)
            b_err = (q_idx % 4 + 2)
            c_err = (q_idx % 2 + 1)
            total_err = 2 * a_err + 3 * b_err + 0.5 * c_err
            return (
                f"A physical quantity $Z$ is calculated as $Z = \\frac{{A^2 B^3}}{{\\sqrt{{C}}}}$. If the percentage errors in measuring $A, B$ and $C$ are ${a_err}\\%$, ${b_err}\\%$ and ${c_err}\\%$ respectively, what is the maximum percentage error in $Z$?",
                f"${total_err}\\%$",
                [f"${a_err + b_err + c_err}\\%$", f"${2*a_err + 3*b_err - 0.5*c_err}\\%$", f"${(2*a_err + 3*b_err)*c_err}\\%$"],
                "Recall: $\\frac{\\Delta Z}{Z} = 2\\frac{\\Delta A}{A} + 3\\frac{\\Delta B}{B} + \\frac{1}{2}\\frac{\\Delta C}{C}$.",
                "Propagation of errors in power and quotient functions.",
                f"$$\\frac{{\\Delta Z}}{{Z}} = 2({a_err}\\%) + 3({b_err}\\%) + 0.5({c_err}\\%) = {total_err}\\%.$$",
                "Option B subtracts the error of $C$ in denominator; fractional errors ALWAYS sum in worst-case analysis.", diff, q_type
            )
        elif "Vernier" in subtopic:
            n_div = 10 if q_idx % 2 == 0 else 20
            msd = 1.0
            lc = round(msd / n_div, 2)
            msr = 5.0 + (q_idx % 5)
            vsr = (q_idx % (n_div - 1)) + 1
            ans = round(msr + vsr * lc, 2)
            d1 = round(msr + vsr * 0.01, 2) if lc != 0.01 else round(msr + vsr * 0.2, 2)
            d2 = round(msr + vsr, 1)
            d3 = round(msr - vsr * lc, 2)
            return (
                f"In a Vernier Calipers, ${n_div}$ vernier scale divisions coincide with ${n_div - 1}$ main scale divisions ($1\\text{{ MSD}} = 1\\text{{ mm}}$). While measuring a cylinder, main scale reads ${msr}\\text{{ mm}}$ and the ${vsr}^{{\\text{{th}}}}$ vernier mark aligns. With zero error nil, the diameter is:",
                f"${ans}\\text{{ mm}}$",
                [f"${d1}\\text{{ mm}}$", f"${d2}\\text{{ mm}}$", f"${d3}\\text{{ mm}}$"],
                "Least Count $LC = 1\\text{ MSD} - 1\\text{ VSD} = \\frac{1\\text{ MSD}}{N}$.",
                "Vernier principle and measurement calculation.",
                f"$$LC = \\frac{{1\\text{{ mm}}}}{{{n_div}}} = {lc}\\text{{ mm}}.$$<br>$$\\text{{Reading}} = \\text{{MSR}} + (\\text{{VSR}} \\times LC) = {msr} + ({vsr} \\times {lc}) = {ans}\\text{{ mm}}.$$",
                "Option B adds VSR directly without multiplying by the Least Count.", diff, q_type
            )
        else: # Dimensional Consistency
            return (
                "Which of the following physical quantity pairs DOES NOT possess identical dimensional formulas?",
                "Torque and Linear Momentum",
                ["Work and Torque", "Impulse and Linear Momentum", "Surface Tension and Surface Energy"],
                "Find base SI dimensions for each pair.",
                "Dimensional homogeneity and physical equivalences.",
                "Torque has dimensions $[M L^2 T^{-2}]$ (same as energy/work). Linear momentum has dimensions $[M L T^{-1}]$. They are dimensionally distinct.",
                "Work and Torque both have $[M L^2 T^{-2}]$. Impulse and Momentum both have $[M L T^{-1}]$. Surface Tension and Surface Energy both have $[M L^0 T^{-2}]$.",
                diff, q_type
            )

    elif "Kinematics" in chapter:
        if "Straight Line" in subtopic:
            u = 10 + (q_idx % 5) * 5
            a = 2 + (q_idx % 3) * 2
            t = 3 + (q_idx % 4)
            v = u + a * t
            s = u * t + 0.5 * a * t**2
            return (
                f"A particle moves along a straight line with initial velocity $u = {u}\\text{{ m/s}}$ and uniform acceleration $a = {a}\\text{{ m/s}}^2$. What is its velocity and displacement after $t = {t}\\text{{ s}}$?",
                f"$v = {v}\\text{{ m/s}}, s = {s}\\text{{ m}}$",
                [f"$v = {v+4}\\text{{ m/s}}, s = {s*2}\\text{{ m}}$", f"$v = {v}\\text{{ m/s}}, s = {u*t}\\text{{ m}}$", f"$v = {u+a}\\text{{ m/s}}, s = {s/2}\\text{{ m}}$"],
                "Equations of motion: $v = u + at$ and $s = ut + \\frac{1}{2}at^2$.",
                "Kinematics of uniformly accelerated rectilinear motion.",
                f"$$v = {u} + ({a})({t}) = {v}\\text{{ m/s}}.$$<br>$$s = ({u})({t}) + \\frac{{1}}{{2}}({a})({t}^2) = {u*t} + {0.5*a*t**2} = {s}\\text{{ m}}.$$",
                "Option B forgets the acceleration contribution to displacement ($\\frac{1}{2}at^2$).", diff, q_type
            )
        elif "Projectile" in subtopic:
            u = 20 + (q_idx % 4) * 10
            theta = 30 if q_idx % 2 == 0 else 45
            rad = math.radians(theta)
            H = round((u**2 * math.sin(rad)**2) / 20, 1)
            T_fl = round((2 * u * math.sin(rad)) / 10, 1)
            return (
                f"A projectile is launched from ground level with speed $u = {u}\\text{{ m/s}}$ at an angle of $\\theta = {theta}^\\circ$ with the horizontal ($g = 10\\text{{ m/s}}^2$). Its maximum height $H$ and total time of flight $T$ are:",
                f"$H = {H}\\text{{ m}}, T = {T_fl}\\text{{ s}}$",
                [f"$H = {H*2}\\text{{ m}}, T = {T_fl}\\text{{ s}}$", f"$H = {H}\\text{{ m}}, T = {T_fl*2}\\text{{ s}}$", f"$H = {round(H/2, 1)}\\text{{ m}}, T = {T_fl}\\text{{ s}}$"],
                "Formulas: $H = \\frac{u^2\\sin^2\\theta}{2g}$ and $T = \\frac{2u\\sin\\theta}{g}$.",
                "Two-dimensional motion under constant gravitational acceleration.",
                f"$$H = \\frac{{{u}^2 \\sin^2({theta}^\\circ)}}{{20}} = {H}\\text{{ m}}.$$<br>$$T = \\frac{{2 \\times {u} \\times \\sin({theta}^\\circ)}}{{10}} = {T_fl}\\text{{ s}}.$$",
                "Option A forgets the factor of 2 in $2g$ in the denominator of $H$.", diff, q_type
            )
        elif "Relative" in subtopic:
            v_r = 10 + (q_idx % 3) * 5
            v_m = 10 + (q_idx % 2) * 5
            return (
                f"Rain is falling vertically downwards with speed $v_r = {v_r}\\text{{ m/s}}$. A man walks horizontally along east with speed $v_m = {v_m}\\text{{ m/s}}$. At what angle $\\theta$ with the vertical should he hold his umbrella to avoid getting wet?",
                f"$\\tan^{{-1}}({round(v_m/v_r, 2)})$ towards east",
                [f"$\\tan^{{-1}}({round(v_r/v_m, 2)})$ towards west", f"Vertically upwards", f"Horizontally towards west"],
                "Relative velocity of rain with respect to man: $\\vec{v}_{\\text{rel}} = \\vec{v}_r - \\vec{v}_m$.",
                "Vector subtraction and relative frames of reference.",
                f"$$\\tan\\theta = \\frac{{|v_m|}}{{|v_r|}} = \\frac{{{v_m}}}{{{v_r}}} = {round(v_m/v_r, 2)}.$$ Umbrella must oppose relative rain velocity.",
                "Option A inverts $\\tan\\theta$ as $v_r/v_m$.", diff, q_type
            )
        else: # Uniform Circular Motion
            r = 2 + (q_idx % 3) * 2
            v = 10 + (q_idx % 4) * 2
            ac = round(v**2 / r, 1)
            omega = round(v / r, 2)
            return (
                f"A car moves at constant speed $v = {v}\\text{{ m/s}}$ around a circular track of radius $r = {r}\\text{{ m}}$. Its centripetal acceleration $a_c$ and angular speed $\\omega$ are:",
                f"$a_c = {ac}\\text{{ m/s}}^2, \\omega = {omega}\\text{{ rad/s}}$",
                [f"$a_c = {round(ac/2, 1)}\\text{{ m/s}}^2, \\omega = {omega}\\text{{ rad/s}}$", f"$a_c = {ac}\\text{{ m/s}}^2, \\omega = {round(omega*r, 1)}\\text{{ rad/s}}$", f"$a_c = {round(v/r, 1)}\\text{{ m/s}}^2, \\omega = {omega}\\text{{ rad/s}}$"],
                "$a_c = \\frac{v^2}{r}$ and $\\omega = \\frac{v}{r}$.",
                "Kinematics of uniform circular motion.",
                f"$$a_c = \\frac{{{v}^2}}{{{r}}} = {ac}\\text{{ m/s}}^2.$$<br>$$\\omega = \\frac{{{v}}}{{{r}}} = {omega}\\text{{ rad/s}}.$$",
                "Option C calculates $v/r$ as acceleration instead of $v^2/r$.", diff, q_type
            )

    elif "Laws of Motion" in chapter:
        if "Newton's" in subtopic:
            m = 5 + (q_idx % 5)
            f = 20 + (q_idx % 4) * 10
            t = 2 + (q_idx % 3)
            imp = f * t
            delta_v = round(imp / m, 2)
            return (
                f"A constant force $F = {f}\\text{{ N}}$ acts on a stationary mass $m = {m}\\text{{ kg}}$ for $\\Delta t = {t}\\text{{ s}}$. The impulse imparted and resulting change in velocity are:",
                f"$\\text{{Impulse}} = {imp}\\text{{ N\\cdot s}}, \\Delta v = {delta_v}\\text{{ m/s}}$",
                [f"$\\text{{Impulse}} = {round(imp/2, 1)}\\text{{ N\\cdot s}}, \\Delta v = {delta_v}\\text{{ m/s}}$", f"$\\text{{Impulse}} = {imp}\\text{{ N\\cdot s}}, \\Delta v = {imp}\\text{{ m/s}}$", f"$\\text{{Impulse}} = {f}\\text{{ N\\cdot s}}, \\Delta v = {round(f/m, 2)}\\text{{ m/s}}$"],
                "Impulse $J = F \\Delta t = \\Delta p = m \\Delta v$.",
                "Impulse-Momentum theorem in classical mechanics.",
                f"$$J = ({f}\\text{{ N}})({t}\\text{{ s}}) = {imp}\\text{{ N\\cdot s}}.$$<br>$$\\Delta v = \\frac{{{imp}}}{{{m}}} = {delta_v}\\text{{ m/s}}.$$",
                "Option B equates $\\Delta v$ directly to impulse, neglecting the mass.", diff, q_type
            )
        elif "Friction" in subtopic:
            mu_s = 0.4 if q_idx % 2 == 0 else 0.5
            return (
                f"A block rests on an inclined plane of inclination $\\theta = 30^\\circ$ ($\\tan 30^\\circ \\approx 0.577$). If $\\mu_s = {mu_s}$, which statement is physically correct?",
                f"The block accelerates down the plane because $\\tan\\theta > \\mu_s$ (inclination exceeds angle of repose)",
                ["The block remains stationary because static friction always cancels gravity", "The block accelerates up the incline due to normal reaction", "Frictional force acting on the block is strictly zero"],
                "Angle of repose $\\phi$ is defined by $\\tan\\phi = \\mu_s$.",
                "Static friction and equilibrium on inclined planes.",
                f"Since $\\tan 30^\\circ \\approx 0.577 > {mu_s}$, the downhill component of gravity exceeds maximum static friction.",
                "Option A fails to recognize that static friction has a finite upper limit $\\mu_s N$.", diff, q_type
            )
        elif "Circular Motion" in subtopic:
            r = 50 + (q_idx % 5) * 10
            v_opt = round(math.sqrt(r * 10 * math.tan(math.radians(30))), 1)
            return (
                f"A curved road of radius $R = {r}\\text{{ m}}$ is banked at $\\theta = 30^\\circ$ ($g = 10\\text{{ m/s}}^2$). The optimum speed at which a vehicle negotiates the turn with zero lateral friction is:",
                f"$v = {v_opt}\\text{{ m/s}}$",
                [f"$v = {round(v_opt * 1.5, 1)}\\text{{ m/s}}$", f"$v = {round(math.sqrt(r * 10), 1)}\\text{{ m/s}}$", f"$v = {round(v_opt / 2, 1)}\\text{{ m/s}}$"],
                "$v = \\sqrt{R g \\tan\\theta}$.",
                "Dynamics of banked roads without friction.",
                f"$$v = \\sqrt{{{r} \\times 10 \\times \\tan(30^\\circ)}} = {v_opt}\\text{{ m/s}}.$$",
                "Option B computes $\\sqrt{Rg}$, forgetting the $\\tan\\theta$ factor.", diff, q_type
            )
        else: # Pulley & Tension
            m1 = 6 + (q_idx % 4)
            m2 = 4
            a = round(((m1 - m2) / (m1 + m2)) * 10, 2)
            t = round((2 * m1 * m2 / (m1 + m2)) * 10, 1)
            return (
                f"In an ideal Atwood machine, masses $m_1 = {m1}\\text{{ kg}}$ and $m_2 = {m2}\\text{{ kg}}$ hang over a massless frictionless pulley ($g = 10\\text{{ m/s}}^2$). System acceleration $a$ and string tension $T$ are:",
                f"$a = {a}\\text{{ m/s}}^2, T = {t}\\text{{ N}}$",
                [f"$a = {a*2}\\text{{ m/s}}^2, T = {t}\\text{{ N}}$", f"$a = {a}\\text{{ m/s}}^2, T = {round(t/2, 1)}\\text{{ N}}$", f"$a = 0\\text{{ m/s}}^2, T = {(m1+m2)*10}\\text{{ N}}$"],
                "$a = \\frac{m_1 - m_2}{m_1 + m_2}g$ and $T = \\frac{2m_1 m_2}{m_1 + m_2}g$.",
                "Newton's second law applied to interconnected constraint systems.",
                f"$$a = \\frac{{{m1 - m2}}}{{{m1 + m2}}} \\times 10 = {a}\\text{{ m/s}}^2.$$<br>$$T = \\frac{{2 \\times {m1} \\times {m2}}}{{{m1 + m2}}} \\times 10 = {t}\\text{{ N}}.$$",
                "Option B computes $T = \\frac{m_1 m_2}{m_1 + m_2}g$, forgetting the factor of 2.", diff, q_type
            )

    elif "Work Energy and Power" in chapter:
        if "Work-Energy" in subtopic:
            m = 2 + (q_idx % 4)
            v1 = 4 + (q_idx % 3) * 2
            v2 = v1 + 6
            w = 0.5 * m * (v2**2 - v1**2)
            return (
                f"A body of mass $m = {m}\\text{{ kg}}$ accelerates from $v_1 = {v1}\\text{{ m/s}}$ to $v_2 = {v2}\\text{{ m/s}}$. The net work done by all forces on the body is:",
                f"$W = {w}\\text{{ J}}$",
                [f"$W = {w * 2}\\text{{ J}}$", f"$W = {0.5 * m * (v2 - v1)**2}\\text{{ J}}$", f"$W = {round(w / 2, 1)}\\text{{ J}}$"],
                "Work-Energy Theorem: $W_{\\text{net}} = \\Delta K = \\frac{1}{2}m(v_2^2 - v_1^2)$.",
                "Equivalence between work done and kinetic energy variation.",
                f"$$W = \\frac{{1}}{{2}}({m})({v2}^2 - {v1}^2) = {w}\\text{{ J}}.$$",
                "Option B mistakenly calculates $\\frac{1}{2}m(v_2 - v_1)^2$.", diff, q_type
            )
        elif "Conservative" in subtopic:
            k = 100 + (q_idx % 4) * 100
            x = 0.1 + (q_idx % 3) * 0.05
            u = round(0.5 * k * x**2, 2)
            return (
                f"A spring of constant $k = {k}\\text{{ N/m}}$ is compressed by $x = {int(x*100)}\\text{{ cm}}$ from its natural length. The elastic potential energy stored in the spring is:",
                f"$U = {u}\\text{{ J}}$",
                [f"$U = {u*2}\\text{{ J}}$", f"$U = {round(k*x, 2)}\\text{{ J}}$", f"$U = {round(u/2, 2)}\\text{{ J}}$"],
                "$U = \\frac{1}{2}kx^2$. Convert compression $x$ to meters.",
                "Conservative potential energy of an ideal Hookean spring.",
                f"$$U = \\frac{{1}}{{2}}({k})({x}^2) = {u}\\text{{ J}}.$$",
                "Option B computes restoring force $kx$ instead of potential energy $\\frac{1}{2}kx^2$.", diff, q_type
            )
        elif "Power" in subtopic:
            p_in = 1000 + (q_idx % 5) * 500
            eta = 80
            m = 200
            h = 10
            p_out = p_in * (eta / 100)
            t = round((m * 10 * h) / p_out, 1)
            return (
                f"An electric water pump of rated power $P_{{\\text{{in}}}} = {p_in}\\text{{ W}}$ operates at $\\eta = {eta}\\%$ efficiency. How much time will it take to lift ${m}\\text{{ kg}}$ of water to height $h = {h}\\text{{ m}}$ ($g = 10\\text{{ m/s}}^2$)?",
                f"$t = {t}\\text{{ s}}$",
                [f"$t = {round((m * 10 * h) / p_in, 1)}\\text{{ s}}$", f"$t = {round(t * 1.5, 1)}\\text{{ s}}$", f"$t = {round(t / 2, 1)}\\text{{ s}}$"],
                "Useful power $P_{\\text{out}} = \\eta P_{\\text{in}} = \\frac{mgh}{t}$.",
                "Power, mechanical efficiency and gravitational potential work.",
                f"$$P_{{\\text{{out}}}} = {p_in} \\times 0.8 = {p_out}\\text{{ W}}.$$<br>$$t = \\frac{{{m*10*h}}}{{{p_out}}} = {t}\\text{{ s}}.$$",
                "Option A calculates time assuming $100\\%$ efficiency, ignoring power loss.", diff, q_type
            )
        else: # Elastic & Inelastic Collisions
            m1 = 2
            m2 = 3
            u1 = 10
            v_com = round((m1 * u1) / (m1 + m2), 2)
            loss = round(0.5 * (m1 * m2 / (m1 + m2)) * u1**2, 1)
            return (
                f"A body of mass $m_1 = {m1}\\text{{ kg}}$ moving at $u_1 = {u1}\\text{{ m/s}}$ undergoes a perfectly inelastic head-on collision with stationary mass $m_2 = {m2}\\text{{ kg}}$. Common speed $v$ and kinetic energy loss $\\Delta K$ are:",
                f"$v = {v_com}\\text{{ m/s}}, \\Delta K = {loss}\\text{{ J}}$",
                [f"$v = {round(u1/2, 2)}\\text{{ m/s}}, \\Delta K = {loss}\\text{{ J}}$", f"$v = {v_com}\\text{{ m/s}}, \\Delta K = 0\\text{{ J}}$", f"$v = {round(v_com*1.5, 2)}\\text{{ m/s}}, \\Delta K = {loss*2}\\text{{ J}}$"],
                "Linear momentum is conserved: $m_1 u_1 = (m_1 + m_2)v$. Kinetic energy loss $\\Delta K = \\frac{1}{2}\\frac{m_1 m_2}{m_1+m_2}u_1^2$.",
                "Conservation of momentum and maximal energy dissipation in inelastic collisions.",
                f"$$v = \\frac{{{m1} \\times {u1}}}{{{m1 + m2}}} = {v_com}\\text{{ m/s}}.$$<br>$$\\Delta K = \\frac{{1}}{{2}} \\left(\\frac{{{m1} \\times {m2}}}{{{m1 + m2}}}\\right)({u1}^2) = {loss}\\text{{ J}}.$$",
                "Option B asserts $\\Delta K = 0$, which is only true for perfectly elastic collisions.", diff, q_type
            )

    elif "Rotational Motion" in chapter:
        if "Center of Mass" in subtopic:
            bodies = [
                ("uniform semicircular wire of radius $R$", "$\\frac{2R}{\\pi}$ along axis of symmetry", ["$\\frac{4R}{3\\pi}$", "$\\frac{R}{2}$", "$\\frac{3R}{8}$"]),
                ("uniform semicircular disc of radius $R$", "$\\frac{4R}{3\\pi}$ along axis of symmetry", ["$\\frac{2R}{\\pi}$", "$\\frac{R}{\\pi}$", "$\\frac{3R}{4}$"]),
                ("uniform solid hemisphere of radius $R$", "$\\frac{3R}{8}$ from flat base", ["$\\frac{R}{2}$", "$\\frac{4R}{3\\pi}$", "$\\frac{R}{4}$"]),
                ("uniform hollow hemisphere of radius $R$", "$\\frac{R}{2}$ from flat base", ["$\\frac{3R}{8}$", "$\\frac{2R}{\\pi}$", "$\\frac{R}{3}$"])
            ]
            item = bodies[q_idx % len(bodies)]
            return (
                f"The center of mass of a {item[0]} is located at a distance of:",
                item[1], item[2], "Recall integral standard values for symmetric geometries.",
                "Determination of center of mass for continuous laminar and volumetric bodies.",
                f"By integration $\\int y dm / M$, the center of mass of {item[0]} is {item[1]}.",
                "Common trap is confusing the circular ring ($2R/\\pi$) with circular disc ($4R/3\\pi$) or hemisphere ($3R/8$).", diff, q_type
            )
        elif "Moment of Inertia" in subtopic:
            m = 2 + (q_idx % 3)
            r = 0.5
            return (
                f"A uniform circular disc has mass $M = {m}\\text{{ kg}}$ and radius $R = {r}\\text{{ m}}$. Its moment of inertia about a tangent in the plane of the disc is:",
                f"$I = \\frac{{5}}{{4}} M R^2 = {round(1.25 * m * r**2, 3)}\\text{{ kg\\cdot m}}^2$",
                [f"$I = \\frac{{1}}{{2}} M R^2 = {round(0.5 * m * r**2, 3)}\\text{{ kg\\cdot m}}^2$", f"$I = \\frac{{3}}{{2}} M R^2 = {round(1.5 * m * r**2, 3)}\\text{{ kg\\cdot m}}^2$", f"$I = \\frac{{7}}{{5}} M R^2 = {round(1.4 * m * r**2, 3)}\\text{{ kg\\cdot m}}^2$"],
                "Parallel Axis Theorem: $I = I_{\\text{diam}} + M R^2 = \\frac{1}{4}MR^2 + MR^2 = \\frac{5}{4}MR^2$.",
                "Theorem of parallel and perpendicular axes for planar rigid bodies.",
                f"$$I = \\frac{{1}}{{4}}MR^2 + MR^2 = \\frac{{5}}{{4}}MR^2 = {round(1.25*m*r**2, 3)}\\text{{ kg\\cdot m}}^2.$$",
                "Option B uses $I = \\frac{3}{2}MR^2$, which is perpendicular to the plane of the disc.", diff, q_type
            )
        elif "Torque" in subtopic:
            return (
                "A child rotates on a turntable with arms outstretched ($\\omega_1$). When folding his arms, moment of inertia halves ($I_2 = I_1 / 2$). What happens to $\\omega_2$ and rotational kinetic energy $K$?",
                "$\\omega_2 = 2\\omega_1$, and kinetic energy doubles ($K_2 = 2K_1$)",
                ["$\\omega_2 = \\omega_1 / 2$, and kinetic energy halves", "$\\omega_2 = 2\\omega_1$, and kinetic energy remains constant", "$\\omega_2 = \\omega_1$, and kinetic energy doubles"],
                "Net external torque $\\tau = 0$, so angular momentum $L = I\\omega$ is conserved.",
                "Conservation of angular momentum and rotational energy variations.",
                "$$L = I_1 \\omega_1 = I_2 \\omega_2 \\implies \\omega_2 = 2\\omega_1.$$ As $I$ halves while $L$ is constant, $K = L^2 / (2I)$ doubles.",
                "Option B assumes kinetic energy is conserved; internal muscular work increases energy.", diff, q_type
            )
        else: # Pure Rolling Motion
            return (
                "A solid sphere, solid cylinder, and circular ring (same mass and radius) roll down an incline from rest without slipping. The arrival sequence at the bottom is:",
                "Solid sphere first, solid cylinder second, circular ring last",
                ["Circular ring first, solid cylinder second, solid sphere last", "All three reach simultaneously because acceleration is independent of shape", "Solid cylinder first, solid sphere second, circular ring last"],
                "Acceleration in pure rolling: $a = \\frac{g\\sin\\theta}{1 + k^2/R^2}$. Smaller $k^2/R^2$ gives larger acceleration.",
                "Pure rolling dynamics and rotational inertia distribution.",
                "Sphere ($k^2/R^2 = 0.4$), cylinder ($0.5$), ring ($1.0$). Hence $a_{\\text{sphere}} > a_{\\text{cylinder}} > a_{\\text{ring}}$.",
                "Option B ignores rolling rotational inertia, treating them as point sliders.", diff, q_type
            )

    elif "Gravitation" in chapter:
        if "Kepler" in subtopic:
            r_ratio = 4 if q_idx % 2 == 0 else 9
            t_ratio = round(r_ratio ** 1.5, 1)
            return (
                f"The orbital radius of a planet around the Sun is ${r_ratio}$ times that of Earth. What is the orbital period in Earth years?",
                f"${t_ratio}\\text{{ years}}$",
                [f"${r_ratio}\\text{{ years}}$", f"${r_ratio**2}\\text{{ years}}$", f"${round(r_ratio / 2, 1)}\\text{{ years}}$"],
                "Kepler's Third Law: $T^2 \\propto R^3 \\implies T = R^{3/2}$.",
                "Harmonic law of planetary motion in central gravitational fields.",
                f"$$T = ({r_ratio})^{{3/2}} = {t_ratio}\\text{{ years}}.$$",
                "Option A assumes a linear relation $T \\propto R$.", diff, q_type
            )
        elif "Field & Potential" in subtopic:
            return (
                "Work required to lift a satellite of mass $m$ from Earth's surface (radius $R$) to altitude $h = R$ is:",
                "$W = \\frac{1}{2} m g R$",
                ["$W = m g R$", "$W = \\frac{1}{4} m g R$", "$W = 2 m g R$"],
                "$\\Delta U = \\frac{mgh}{1 + h/R}$.",
                "Gravitational potential energy in variable gravitational fields.",
                "$$W = \\frac{mgR}{1 + R/R} = \\frac{1}{2}mgR.$$",
                "Option A calculates $mgh = mgR$, which holds only near Earth's surface.", diff, q_type
            )
        elif "Escape" in subtopic:
            return (
                "If escape velocity on Earth is $v_e = 11.2\\text{ km/s}$, what is escape velocity on a planet with $4\\times$ Earth mass and $1/4\\times$ Earth radius?",
                "$v_p = 4 v_e = 44.8\\text{ km/s}$",
                ["$v_p = 2 v_e = 22.4\\text{ km/s}$", "$v_p = v_e = 11.2\\text{ km/s}$", "$v_p = 8 v_e = 89.6\\text{ km/s}$"],
                "$v_e = \\sqrt{\\frac{2GM}{R}} \\implies v_p = v_e \\sqrt{\\frac{M_p/M_e}{R_p/R_e}}$.",
                "Escape velocity dependence on planetary mass and radius.",
                "$$v_p = v_e \\sqrt{4 / (1/4)} = 4 v_e = 44.8\\text{ km/s}.$$",
                "Option A forgets the inverse dependence on radius in square root.", diff, q_type
            )
        else: # Variation of g
            return (
                "At what depth $d$ below Earth's surface does acceleration due to gravity become half of its surface value ($g_d = g/2$)?",
                "$d = \\frac{R}{2}$ (where $R$ is Earth's radius)",
                ["$d = \\frac{R}{4}$", "$d = \\frac{R}{\\sqrt{2}}$", "$d = \\frac{3R}{4}$"],
                "Variation with depth: $g_d = g(1 - d/R)$.",
                "Linear decrease of gravitational acceleration inside a solid sphere.",
                "$$\\frac{g}{2} = g(1 - d/R) \\implies d = \\frac{R}{2}.$$",
                "Option C confuses depth below surface with distance from center.", diff, q_type
            )

    elif "Mechanical Properties" in chapter:
        if "Hooke" in subtopic:
            return (
                "A steel wire is stretched under tension. The elastic potential energy stored per unit volume (energy density $u$) is:",
                "$u = \\frac{1}{2} \\times \\text{Stress} \\times \\text{Strain} = \\frac{1}{2} Y (\\text{Strain})^2$",
                ["$u = \\text{Stress} \\times \\text{Strain}$", "$u = \\frac{1}{2} Y (\\text{Strain})$", "$u = \\frac{\\text{Stress}}{\\text{Strain}}$"],
                "Energy density $u = \\frac{1}{2} \\sigma \\varepsilon$.",
                "Strain energy density in linearly elastic Hookean materials.",
                "$$u = \\frac{1}{2} (Y \\times \\text{strain}) \\times \\text{strain} = \\frac{1}{2} Y \\varepsilon^2.$$",
                "Option A forgets the factor of $1/2$ from $\\int \\sigma d\\varepsilon$.", diff, q_type
            )
        elif "Pascal" in subtopic:
            f1 = 200
            a1, a2 = 10, 500
            f2 = f1 * (a2 / a1)
            return (
                f"In a hydraulic lift, small piston area is $A_1 = {a1}\\text{{ cm}}^2$ with force $F_1 = {f1}\\text{{ N}}$. If large piston area is $A_2 = {a2}\\text{{ cm}}^2$, the supported weight is:",
                f"$F_2 = {int(f2)}\\text{{ N}}$",
                [f"$F_2 = {int(f2/2)}\\text{{ N}}$", f"$F_2 = {int(f1 * a1 / a2)}\\text{{ N}}$", f"$F_2 = {int(f2 * 2)}\\text{{ N}}$"],
                "Pascal's Law: $F_1/A_1 = F_2/A_2$.",
                "Hydraulic multiplication of force via Pascal's principle.",
                f"$$F_2 = {f1} \\times ({a2}/{a1}) = {int(f2)}\\text{{ N}}.$$",
                "Option B inverts the area ratio $A_1 / A_2$.", diff, q_type
            )
        elif "Surface Tension" in subtopic:
            return (
                "Two soap bubbles of radii $r_1 = 3\\text{ cm}$ and $r_2 = 6\\text{ cm}$ have excess pressures $\\Delta P_1$ and $\\Delta P_2$. The ratio $\\Delta P_1 : \\Delta P_2$ is:",
                "$2 : 1$",
                ["$1 : 2$", "$4 : 1$", "$1 : 4$"],
                "Excess pressure inside soap bubble: $\\Delta P = 4T/r \\propto 1/r$.",
                "Laplace's law of excess pressure across curved interfaces.",
                "$$\\frac{\\Delta P_1}{\\Delta P_2} = \\frac{r_2}{r_1} = \\frac{6}{3} = 2 : 1.$$",
                "Option A assumes excess pressure is directly proportional to radius.", diff, q_type
            )
        else: # Bernoulli's Principle & Viscosity
            return (
                "A spherical raindrop of radius $r$ falls through air of viscosity $\\eta$. Its terminal velocity $v_t$ scales with radius $r$ as:",
                "$v_t \\propto r^2$",
                ["$v_t \\propto r$", "$v_t \\propto r^3$", "$v_t \\propto 1/r$"],
                "Stokes' Law: $v_t = \\frac{2r^2(\\rho - \\sigma)g}{9\\eta}$.",
                "Terminal velocity equilibrium under viscous drag and buoyancy.",
                "Balancing weight against viscous drag yields $v_t \\propto r^2$.",
                "Option A forgets that weight scales with volume ($r^3$).", diff, q_type
            )

    elif "Thermal Properties of Matter and KTG" in chapter:
        if "Thermal Expansion" in subtopic:
            return (
                "A metal rod of length $L_0 = 1.0\\text{ m}$ with coefficient of linear expansion $\\alpha = 2.0 \\times 10^{-5}\\text{ K}^{-1}$ is heated through $\\Delta T = 50^\\circ\\text{C}$. The increase in length $\\Delta L$ is:",
                "$\\Delta L = 1.0\\text{ mm} = 1.0 \\times 10^{-3}\\text{ m}$",
                ["$\\Delta L = 0.1\\text{ mm}$", "$\\Delta L = 2.0\\text{ mm}$", "$\\Delta L = 5.0\\text{ mm}$"],
                "Thermal expansion: $\\Delta L = L_0 \\alpha \\Delta T$.",
                "Linear thermal expansion in solid conductors.",
                "$$\\Delta L = (1.0)(2.0 \\times 10^{-5})(50) = 100 \\times 10^{-5}\\text{ m} = 1.0 \\times 10^{-3}\\text{ m} = 1.0\\text{ mm}.$$",
                "Option B forgets the factor of 50 temperature increase.", diff, q_type
            )
        elif "Heat Transfer" in subtopic:
            return (
                "A hot liquid cools from $80^\\circ\\text{C}$ to $70^\\circ\\text{C}$ in $5\\text{ minutes}$ in an ambient room at $30^\\circ\\text{C}$. The time taken to cool from $70^\\circ\\text{C}$ to $60^\\circ\\text{C}$ in the same room will be:",
                "Greater than $5\\text{ minutes}$ (cooling rate decreases as temperature difference from surroundings decreases)",
                ["Exactly $5\\text{ minutes}$", "Less than $5\\text{ minutes}$", "Independent of ambient temperature"],
                "Newton's Law of Cooling: $\\frac{dT}{dt} = -K(T - T_0)$.",
                "Convective and radiative cooling under small temperature gradients.",
                "As the liquid cools, the temperature gradient $(T - T_0)$ decreases, slowing the rate of heat loss and requiring more time for each successive $10^\\circ\\text{C}$ interval.",
                "Option A assumes a linear constant rate of heat loss.", diff, q_type
            )
        elif "Kinetic Theory" in subtopic:
            return (
                "At absolute temperature $T$, what is the ratio of the root-mean-square speed ($v_{\\text{rms}}$) to the average speed ($v_{\\text{avg}}$) of ideal gas molecules of molar mass $M$?",
                "$\\frac{v_{\\text{rms}}}{v_{\\text{avg}}} = \\sqrt{\\frac{3\\pi}{8}} \\approx 1.086$",
                ["$\\frac{v_{\\text{rms}}}{v_{\\text{avg}}} = 1.0$", "$\\frac{v_{\\text{rms}}}{v_{\\text{avg}}} = \\sqrt{\\frac{8}{3\\pi}}$", "$\\frac{v_{\\text{rms}}}{v_{\\text{avg}}} = \\sqrt{\\frac{2}{3}}$"],
                "$v_{\\text{rms}} = \\sqrt{\\frac{3RT}{M}}$, $v_{\\text{avg}} = \\sqrt{\\frac{8RT}{\\pi M}}$.",
                "Maxwell-Boltzmann molecular speed distributions in ideal gases.",
                "$$\\frac{v_{\\text{rms}}}{v_{\\text{avg}}} = \\frac{\\sqrt{3RT/M}}{\\sqrt{8RT/(\\pi M)}} = \\sqrt{\\frac{3\\pi}{8}} \\approx 1.086.$$ Always $v_{\\text{rms}} > v_{\\text{avg}} > v_{\\text{mp}}$.",
                "Option C inverts the ratio.", diff, q_type
            )
        else: # Degrees of Freedom & Molar Heat Capacities
            return (
                "For an ideal diatomic gas with 5 active degrees of freedom at moderate temperatures, the ratio of specific heats $\\gamma = C_p / C_v$ is:",
                "$\\gamma = \\frac{7}{5} = 1.40$ ($C_v = \\frac{5}{2}R, C_p = \\frac{7}{2}R$)",
                ["$\\gamma = \\frac{5}{3} \\approx 1.67$ (monoatomic gas)", "$\\gamma = \\frac{4}{3} \\approx 1.33$ (polyatomic gas)", "$\\gamma = 1.00$"],
                "$C_v = \\frac{f}{2}R$, $C_p = \\left(\\frac{f}{2} + 1\\right)R$, $\\gamma = 1 + \\frac{2}{f}$.",
                "Equipartition of energy and molar heat capacities of gases.",
                "For diatomic gas with 3 translational + 2 rotational degrees of freedom ($f = 5$): $C_v = \\frac{5}{2}R$, $C_p = \\frac{7}{2}R \\implies \\gamma = 7/5 = 1.40$.",
                "Option A is for monoatomic gases like Helium ($f = 3$).", diff, q_type
            )

    elif "Thermodynamics" in chapter:
        if "First Law" in subtopic:
            q = 500 + (q_idx % 4) * 200
            w = 200 + (q_idx % 3) * 100
            du = q - w
            return (
                f"An ideal gas absorbs $\\Delta Q = {q}\\text{{ J}}$ of heat and does $\\Delta W = {w}\\text{{ J}}$ of work. The change in internal energy $\\Delta U$ is:",
                f"$\\Delta U = +{du}\\text{{ J}}$",
                [f"$\\Delta U = +{q + w}\\text{{ J}}$", f"$\\Delta U = -{du}\\text{{ J}}$", f"$\\Delta U = 0\\text{{ J}}$"],
                "First Law: $\\Delta Q = \\Delta U + \\Delta W \\implies \\Delta U = \\Delta Q - \\Delta W$.",
                "First law energy balance in closed thermodynamic systems.",
                f"$$\\Delta U = {q} - {w} = +{du}\\text{{ J}}.$$",
                "Option A adds work and heat, violating sign convention for work done BY the gas.", diff, q_type
            )
        elif "Isothermal" in subtopic:
            return (
                "In an adiabatic process of an ideal diatomic gas ($\\gamma = 1.4$), pressure and volume obey which fundamental thermodynamic relation?",
                "$P V^{1.4} = \\text{constant}$, and $T V^{0.4} = \\text{constant}$",
                ["$P V = \\text{constant}$", "$P / T^{1.4} = \\text{constant}$", "$P^{1.4} V = \\text{constant}$"],
                "Adiabatic equation: $P V^\\gamma = \\text{const}$ and $T V^{\\gamma - 1} = \\text{const}$.",
                "Thermodynamic equations of state for reversible adiabatic expansions.",
                "For diatomic gas $\\gamma = 7/5 = 1.4$. Hence $P V^{1.4} = \\text{const}$ and $T V^{0.4} = \\text{const}$.",
                "Option A describes an isothermal process ($T = \\text{const}$).", diff, q_type
            )
        elif "Carnot" in subtopic:
            t1 = 500 + (q_idx % 3) * 100
            t2 = 300
            eta = round((1 - t2 / t1) * 100, 1)
            d1 = f"$\\eta = {round(((t1 - t2) / t2) * 100, 1)}\\%$"
            d2 = f"$\\eta = {round((t2 / (t1 + t2)) * 100, 1)}\\%$"
            d3 = f"$\\eta = {round((t1 / (t1 + t2)) * 100, 1)}\\%$"
            return (
                f"A Carnot heat engine operates between $T_1 = {t1}\\text{{ K}}$ (source) and $T_2 = {t2}\\text{{ K}}$ (sink). Its thermal efficiency is:",
                f"$\\eta = {eta}\\%$",
                [d1, d2, d3],
                "Carnot efficiency $\\eta = 1 - \\frac{T_2}{T_1}$.",
                "Second law of thermodynamics and reversible Carnot cycle efficiency.",
                f"$$\\eta = \\left(1 - \\frac{{{t2}}}{{{t1}}}\\right) \\times 100\\% = {eta}\\%.$$",
                "Option B calculates heat rejection ratio $T_2/T_1$ instead of efficiency.", diff, q_type
            )
        elif "Second Law" in subtopic or "Entropy" in subtopic:
            return (
                "According to the Second Law of Thermodynamics and Clausius theorem, for any real irreversible cyclical process, the cyclic integral of $\\frac{dQ}{T}$ satisfies:",
                "$\\oint \\frac{dQ}{T} < 0$ (and total entropy of an isolated universe increases, $\\Delta S_{\\text{univ}} > 0$)",
                ["$\\oint \\frac{dQ}{T} > 0$", "$\\oint \\frac{dQ}{T} = 0$", "$\\Delta S_{\\text{univ}} = 0$ for all real irreversible processes"],
                "Clausius Inequality: $\\oint \\frac{dQ}{T} \\le 0$, equality holding only for reversible cycles.",
                "Entropy and irreversibility principle in thermodynamic systems.",
                "Real spontaneous processes generate internal entropy through dissipation, leading to $\\oint \\frac{dQ}{T} < 0$ and $\\Delta S_{\\text{univ}} > 0$.",
                "Option C asserts reversibility, while Option A violates the Second Law.", diff, q_type
            )
        else: # Heat Transfer & Cooling
            return (
                "A hot liquid cools from $80^\\circ\\text{C}$ to $70^\\circ\\text{C}$ in $5\\text{ minutes}$ in an ambient room at $30^\\circ\\text{C}$. The time taken to cool from $70^\\circ\\text{C}$ to $60^\\circ\\text{C}$ will be:",
                "Greater than $5\\text{ minutes}$ (cooling rate decreases as temperature difference decreases)",
                ["Exactly $5\\text{ minutes}$", "Less than $5\\text{ minutes}$", "Independent of ambient temperature"],
                "Newton's Law of Cooling: $\\frac{dT}{dt} = -k(T - T_0)$.",
                "Radiative and convective heat loss governed by temperature gradients.",
                "In the second interval, the average temperature difference ($35^\\circ\\text{C}$) is smaller than the first ($45^\\circ\\text{C}$). Slower rate requires more time.",
                "Option A assumes a constant linear rate of cooling.", diff, q_type
            )

    elif "Oscillations and Waves" in chapter:
        if "SHM" in subtopic:
            a = 0.1
            omega = 10 + (q_idx % 4) * 2
            v_max = round(omega * a, 2)
            a_max = round(omega**2 * a, 1)
            return (
                f"In Simple Harmonic Motion with amplitude $A = {a}\\text{{ m}}$ and angular frequency $\\omega = {omega}\\text{{ rad/s}}$, maximum velocity $v_{{\\max}}$ and maximum acceleration $a_{{\\max}}$ are:",
                f"$v_{{\\max}} = {v_max}\\text{{ m/s}}, a_{{\\max}} = {a_max}\\text{{ m/s}}^2$",
                [f"$v_{{\\max}} = {a_max}\\text{{ m/s}}, a_{{\\max}} = {v_max}\\text{{ m/s}}^2$", f"$v_{{\\max}} = {round(v_max/2, 2)}\\text{{ m/s}}, a_{{\\max}} = {a_max}\\text{{ m/s}}^2$", f"$v_{{\\max}} = {v_max}\\text{{ m/s}}, a_{{\\max}} = {round(omega * a, 1)}\\text{{ m/s}}^2$"],
                "$v_{\\max} = \\omega A$ and $a_{\\max} = \\omega^2 A$.",
                "Differential kinematics of simple harmonic oscillators.",
                f"$$v_{{\\max}} = {omega} \\times {a} = {v_max}\\text{{ m/s}}.$$<br>$$a_{{\\max}} = {omega}^2 \\times {a} = {a_max}\\text{{ m/s}}^2.$$",
                "Option C computes $a_{\\max} = \\omega A$ without squaring $\\omega$.", diff, q_type
            )
        elif "Simple Pendulum" in subtopic:
            return (
                "The length of a simple pendulum is increased by $44\\%$. What is the percentage increase in its time period?",
                "$20\\%$",
                ["$44\\%$", "$22\\%$", "$10\\%$"],
                "$T = 2\\pi\\sqrt{L/g} \\implies T \\propto \\sqrt{L}$. New length $L' = 1.44 L$.",
                "Oscillation dynamics of the simple gravity pendulum.",
                "$$T' = \\sqrt{1.44} T = 1.20 T \\implies 20\\%\\text{ increase}.$$",
                "Option B simply halves $44\\%$ ($22\\%$), neglecting the square root.", diff, q_type
            )
        elif "Wave Velocity" in subtopic:
            return (
                "An organ pipe closed at one end of length $L$ has fundamental $\\nu_1$. An open pipe of same length $L$ has fundamental $\\nu_2$. Ratio $\\nu_1 : \\nu_2$ is:",
                "$1 : 2$",
                ["$2 : 1$", "$1 : 4$", "$1 : 1$"],
                "Closed pipe: $\\nu_1 = v/(4L)$. Open pipe: $\\nu_2 = v/(2L)$.",
                "Standing acoustic waves and boundary conditions in pipes.",
                "$$\\frac{\\nu_1}{\\nu_2} = \\frac{v / (4L)}{v / (2L)} = \\frac{2}{4} = 1 : 2.$$",
                "Option A inverts the fundamental frequencies of open and closed pipes.", diff, q_type
            )
        else: # Doppler Effect & Resonance
            v, vs, nu = 340, 34, 500
            nu_app = round(nu * (v / (v - vs)), 1)
            return (
                f"A train emitting $\\nu = {nu}\\text{{ Hz}}$ whistle approaches a stationary observer at $v_s = {vs}\\text{{ m/s}}$ (speed of sound $v = {v}\\text{{ m/s}}$). The apparent frequency heard is:",
                f"$\\nu' = {nu_app}\\text{{ Hz}}$",
                [f"$\\nu' = {round(nu * ((v - vs) / v), 1)}\\text{{ Hz}}$", f"$\\nu' = {nu}\\text{{ Hz}}$", f"$\\nu' = {round(nu * (v / (v + vs)), 1)}\\text{{ Hz}}$"],
                "Doppler formula (source moving towards stationary observer): $\\nu' = \\nu\\frac{v}{v - v_s}$.",
                "Doppler effect for acoustic wave propagation.",
                f"$$\\nu' = {nu} \\left(\\frac{{340}}{{306}}\\right) = {nu_app}\\text{{ Hz}}.$$",
                "Option C uses $v + v_s$ in denominator, which corresponds to receding source.", diff, q_type
            )

    # =========================================================================
    # CLASS 12 PHYSICS
    # =========================================================================
    elif "Electrostatics" in chapter:
        if "Coulomb" in subtopic:
            return (
                "Two point charges $+q$ and $+4q$ are separated by distance $L$. At what position on the line joining them is net electric force on a third charge zero?",
                "At distance $L/3$ from charge $+q$",
                ["At distance $L/2$ from charge $+q$", "At distance $2L/3$ from charge $+q$", "At distance $L/4$ from charge $+q$"],
                "Equilibrium: $\\frac{kq}{x^2} = \\frac{k(4q)}{(L-x)^2} \\implies \\frac{1}{x} = \\frac{2}{L-x}$.",
                "Coulomb's law and electrostatic null points.",
                "$$\\frac{1}{x} = \\frac{2}{L-x} \\implies L - x = 2x \\implies x = \\frac{L}{3}.$$",
                "Option B places it at midpoint, ignoring the $4\\times$ charge magnitude ratio.", diff, q_type
            )
        elif "Dipole" in subtopic or "Electric Field" in subtopic:
            return (
                "An electric dipole of moment $\\vec{p}$ is placed in a uniform electric field $\\vec{E}$. The maximum torque experienced by the dipole and its potential energy at that orientation are:",
                "$\\tau_{\\max} = p E$ (at $\\theta = 90^\\circ$), and $U = 0$",
                ["$\\tau_{\\max} = 2 p E$, and $U = -pE$", "$\\tau_{\\max} = p E$, and $U = -pE$", "$\\tau_{\\max} = 0$, and $U = +pE$"],
                "Torque: $\\vec{\\tau} = \\vec{p} \\times \\vec{E} \\implies \\tau = p E \\sin\\theta$. Potential energy: $U = -p E \\cos\\theta$.",
                "Electrostatic dipole dynamics in uniform external electric fields.",
                "Maximum torque occurs at $\\theta = 90^\\circ$ where $\\sin 90^\\circ = 1$, giving $\\tau_{\\max} = p E$. At this orientation, $U = -p E \\cos 90^\\circ = 0$.",
                "Option C confuses minimum torque with maximum torque.", diff, q_type
            )
        elif "Gauss" in subtopic or "Potential" in subtopic:
            return (
                "Total electric flux through a closed spherical Gaussian surface enclosing charge $q$ is $\\Phi_0 = q / \\varepsilon_0$. If radius of sphere is doubled, the flux becomes:",
                "$\\Phi = \\Phi_0$ (remains unchanged)",
                ["$\\Phi = 2 \\Phi_0$", "$\\Phi = 4 \\Phi_0$", "$\\Phi = \\Phi_0 / 4$"],
                "Gauss's Law: $\\Phi = \\oint \\vec{E}\\cdot d\\vec{A} = q_{\\text{encl}}/\\varepsilon_0$. Independent of surface radius.",
                "Gauss's law flux invariance with respect to Gaussian boundary geometry.",
                "Flux depends exclusively on net enclosed charge, not on boundary geometry.",
                "Option B assumes flux scales with radius; Option C assumes inverse square scaling.", diff, q_type
            )
        else: # Capacitance & Dielectric Polarisation
            return (
                "A parallel plate capacitor has capacitance $C_0$. If plate separation is halved ($d' = d/2$) and dielectric $K = 4$ fills the space, new capacitance is:",
                "$C = 8 C_0$",
                ["$C = 4 C_0$", "$C = 2 C_0$", "$C = 16 C_0$"],
                "$C = \\frac{K \\varepsilon_0 A}{d'} = \\frac{4 \\varepsilon_0 A}{d / 2} = 8 C_0$.",
                "Capacitance dependence on geometry and dielectric polarization.",
                "Halving separation doubles capacitance ($2\\times$); dielectric multiplies by $4$. $2 \\times 4 = 8 C_0$.",
                "Option A forgets the factor of 2 gained from halving distance.", diff, q_type
            )

    elif "Current Electricity" in chapter:
        if "Drift" in subtopic:
            return (
                "A copper wire of resistance $R$ is stretched uniformly until its length is doubled ($L' = 2L$). What is the new resistance?",
                "$R' = 4 R$",
                ["$R' = 2 R$", "$R' = R / 2$", "$R' = 8 R$"],
                "Volume $V = A L$ is conserved. When length doubles, cross-sectional area halves ($A' = A/2$).",
                "Electrical resistance dependence on geometry and mass conservation.",
                "$$R' = \\rho \\frac{2L}{A / 2} = 4 \\rho \\frac{L}{A} = 4R.$$",
                "Option A forgets that cross-sectional area simultaneously decreases.", diff, q_type
            )
        elif "Kirchhoff" in subtopic:
            return (
                "Kirchhoff's First Rule (Junction rule $\\sum I = 0$) and Second Rule (Loop rule $\\sum \\Delta V = 0$) are based on conservation of:",
                "Electric Charge and Energy, respectively",
                ["Energy and Electric Charge, respectively", "Momentum and Energy, respectively", "Electric Charge and Angular Momentum, respectively"],
                "Junction rule: no charge accumulates at junction. Loop rule: work done in closed loop is zero.",
                "Conservation laws underlying Kirchhoff's circuit theorems.",
                "Junction rule represents charge conservation; Loop rule represents energy conservation in electrostatic fields.",
                "Option A inverts charge and energy conservation.", diff, q_type
            )
        elif "Potentiometer" in subtopic:
            return (
                "In a balanced Wheatstone bridge with arms $P = 10\\text{ }\\Omega, Q = 20\\text{ }\\Omega, R = 15\\text{ }\\Omega$, what is the resistance $S$ of the fourth arm?",
                "$S = 30\\text{ }\\Omega$",
                ["$S = 15\\text{ }\\Omega$", "$S = 25\\text{ }\\Omega$", "$S = 7.5\\text{ }\\Omega$"],
                "Bridge balance condition: $P/Q = R/S \\implies S = R(Q/P)$.",
                "Null deflection balance in Wheatstone bridge networks.",
                "$$S = 15 \\times \\left(\\frac{20}{10}\\right) = 30\\text{ }\\Omega.$$",
                "Option D inverts the ratio ($15 \\times 10/20 = 7.5\\text{ }\\Omega$).", diff, q_type
            )
        else: # Heating Effects & Power
            r1, r2 = 4, 6
            r_par = round((r1 * r2) / (r1 + r2), 2)
            return (
                f"Two resistors $R_1 = {r1}\\text{{ }}\\Omega$ and $R_2 = {r2}\\text{{ }}\\Omega$ are connected in parallel across a $12\\text{{ V}}$ battery. Total current drawn is:",
                f"$I = {round(12/r_par, 2)}\\text{{ A}}$",
                [f"$I = {round(12/(r1+r2), 2)}\\text{{ A}}$", f"$I = {round(12*(r1+r2), 1)}\\text{{ A}}$", f"$I = 1.0\\text{{ A}}$"],
                "$1/R_{\\text{eq}} = 1/R_1 + 1/R_2$ and $I = V/R_{\\text{eq}}$.",
                "Parallel circuit laws and equivalent resistance.",
                f"$$R_{{\\text{{eq}}}} = \\frac{{{r1} \\times {r2}}}{{{r1 + r2}}} = {r_par}\\text{{ }}\\Omega \\implies I = \\frac{{12}}{{{r_par}}} = {round(12/r_par, 2)}\\text{{ A}}.$$",
                "Option A uses series equivalent resistance ($R_1 + R_2$).", diff, q_type
            )

    elif "Moving Charges" in chapter:
        if "Biot" in subtopic:
            return (
                "Magnetic field at the center of a circular current loop of radius $R$ carrying current $I$ is:",
                "$B = \\frac{\\mu_0 I}{2R}$",
                ["$B = \\frac{\\mu_0 I}{2\\pi R}$", "$B = \\frac{\\mu_0 I}{4\\pi R}$", "$B = \\frac{\\mu_0 I R^2}{2}$"],
                "Biot-Savart Law integrated around circular loop gives $\\frac{\\mu_0 I}{2R}$.",
                "Magnetic field geometry of circular current loops.",
                "$$\\int dB = \\frac{\\mu_0 I}{4\\pi R^2} (2\\pi R) = \\frac{\\mu_0 I}{2R}.$$",
                "Option A is the field around an infinitely long straight wire.", diff, q_type
            )
        elif "Ampere" in subtopic or "Solenoid" in subtopic:
            return (
                "A long solenoid has $n = 500\\text{ turns/m}$ and carries a current of $I = 2.0\\text{ A}$. The magnetic field inside the central core of the solenoid is:",
                "$B = \\mu_0 n I = 4\\pi \\times 10^{-4}\\text{ T}$",
                ["$B = \\frac{\\mu_0 n I}{2} = 2\\pi \\times 10^{-4}\\text{ T}$", "$B = 0\\text{ T}$", "$B = \\mu_0 n^2 I = 2\\pi \\times 10^{-1}\\text{ T}$"],
                "Ampere's law for ideal long solenoid: $B = \\mu_0 n I$.",
                "Magnetic field inside helical solenoids.",
                "$$B = (4\\pi \\times 10^{-7}) \\times 500 \\times 2.0 = 4\\pi \\times 10^{-4}\\text{ T} \\approx 1.26\\text{ mT}.$$",
                "Option A is the magnetic field at the extreme end of a semi-infinite solenoid.", diff, q_type
            )
        elif "Lorentz" in subtopic or "Motion in Magnetic" in subtopic:
            return (
                "A proton and an $\\alpha$-particle with the same kinetic energy enter perpendicularly into uniform magnetic field $B$. Path radius ratio $r_p : r_\\alpha$ is:",
                "$1 : 1$",
                ["$1 : 2$", "$2 : 1$", "$1 : 4$"],
                "Radius $r = \\frac{\\sqrt{2mK}}{qB}$. Proton: $m, e$. Alpha: $4m, 2e$.",
                "Lorentz magnetic force and cyclotron trajectory geometry.",
                "$$r_\\alpha = \\frac{\\sqrt{2(4m)K}}{2eB} = \\frac{2\\sqrt{2mK}}{2eB} = r_p \\implies 1 : 1.$$",
                "Option A considers charge ratio without taking square root of mass.", diff, q_type
            )
        elif "Dipole" in subtopic:
            return (
                "A planar circular loop of radius $r$ carrying current $I$ has magnetic dipole moment $M$. If radius is doubled ($r' = 2r$) and current is halved ($I' = I/2$), new dipole moment is:",
                "$M' = 2 M$",
                ["$M' = M$", "$M' = 4 M$", "$M' = M / 2$"],
                "Magnetic dipole moment $M = I A = I(\\pi r^2)$.",
                "Magnetic dipole moment dependence on area and current.",
                "$$M' = (I/2)(\\pi (2r)^2) = \\frac{I}{2} (4\\pi r^2) = 2 M.$$",
                "Option A assumes radius doubling simply cancels current halving, forgetting area scales as $r^2$.", diff, q_type
            )
        else: # Galvanometer Conversion
            return (
                "A galvanometer of resistance $G = 50\\text{ }\\Omega$ gives full-scale deflection for $I_g = 10\\text{ mA}$. To convert it into an ammeter of range $0$ to $10\\text{ A}$, the required shunt resistance $S$ is:",
                "$S \\approx 0.05\\text{ }\\Omega$ connected in parallel",
                ["$S = 50\\text{ }\\Omega$ in series", "$S = 0.5\\text{ }\\Omega$ in parallel", "$S = 5\\text{ }\\Omega$ in series"],
                "Shunt formula: $S = \\frac{I_g G}{I - I_g}$. Connect in parallel.",
                "Galvanometer ammeter conversion and current division.",
                "$$S = \\frac{0.01 \\times 50}{10 - 0.01} \\approx \\frac{0.5}{10} = 0.05\\text{ }\\Omega\\text{ in parallel}.$$",
                "Option B puts resistance in series (voltmeter conversion).", diff, q_type
            )

    elif "Electromagnetic Induction" in chapter:
        if "Faraday" in subtopic:
            return (
                "A straight conductor of length $l = 1\\text{ m}$ moves with velocity $v = 10\\text{ m/s}$ perpendicular to uniform magnetic field $B = 0.5\\text{ T}$. Motional EMF induced is:",
                "$\\varepsilon = 5.0\\text{ V}$",
                ["$\\varepsilon = 10.0\\text{ V}$", "$\\varepsilon = 2.5\\text{ V}$", "$\\varepsilon = 0.5\\text{ V}$"],
                "Motional EMF $\\varepsilon = B v l$.",
                "Faraday's law of induction and motional electromotive force.",
                "$$\\varepsilon = (0.5\\text{ T})(10\\text{ m/s})(1\\text{ m}) = 5.0\\text{ V}.$$",
                "Option B forgets the $0.5$ magnetic field factor.", diff, q_type
            )
        elif "Inductance" in subtopic:
            return (
                "An inductor of inductance $L = 2\\text{ H}$ carries current $I = 4\\text{ A}$. The magnetic energy stored in the inductor is:",
                "$U = 16\\text{ J}$",
                ["$U = 8\\text{ J}$", "$U = 32\\text{ J}$", "$U = 4\\text{ J}$"],
                "Energy in inductor: $U = \\frac{1}{2} L I^2$.",
                "Magnetic field energy storage in inductive components.",
                "$$U = \\frac{1}{2} (2) (4^2) = 16\\text{ J}.$$",
                "Option A forgets the square on current ($L I$).", diff, q_type
            )
        elif "LCR" in subtopic:
            return (
                "In a series LCR resonant circuit with $L = 0.1\\text{ H}, C = 10\\text{ }\\mu\\text{F}, R = 10\\text{ }\\Omega$, resonant frequency $\\omega_0$ and impedance $Z_0$ are:",
                "$\\omega_0 = 1000\\text{ rad/s}, Z_0 = 10\\text{ }\\Omega$",
                ["$\\omega_0 = 100\\text{ rad/s}, Z_0 = 0\\text{ }\\Omega$", "$\\omega_0 = 1000\\text{ rad/s}, Z_0 = 100\\text{ }\\Omega$", "$\\omega_0 = 500\\text{ rad/s}, Z_0 = 10\\text{ }\\Omega$"],
                "Resonance: $\\omega_0 = 1/\\sqrt{LC}$ and $Z = R$.",
                "Resonance in series LCR alternating current circuits.",
                "$$\\omega_0 = \\frac{1}{\\sqrt{0.1 \\times 10^{-5}}} = 1000\\text{ rad/s}.$$ At resonance $X_L = X_C$, so $Z = R = 10\\text{ }\\Omega$.",
                "Option A assumes impedance drops to zero, forgetting resistance $R$.", diff, q_type
            )
        else: # Power in AC & Transformers
            return (
                "In an ideal step-down transformer, turns ratio $N_p/N_s = 10$. If primary voltage is $220\\text{ V}$ and primary current is $0.5\\text{ A}$, secondary voltage and current are:",
                "$V_s = 22\\text{ V}, I_s = 5.0\\text{ A}$",
                ["$V_s = 2200\\text{ V}, I_s = 0.05\\text{ A}$", "$V_s = 22\\text{ V}, I_s = 0.05\\text{ A}$", "$V_s = 110\\text{ V}, I_s = 1.0\\text{ A}$"],
                "$V_s/V_p = N_s/N_p$ and $I_s/I_p = N_p/N_s$ (power conservation $V_p I_p = V_s I_s$).",
                "Transformer turns ratios and electromagnetic mutual coupling.",
                "$$V_s = 220 / 10 = 22\\text{ V}.$$<br>$$I_s = 0.5 \\times 10 = 5.0\\text{ A}.$$",
                "Option A computes step-up instead of step-down.", diff, q_type
            )

    elif "Magnetism and Matter" in chapter:
        if "Dipole Moment" in subtopic:
            return (
                "A bar magnet of magnetic dipole moment $M = 2.0\\text{ A}\\cdot\\text{m}^2$ is placed in a uniform magnetic field $B = 0.5\\text{ T}$. What is the work done in rotating it from stable equilibrium ($\\theta = 0^\\circ$) to unstable equilibrium ($\\theta = 180^\\circ$)?",
                "$W = 2.0\\text{ J}$ ($W = 2MB$)",
                ["$W = 1.0\\text{ J}$", "$W = 0\\text{ J}$", "$W = 4.0\\text{ J}$"],
                "$W = -MB(\\cos 180^\\circ - \\cos 0^\\circ) = 2MB$.",
                "Potential energy and mechanical work in magnetic dipoles.",
                "$$W = U(180^\\circ) - U(0^\\circ) = -MB(-1) - (-MB) = 2MB = 2(2.0)(0.5) = 2.0\\text{ J}.$$",
                "Option B computes $MB$ instead of $2MB$.", diff, q_type
            )
        elif "Earth's Magnetic" in subtopic:
            return (
                "At a place on Earth where horizontal component $B_H = 0.3\\text{ G}$ and vertical component $B_V = 0.3\\sqrt{3}\\text{ G}$, what is the angle of magnetic dip ($\\delta$)?",
                "$\\delta = 60^\\circ$ (since $\\tan\\delta = \\frac{B_V}{B_H} = \\sqrt{3}$)",
                ["$\\delta = 30^\\circ$", "$\\delta = 45^\\circ$", "$\\delta = 90^\\circ$"],
                "Angle of dip: $\\tan\\delta = \\frac{B_V}{B_H}$.",
                "Terrestrial magnetism and geomagnetic field components.",
                "$$\\tan\\delta = \\frac{0.3\\sqrt{3}}{0.3} = \\sqrt{3} \\implies \\delta = 60^\\circ.$$",
                "Option A inverts numerator and denominator ($\\cot\\delta$).", diff, q_type
            )
        elif "Diamagnetism" in subtopic:
            return (
                "Which magnetic material property is characteristic of diamagnetic substances according to Curie's and Meissner's laws?",
                "Negative magnetic susceptibility ($\\chi < 0$) independent of temperature, expelling magnetic flux lines",
                ["Positive and large magnetic susceptibility ($\\chi \\gg 1$)", "Susceptibility inversely proportional to absolute temperature ($\\chi \\propto 1/T$)", "Permanent magnetic domains without external field"],
                "Diamagnets have $\\chi < 0$ and $\\mu_r < 1$; paramagnets have $\\chi > 0$ with $\\chi \\propto 1/T$.",
                "Magnetic classification and orbital diamagnetism.",
                "Diamagnetism arises from induced orbital electron currents opposing the applied magnetic field (Lenz's law). Hence $\\chi$ is negative and independent of temperature.",
                "Option B and C describe ferromagnetic materials.", diff, q_type
            )
        else: # Curie's Law, Retentivity & Hysteresis
            return (
                "For constructing permanent magnets and transformer electromagnet cores respectively, the ideal magnetic properties of materials are:",
                "Permanent magnet: High retentivity and high coercivity; Electromagnet core: High retentivity and low coercivity (e.g. soft iron)",
                ["Permanent magnet: Low retentivity and low coercivity; Electromagnet: High coercivity", "Both require zero retentivity and infinite coercivity", "Permanent magnet: Low retentivity; Electromagnet: High hysteresis loss"],
                "Electromagnets need narrow hysteresis loops (low energy dissipation) and low coercivity.",
                "Hysteresis loop parameters, remanence, and coercive force.",
                "A permanent magnet must retain strong magnetism and resist demagnetization (high retentivity, high coercivity). An electromagnet must magnetize easily and demagnetize rapidly with minimal hysteresis heat loss (low coercivity).",
                "Option A interchanges the requirements.", diff, q_type
            )

    elif "Ray Optics" in chapter:
        if "Reflection" in subtopic:
            return (
                "A ray of light traveling from a medium of refractive index $n_1 = \\sqrt{2}$ into air ($n_2 = 1.0$) undergoes total internal reflection when angle of incidence exceeds:",
                "Critical angle $\\theta_c = 45^\\circ$ (since $\\sin\\theta_c = \\frac{1}{\\sqrt{2}}$)",
                ["$\\theta_c = 30^\\circ$", "$\\theta_c = 60^\\circ$", "$\\theta_c = 90^\\circ$"],
                "Critical angle condition: $\\sin\\theta_c = \\frac{n_2}{n_1}$.",
                "Total internal reflection and optical boundary conditions.",
                "$$\\sin\\theta_c = \\frac{1}{\\sqrt{2}} \\implies \\theta_c = 45^\\circ.$$ For $i > 45^\\circ$, total internal reflection occurs.",
                "Option B corresponds to index $n = 2.0$.", diff, q_type
            )
        elif "Lens Maker" in subtopic:
            return (
                "A glass equiconvex lens of refractive index $n_g = 1.5$ has focal length $f = 20\\text{ cm}$ in air. When completely immersed in water ($n_w = 4/3$), its new focal length $f_w$ becomes:",
                "$f_w = +80\\text{ cm}$ (focal length quadruples: $f_w = 4f$)",
                ["$f_w = +40\\text{ cm}$", "$f_w = +20\\text{ cm}$", "$f_w = +10\\text{ cm}$"],
                "$\\frac{f_w}{f_a} = \\frac{n_g - 1}{\\frac{n_g}{n_w} - 1} = \\frac{1.5 - 1}{\\frac{1.5}{4/3} - 1} = \\frac{0.5}{0.125} = 4$.",
                "Lens Maker's formula and medium refractive index dependence.",
                "Immersing in water reduces relative refractive index $(n_{\\text{rel}} - 1)$ from $0.5$ to $0.125$ (a four-fold reduction), increasing focal length to $4 \\times 20 = 80\\text{ cm}$.",
                "Option A calculates a two-fold increase.", diff, q_type
            )
        elif "Prism" in subtopic:
            return (
                "A glass prism of refracting angle $A = 60^\\circ$ produces an angle of minimum deviation $\\delta_m = 30^\\circ$. The refractive index $n$ of the prism material is:",
                "$n = \\sqrt{2} \\approx 1.414$",
                ["$n = 1.500$", "$n = \\sqrt{3} \\approx 1.732$", "$n = 1.333$"],
                "Prism formula: $n = \\frac{\\sin\\left(\\frac{A + \\delta_m}{2}\\right)}{\\sin(A/2)}$.",
                "Refraction through triangular prisms and minimum deviation.",
                "$$n = \\frac{\\sin((60^\\circ + 30^\\circ)/2)}{\\sin(60^\\circ/2)} = \\frac{\\sin 45^\\circ}{\\sin 30^\\circ} = \\frac{1/\\sqrt{2}}{1/2} = \\sqrt{2} \\approx 1.414.$$",
                "Option C is refractive index of water.", diff, q_type
            )
        else: # Compound Microscope & Telescope
            return (
                "An astronomical telescope in normal adjustment has an objective lens of focal length $f_o = 100\\text{ cm}$ and an eyepiece of focal length $f_e = 5\\text{ cm}$. Its magnifying power $m$ and tube length $L$ are:",
                "$m = 20$, and $L = 105\\text{ cm}$ ($m = f_o/f_e, L = f_o + f_e$)",
                ["$m = 500$, and $L = 95\\text{ cm}$", "$m = 20$, and $L = 20\\text{ cm}$", "$m = 0.05$, and $L = 105\\text{ cm}$"],
                "Telescope normal adjustment: $m = f_o / f_e$ and $L = f_o + f_e$.",
                "Optical instruments and angular magnification in normal adjustment.",
                "$$m = \\frac{f_o}{f_e} = \\frac{100}{5} = 20.$$<br>$$L = f_o + f_e = 100 + 5 = 105\\text{ cm}.$$",
                "Option A multiplies focal lengths instead of dividing.", diff, q_type
            )

    elif "Wave Optics" in chapter:
        if "Huygens" in subtopic:
            return (
                "According to Huygens' principle, each point on a primary wavefront acts as a source of:",
                "Secondary spherical wavelets that spread out in all forward directions with the speed of light",
                ["Longitudinal particle vibrations restricted to the normal plane", "Reflected planar electromagnetic solitons", "Photons undergoing spontaneous pair creation"],
                "Huygens' construction: secondary wavelets form the new wavefront envelope.",
                "Wavefront propagation and secondary wavelet envelope construction.",
                "Every point on a wavefront acts as a secondary source of disturbance radiating spherical wavelets. The forward tangential envelope to these wavelets gives the new wavefront.",
                "Option A describes particle acoustics.", diff, q_type
            )
        elif "Young's Double Slit" in subtopic:
            return (
                "In a Young's Double Slit Experiment, the fringe width is $\\beta = 2.0\\text{ mm}$ in air. If the entire apparatus is immersed in water of refractive index $n = 4/3$, the new fringe width $\\beta'$ will be:",
                "$\\beta' = 1.5\\text{ mm}$ (since $\\beta' = \\frac{\\beta}{n} = \\frac{2.0}{4/3}$)",
                ["$\\beta' = 2.67\\text{ mm}$", "$\\beta' = 2.0\\text{ mm}$", "$\\beta' = 0.5\\text{ mm}$"],
                "Fringe width in medium: $\\beta' = \\frac{\\lambda' D}{d} = \\frac{\\lambda D}{n d} = \\frac{\\beta}{n}$.",
                "Optical path alteration and fringe spacing in dielectric media.",
                "Wavelength inside water decreases to $\\lambda' = \\lambda/n$. Consequently, fringe width decreases proportionally: $\\beta' = \\frac{2.0\\text{ mm}}{4/3} = 1.5\\text{ mm}$.",
                "Option A multiplies by $n$ instead of dividing.", diff, q_type
            )
        elif "Diffraction" in subtopic:
            return (
                "In single-slit Fraunhofer diffraction, the first minimum occurs at angle $\\theta$ satisfying:",
                "$a\\sin\\theta = \\lambda$ (where $a$ is slit width, and path difference between extremities is $\\lambda$)",
                ["$a\\sin\\theta = \\frac{\\lambda}{2}$", "$a\\sin\\theta = \\frac{3\\lambda}{2}$", "$a\\sin\\theta = 2\\lambda$"],
                "Single slit minima condition: $a\\sin\\theta = m\\lambda$ ($m = 1, 2, \\dots$).",
                "Fraunhofer diffraction at a single slit and destructive wave interference.",
                "Dividing the slit into two equal halves of width $a/2$, wavelets from corresponding points have path difference $\\frac{a}{2}\\sin\\theta = \\frac{\\lambda}{2}$, destructively interfering to form the first minimum.",
                "Option A is the condition for double-slit destructive interference, not single slit minimum.", diff, q_type
            )
        else: # Polarisation of Light & Brewster's Law
            return (
                "When unpolarized light reflects from a glass surface of refractive index $n = \\sqrt{3}$ at polarizing Brewster angle $i_p$, the angle of refraction $r$ is:",
                "$r = 30^\\circ$ (Brewster's angle $i_p = 60^\\circ$, and $i_p + r = 90^\\circ$)",
                ["$r = 60^\\circ$", "$r = 45^\\circ$", "$r = 90^\\circ$"],
                "Brewster's law: $\\tan i_p = n = \\sqrt{3} \\implies i_p = 60^\\circ$. Also $i_p + r = 90^\\circ$.",
                "Polarisation by reflection and Brewster's law.",
                "$$\\tan i_p = \\sqrt{3} \\implies i_p = 60^\\circ.$$ Since reflected and refracted rays are perpendicular, $r = 90^\\circ - 60^\\circ = 30^\\circ$.",
                "Option A confuses angle of refraction with angle of incidence.", diff, q_type
            )

    elif "Atoms and Nuclei" in chapter:
        if "Bohr Hydrogen" in subtopic:
            return (
                "In the Bohr hydrogen atom, radius of $n^{\\text{th}}$ orbit $r_n$ and total energy $E_n$ depend on principal quantum number $n$ as:",
                "$r_n \\propto n^2, E_n \\propto -\\frac{1}{n^2}$",
                ["$r_n \\propto n, E_n \\propto -\\frac{1}{n}$", "$r_n \\propto n^2, E_n \\propto -n^2$", "$r_n \\propto \\frac{1}{n^2}, E_n \\propto -\\frac{1}{n^2}$"],
                "$r_n = 0.529 n^2/Z\\text{ \\AA}$ and $E_n = -13.6 Z^2/n^2\\text{ eV}$.",
                "Bohr's quantization postulates and atomic orbits.",
                "Quantization of angular momentum $mvr = nh/(2\\pi)$ yields $r_n \\propto n^2$ and $E_n \\propto -1/n^2$.",
                "Option A assumes linear orbit scaling.", diff, q_type
            )
        elif "Nuclear Radius" in subtopic:
            return (
                "The nuclear radius $R$ of an atom with mass number $A$ scales as $R = R_0 A^{1/3}$. Therefore, nuclear matter density $\\rho$ is:",
                "Constant and independent of mass number $A$ (approximately $2.3 \\times 10^{17}\\text{ kg/m}^3$ across all elements)",
                ["Directly proportional to $A$", "Inversely proportional to $A^{1/3}$", "Directly proportional to $A^2$"],
                "Nuclear density: $\\rho = \\frac{M}{V} = \\frac{A m_N}{\\frac{4}{3}\\pi R_0^3 A} = \\frac{3 m_N}{4\\pi R_0^3} = \\text{const}$.",
                "Nuclear geometry and universal saturation of nuclear density.",
                "Because mass scales with $A$ and volume scales with $R^3 \\propto A$, the mass number cancels out, making nuclear density universally constant at $\\sim 2.3 \\times 10^{17}\\text{ kg/m}^3$.",
                "Option A assumes volume is constant.", diff, q_type
            )
        elif "Binding Energy" in subtopic:
            return (
                "According to the Binding Energy per Nucleon ($BE/A$) curve against mass number $A$, the peak maximum stability occurs around:",
                "Iron ($^{56}\\text{Fe}$), with maximum binding energy of approximately $8.75\\text{ MeV per nucleon}$",
                ["Uranium ($^{238}\\text{U}$), at $7.6\\text{ MeV/nucleon}$", "Helium ($^{4}\\text{He}$), at $2.2\\text{ MeV/nucleon}$", "Carbon ($^{12}\\text{C}$), at $12.0\\text{ MeV/nucleon}$"],
                "Maximum $BE/A \\approx 8.75\\text{ MeV}$ at $A=56$ (Fe); low $BE/A$ for very light and very heavy nuclei.",
                "Nuclear binding energy curve and energy release in fission vs fusion.",
                "Iron-56 lies at the global maximum of the nuclear stability curve. Fusion of lighter nuclei ($A < 50$) and fission of heavier nuclei ($A > 200$) both move products towards the $A \\approx 56$ peak, releasing binding energy.",
                "Option B is near the fissionable heavy end where stability decreases to $7.6\\text{ MeV}$.", diff, q_type
            )
        else: # Radioactivity Law & Fission
            return (
                "The half-life of a radioactive isotope is $T_{1/2} = 10\\text{ days}$. What fraction of the original sample remains undecayed after $30\\text{ days}$?",
                "$\\frac{1}{8} = 12.5\\%$ (after $3$ half-lives)",
                ["$\\frac{1}{4} = 25\\%$", "$\\frac{1}{16} = 6.25\\%$", "$\\frac{1}{3} = 33.3\\%$"],
                "$N = N_0(1/2)^n$ where $n = t/T_{1/2}$.",
                "Law of radioactive exponential decay and half-life intervals.",
                "$$n = \\frac{30}{10} = 3 \\implies \\frac{N}{N_0} = \\left(\\frac{1}{2}\\right)^3 = \\frac{1}{8} = 12.5\\%.$$",
                "Option A calculates for 2 half-lives.", diff, q_type
            )

    elif "Dual Nature" in chapter:
        if "Einstein" in subtopic or "Photoelectric" in subtopic:
            return (
                "In a photoelectric experiment, when frequency of incident light is doubled ($2\\nu$), maximum kinetic energy of emitted photoelectrons:",
                "More than doubles ($K_{\\max}' = 2K_{\\max} + \\phi_0$)",
                ["Exactly doubles", "Halves", "Remains unchanged"],
                "Einstein's equation: $K_{\\max} = h\\nu - \\phi_0$.",
                "Photoelectric effect and Einstein's quantum photon equation.",
                "$$K_{\\max}' = h(2\\nu) - \\phi_0 = 2(h\\nu - \\phi_0) + \\phi_0 = 2K_{\\max} + \\phi_0 > 2K_{\\max}.$$",
                "Option B assumes kinetic energy is directly proportional to frequency.", diff, q_type
            )
        elif "Work Function" in subtopic or "Stopping Potential" in subtopic:
            return (
                "A graph plotted between stopping potential ($V_0$) on the y-axis and frequency of incident radiation ($\\nu$) on the x-axis yields a straight line whose slope is:",
                "$\\frac{h}{e}$ (Planck's constant divided by electronic charge, universal across all metals)",
                ["Planck's constant $h$", "Electronic charge $e$", "Work function $\\phi_0$"],
                "Einstein's photoelectric equation: $e V_0 = h\\nu - \\phi_0 \\implies V_0 = \\left(\\frac{h}{e}\\right)\\nu - \\frac{\\phi_0}{e}$.",
                "Stopping potential vs frequency characteristics and determination of $h/e$.",
                "The slope of the $V_0$ vs $\\nu$ graph is $\\frac{h}{e}$, which depends only on universal physical constants and is strictly independent of the metal photosensitive target.",
                "Option A forgets the electronic charge $e$ in the denominator.", diff, q_type
            )
        elif "De Broglie" in subtopic:
            return (
                "The de Broglie wavelength of an electron accelerated from rest across potential difference $V = 100\\text{ V}$ is:",
                "$\\lambda = 0.123\\text{ nm} = 1.23\\text{ \\AA}$",
                ["$\\lambda = 1.23\\text{ nm}$", "$\\lambda = 0.0123\\text{ nm}$", "$\\lambda = 12.3\\text{ \\AA}$"],
                "$\\lambda = \\frac{1.227}{\\sqrt{V}}\\text{ nm}$.",
                "Wave-particle duality and de Broglie electron wavelength.",
                "$$\\lambda = \\frac{1.227}{\\sqrt{100}} = \\frac{1.227}{10} = 0.1227\\text{ nm} \\approx 1.23\\text{ \\AA}.$$",
                "Option A forgets the square root of $100$.", diff, q_type
            )
        else: # Davisson-Germer Experiment Significance
            return (
                "The historic Davisson-Germer electron scattering experiment provided the first direct experimental verification of:",
                "The wave nature of moving electrons through constructive Bragg diffraction from nickel crystal lattices",
                ["The particulate photon hypothesis of radiation", "Quantization of atomic orbital angular momentum", "The existence of positive atomic nuclei"],
                "Davisson and Germer observed a sharp diffraction peak for $54\\text{ V}$ electrons at scattering angle $\\theta = 50^\\circ$.",
                "Electron wave diffraction and experimental proof of de Broglie hypothesis.",
                "The measured electron de Broglie wavelength ($1.65\\text{ \\AA}$) matched the crystal diffraction spacing using Bragg's law ($1.67\\text{ \\AA}$), confirming that electrons exhibit wave properties.",
                "Option A was verified by the Compton and photoelectric effects.", diff, q_type
            )
    else: # Semiconductor Electronics
        if "Intrinsic" in subtopic:
            return (
                "To produce an n-type semiconductor from pure silicon crystal, it must be doped with pentavalent impurity atoms such as:",
                "Phosphorus (P) or Arsenic (As), providing excess conduction electrons",
                ["Boron (B) or Aluminum (Al)", "Indium (In) or Gallium (Ga)", "Carbon (C) or Germanium (Ge)"],
                "Pentavalent dopants (Group 15) donate free electrons (n-type); Trivalent dopants (Group 13) create holes (p-type).",
                "Extrinsic semiconductor doping and majority charge carriers.",
                "Group 15 atoms have 5 valence electrons. Four form covalent bonds with silicon; the fifth electron is loosely bound and enters conduction band.",
                "Option A and B are trivalent dopants producing p-type semiconductors.", diff, q_type
            )
        elif "Rectifier" in subtopic:
            return (
                "In a full-wave bridge rectifier supplied with $50\\text{ Hz}$ AC mains input, what is the fundamental ripple frequency of the output DC?",
                "$100\\text{ Hz}$ (output ripple frequency $= 2 \\times f_{\\text{in}}$)",
                ["$50\\text{ Hz}$", "$25\\text{ Hz}$", "$200\\text{ Hz}$"],
                "Full-wave rectifies both positive and negative half-cycles: $f_{\\text{out}} = 2 f_{\\text{in}}$.",
                "p-n junction diodes in AC to DC rectification circuits.",
                "Both half-cycles are converted to unidirectional pulses in the same direction, doubling the frequency of output pulses to $2 \\times 50 = 100\\text{ Hz}$.",
                "Option A ($50\\text{ Hz}$) is the ripple frequency of a HALF-wave rectifier.", diff, q_type
            )
        elif "Zener" in subtopic:
            return (
                "A Zener diode is operated in which bias configuration to function as a constant DC voltage regulator?",
                "Reverse breakdown region with reverse bias voltage exceeding breakdown voltage $V_Z$",
                ["Forward bias region with forward current exceeding threshold", "Zero bias equilibrium condition", "Reverse bias with voltage strictly below breakdown"],
                "Zener diode maintains constant voltage across its terminals in reverse breakdown.",
                "Zener breakdown mechanisms and voltage stabilization.",
                "In reverse breakdown, current changes dramatically while voltage across the Zener diode remains virtually constant at $V_Z$.",
                "Option A uses forward bias, where it behaves like a standard diode with $0.7\\text{ V}$ drop.", diff, q_type
            )
        else: # Logic Gates
            return (
                "Which digital logic gate produces an output of $0$ ONLY when both inputs $A$ and $B$ are $1$ (NAND function)?",
                "NAND gate ($Y = \\overline{A \\cdot B}$)",
                ["NOR gate ($Y = \\overline{A + B}$)", "AND gate ($Y = A \\cdot B$)", "XOR gate ($Y = A \\oplus B$)"],
                "Truth table for NAND: $1$ for $(0,0), (0,1), (1,0)$, and $0$ for $(1,1)$.",
                "Universal digital logic gates and Boolean truth tables.",
                "NAND is the negation of AND. An AND gate outputs $1$ only when both are $1$; thus NAND outputs $0$ only when both inputs are $1$.",
                "Option A (NOR gate) outputs $1$ only when both inputs are $0$.", diff, q_type
            )
