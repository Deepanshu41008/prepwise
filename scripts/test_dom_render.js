// scripts/test_dom_render.js - Comprehensive DOM Rendering & Interaction Tests for Features 1, 2, 3
const assert = require('assert');

// Setup full DOM emulation
global.window = global;
global.localStorage = {
  store: {},
  getItem(k) { return this.store[k] || null; },
  setItem(k, v) { this.store[k] = String(v); },
  removeItem(k) { delete this.store[k]; }
};

const domStore = {};
function createMockElement(id) {
  return {
    id,
    textContent: '',
    innerHTML: '',
    style: {},
    dataset: {},
    value: '',
    classList: {
      classes: new Set(),
      add(c) { this.classes.add(c); },
      remove(c) { this.classes.delete(c); },
      toggle(c, force) {
        if (force === undefined) {
          if (this.classes.has(c)) this.classes.delete(c);
          else this.classes.add(c);
        } else if (force) this.classes.add(c);
        else this.classes.delete(c);
      },
      contains(c) { return this.classes.has(c); }
    }
  };
}

global.document = {
  elements: domStore,
  getElementById(id) {
    if (!this.elements[id]) {
      this.elements[id] = createMockElement(id);
    }
    return this.elements[id];
  },
  querySelectorAll(sel) {
    return [];
  }
};

