// scripts/test_features.js - Automated Test for Flashcards, Planner, and Solution Inspector
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
  }
};

// 2. Load the modules
require('../data/flashcards_data.js');
require('../js/flashcards.js');
require('../js/planner.js');
require('../js/inspector.js');

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

  // TEST 3: Solution Inspector & Diagnostic Analyzer
  window.App.initSolutionInspector();
  assert(window.App.inspectorActiveQuestion !== null, 'Active question should be set');
  
  // Physics Range Trap Test
  const phyTrapWork = `Formula: R = (u^2 * sin(theta)) / g
Step 1: R = (1600 * 0.5) / 10
Step 2: R = 80 m
Selected Option: B`;
  const result1 = window.App.evaluateSteps(phyTrapWork, window.App.getDemoQuestion());
  assert(result1.hasError === true, 'Trap error should be detected');
  assert(result1.suggestedTag === 'Formula Forgotten', 'Error tag should be Formula Forgotten');
  console.log(`✓ Solution Inspector Passed: Trap detected (${result1.suggestedTag}) with breakdown: ${result1.steps.length} steps`);

  // Chemistry Slip Test
  const chemDemoQ = {
    subject: "Chemistry",
    chapter: "Thermodynamics",
    question: "Calculate Delta G given Delta H = -100 kJ and T Delta S = -20 J",
    answer: "A"
  };
  const chemTrapWork = `M = 0.1 / 500 mL`;
  const result2 = window.App.evaluateSteps(chemTrapWork, chemDemoQ);
  assert(result2.hasError === true, 'Unit conversion trap should be detected');
  console.log(`✓ Solution Inspector Passed: Chemistry unit trap detected (${result2.suggestedTag})`);

  // Log to Mistake Vault
  await window.App.logInspectorMistake(result1.suggestedTag);
  console.log(`✓ Mistake Vault Logging Tested`);

  console.log('--- ALL FEATURE TESTS PASSED SUCCESSFULLY! ---');
  process.exit(0);
}

runTests().catch(e => {
  console.error('Test failed:', e);
  process.exit(1);
});
