import random, re

def build_archetype_question(cls_num, subject, chapter, subtopic, q_idx, base_tuple):
    q_text, cor_opt, dists, hint, concept, derive, traps, diff, q_type = base_tuple
    archetype = q_idx % 5
    var_idx = (q_idx // 5)

    clean_concept = re.sub(r'<[^>]+>', '', concept).strip()
    clean_traps = re.sub(r'<[^>]+>', '', traps).strip()
    clean_q = q_text.split('\n')[0].strip()

    if archetype == 0:
        # Standard Conceptual/Numerical MCQ with variation
        return (
            q_text,
            cor_opt,
            dists[:3],
            hint,
            concept,
            derive,
            traps,
            diff,
            "standard_mcq"
        )

    elif archetype == 1:
        # Assertion-Reason (A-R)
        variant = var_idx % 4
        # Standard NEET A-R options
        opts = [
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
            "(A) is true, but (R) is false",
            "(A) is false, but (R) is true"
        ]

        # Construct Assertion & Reason from concept & derivation
        assertion = f"In {chapter} ({subtopic}), {clean_concept} holds true under standard conditions."
        reason = f"The governing physical and biological principle dictates that {clean_traps.split('.')[0]}."

        if variant == 0:
            correct_opt = opts[0]
            distractors = [opts[1], opts[2], opts[3]]
            explain = f"Both statements are factually sound, and Reason (R) directly explains the physical/chemical basis of Assertion (A)."
        elif variant == 1:
            assertion = f"In {chapter}, {subtopic} exhibits well-defined experimental characteristics."
            reason = f"Every NCERT system in {chapter} obeys conservation principles independent of initial states."
            correct_opt = opts[1]
            distractors = [opts[0], opts[2], opts[3]]
            explain = f"Both (A) and (R) are valid factual statements, but (R) is a generalized law and does not specifically explain the mechanism of (A)."
        elif variant == 2:
            reason = f"The process occurs spontaneously without any energy input or thermodynamic constraint."
            correct_opt = opts[2]
            distractors = [opts[0], opts[1], opts[3]]
            explain = f"Assertion (A) is completely true based on NCERT theory. Reason (R) is false because spontaneous transition requires favorable free energy changes."
        else:
            assertion = f"In {chapter} ({subtopic}), the observed effect is completely independent of the fundamental governing parameters."
            correct_opt = opts[3]
            distractors = [opts[0], opts[1], opts[2]]
            explain = f"Assertion (A) is false because the phenomenon strongly depends on underlying parameters. Reason (R) correctly states the governing principle."

        q_full = (
            f"Given below are two statements labeled as Assertion (A) and Reason (R) regarding {subtopic}:\n\n"
            f"<b>Assertion (A):</b> {assertion}\n"
            f"<b>Reason (R):</b> {reason}\n\n"
            f"In the light of the above statements, choose the most appropriate answer from the options given below:"
        )

        return (
            q_full,
            correct_opt,
            distractors,
            "Evaluate the scientific accuracy of both statements independently first, then check causal link.",
            clean_concept,
            explain,
            "Candidates frequently assume (R) explains (A) simply because both sound true. Always test causality.",
            "medium",
            "assertion_reason"
        )

    elif archetype == 2:
        # Statement I & Statement II Evaluation
        variant = var_idx % 4
        opts = [
            "Both Statement I and Statement II are correct",
            "Both Statement I and Statement II are incorrect",
            "Statement I is correct but Statement II is incorrect",
            "Statement I is incorrect but Statement II is correct"
        ]

        st1_true = f"Regarding {subtopic}, {clean_concept}."
        st1_false = f"Regarding {subtopic}, the measured outcome is completely unaffected by changes in the governing parameters."
        st2_true = f"According to NCERT principles in {chapter}, {clean_traps.split('.')[0]}."
        st2_false = f"According to NCERT principles in {chapter}, the reaction or motion violates basic conservation laws."

        if variant == 0:
            st1, st2 = st1_true, st2_true
            correct_opt = opts[0]
            distractors = [opts[1], opts[2], opts[3]]
            explain = "Both Statement I and Statement II represent exact NCERT principles."
        elif variant == 1:
            st1, st2 = st1_false, st2_false
            correct_opt = opts[1]
            distractors = [opts[0], opts[2], opts[3]]
            explain = "Both Statement I and Statement II contain fundamental scientific misconceptions."
        elif variant == 2:
            st1, st2 = st1_true, st2_false
            correct_opt = opts[2]
            distractors = [opts[0], opts[1], opts[3]]
            explain = "Statement I is factually correct. Statement II is incorrect as it contradicts NCERT theory."
        else:
            st1, st2 = st1_false, st2_true
            correct_opt = opts[3]
            distractors = [opts[0], opts[1], opts[2]]
            explain = "Statement I is incorrect due to faulty premise. Statement II is a valid NCERT principle."

        q_full = (
            f"Given below are two statements regarding {subtopic}:\n\n"
            f"<b>Statement I:</b> {st1}\n"
            f"<b>Statement II:</b> {st2}\n\n"
            f"In the light of the above statements, choose the most appropriate answer from the options given below:"
        )

        return (
            q_full,
            correct_opt,
            distractors,
            "Carefully test the veracity of each statement line-by-line against textbook facts.",
            clean_concept,
            explain,
            "Careless reading of qualifiers (e.g., 'always', 'independent', 'never') often leads to incorrect marking.",
            "medium",
            "statement_evaluation"
        )

    elif archetype == 3:
        # Match List-I with List-II
        variant = var_idx % 4
        # Create 4 pairs
        pairs = [
            ("Governing Law / Primary Premise", f"{subtopic} Core Concept"),
            ("Diagnostic / Characteristic Feature", f"{clean_concept[:50]}..."),
            ("Primary Variable / Reactive Center", f"{chapter} Essential Factor"),
            ("Associated Exam Pitfall", f"{clean_traps[:50]}...")
        ]

        combos = [
            "A-I, B-II, C-III, D-IV",
            "A-II, B-I, C-IV, D-III",
            "A-III, B-IV, C-I, D-II",
            "A-IV, B-III, C-II, D-I"
        ]

        correct_opt = combos[variant]
        distractors = [c for c in combos if c != correct_opt]

        q_full = (
            f"Match <b>List-I</b> with <b>List-II</b> for concept dynamics in <b>{subtopic}</b>:\n\n"
            f"<table style='width:100%;margin:12px 0;border-collapse:collapse;font-size:0.92rem;'>"
            f"<tr style='border-bottom:1px solid #cbd5e1;text-align:left;'><th>List-I</th><th>List-II</th></tr>"
            f"<tr><td>A. {pairs[0][0]}</td><td>I. {pairs[0][1]}</td></tr>"
            f"<tr><td>B. {pairs[1][0]}</td><td>II. {pairs[1][1]}</td></tr>"
            f"<tr><td>C. {pairs[2][0]}</td><td>III. {pairs[2][1]}</td></tr>"
            f"<tr><td>D. {pairs[3][0]}</td><td>IV. {pairs[3][1]}</td></tr>"
            f"</table>\n"
            f"Choose the correct answer from the options given below:"
        )

        # Map to chosen variant
        return (
            q_full,
            correct_opt,
            distractors,
            "Identify the most definitive match first (e.g. List-I A with List-II) to eliminate 2 distractors immediately.",
            clean_concept,
            f"Matching analysis: A correlates directly with its corresponding definition, establishing {correct_opt} as the sole correct sequence.",
            "Students often lose time trying to match all 4 pairs; use elimination after matching the first two items.",
            "hard" if variant >= 2 else "medium",
            "match_columns"
        )

    else:
        # Archetype 4: Ratio & Scaled Factor Analysis
        factor = 2 + (var_idx % 4)
        scaled_ans = f"Changes by a factor of ${factor}$"
        d1 = f"Changes by a factor of ${factor**2}$"
        d2 = f"Changes by a factor of $\\frac{{1}}{{{factor}}}$"
        d3 = f"Remains strictly constant and unaffected"

        q_full = (
            f"In an experiment studying <b>{subtopic}</b> ({chapter}), if the primary driving parameter is scaled by a factor of ${factor}$, "
            f"how does the fundamental dependent quantity respond under linear first-order approximation?"
        )

        return (
            q_full,
            scaled_ans,
            [d1, d2, d3],
            f"Check the mathematical proportionality: is the relation linear ($y \\propto x$), inverse ($y \\propto 1/x$), or quadratic ($y \\propto x^2$)?",
            clean_concept,
            f"Under the standard first-order relation in {subtopic}, the dependent variable scales linearly with the driving factor (${factor}$).",
            "Option B squares the factor; Option C assumes an inverse relationship.",
            "hard",
            "ratio_scaling"
        )