const memStore = {
  attempts: [],
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

window.App = window.App || {};
window.App.showView = () => {};
window.App.typesetMath = () => {};
window.App.shuffle = (arr) => arr;

require('../js/polymorphism.js');
require('../js/analytics.js');
require('../js/engine.js');

async function testDomRender() {
  console.log('--- STARTING DOM RENDERING AUDIT ---');

  // TEST FEATURE 1: Mistake Vault DOM & Saved Questions DOM
  const sampleQ = {
    id: "q_dom_1",
    question: "What is the unit of electric flux?",
    options: ["N·m²/C", "V/m", "J/C", "Wb"],
    correct_option: 0,
    solution: "Flux Φ = E·A = N/C * m² = N·m²/C"
  };

  await global.db.mistakes.put({
    questionId: sampleQ.id,
    subject: "Physics",
    chapter: "Electrostatics",
    subtopic: "Electric Flux & Gauss Law",
    errorTag: "Formula Forgotten",
    timeSpent: 40,
    q: sampleQ
  });

  // Render Mistake Vault
  await window.App.showMistakes();
  const mistakeHtml = document.getElementById('mistakeList').innerHTML;
  assert(mistakeHtml.includes('Save to Previous Mistakes'), 'Mistake card must contain "Save to Previous Mistakes" button');
  assert(mistakeHtml.includes('Test Your Knowledge'), 'Mistake card must contain "Test Your Knowledge" button');
  assert(mistakeHtml.includes('Formula Forgotten'), 'Mistake card must display error tag');
  console.log('✓ Mistake Vault DOM verified: Save to Previous Mistakes & Test Your Knowledge buttons rendered');

  // Toggle Save into Previous Mistakes
  await window.App.toggleSaveMistakeConcept(sampleQ.id);
  await window.App.showMistakes();
  const updatedMistakeHtml = document.getElementById('mistakeList').innerHTML;
  assert(updatedMistakeHtml.includes('Saved in Previous Mistakes ✓'), 'Button should update to active saved state');
  console.log('✓ Toggle save state verified: shows "Saved in Previous Mistakes ✓"');

  // Render Saved Questions (Bookmarks)
  await window.App.showBookmarks();
  const bmHtml = document.getElementById('bookmarkList').innerHTML;
  assert(bmHtml.includes('High-Yield Previous Mistake'), 'Card in Saved Questions must display "High-Yield Previous Mistake" badge');
  assert(bmHtml.includes('Formula Forgotten'), 'Card must retain root cause error tag');
  assert(bmHtml.includes('Test Your Knowledge'), 'Card must feature "Test Your Knowledge" button');
  console.log('✓ Saved Questions DOM verified: Badges, root cause tags, and Test Your Knowledge actions rendered cleanly');

  // TEST FEATURE 2: Smart Nudge & Growth Board Recovery Section
  // Populate struggle attempts
  memStore.attempts.push(
    { questionId: 'att1', subject: 'Physics', chapter: 'Electrostatics', subtopic: 'Electric Flux & Gauss Law', correct: 0, timestamp: Date.now() - 3600000 },
    { questionId: 'att2', subject: 'Physics', chapter: 'Electrostatics', subtopic: 'Electric Flux & Gauss Law', correct: 0, timestamp: Date.now() - 3500000 },
    { questionId: 'att3', subject: 'Physics', chapter: 'Electrostatics', subtopic: 'Electric Flux & Gauss Law', correct: 1, timestamp: Date.now() - 86400000 },
    { questionId: 'att4', subject: 'Physics', chapter: 'Electrostatics', subtopic: 'Electric Flux & Gauss Law', correct: 0, timestamp: Date.now() - 86400000 }
  );

  // Render Smart Nudge
  global.localStorage.removeItem('prepwise_struggle_nudge_snooze');
  await window.App.renderSmartConceptNudge();
  const nudgeHtml = document.getElementById('smartConceptNudgeContainer').innerHTML;
  assert(nudgeHtml.includes('FINESSE YOUR STRENGTH'), 'Nudge card must feature positive framing');
  assert(nudgeHtml.includes('Electric Flux & Gauss Law'), 'Nudge must target the exact struggling subtopic');
  assert(nudgeHtml.includes('Hard Data Proof'), 'Nudge must contain the data proof section');
  assert(nudgeHtml.includes('Test Your Knowledge'), 'Nudge must contain Test Your Knowledge CTA');
  assert(nudgeHtml.includes('Remind Me Tomorrow'), 'Nudge must contain snooze option');
  console.log('✓ Smart Nudge DOM verified: Positive framing, exact proof data, snooze & Test Your Knowledge CTA');

  // Render Growth Board Recovery Opportunities
  const insights = await window.App.computeCognitiveStruggleInsights();
  window.App.renderGrowthBoardCognitiveRecovery(insights.allStruggles);
  const gbRecoveryHtml = document.getElementById('gbCognitiveRecoveryContainer').innerHTML;
  assert(gbRecoveryHtml.includes('Data-Proven Mark Recovery Opportunities'), 'Growth Board must show recovery section');
  assert(gbRecoveryHtml.includes('Calibrate Strength'), 'Growth Board must show calibration button');
  console.log('✓ Growth Board Recovery DOM verified: Comprehensive topic audit cards rendered');

  // TEST FEATURE 3: Polymorphic Question & 360 Mastery Matrix
  const polyQ = window.QuestionPolymorphismEngine.morphInverseSolve(sampleQ);
  polyQ.classNum = '12';
  polyQ.difficulty = 'medium';
  polyQ.year_tag = 'NEET 2024';

  window.App.session = [polyQ];
  window.App.states = [{ picked: 0, locked: true, timeSpent: 25, unlockedHints: 0, hintsCollapsed: false, showFullSolution: false }];
  window.App.index = 0;
  window.App.isMock = false;
  window.App.isExamMode = false;
  window.App.isBlind = false;

  await window.App.renderQuestion();
  const qAreaHtml = document.getElementById('questionArea').innerHTML;
  assert(qAreaHtml.includes('🧬 Inverse Unknown Solve'), 'Question card header must display the polymorphic lens badge');
  assert(qAreaHtml.includes('360° Concept Mastery Matrix'), 'Solution area must render the 360° concept matrix');
  assert(qAreaHtml.includes('Lens 2: Reverse Unknown'), 'Matrix must highlight the active lens');
  console.log('✓ Polymorphic Question DOM verified: Lens badge and 360° Concept Mastery Matrix rendered cleanly');

  console.log('--- ALL DOM RENDERING AUDITS PASSED WITH 100% SUCCESS! ---');
  process.exit(0);
}

testDomRender().catch(e => {
  console.error('DOM Render test failed:', e);
  process.exit(1);
});
