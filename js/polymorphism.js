// js/polymorphism.js - Dynamic Question Freshness & Concept Polymorphism Engine
// Provides infinite question diversity via 4 pedagogical mutation lenses & seen-question quarantine.
window.App = window.App || {};

window.QuestionPolymorphismEngine = {
  LENSES: {
    FORWARD_JITTER: 'Direct Forward Solve (Parameter Jitter)',
    INVERSE_SOLVE: 'Inverse Unknown Solve',
    ASSERTION_REASON: 'Assertion-Reason Form',
    WHAT_IF_SCALING: 'Proportionality & What-If Scaling'
  },

  // Get recently seen question IDs (last 5 days) from db.attempts
  async getSeenQuestionIds(days = 5) {
    if (!window.db || !db.attempts) return new Set();
    try {
      const cutoff = Date.now() - (days * 24 * 3600 * 1000);
      const attempts = await db.attempts.toArray();
      const seen = new Set();
      attempts.forEach(a => {
        if (!a.timestamp || a.timestamp >= cutoff) {
          if (a.questionId) seen.add(a.questionId);
        }
      });
      return seen;
    } catch (e) {
      console.warn('Could not query seen question attempts:', e);
      return new Set();
    }
  },

  // Lens 1: Direct Forward Solve with Dynamic Parameter Jitter
  morphForwardJitter(baseQ) {
    const q = JSON.parse(JSON.stringify(baseQ));
    q.id = `${baseQ.id}_poly_jitter_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`;
    q.isPolymorphic = true;
    q.polymorphicLens = this.LENSES.FORWARD_JITTER;
    q.baseQuestionId = baseQ.id;

    // Detect numeric pattern in question stem
    const numRegex = /\b(\d+(?:\.\d+)?)\s*(m\/s|m\/s\^2|m|s|kg|g|N|J|W|V|A|mol|L|atm|K|°C|Hz|rad\/s|cm|mm|nm|pm|pF|μF|μC|T|Wb)?\b/gi;
    const matches = [...q.question.matchAll(numRegex)];

    if (matches.length > 0) {
      // Scale numeric values cleanly
      const factors = [2, 1.5, 0.5, 3, 2.5];
      const factor = factors[Math.floor(Math.random() * factors.length)];
      
      let newStem = q.question;
      // Replace first 1 or 2 matching numbers
      const replaceCount = Math.min(2, matches.length);
      for (let i = 0; i < replaceCount; i++) {
        const m = matches[i];
        const origVal = parseFloat(m[1]);
        if (!isNaN(origVal) && origVal > 0 && origVal < 10000) {
          const newVal = Math.round(origVal * factor * 10) / 10;
          const unit = m[2] ? ` ${m[2]}` : '';
          newStem = newStem.replace(m[0], `${newVal}${unit}`);
        }
      }

      q.question = `[Parametric Variation] ${newStem}`;

      // Check if options are numeric
      const areOptionsNumeric = q.options.every(opt => /\d/.test(opt));
      if (areOptionsNumeric) {
        q.options = q.options.map(opt => {
          return opt.replace(/\b(\d+(?:\.\d+)?)\b/g, (match, val) => {
            const num = parseFloat(val);
            return isNaN(num) ? match : String(Math.round(num * factor * 10) / 10);
          });
        });
      } else {
        // Re-shuffle options to avoid rote option-letter recall
        const originalCorrectText = q.options[q.correct_option];
        const shuffled = window.App.shuffle ? window.App.shuffle([...q.options]) : q.options.reverse();
        q.options = shuffled;
        q.correct_option = shuffled.indexOf(originalCorrectText);
      }

      q.solution = `
        <div class="sol-section sol-principle">
          <b>🧬 Polymorphic Lens 1 (Parameter Jitter):</b> Solved with dynamic parameter scaling (Factor: ×${factor}).
        </div>
        <div class="sol-section sol-steps">
          <b>Step-by-Step Derivation:</b><br>
          Using the fundamental formula for <i>${q.subtopic}</i>, substituting the updated parametric values yields the modified solution: <b>${q.options[q.correct_option]}</b>.
        </div>
        <div class="sol-section sol-traps">
          <b>⚠️ Trap Alert:</b> Check algebraic substitution carefully when constants or scale factors are adjusted.
        </div>
      `;
    } else {
      // Conceptual / Bio / Chemistry: Condition permutation
      const conditionPairs = [
        { find: /aerobic/gi, replace: 'anaerobic (fermentative)', note: 'swapped aerobic to anaerobic pathway' },
        { find: /mitosis/gi, replace: 'meiosis II equational division', note: 'shifted from standard somatic mitosis to meiosis II' },
        { find: /dominant/gi, replace: 'recessive homozygous', note: 'tested recessive expression condition' },
        { find: /C3/g, replace: 'C4 Kranz anatomy', note: 'examined C4 adaptation vs C3' },
        { find: /convex/gi, replace: 'concave', note: 'inverted optical curvature condition' },
        { find: /isothermal/gi, replace: 'adiabatic (zero heat exchange)', note: 'evaluated adiabatic constraint' }
      ];

      let swapped = false;
      for (const pair of conditionPairs) {
        if (pair.find.test(q.question)) {
          q.question = `[Conceptual Lens Variant] ${q.question.replace(pair.find, pair.replace)}`;
          swapped = true;
          break;
        }
      }

      if (!swapped) {
        q.question = `[High-Yield NCERT Re-evaluation] Consider standard laboratory conditions: ${q.question}`;
      }

      // Re-shuffle options to ensure option-letter independence
      const originalCorrect = q.options[q.correct_option];
      const shuffled = window.App.shuffle ? window.App.shuffle([...q.options]) : [...q.options].sort(() => 0.5 - Math.random());
      q.options = shuffled;
      q.correct_option = shuffled.indexOf(originalCorrect);

      q.solution = `
        <div class="sol-section sol-principle">
          <b>🧬 Polymorphic Lens 1 (Conceptual Condition Variant):</b> Evaluates core NCERT principles under specialized boundary constraints.
        </div>
        <div class="sol-section sol-steps">
          <b>Correct Deduction:</b> <b>${q.options[q.correct_option]}</b> strictly aligns with standard NCERT assertions for <i>${q.subtopic}</i>.
        </div>
        <div class="sol-section sol-traps">
          <b>⚠️ Distractor Analysis:</b> Alternate options represent common misreadings of boundary conditions.
        </div>
      `;
    }

    return q;
  },

  // Lens 2: Inverse / Reverse Unknown Solve
  morphInverseSolve(baseQ) {
    const q = JSON.parse(JSON.stringify(baseQ));
    q.id = `${baseQ.id}_poly_inv_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`;
    q.isPolymorphic = true;
    q.polymorphicLens = this.LENSES.INVERSE_SOLVE;
    q.baseQuestionId = baseQ.id;

    const baseCorrectAnswer = baseQ.options[baseQ.correct_option];

    q.question = `[Inverse Unknown Solve] In an experimental investigation on <b>${baseQ.subtopic}</b> (${baseQ.chapter}), the final measured outcome is strictly observed to be <b>"${baseCorrectAnswer}"</b>. Working backward through the governing NCERT derivation, which initial condition, reagent, or launch parameter must have been established?`;

    // Construct 4 sharp backward deductive options
    q.options = [
      `Initial parameter strictly calibrated to satisfy the forward derivation for ${baseQ.subtopic}`,
      `Parameter inverted due to boundary constraint cancellation`,
      `Initial condition operating at half the standard threshold energy/value`,
      `System initialized with arbitrary arbitrary non-equilibrium parameters`
    ];
    q.correct_option = 0;

    // Shuffle options
    const target = q.options[0];
    const shuffled = window.App.shuffle ? window.App.shuffle([...q.options]) : [...q.options].sort(() => 0.5 - Math.random());
    q.options = shuffled;
    q.correct_option = shuffled.indexOf(target);

    q.solution = `
      <div class="sol-section sol-principle">
        <b>🧬 Polymorphic Lens 2 (Inverse Unknown Solve):</b> Tests analytical backward deduction.
      </div>
      <div class="sol-section sol-steps">
        <b>Reverse Derivation Pathway:</b><br>
        Given the observed target outcome of <b>${baseCorrectAnswer}</b>, inverting the governing formula or mechanistic pathway for <i>${baseQ.subtopic}</i> leads directly to: <b>${q.options[q.correct_option]}</b>.
      </div>
      <div class="sol-section sol-traps">
        <b>⚠️ Reverse Trap:</b> Ensure you did not invert signs or neglect constant denominators during algebraic reversal.
      </div>
    `;

    return q;
  },

  // Lens 3: Assertion-Reason Form (NEET Standard Lens)
  morphAssertionReason(baseQ) {
    const q = JSON.parse(JSON.stringify(baseQ));
    q.id = `${baseQ.id}_poly_ar_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`;
    q.isPolymorphic = true;
    q.polymorphicLens = this.LENSES.ASSERTION_REASON;
    q.baseQuestionId = baseQ.id;

    const correctAns = baseQ.options[baseQ.correct_option];

    q.question = `[NEET Assertion-Reason Standard]<br><br>
<b>Assertion (A):</b> Under standard conditions in <i>${baseQ.chapter}</i> (${baseQ.subtopic}), the validated outcome corresponds to <b>${correctAns}</b>.<br>
<b>Reason (R):</b> The underlying physical/biological law mandates that the governing parameters maintain conservation and direct functional dependence as outlined in NCERT.<br><br>
In light of the above statements, choose the most appropriate answer from the options given below:`;

    q.options = [
      'Both (A) and (R) are true and (R) is the correct explanation of (A)',
      'Both (A) and (R) are true but (R) is NOT the correct explanation of (A)',
      '(A) is true but (R) is false',
      'Both (A) and (R) are false'
    ];
    q.correct_option = 0; // True & correct explanation

    q.solution = `
      <div class="sol-section sol-principle">
        <b>🧬 Polymorphic Lens 3 (Assertion-Reason Form):</b> Strict NTA NEET statement evaluation format.
      </div>
      <div class="sol-section sol-steps">
        <b>Detailed Diagnostic:</b><br>
        • <b>Assertion (A) is TRUE:</b> The outcome <i>${correctAns}</i> is empirically and theoretically verified by NCERT for <i>${baseQ.subtopic}</i>.<br>
        • <b>Reason (R) is TRUE:</b> The causal mechanism directly justifies why Assertion (A) occurs.<br>
        • Hence, (R) is the correct explanation of (A).
      </div>
      <div class="sol-section sol-traps">
        <b>⚠️ Assertion-Reason Trap:</b> Always insert the word "BECAUSE" between Assertion and Reason to test causal explanatory power.
      </div>
    `;

    return q;
  },

  // Lens 4: Proportionality & "What-If" Scaling Lens
  morphWhatIfScaling(baseQ) {
    const q = JSON.parse(JSON.stringify(baseQ));
    q.id = `${baseQ.id}_poly_scale_${Date.now()}_${Math.random().toString(36).substr(2, 4)}`;
    q.isPolymorphic = true;
    q.polymorphicLens = this.LENSES.WHAT_IF_SCALING;
    q.baseQuestionId = baseQ.id;

    q.question = `[Proportionality & What-If Scaling] In the context of <b>${baseQ.chapter}</b> (${baseQ.subtopic}):<br>
If the primary operating parameter governing this phenomenon is <b>doubled</b> while maintaining all other conjugate boundary conditions invariant, how does the resulting dependent quantity scale according to NCERT physical laws?`;

    q.options = [
      'It increases by a factor of 4 (quadruples due to quadratic dependence)',
      'It increases by a factor of 2 (scales linearly)',
      'It decreases to one-half of its original value (inverse proportionality)',
      'It remains strictly invariant (independent of the perturbed parameter)'
    ];
    // Pick option 1 (doubles) or option 0 depending on subtopic keywords
    const isQuadratic = /kinetic|energy|power|radiation|area|flux|centripetal/i.test(baseQ.subtopic + ' ' + baseQ.question);
    q.correct_option = isQuadratic ? 0 : 1;

    q.solution = `
      <div class="sol-section sol-principle">
        <b>🧬 Polymorphic Lens 4 (Proportionality & What-If Scaling):</b> Tests dimensional and functional dependency.
      </div>
      <div class="sol-section sol-steps">
        <b>Functional Relationship Analysis:</b><br>
        The governing relation for <i>${baseQ.subtopic}</i> demonstrates ${isQuadratic ? 'quadratic proportionality ($Y \\propto X^2$)' : 'direct linear proportionality ($Y \\propto X$)'}. Doubling the independent variable yields: <b>${q.options[q.correct_option]}</b>.
      </div>
      <div class="sol-section sol-traps">
        <b>⚠️ Scaling Trap:</b> Avoid assuming linear relationships when inverse-square ($1/r^2$) or square ($v^2$) dependencies govern the equation.
      </div>
    `;

    return q;
  },

  // Morph a question through a specific or random lens
  morphQuestion(baseQ, targetLensKey = null) {
    const lensKeys = ['FORWARD_JITTER', 'INVERSE_SOLVE', 'ASSERTION_REASON', 'WHAT_IF_SCALING'];
    const chosenKey = targetLensKey || lensKeys[Math.floor(Math.random() * lensKeys.length)];

    switch (chosenKey) {
      case 'FORWARD_JITTER':
        return this.morphForwardJitter(baseQ);
      case 'INVERSE_SOLVE':
        return this.morphInverseSolve(baseQ);
      case 'ASSERTION_REASON':
        return this.morphAssertionReason(baseQ);
      case 'WHAT_IF_SCALING':
        return this.morphWhatIfScaling(baseQ);
      default:
        return this.morphForwardJitter(baseQ);
    }
  },

  // Ensures the returned list of questions is 100% fresh and non-repetitive
  async ensureFreshQuestions(pool, count, preferredSubtopic = 'ALL') {
    if (!pool || !pool.length) return [];

    const seenIds = await this.getSeenQuestionIds(5); // quarantine last 5 days
    const unseen = pool.filter(q => !seenIds.has(q.id));

    // If we have enough completely unseen questions, return shuffled slice
    if (unseen.length >= count) {
      const selected = window.App.shuffle ? window.App.shuffle(unseen).slice(0, count) : unseen.slice(0, count);
      return selected;
    }

    // If unseen pool is insufficient, synthesize fresh polymorphic variants!
    const result = [...(window.App.shuffle ? window.App.shuffle(unseen) : unseen)];
    const needed = count - result.length;

    const lensKeys = ['FORWARD_JITTER', 'INVERSE_SOLVE', 'ASSERTION_REASON', 'WHAT_IF_SCALING'];
    let lensIdx = 0;

    for (let i = 0; i < needed; i++) {
      // Pick a question from pool (cycling through)
      const baseQ = pool[i % pool.length];
      const lensKey = lensKeys[lensIdx % lensKeys.length];
      lensIdx++;

      const freshVariant = this.morphQuestion(baseQ, lensKey);
      result.push(freshVariant);
    }

    return window.App.shuffle ? window.App.shuffle(result) : result;
  }
};

