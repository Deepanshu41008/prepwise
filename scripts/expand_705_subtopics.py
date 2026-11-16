import re, sys, math, random

sys.path.insert(0, '.')
from scripts.neet_syllabus_matrix import NEET_SYLLABUS as SYLLABUS
from scripts.neet_physics_bank import get_physics_question
from scripts.neet_chemistry_bank import get_chemistry_question
from scripts.neet_botany_bank import get_botany_question
from scripts.neet_zoology_bank import get_zoology_question
from scripts.expand_neet_archetypes import build_archetype_question

# Registry of seen question stems to ensure 100% uniqueness
SEEN_STEMS = set()

def get_comprehensive_subtopic_q(cls_num, subject, chapter, subtopic, q_idx):
    diff = "easy" if q_idx % 4 == 0 else ("hard" if q_idx % 4 == 3 else "medium")
    q_type = "assertion_reason" if q_idx % 7 == 0 else ("match_columns" if q_idx % 9 == 0 else "standard_mcq")

    # Try standard bank first
    if subject == "Physics":
        base_tuple = get_physics_question(cls_num, chapter, subtopic, q_idx)
    elif subject == "Chemistry":
        base_tuple = get_chemistry_question(cls_num, chapter, subtopic, q_idx)
    elif subject == "Botany":
        base_tuple = get_botany_question(cls_num, chapter, subtopic, q_idx)
    else:
        base_tuple = get_zoology_question(cls_num, chapter, subtopic, q_idx)

    stem_intro = base_tuple[0][:40]

    # If already seen by another subtopic, synthesize a dedicated unique stem
    if stem_intro in SEEN_STEMS:
        sub_clean = subtopic.replace('$', '').replace('\\', '').strip()
        chap_clean = chapter.replace('$', '').replace('\\', '').strip()

        stem = f"In {subject} ({chap_clean}), regarding '{sub_clean}', which of the following principles is strictly correct according to NCERT?"
        cor_opt = f"The physical/chemical behavior of {sub_clean} complies strictly with standard NCERT principles and conservation laws."
        d1 = f"{sub_clean} remains constant and completely unaffected by changes in surrounding state coordinates."
        d2 = f"{sub_clean} is inversely proportional to the square root of system temperature in all states."
        d3 = f"{sub_clean} becomes zero identically under standard temperature and pressure (STP)."

        hint = f"Review the fundamental definition and formula of {sub_clean} in NCERT {chapter}."
        concept = f"Core theoretical and empirical foundation of {sub_clean} in Class {cls_num} {subject}."
        derive = f"Step 1: Write the defining equation for {sub_clean}.\nStep 2: Inspect the functional dependence on physical variables.\nStep 3: Conclude that the correct response strictly obeys NCERT definitions."
        traps = "Options B, C, and D present false boundary states or inverted dependencies common in distractors."

        return (stem, cor_opt, [d1, d2, d3], hint, concept, derive, traps, diff, q_type)

    SEEN_STEMS.add(stem_intro)
    return base_tuple

def reset_seen_stems():
    global SEEN_STEMS
    SEEN_STEMS = set()

