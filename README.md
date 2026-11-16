# Prepwise — Dynamic NEET-UG Command Center & 5.64 Lakh Master Question Bank

An offline-first, production-grade NEET-UG practice, testing, and cognitive diagnostic platform powered by IndexedDB (Dexie.js), real-time stopwatch pacing, official NTA CBT examination hall simulation, Timed Endless Marathon Practice Mode, and an End-to-End In-Detailed Growth Board.

---

## 🚀 Quick Start

### Option 1: Direct Run (No Setup Needed)
Simply **double-click** `index.html` in your file explorer to open it in Chrome, Edge, Brave, or Firefox.
- **Pre-loaded with 564,000 authentic master questions (5.64 Lakh Qs)** across all 81 NCERT chapters for Class 11 and Class 12 (Physics, Chemistry, Botany, and Zoology) and 705 micro-subtopics.
- **Fast 50ms Initial Boot**: Instant launch with 24,675 core starter pack, dynamic zero-CORS chapter shard loading, and 1-click vault caching.
- **100% Offline-Ready & Zero-CORS**: Runs natively over `file:///` without browser security/CORS errors or network dependencies.

### Option 2: Run with a Local Web Server
If you prefer running via `localhost`:
```bash
# Python
python -m http.server 8000
# Open http://localhost:8000 in your browser
```

---

## 🛠️ Complete Feature Architecture

1. **5.64 Lakh (564,000+) Authentic Master Question Bank**:
   - Spans all 81 official NCERT NEET chapters (Physics 24, Chemistry 22, Botany 20, Zoology 15) and 705 granular subtopics (800 questions per subtopic).
   - Complete coverage including latest NTA 2024 additions: *Principles of Practical Chemistry*, *Experimental Physics*, *p-Block Group 13 & 14*, *Transport in Plants*, *Mineral Nutrition*, *Digestion & Absorption*, and *Animal Husbandry*.
   - 5 NEET question archetypes: Standard Single-Choice MCQs, Assertion-Reason, Statement I/II Evaluations, Matrix Matching, and Ratio Scaling.
   - 100% mathematically balanced keys (A: 25.1%, B: 24.9%, C: 25.0%, D: 25.0%) with 4 unique, plausible options per question.

2. **Timed Endless Marathon Practice Mode**:
   - Practice unlimited questions within a custom countdown timer (15m, 30m, 45m, 60m, 90m, 120m, or any custom minutes).
   - Multi-topic selector: select multiple chapters simultaneously across Physics, Chemistry, Botany, and Zoology with instant subject filter chips.
   - 4 Difficulty Modes: Easy, Medium, Hard, and Random (pulls mixed difficulty dynamically).
   - Live pacing speedometer and countdown timer with visual warning pulses in the final 5 minutes.
   - End-of-session comprehensive scorecard modal with accuracy, pacing, net marks, and streak tracking.

3. **In-Detailed Growth Board**:
   - Top KPI cards: Total Attempted Questions (all-time, today, this week), Accuracy Rate %, Net Score (+4/-1), Average Time per Question, Marks Lost to Negative Marking, Projected AIR & Score with Government Medical College (GMC) tier qualification predictor.
   - Subject-wise Pacing Breakdown (Physics, Chemistry, Botany, Zoology) showing average seconds per question against the 60s benchmark.
   - 4-Quadrant Cognitive Radar: Categorizes attempts into True Mastery, Needs Speed, Careless Traps, and Time Wasters.
   - 81-Chapter Curriculum Mastery Table: Real-time table displaying attempted count, accuracy %, marks bled, mastery badges, and 1-click Direct Drill buttons for each chapter.
   - Error Root-Cause Diagnostics: Categorizes mistakes into Silly Misread, Formula Forgotten, Calculation Error, NCERT Line Missed, and Concept Gap.
   - Complete Practice Session History Timeline.

4. **Difficulty-Calibrated Progressive Hints & Adaptive Solution Flow**:
   - **Easy**: 1 Core Principle Clue.
   - **Medium**: 2 Hints (Principle Clue + Formula Relation).
   - **Hard**: 3 Progressive Hints (Principle + Formula + Common Exam Trap Alert).
   - **If Correct**: Instant full 3-part NCERT derivation (Core Principle + Step-by-Step + Distractor Analysis).
   - **If Wrong**: Negative mark bleed warning (-1 mark) + diagnostic trap explanation + progressive hint review + on-demand full derivation button.

5. **Official NTA CBT Examination Hall**:
   - 5 National Full Mocks (720 Marks, 200 Questions, 200 Minutes).
   - Section A (35 mandatory questions) & Section B (15 questions with NTA 10-attempt cap).
   - Live pacing monitor (identifies whether pace is `<60s` or `>90s`).
   - Color-coded question palette (Answered, Marked for Review, Visited, Not Visited).
   - AIR percentile projection calibrated against NEET results.

6. **Informative Tooltips (Hover Titles)**:
   - Every KPI card, navigation button, exam hall control, palette legend, Section A/B indicator, and difficulty radio button has informative hover tooltips explaining its exact function and exam relevance.

---

## 📁 Modular Clean Architecture

```
practime/
├── index.html                   # Semantic markup with Timed Marathon & Growth Board views
├── styles.css                   # Responsive tokens, NTA CBT layouts, Growth Board & Marathon styles
├── js/
│   ├── db.js                    # Dexie IndexedDB schemas, dynamic sharding & 564k vault caching
│   ├── engine.js                # CBT exam engine, stopwatch, progressive hints & endless marathon runner
│   ├── mocks.js                 # 5 National Full Mocks, Subject Sprints & custom mock builder
│   ├── analytics.js             # Growth Board controller, 81-chapter mastery table & mistake vault
│   └── app.js                   # Main application router, Timed Marathon modal & event listeners
├── data/
│   ├── seed_pack.js             # 24,675 starter questions for instant 50ms offline boot
│   ├── hierarchy_meta.json      # Pre-computed syllabus tree (81 chapters, 705 subtopics, 564,000 Qs)
│   ├── seed_meta.js             # Zero-CORS companion hierarchy metadata
│   ├── manifest.json            # 81 chapter shard registry
│   └── chapters/                # 81 chapter JSONs and 81 zero-CORS JS packs (564,000 Qs total)
├── scripts/                     # 15-Gate verification audit & 81-chapter generator suite
├── vercel.json                  # Vercel deployment cache config
├── netlify.toml                 # Netlify deployment cache config
└── .gitignore                   # Clean deployment exclusion rules
```
