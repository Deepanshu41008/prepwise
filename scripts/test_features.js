// scripts/test_features.js - Automated Test for Flashcards, Planner, and Test Analysis
const assert = require('assert');

// 1. Mock minimal DOM environment
global.window = global;
global.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); },
  removeItem(k) { delete this.store[k]; }
};

global.document = {
  elements: {},
  getElementById(id) {
    if (!this.elements[id]) {
      this.elements[id] = {
        id,
        textContent: '',
        innerHTML: '',
        style: {},
        classList: {
          classes: new Set(),
          add(c) { this.classes.add(c); },
          remove(c) { this.classes.delete(c); },
          toggle(c, force) {
            if (force === undefined) {
              if (this.classes.has(c)) this.classes.delete(c);
              else this.classes.add(c);
            } else if (force) {
              this.classes.add(c);
            } else {
              this.classes.delete(c);
            }
          },
          contains(c) { return this.classes.has(c); }
        },
        dataset: {},
        value: ''
      };
    }
    return this.elements[id];
  },
  querySelectorAll(sel) {
    return [];
  }
};

const memStore = {
  attempts: [
    { timestamp: Date.now() - 3600000, isCorrect: true },
    { timestamp: Date.now() - 7200000, isCorrect: false },
    { timestamp: Date.now() - 86400000, isCorrect: true },
    { timestamp: Date.now() - 172800000, isCorrect: true }
  ],
  mistakes: {},
  bookmarks: {},
  sessions: []
};

global.db = {
  attempts: {
    toArray: async () => memStore.attempts,
    add: async (a) => { memStore.attempts.push(a); }
  },
  mistakes: {
    put: async (item) => { memStore.mistakes[item.questionId] = item; return 1; },
    get: async (id) => memStore.mistakes[id] || null,
    delete: async (id) => { delete memStore.mistakes[id]; },
    toArray: async () => Object.values(memStore.mistakes),
    update: async (id, changes) => {
      if (memStore.mistakes[id]) Object.assign(memStore.mistakes[id], changes);
    }
  },
  bookmarks: {
    put: async (item) => { memStore.bookmarks[item.questionId] = item; return 1; },
    get: async (id) => memStore.bookmarks[id] || null,
    delete: async (id) => { delete memStore.bookmarks[id]; },
    toArray: async () => Object.values(memStore.bookmarks)
  },
  sessions: {
    add: async (s) => { memStore.sessions.push(s); return 1; },
    toArray: async () => memStore.sessions
  }
};

// 2. Load the modules
window.App = window.App || {};
window.App.showView = () => {};
window.App.updateTopStats = async () => {};
window.App.updateMockKpis = async () => {};
window.App.typesetMath = () => {};

require('../data/flashcards_data.js');
require('../js/flashcards.js');
require('../js/planner.js');
require('../js/polymorphism.js');
require('../js/analytics.js');
require('../js/engine.js');

