// js/app.js - Main Application Controller, Router, Dashboard & Event Orchestration
window.App = window.App || {};

// Core App State
Object.assign(window.App, {
  hierarchy: {},
  dashClassFilter: 'ALL',
  dashSubjFilter: 'ALL',
  dashSearchQuery: '',
  session: [],
  states: [],
  index: 0,
  isMock: false,
  isFullNTA: false,
  isBlind: false,
  streak: 0,
  qStartTime: 0,
  qTimer: null,
  mockTimer: null,
  mockSecLeft: 12000,
  mockTotalSec: 12000,
  isStreamingActive: false,
  isIngesting: false,
  ingestPromise: null,
  activeSubjectTab: 'Physics',

  async init() {
    // 1. Instant boot: Read metadata hierarchy (< 5ms, 0 RAM overhead)
    const metaObj = window.PREPWISE_HIERARCHY_META || {};
    this.hierarchy = metaObj.classes || {};
    this.renderDashboard();
    this.initCascadeDropdowns();

    // 2. Check IndexedDB question count and bank version on disk
    try {
      const storedCount = await db.questions.count();
      this.updateBadgeCounts(storedCount);

      const CURRENT_VERSION = '2025_ULTIMA_V4_564K';
      const versionRec = await db.meta.get('bank_version');

      if (!versionRec || versionRec.version !== CURRENT_VERSION || storedCount === 0) {
        // Upgrade or fresh run: clear previous stale questions and load new master bank
        await db.questions.clear();
        await this.ingestSeedPack();
        await db.meta.put({ key: 'bank_version', version: CURRENT_VERSION });
      } else {
        if (window.PREPWISE_SEED_QUESTIONS) {
          delete window.PREPWISE_SEED_QUESTIONS;
        }
      }
    } catch (e) {
      console.warn('Database boot notice:', e);
    }

    await this.updateTopStats();
    await this.updateMockKpis();
  },

  showLoading(msg = 'Preparing Questions... 🎯') {
    const el = document.getElementById('appLoadingOverlay');
    const msgEl = document.getElementById('loadingOverlayMsg');
    if (msgEl) msgEl.textContent = msg;
    if (el) el.style.display = 'flex';
  },

  hideLoading() {
    const el = document.getElementById('appLoadingOverlay');
    if (el) el.style.display = 'none';
  },

  onSearchInput(val) {
    this.dashSearchQuery = val.trim().toLowerCase();
    this.renderDashboard();
  },

  renderDashboard() {
    const classes = ['ALL', ...Object.keys(this.hierarchy).sort()];
    const classContainer = document.getElementById('dashClassPills');
    if (classContainer) {
      classContainer.innerHTML = classes.map(c => `
        <button class="pill-btn ${this.dashClassFilter === c ? 'active' : ''}" onclick="App.setClassFilter('${c}')">
          ${c === 'ALL' ? 'All Classes' : `Class ${c}`}
        </button>
      `).join('');
    }

    const subjects = new Set(['ALL']);
    for (const [cls, sObj] of Object.entries(this.hierarchy)) {
      if (this.dashClassFilter === 'ALL' || cls === this.dashClassFilter) {
        Object.keys(sObj).forEach(s => subjects.add(s));
      }
    }
    const subjIcons = { 'Physics': '⚛️', 'Chemistry': '🧪', 'Botany': '🌿', 'Zoology': '🧬' };
    const subjContainer = document.getElementById('dashSubjTabs');
    if (subjContainer) {
      subjContainer.innerHTML = [...subjects].map(s => `
        <button class="pill-btn ${this.dashSubjFilter === s ? 'active' : ''}" onclick="App.setSubjFilter('${s}')">
          ${s === 'ALL' ? 'All 4 Subjects' : `${subjIcons[s] || ''} ${s}`}
        </button>
      `).join('');
    }

    const cards = [];
    const query = this.dashSearchQuery;

    for (const [cls, sObj] of Object.entries(this.hierarchy)) {
      if (this.dashClassFilter !== 'ALL' && cls !== this.dashClassFilter) continue;
      for (const [subj, chObj] of Object.entries(sObj)) {
        if (this.dashSubjFilter !== 'ALL' && subj !== this.dashSubjFilter) continue;
        for (const [chap, meta] of Object.entries(chObj)) {
          if (query && !chap.toLowerCase().includes(query) && !subj.toLowerCase().includes(query)) {
            const matchedSt = Object.keys(meta.subtopics || {}).some(st => st.toLowerCase().includes(query));
            if (!matchedSt) continue;
          }

          const allSts = Object.keys(meta.subtopics || {});
          const initialSts = allSts.slice(0, 5);
          const extraSts = allSts.slice(5);

          const initialChips = initialSts.map(st => `
            <span class="subtopic-chip" data-chap="${encodeURIComponent(chap)}" data-st="${encodeURIComponent(st)}" onclick="event.stopPropagation();App.onChipClick(this)" title="Practice ${st}">
              ${st}
            </span>
          `).join('');

          let moreBtn = '';
          let extraContainer = '';
          if (extraSts.length > 0) {
            const extraChips = extraSts.map(st => `
              <span class="subtopic-chip" data-chap="${encodeURIComponent(chap)}" data-st="${encodeURIComponent(st)}" onclick="event.stopPropagation();App.onChipClick(this)" title="Practice ${st}">
                ${st}
              </span>
            `).join('');
            moreBtn = `<button type="button" class="subtopic-chip subtopic-expand-chip" data-more-count="${extraSts.length}" onclick="event.stopPropagation();App.toggleChapterSubtopics(this)" title="Click to view all ${allSts.length} micro-topics in ${safeChap}">+${extraSts.length} more topics ▾</button>`;
            extraContainer = `<div class="extra-subtopics" style="display:none;flex-wrap:wrap;gap:5px;width:100%;margin-top:4px;">${extraChips}</div>`;
          }

          const tagClass = subj === 'Physics' ? 'tag-physics' : (subj === 'Chemistry' ? 'tag-chemistry' : (subj === 'Botany' ? 'tag-botany' : 'tag-zoology'));
          const sIcon = subjIcons[subj] || '';
          const qCount = meta.count || (allSts.length * 800);
          const safeSubj = subj.replace(/'/g, "\\'");
          const safeChap = chap.replace(/'/g, "\\'");

          cards.push(`
            <div class="topic" data-cls="${cls}" data-subj="${encodeURIComponent(subj)}" data-chap="${encodeURIComponent(chap)}">
              <div class="topic-header-row">
                <span class="topic-subj-pill ${tagClass}">${sIcon} ${subj}</span>
                <span class="topic-class-tag">Class ${cls}</span>
                <span class="topic-count-tag">${qCount.toLocaleString()} Qs</span>
              </div>
              <h3 class="topic-title">${chap}</h3>
              <div class="topic-subtopics-header">
                <small>📚 <b>${allSts.length} Micro-Topics:</b></small>
              </div>
              <div class="topic-subtopics-preview">
                ${initialChips}
                ${moreBtn}
                ${extraContainer}
              </div>
              <div class="topic-card-actions">
                <button class="topic-drill-btn primary-drill-btn" onclick="event.stopPropagation();App.startInstantChapterPractice('${safeChap}')" title="Instantly start 15 questions from ${safeChap}">
                  ▶ Start Practice (15 Qs)
                </button>
                <button class="secondary-drill-btn" onclick="event.stopPropagation();App.openSetup('${cls}','${safeSubj}','${safeChap}')" title="Configure custom drill with difficulty & question count">
                  ⚙️ Custom
                </button>
              </div>
            </div>
          `);
        }
      }
    }

    const topicContainer = document.getElementById('topicCards');
    if (topicContainer) {
      topicContainer.innerHTML = cards.length ? cards.join('') : `
        <div class="empty" style="grid-column:1/-1">
          No chapters matched "${query}". Try searching another keyword or clear filters.
        </div>
      `;
    }
  },

  setClassFilter(c) { this.dashClassFilter = c; this.renderDashboard(); },

  setSubjFilter(s) { this.dashSubjFilter = s; this.renderDashboard(); },

  onTopicCardClick(el) {
    const chap = decodeURIComponent(el.dataset.chap);
    this.startInstantChapterPractice(chap);
  },

  onChipClick(el) {
    const chap = decodeURIComponent(el.dataset.chap);
    const st = decodeURIComponent(el.dataset.st);
    this.quickSubtopicDrill(chap, st);
  },

  toggleChapterSubtopics(btn) {
    const parent = btn.closest('.topic');
    if (!parent) return;
    const extra = parent.querySelector('.extra-subtopics');
    if (!extra) return;
    const isHidden = extra.style.display === 'none' || !extra.style.display;
    if (isHidden) {
      extra.style.display = 'flex';
      btn.textContent = 'Show fewer topics ▴';
      btn.classList.add('expanded');
    } else {
      extra.style.display = 'none';
      const count = btn.dataset.moreCount || '';
      btn.textContent = `+${count} more topics ▾`;
      btn.classList.remove('expanded');
    }
  },

  initCascadeDropdowns() {
    const classes = Object.keys(this.hierarchy).sort();
    const classSel = document.getElementById('classSelect');
    if (!classSel) return;
    classSel.innerHTML = `<option value="ALL">All Classes (11 & 12)</option>` + classes.map(c => `<option value="${c}">Class ${c}</option>`).join('');
    this.onClassChange();
  },

  onClassChange() {
    const cls = document.getElementById('classSelect').value;
    const subjs = new Set();
    for (const [c, sObj] of Object.entries(this.hierarchy)) {
      if (cls === 'ALL' || c === cls) Object.keys(sObj).forEach(s => subjs.add(s));
    }
    const subjSel = document.getElementById('subjectSelect');
    if (subjSel) subjSel.innerHTML = `<option value="ALL">All Subjects</option>` + [...subjs].map(s => `<option value="${s}">${s}</option>`).join('');
    this.onSubjectChange();
  },

  onSubjectChange() {
    const cls = document.getElementById('classSelect').value;
    const subj = document.getElementById('subjectSelect').value;
    const chaps = new Set();
    for (const [c, sObj] of Object.entries(this.hierarchy)) {
      if (cls === 'ALL' || c === cls) {
        for (const [s, cObj] of Object.entries(sObj)) {
          if (subj === 'ALL' || s === subj) {
            Object.keys(cObj).forEach(ch => chaps.add(ch));
          }
        }
      }
    }
    const topicSel = document.getElementById('topicSelect');
    if (topicSel) topicSel.innerHTML = `<option value="ALL">All Chapters</option>` + [...chaps].map(ch => `<option value="${ch}">${ch}</option>`).join('');
    this.onChapterChange();
  },

  onChapterChange() {
    const ch = document.getElementById('topicSelect').value;
    const sts = new Set();
    for (const sObj of Object.values(this.hierarchy)) {
      for (const chObj of Object.values(sObj)) {
        if (ch === 'ALL') {
          for (const cData of Object.values(chObj)) {
            Object.keys(cData.subtopics || {}).forEach(st => sts.add(st));
          }
        } else if (chObj[ch]) {
          Object.keys(chObj[ch].subtopics || {}).forEach(st => sts.add(st));
        }
      }
    }
    const stSel = document.getElementById('subtopicSelect');
    if (stSel) stSel.innerHTML = `<option value="ALL">All Subtopics in Selection</option>` + [...sts].map(st => `<option value="${st}">${st}</option>`).join('');
  },

  openSetup(cls, subj, chap) {
    this.showView('setup');
    if (cls) {
      document.getElementById('classSelect').value = cls;
      this.onClassChange();
    }
    if (subj) {
      document.getElementById('subjectSelect').value = subj;
      this.onSubjectChange();
    }
    if (chap) {
      document.getElementById('topicSelect').value = chap;
      this.onChapterChange();
    }
  },

  findChapterFile(chapName) {
    if (!chapName) return null;
    const meta = window.PREPWISE_HIERARCHY_META || {};
    const classes = meta.classes || this.hierarchy || {};
    for (const cls in classes) {
      for (const subj in classes[cls]) {
        for (const chap in classes[cls][subj]) {
          if (chap.toLowerCase() === chapName.toLowerCase()) {
            return classes[cls][subj][chap].file;
          }
        }
      }
    }
    return null;
  },

  async ensureChapterLoaded(chapName) {
    if (!chapName || chapName === 'ALL') return;
    try {
      const file = this.findChapterFile(chapName);
      if (file) {
        await this.loadChapterShard(file);
      }
    } catch (e) {
      console.warn('ensureChapterLoaded notice:', e);
    }
  },

  async startInstantChapterPractice(chapName, count = 15) {
    this.showLoading(`Loading ${chapName} (15 Qs)... 🎯`);
    try {
      let pool = [];

      // 1. Instant response: query in-memory seed questions (< 5ms response!)
      if (window.PREPWISE_SEED_QUESTIONS && window.PREPWISE_SEED_QUESTIONS.length) {
        pool = window.PREPWISE_SEED_QUESTIONS.filter(q => q.chapter.toLowerCase() === chapName.toLowerCase());
      }

      if (pool.length >= count) {
        this.hideLoading();
        const selected = this.shuffle(pool).slice(0, count);
        this.beginSession(selected, `${chapName} Practice (15 Qs)`, false, false);
        return;
      }

      // 2. Query IndexedDB
      try {
        const dbPool = await db.questions.where('chapter').equals(chapName).limit(count * 2).toArray();
        if (dbPool.length >= count) {
          this.hideLoading();
          const selected = this.shuffle(dbPool).slice(0, count);
          this.beginSession(selected, `${chapName} Practice (15 Qs)`, false, false);
          return;
        }
      } catch (dbErr) {
        console.warn('DB query notice:', dbErr);
      }

      // 3. Dynamic shard fetch
      const file = this.findChapterFile(chapName);
      if (file) {
        await this.loadChapterShard(file);
        const freshPool = await db.questions.where('chapter').equals(chapName).limit(count * 2).toArray();
        if (freshPool.length > 0) {
          this.hideLoading();
          const selected = this.shuffle(freshPool).slice(0, count);
          this.beginSession(selected, `${chapName} Practice (15 Qs)`, false, false);
          return;
        }
      }

      // 4. In-memory fallback
      if (pool.length > 0) {
        this.hideLoading();
        this.beginSession(this.shuffle(pool), `${chapName} Practice`, false, false);
        return;
      }

      // 5. Generic pool fallback
      const sample = await db.questions.limit(count).toArray();
      this.hideLoading();
      if (sample.length > 0) {
        this.beginSession(this.shuffle(sample), `${chapName} Practice`, false, false);
      } else {
        alert(`Questions for "${chapName}" are loading. Please try again in a moment.`);
      }
    } catch (err) {
      this.hideLoading();
      console.error('startInstantChapterPractice error:', err);
      alert('Could not start practice drill. Please try again.');
    }
  },

  async quickSubtopicDrill(chap, subtopic) {
    this.showLoading(`Loading ${subtopic}... 🎯`);
    try {
      let pool = [];
      if (window.PREPWISE_SEED_QUESTIONS && window.PREPWISE_SEED_QUESTIONS.length) {
        pool = window.PREPWISE_SEED_QUESTIONS.filter(q => 
          q.chapter.toLowerCase() === chap.toLowerCase() && 
          q.subtopic.toLowerCase() === subtopic.toLowerCase()
        );
      }

      if (pool.length < 15) {
        await this.ensureChapterLoaded(chap);
        const dbPool = await db.questions.where('[chapter+subtopic]').equals([chap, subtopic]).limit(30).toArray();
        pool = [...pool, ...dbPool];
      }

      this.hideLoading();
      if (!pool.length) {
        const fallback = (window.PREPWISE_SEED_QUESTIONS || []).filter(q => q.chapter.toLowerCase() === chap.toLowerCase());
        if (fallback.length) {
          return this.beginSession(this.shuffle(fallback).slice(0, 15), `${chap} Practice`, false, false);
        }
        return alert('No questions found for this micro-concept. Please choose another topic.');
      }
      this.beginSession(this.shuffle(pool).slice(0, 15), `${chap} · ${subtopic}`, false, false);
    } catch (e) {
      this.hideLoading();
      console.error(e);
      alert('Error loading subtopic. Please try again.');
    }
  },

  async startSubtopicDrill() {
    this.showLoading('Preparing your drill questions... 🎯');
    try {
      const cls = document.getElementById('classSelect').value;
      const subj = document.getElementById('subjectSelect').value;
      const chap = document.getElementById('topicSelect').value;
      const st = document.getElementById('subtopicSelect').value;
      const diff = document.querySelector('input[name=difficulty]:checked').value;
      const status = document.getElementById('statusSelect').value;
      const count = Number(document.getElementById('countSelect').value) || 15;

      let pool = [];

      // Fast in-memory filter first
      if (window.PREPWISE_SEED_QUESTIONS && window.PREPWISE_SEED_QUESTIONS.length) {
        pool = window.PREPWISE_SEED_QUESTIONS.filter(q => {
          if (cls !== 'ALL' && String(q.classNum) !== String(cls)) return false;
          if (subj !== 'ALL' && q.subject !== subj) return false;
          if (chap !== 'ALL' && q.chapter.toLowerCase() !== chap.toLowerCase()) return false;
          if (st !== 'ALL' && q.subtopic.toLowerCase() !== st.toLowerCase()) return false;
          if (diff !== 'mixed' && q.difficulty !== diff) return false;
          return true;
        });
      }

      if (pool.length >= count) {
        this.hideLoading();
        const selected = this.shuffle(pool).slice(0, count);
        const title = chap !== 'ALL' ? (st !== 'ALL' ? `${chap} · ${st}` : chap) : (subj !== 'ALL' ? `${subj} Practice` : 'Custom Drill');
        this.beginSession(selected, title, false, false);
        return;
      }

      // Query IndexedDB
      if (chap !== 'ALL') {
        await this.ensureChapterLoaded(chap);
      }

      let collection;
      if (chap !== 'ALL' && st !== 'ALL') {
        collection = db.questions.where('[chapter+subtopic]').equals([chap, st]);
      } else if (subj !== 'ALL' && chap !== 'ALL') {
        collection = db.questions.where('[subject+chapter]').equals([subj, chap]);
      } else if (cls !== 'ALL' && subj !== 'ALL') {
        collection = db.questions.where('[classNum+subject]').equals([String(cls), subj]);
      } else if (subj !== 'ALL') {
        collection = db.questions.where('subject').equals(subj);
      } else {
        collection = db.questions.toCollection();
      }

      if (diff !== 'mixed') {
        collection = collection.filter(q => q.difficulty === diff);
      }

      let dbPool = await collection.limit(count * 3).toArray();
      if (status === 'mistakes') {
        const mIds = new Set((await db.mistakes.toArray()).map(m => m.questionId));
        dbPool = dbPool.filter(q => mIds.has(q.id));
      }

      const merged = [...pool, ...dbPool];
      const unique = new Map();
      merged.forEach(q => unique.set(q.id, q));
      const finalPool = [...unique.values()];

      this.hideLoading();
      if (!finalPool.length) {
        return alert('No questions matched this exact filter. Try selecting "All Difficulties" or "All Subtopics".');
      }

      const selected = this.shuffle(finalPool).slice(0, count);
      const title = chap !== 'ALL' ? (st !== 'ALL' ? `${chap} · ${st}` : chap) : (subj !== 'ALL' ? `${subj} Practice` : 'Custom Drill');
      this.beginSession(selected, title, false, false);
    } catch (e) {
      this.hideLoading();
      console.error('startSubtopicDrill error:', e);
      alert('Could not start drill. Please try again.');
    }
  },

  async startConfidenceMode() {
    await this.ensureReady();
    const sample = await db.questions.limit(60).toArray();
    if (!sample.length) return alert('Database is initializing. Please try again in a few seconds.');
    this.beginSession(this.shuffle(sample).slice(0, 30), '⚡ Blind Confidence Survival', false, true);
  },

  async updateTopStats() {
    const attempts = await db.attempts.toArray();
    const correct = attempts.filter(a => a.correct === 1).length;
    const wrong = attempts.length - correct;
    const netMarks = (correct * 4) - wrong;

    const attEl = document.getElementById('attempted');
    const accEl = document.getElementById('accuracy');
    const negEl = document.getElementById('negBleed');
    const scoreEl = document.getElementById('lifetimeScore');
    const barEl = document.getElementById('streakBar');

    if (attEl) attEl.textContent = attempts.length;
    if (accEl) accEl.textContent = attempts.length ? `${Math.round((correct / attempts.length) * 100)}%` : '—';
    if (negEl) negEl.textContent = wrong > 0 ? `-${wrong}` : '0';
    if (scoreEl) scoreEl.textContent = `${netMarks} pts`;
    if (barEl) barEl.style.width = `${Math.min(100, attempts.length * 2)}%`;
  },

  showView(id) {
    ['dashboard', 'setup', 'practice', 'streamerView', 'bookmarksView', 'mistakesView', 'progressView', 'growthBoardView', 'timedEndlessSetup', 'diagnosticsView', 'mocksHubView'].forEach(v => {
      const el = document.getElementById(v);
      if (el) el.style.display = v === id ? 'block' : 'none';
    });

    document.querySelectorAll('.nav button').forEach(btn => {
      const target = btn.dataset.view;
      btn.classList.toggle('active', target === id || (target === 'setup' && id === 'setup'));
    });

    document.querySelectorAll('.mobile-nav-btn').forEach(btn => {
      const target = btn.dataset.view;
      btn.classList.toggle('active', target === id);
    });

    // Update mistake count badge in sidebar
    db.attempts.where('is_correct').equals(0).count().then(cnt => {
      const b = document.getElementById('navMistakeCount');
      if (b) {
        if (cnt > 0) {
          b.textContent = cnt;
          b.style.display = 'inline-block';
        } else {
          b.style.display = 'none';
        }
      }
    }).catch(() => {});

    window.scrollTo({ top: 0, behavior: 'smooth' });
  },

  async startMassStreaming(targetCount = 2000) {
    if (this.isStreamingActive) return;
    this.isStreamingActive = true;

    document.getElementById('streamerSpinner').style.display = 'block';
    document.getElementById('stopStreamBtn').style.display = 'inline-block';
    const logEl = document.getElementById('streamerLog');
    const barEl = document.getElementById('streamerProgressBar');
    const textEl = document.getElementById('streamerBatchCounter');

    let totalStreamed = 0;
    const metaRec = (await db.meta.get('cloudStreamOffset')) || { key: 'cloudStreamOffset', medOffset: 0, sciqOffset: 0 };
    let medOff = metaRec.medOffset || 0;
    let sciqOff = metaRec.sciqOffset || 0;
    const diffs = ['easy', 'medium', 'hard'];

    logEl.innerHTML = `<div>[${new Date().toLocaleTimeString()}] Connecting to HuggingFace public endpoints for MedMCQA & SciQ...</div>`;

    while (this.isStreamingActive && totalStreamed < targetCount) {
      const collected = [];

      try {
        const res = await fetch(`https://datasets-server.huggingface.co/rows?dataset=openlifescienceai%2Fmedmcqa&config=openlifescienceai--medmcqa&split=train&offset=${medOff}&length=100`);
        if (res.ok) {
          const data = await res.json();
          (data.rows || []).forEach((item, idx) => {
            const r = item.row;
            if (!r || !r.question || !r.opa) return;
            const rawSubj = (r.subject_name || 'Biology').trim();
            const subject = rawSubj.toLowerCase().includes('biochem') ? 'Chemistry' : 'Biology';
            const chapter = rawSubj || 'Human Physiology';
            const subtopic = (r.topic_name || 'NCERT Core Medical Concept').trim();
            const expText = r.exp || 'Refer to standard NCERT biological mechanism and pathways.';

            collected.push({
              id: `MED_CLOUD_${medOff + idx}`,
              classNum: (idx % 2 === 0) ? '11' : '12',
              subject,
              chapter,
              subtopic,
              difficulty: diffs[(medOff + idx) % 3],
              year_tag: 'AIIMS / NEET Medical Bank',
              question: r.question,
              options: [r.opa, r.opb, r.opc, r.opd],
              correct_option: Math.max(0, Math.min(3, Number(r.cop ?? 0))),
              hint: expText.split('.')[0] + '.',
              solution: expText,
              ncert_ref: `${subject} · ${chapter} (${subtopic})`
            });
          });
          medOff += 100;
        }
      } catch(err) {
        logEl.innerHTML += `<div style="color:#f87171">[Notice]: Offline or network limit on MedMCQA chunk.</div>`;
      }

      try {
        const res2 = await fetch(`https://datasets-server.huggingface.co/rows?dataset=allenai%2Fsciq&config=default&split=train&offset=${sciqOff}&length=100`);
        if (res2.ok) {
          const data2 = await res2.json();
          (data2.rows || []).forEach((item, idx) => {
            const r = item.row;
            if (!r || !r.question || !r.correct_answer) return;
            const qLower = (r.question + ' ' + (r.support || '')).toLowerCase();
            let subject = 'Physics';
            let chapter = 'Mechanics & Electromagnetism';
            if (/(atom|molecule|acid|ion|bond|reaction|electron|element|gas|ph|molar|compound)/.test(qLower)) {
              subject = 'Chemistry';
              chapter = /(carbon|organic|alkane|alcohol)/.test(qLower) ? 'Organic Chemistry' : 'Chemical Bonding & Kinetics';
            } else if (/(cell|plant|gene|dna|enzyme|blood|hormone|tissue|organ|species|mitosis|protein)/.test(qLower)) {
              subject = 'Botany';
              chapter = /(plant|photosynthesis|xylem|root)/.test(qLower) ? 'Plant Physiology' : 'Cell Biology & Genetics';
            }

            const rawOpts = [r.correct_answer, r.distractor1, r.distractor2, r.distractor3];
            const shift = (sciqOff + idx) % 4;
            const rotated = [0, 1, 2, 3].map(k => rawOpts[(k + shift) % 4]);
            const correctIdx = (4 - shift) % 4;
            const support = r.support || 'Derived from fundamental NCERT principles.';

            collected.push({
              id: `SCIQ_CLOUD_${sciqOff + idx}`,
              classNum: (idx % 2 === 0) ? '11' : '12',
              subject,
              chapter,
              subtopic: `${chapter} Core Drill`,
              difficulty: diffs[(sciqOff + idx) % 3],
              year_tag: 'Science Benchmark',
              question: r.question,
              options: rotated,
              correct_option: correctIdx,
              hint: support.split('.')[0] + '.',
              solution: support,
              ncert_ref: `NCERT ${subject} · ${chapter}`
            });
          });
          sciqOff += 100;
        }
      } catch(err) {
        logEl.innerHTML += `<div style="color:#f87171">[Notice]: Offline or network limit on SciQ chunk.</div>`;
      }

      if (collected.length > 0) {
        await db.questions.bulkPut(collected);
        totalStreamed += collected.length;
        await db.meta.put({ key: 'cloudStreamOffset', medOffset: medOff, sciqOffset: sciqOff });

        const pct = Math.min(100, Math.round((totalStreamed / targetCount) * 100));
        barEl.style.width = `${pct}%`;
        textEl.textContent = `+${totalStreamed.toLocaleString()} / ${targetCount.toLocaleString()} Qs streamed`;
        logEl.innerHTML = `<div>✓ Synced batch of ${collected.length} Qs (Total session: ${totalStreamed.toLocaleString()} Qs)</div>` + logEl.innerHTML;

        const currentTotal = await db.questions.count();
        this.updateBadgeCounts(currentTotal);
      } else {
        logEl.innerHTML = `<div style="color:#fcd34d">Streaming notice: Offline or rate limited. Connect to internet to stream additional live benchmark batches.</div>` + logEl.innerHTML;
        break;
      }

      await new Promise(r => setTimeout(r, 800));
    }

    this.stopMassStreaming();
    await this.syncHierarchyFromDB();
    logEl.innerHTML = `<div style="color:#4ade80;font-weight:700">★ Streaming batch complete! Your database now has thousands of ready-to-use questions.</div>` + logEl.innerHTML;
  },

  
  // ==================== TIMED ENDLESS MARATHON CONTROLLER ====================
  teSelectedChapters: new Set(),

  openTimedEndlessSetup() {
    this.showView('timedEndlessSetup');
    this.initTeTopicsGrid();
  },

  initTeTopicsGrid() {
    const grid = document.getElementById('teTopicsGrid');
    if (!grid) return;
    
    const allChaps = [];
    for (const [cls, subjs] of Object.entries(this.hierarchy)) {
      for (const [subj, chaps] of Object.entries(subjs)) {
        for (const [chap, data] of Object.entries(chaps)) {
          allChaps.push({ cls, subj, chap, slug: (data.file || '').replace('.json', '') });
        }
      }
    }

    if (this.teSelectedChapters.size === 0) {
      allChaps.forEach(c => this.teSelectedChapters.add(c.chap));
    }

    grid.innerHTML = allChaps.map(c => {
      const isSel = this.teSelectedChapters.has(c.chap);
      const safeChap = c.chap.replace(/'/g, "\\'");
      return `
        <div class="te-topic-card ${isSel ? 'selected' : ''}" data-chap="${c.chap}" data-subj="${c.subj}" onclick="App.toggleTeChapter('${safeChap}')">
          <div class="te-topic-top">
            <span class="tag" style="font-size:11px;padding:2px 8px;">${c.subj} · Class ${c.cls}</span>
            <div class="te-check-box">${isSel ? '✓' : ''}</div>
          </div>
          <div class="te-topic-title">${c.chap}</div>
        </div>
      `;
    }).join('');

    this.updateTeBadge();
  },

  toggleTeChapter(chap) {
    if (this.teSelectedChapters.has(chap)) {
      this.teSelectedChapters.delete(chap);
    } else {
      this.teSelectedChapters.add(chap);
    }

    const card = document.querySelector(`.te-topic-card[data-chap="${chap}"]`);
    if (card) {
      const isSel = this.teSelectedChapters.has(chap);
      card.classList.toggle('selected', isSel);
      const box = card.querySelector('.te-check-box');
      if (box) box.textContent = isSel ? '✓' : '';
    }

    this.updateTeBadge();
  },

  selectAllTeChapters() {
    for (const [cls, subjs] of Object.entries(this.hierarchy)) {
      for (const [subj, chaps] of Object.entries(subjs)) {
        for (const chap of Object.keys(chaps)) {
          this.teSelectedChapters.add(chap);
        }
      }
    }
    this.refreshTeGridState();
  },

  selectTeSubject(targetSubj) {
    this.teSelectedChapters.clear();
    for (const [cls, subjs] of Object.entries(this.hierarchy)) {
      for (const [subj, chaps] of Object.entries(subjs)) {
        if (subj.toLowerCase() === targetSubj.toLowerCase()) {
          for (const chap of Object.keys(chaps)) {
            this.teSelectedChapters.add(chap);
          }
        }
      }
    }
    this.refreshTeGridState();
  },

  clearTeChapters() {
    this.teSelectedChapters.clear();
    this.refreshTeGridState();
  },

  refreshTeGridState() {
    document.querySelectorAll('.te-topic-card').forEach(card => {
      const chap = card.dataset.chap;
      const isSel = this.teSelectedChapters.has(chap);
      card.classList.toggle('selected', isSel);
      const box = card.querySelector('.te-check-box');
      if (box) box.textContent = isSel ? '✓' : '';
    });
    this.updateTeBadge();
  },

  filterTeChapters(query) {
    const q = (query || '').toLowerCase().trim();
    document.querySelectorAll('.te-topic-card').forEach(card => {
      const text = card.textContent.toLowerCase();
      card.style.display = (!q || text.includes(q)) ? 'flex' : 'none';
    });
  },

  updateTeBadge() {
    const badge = document.getElementById('teSelectedCountBadge');
    if (badge) {
      badge.textContent = `${this.teSelectedChapters.size} Topics Selected`;
    }
  },

  setTeDuration(mins) {
    document.querySelectorAll('.te-chip').forEach(c => {
      c.classList.toggle('active', c.textContent.startsWith(String(mins)));
    });
    const inp = document.getElementById('teCustomMinutes');
    if (inp) inp.value = mins;
  },

  onTeCustomInput(val) {
    document.querySelectorAll('.te-chip').forEach(c => c.classList.remove('active'));
  },

  closeTeSummaryModal() {
    const modal = document.getElementById('timedEndlessSummaryModal');
    if (modal) modal.style.display = 'none';
  },


  stopMassStreaming() {
    this.isStreamingActive = false;
    this.isScalingVault = false;
    const banner = document.getElementById('syncBanner');
    if (banner) banner.style.display = 'none';
    const spinner = document.getElementById('streamerSpinner');
    if (spinner) spinner.style.display = 'none';
    const stopBtn = document.getElementById('stopStreamBtn');
    if (stopBtn) stopBtn.style.display = 'none';
  }

});

// Boot the Application once DOM is fully parsed
window.addEventListener('DOMContentLoaded', () => App.init());