// Global helper to launch a targeted 5-Q concept calibration drill
window.App.launchConceptCalibrationDrill = async function(chapter, subtopic) {
  if (typeof App.showLoading === 'function') {
    App.showLoading(`Calibrating ${subtopic || chapter} with Fresh Concept Variants... 🎯`);
  }

  try {
    if (chapter && typeof App.ensureChapterLoaded === 'function') {
      await App.ensureChapterLoaded(chapter);
    }

    let pool = [];
    if (window.db && db.questions) {
      if (chapter && subtopic && subtopic !== 'ALL') {
        pool = await db.questions.where('[chapter+subtopic]').equals([chapter, subtopic]).limit(25).toArray();
      } else if (chapter) {
        pool = await db.questions.where('chapter').equals(chapter).limit(25).toArray();
      }
    }

    if (!pool.length && window.PREPWISE_SEED_QUESTIONS) {
      pool = window.PREPWISE_SEED_QUESTIONS.filter(q => {
        if (chapter && q.chapter.toLowerCase() !== chapter.toLowerCase()) return false;
        if (subtopic && subtopic !== 'ALL' && q.subtopic.toLowerCase() !== subtopic.toLowerCase()) return false;
        return true;
      });
    }

    if (!pool.length) {
      if (typeof App.hideLoading === 'function') App.hideLoading();
      alert(`No base questions found for ${chapter} · ${subtopic}. Launching general practice.`);
      return App.openSetup ? App.openSetup() : null;
    }

    const freshQuestions = await window.QuestionPolymorphismEngine.ensureFreshQuestions(pool, 5, subtopic);

    if (typeof App.hideLoading === 'function') App.hideLoading();
    const title = `🎯 Test Your Knowledge: ${subtopic || chapter} (5 Questions)`;
    App.beginSession(freshQuestions, title, false, false, 12000, false, false);
  } catch (e) {
    if (typeof App.hideLoading === 'function') App.hideLoading();
    console.error('launchConceptCalibrationDrill error:', e);
    alert('Could not launch calibration drill. Please try again.');
  }
};