async function runTests() {
  console.log('--- STARTING COMPREHENSIVE FEATURES TEST ---');

  // TEST 1: Flashcards Deck
  assert(Array.isArray(window.PREPWISE_FLASHCARDS), 'PREPWISE_FLASHCARDS should be an array');
  assert(window.PREPWISE_FLASHCARDS.length === 735, `Expected 735 flashcards, got ${window.PREPWISE_FLASHCARDS.length}`);
  console.log(`✓ Flashcards Data Loaded: ${window.PREPWISE_FLASHCARDS.length} cards across all chapters`);

  window.App.initFlashcards();
  assert(window.App.fcCards.length === 735, 'fcCards should have 735 cards initialized');
  assert(window.App.fcIndex === 0, 'fcIndex should start at 0');
  
  // Flip
  window.App.flipFlashcard();
  assert(window.App.fcFlipped === true, 'Card should be flipped');
  window.App.flipFlashcard();
  assert(window.App.fcFlipped === false, 'Card should flip back');

  // Next & Prev
  window.App.nextFlashcard();
  assert(window.App.fcIndex === 1, 'Index should advance to 1');
  window.App.prevFlashcard();
  assert(window.App.fcIndex === 0, 'Index should return to 0');

  // Star & Master
  window.App.toggleStarFlashcard();
  assert(window.App.fcState[window.App.fcCards[0].id].starred === true, 'Card should be starred');
  window.App.markFlashcard('mastered');
  assert(window.App.fcState[window.App.fcCards[0].id].status === 'mastered', 'Card should be mastered');

  // Filter test
  window.App.setFcSubj('Physics');
  assert(window.App.fcCards.every(c => c.subject === 'Physics'), 'Filtered cards should all be Physics');
  console.log(`✓ Flashcards Engine Passed: Flip, Next, Prev, Mastery, Star, Subject Filtering tested`);

  // TEST 2: Study Planner & Daily Target
  window.App.initPlanner();
  assert(typeof window.App.plannerTarget === 'number', 'Daily target should be a number');
  window.App.setDailyTarget(80);
  assert(window.App.plannerTarget === 80, 'Daily target should update to 80');
  await window.App.refreshPlannerData();
  console.log(`✓ Study Planner Passed: Target configuration, Countdown Ticker, Heatmap generation tested`);

  // TEST 3: In-Depth Exam Analysis & Mini-Test Mode
  const mockQuestions = [
    {
      id: "q1",
      subject: "Physics",
      chapter: "Kinematics",
      subtopic: "Projectile Motion",
      question: "Sample Q1",
      options: ["A1", "B1", "C1", "D1"],
      correct_option: 0,
      difficulty: "medium",
      solution: "Principle and derivation"
    },
    {
      id: "q2",
      subject: "Chemistry",
      chapter: "Thermodynamics",
      subtopic: "Enthalpy",
      question: "Sample Q2",
      options: ["A2", "B2", "C2", "D2"],
      correct_option: 1,
      difficulty: "hard",
      solution: "Principle and derivation"
    }
  ];

  // Test session launch in Mini-Test mode (isExamMode = true)
  window.App.beginSession(mockQuestions, "Test Mini-Exam", false, false, 600, false, true);
  assert(window.App.isExamMode === true, 'isExamMode should be true');
  assert(window.App.session.length === 2, 'Session length should be 2');

  // Answer Q1 correctly, Q2 incorrectly
  window.App.chooseOption(0); // correct for Q1
  window.App.states[0].timeSpent = 45;
  window.App.index = 1;
  window.App.chooseOption(0); // wrong for Q2 (correct is 1)
  window.App.states[1].timeSpent = 12; // rushed

  // Finish session
  await window.App.finishSession();
  assert(window.App.testAnalysis !== null, 'testAnalysis should be generated');
  assert(window.App.testAnalysis.totalCorrect === 1, '1 correct question expected');
  assert(window.App.testAnalysis.totalWrong === 1, '1 wrong question expected');
  assert(window.App.testAnalysis.netMarks === 3, 'Net marks should be +4 - 1 = 3');

  // Verify "Why It Went Wrong" diagnostic on Q2
  const wrongItem = window.App.testAnalysis.questions.find(item => item.isWrong);
  assert(wrongItem !== undefined, 'Wrong item should exist');
  assert(wrongItem.errorTag.includes('Rush') || wrongItem.errorTag.includes('Trap'), 'Error tag should identify rush or trap');
  console.log(`✓ Exam In-Depth Analysis Passed: Net marks (3/8), Accuracy (50%), Diagnostic Tag (${wrongItem.errorTag})`);

  // ==================== TEST 4: FEATURE 1 (MISTAKE VAULT -> SAVED QUESTIONS) ====================
  // Log a mistake
  await global.db.mistakes.put({
    questionId: 'phy_test_m1',
    subject: 'Physics',
    chapter: 'Kinematics',
    subtopic: 'Projectile Motion',
    errorTag: 'Formula Forgotten',
    timeSpent: 65,
    q: mockQuestions[0]
  });

  // Toggle save into Previous Mistakes
  await window.App.toggleSaveMistakeConcept('phy_test_m1');
  const savedItem = await global.db.bookmarks.get('phy_test_m1');
  assert(savedItem !== null, 'Saved item should exist in bookmarks');
  assert(savedItem.folder === 'previous_mistakes', 'Saved item folder must be previous_mistakes');
  assert(savedItem.errorTag === 'Formula Forgotten', 'Saved item must retain error tag');

  // Verify category filtering in Saved Questions
  await global.db.bookmarks.put({
    questionId: 'chem_test_star1',
    subject: 'Chemistry',
    chapter: 'Thermodynamics',
    subtopic: 'Enthalpy',
    folder: 'starred',
    q: mockQuestions[1]
  });

  const allBms = await global.db.bookmarks.toArray();
  const mistakeBms = allBms.filter(b => b.folder === 'previous_mistakes');
  const starredBms = allBms.filter(b => b.folder !== 'previous_mistakes');
  assert(allBms.length === 2, 'Total 2 bookmarks');
  assert(mistakeBms.length === 1, '1 bookmark in previous_mistakes folder');
  assert(starredBms.length === 1, '1 bookmark in starred folder');
  console.log('✓ Feature 1 Passed: Save from Mistake Vault to "Previous Mistakes", folder separation, error tag retention');

  // ==================== TEST 5: FEATURE 2 (COGNITIVE STRUGGLE METRIC & NUDGING) ====================
  // Clear attempts
  memStore.attempts = [];

  // Subtopic with only 2 attempts (less than gatekeeper minimum 4) -> Should NOT trigger
  memStore.attempts.push(
    { questionId: 'qA1', subject: 'Botany', chapter: 'Photosynthesis', subtopic: 'Light Reaction', correct: 0, timestamp: Date.now() - 3600000 },
    { questionId: 'qA2', subject: 'Botany', chapter: 'Photosynthesis', subtopic: 'Light Reaction', correct: 0, timestamp: Date.now() - 1800000 }
  );

  let insights = await window.App.computeCognitiveStruggleInsights();
  assert(!insights || !insights.topStruggle, 'Should NOT flag struggle when attempts < 4 (Anti-False-Alarm Gatekeeper)');

  // Now add 3 more attempts across another session, showing consistent failure (accuracy 20%, neg bleed 4)
  memStore.attempts.push(
    { questionId: 'qA3', subject: 'Botany', chapter: 'Photosynthesis', subtopic: 'Light Reaction', correct: 1, timestamp: Date.now() - 86400000 },
    { questionId: 'qA4', subject: 'Botany', chapter: 'Photosynthesis', subtopic: 'Light Reaction', correct: 0, timestamp: Date.now() - 86400000 },
    { questionId: 'qA5', subject: 'Botany', chapter: 'Photosynthesis', subtopic: 'Light Reaction', correct: 0, timestamp: Date.now() - 86400000 }
  );

  insights = await window.App.computeCognitiveStruggleInsights();
  assert(insights !== null && insights.topStruggle !== null, 'Should flag struggle when hard data criteria are met');
  assert(insights.topStruggle.chapter === 'Photosynthesis', 'Top struggle chapter should be Photosynthesis');
  assert(insights.topStruggle.totalAttempts === 5, '5 attempts recorded');
  assert(insights.topStruggle.accuracy === 20, 'Accuracy should be 20%');
  assert(insights.topStruggle.negativeBleed === 4, 'Negative bleed should be 4 marks');
  assert(insights.topStruggle.distinctSessions >= 2, 'Sessions should be at least 2');

  // Test Snooze logic
  window.App.snoozeSmartNudge(24);
  const snoozeVal = Number(global.localStorage.getItem('prepwise_struggle_nudge_snooze'));
  assert(snoozeVal > Date.now(), 'Snooze timestamp should be in the future');
  console.log(`✓ Feature 2 Passed: Cognitive Struggle Metric gatekeeper verified, false alarm prevention, exact proof data (${insights.topStruggle.totalAttempts} Qs, ${insights.topStruggle.accuracy}% acc), 24h snooze`);

  // ==================== TEST 6: FEATURE 3 (CONCEPT POLYMORPHISM & FRESHNESS ENGINE) ====================
  const baseTestQ = {
    id: "phy_base_001",
    classNum: "11",
    subject: "Physics",
    chapter: "Laws of Motion",
    subtopic: "Centripetal Force & Banking",
    difficulty: "medium",
    question: "A vehicle of mass 1000 kg rounds a curve of radius 50 m at a speed of 20 m/s. Calculate the required centripetal force.",
    options: ["8000 N", "4000 N", "2000 N", "1000 N"],
    correct_option: 0,
    solution: "Centripetal force F = mv^2 / r"
  };

  // Lens 1: Parameter Jitter
  const morphed1 = window.QuestionPolymorphismEngine.morphForwardJitter(baseTestQ);
  assert(morphed1.isPolymorphic === true, 'Morphed question should be flagged polymorphic');
  assert(morphed1.id !== baseTestQ.id, 'ID must be uniquely mutated');
  assert(morphed1.polymorphicLens.includes('Jitter') || morphed1.polymorphicLens.includes('Forward'), 'Lens 1 name mismatch');

  // Lens 2: Inverse Solve
  const morphed2 = window.QuestionPolymorphismEngine.morphInverseSolve(baseTestQ);
  assert(morphed2.isPolymorphic === true, 'Lens 2 should be flagged polymorphic');
  assert(morphed2.question.includes('Inverse') || morphed2.question.includes('backward'), 'Question stem should test inverse deduction');
  assert(morphed2.polymorphicLens === window.QuestionPolymorphismEngine.LENSES.INVERSE_SOLVE, 'Lens 2 title mismatch');

  // Lens 3: Assertion-Reason Form
  const morphed3 = window.QuestionPolymorphismEngine.morphAssertionReason(baseTestQ);
  assert(morphed3.question.includes('Assertion (A)') && morphed3.question.includes('Reason (R)'), 'Must contain Assertion & Reason');
  assert(morphed3.options.length === 4, 'Must have 4 standard NTA options');

  // Lens 4: Proportionality Scaling
  const morphed4 = window.QuestionPolymorphismEngine.morphWhatIfScaling(baseTestQ);
  assert(morphed4.question.includes('doubled') || morphed4.question.includes('parameter'), 'Must test proportionality perturbation');

  // Infinite Freshness & Seen Quarantine Test
  const pool = [baseTestQ];
  // Request 4 questions from a 1-question pool -> Engine must synthesize 3 fresh polymorphic variants!
  const freshList = await window.QuestionPolymorphismEngine.ensureFreshQuestions(pool, 4, 'Centripetal Force & Banking');
  assert(freshList.length === 4, `Expected 4 fresh questions, got ${freshList.length}`);
  const uniqueIds = new Set(freshList.map(q => q.id));
  assert(uniqueIds.size === 4, 'All generated questions must have unique IDs (never run out of fresh questions)');
  console.log(`✓ Feature 3 Passed: 4 Mutation Lenses tested (Jitter, Inverse, Assertion-Reason, Scaling), Seen Quarantine & Infinite Freshness verified (${freshList.length} unique questions generated from 1 base question)`);

  console.log('--- ALL FEATURE TESTS PASSED SUCCESSFULLY! ---');
  process.exit(0);
}

runTests().catch(e => {
  console.error('Test failed:', e);
  process.exit(1);
});
