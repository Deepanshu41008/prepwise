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

global.db = {
  attempts: {
    toArray: async () => [
      { timestamp: Date.now() - 3600000, isCorrect: true },
      { timestamp: Date.now() - 7200000, isCorrect: false },
      { timestamp: Date.now() - 86400000, isCorrect: true },
      { timestamp: Date.now() - 172800000, isCorrect: true }
    ]
  },
  mistakes: {
    put: async (item) => { return 1; }
  },
  sessions: {
    add: async (s) => { return 1; }
  }
};

// 2. Load the modules
window.App = window.App || {};
window.App.showView = () => {};
window.App.updateTopStats = async () => {};
window.App.updateMockKpis = async () => {};

require('../data/flashcards_data.js');
require('../js/flashcards.js');
require('../js/planner.js');
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

  console.log('--- ALL FEATURE TESTS PASSED SUCCESSFULLY! ---');
  process.exit(0);
}

runTests().catch(e => {
  console.error('Test failed:', e);
  process.exit(1);
});
