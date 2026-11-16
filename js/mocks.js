// js/mocks.js - Full Mocks Hub (720-Mark National Benchmark Papers, Sprints, NTA Modal & Configurator)
window.App = window.App || {};

Object.assign(window.App, {
  async showMocksHub() {
    this.showView('mocksHubView');
    await this.updateMockKpis();
    await this.renderMockHistoryTable();
  },

  async updateMockKpis() {
    const allSessions = await db.sessions.toArray();
    const mockSessions = allSessions.filter(s => s.isMock || s.maxMarks >= 180);

    const countEl = document.getElementById('kpiMockAttempts');
    const avgEl = document.getElementById('kpiAvgScore');
    const rankEl = document.getElementById('kpiRankEstimate');

    if (countEl) countEl.textContent = `${mockSessions.length} Papers`;

    if (mockSessions.length) {
      const totalScore = mockSessions.reduce((acc, s) => acc + s.netMarks, 0);
      const avg = Math.round(totalScore / mockSessions.length);
      if (avgEl) avgEl.textContent = `${avg} / 720`;

      // Project NEET All-India Rank
      let estRank = 'AIR ~35,000+';
      if (avg >= 700) estRank = 'AIR 1 - 150 (AIIMS Delhi)';
      else if (avg >= 680) estRank = 'AIR 151 - 1,500 (Top Central GMC)';
      else if (avg >= 650) estRank = 'AIR 1,501 - 8,000 (Top State GMC)';
      else if (avg >= 600) estRank = 'AIR 8,001 - 22,000 (Govt Medical College)';
      else if (avg >= 550) estRank = 'AIR 22,001 - 50,000 (State Quota / Semi-Govt)';
      else estRank = 'Subtopic Revision Recommended';

      if (rankEl) rankEl.textContent = estRank;
    } else {
      if (avgEl) avgEl.textContent = '— / 720';
      if (rankEl) rankEl.textContent = 'Ready to Predict';
    }
  },

  async renderMockHistoryTable() {
    const allSessions = await db.sessions.reverse().toArray();
    const mockSessions = allSessions.filter(s => s.isMock || s.maxMarks >= 180);
    const container = document.getElementById('fullMockHistoryList');
    if (!container) return;

    if (!mockSessions.length) {
      container.innerHTML = '<div class="empty">No full-length mock exams submitted yet. Launch Mock 01 above to establish your baseline score.</div>';
      return;
    }

    container.innerHTML = `
      <div style="overflow-x:auto">
        <table style="width:100%;border-collapse:collapse;font-size:13px;text-align:left;">
          <thead>
            <tr style="border-bottom:2px solid var(--line);color:var(--muted);">
              <th style="padding:10px 8px">Exam Title</th>
              <th style="padding:10px 8px">Marks Scored</th>
              <th style="padding:10px 8px">Accuracy</th>
              <th style="padding:10px 8px">Rank Projection</th>
              <th style="padding:10px 8px">Completed At</th>
            </tr>
          </thead>
          <tbody>
            ${mockSessions.map(s => {
              let proj = 'State Quota GMC';
              if (s.netMarks >= 680) proj = 'AIIMS / Central GMC';
              else if (s.netMarks >= 650) proj = 'Top State GMC';
              else if (s.netMarks >= 600) proj = 'Govt Medical College';
              else if (s.netMarks < 500) proj = 'Needs Revision';

              return `
                <tr style="border-bottom:1px solid var(--line);">
                  <td style="padding:12px 8px;font-weight:700;">${s.title}</td>
                  <td style="padding:12px 8px;"><b style="color:${s.netMarks >= 600 ? 'var(--emerald)' : 'var(--ink)'}">${s.netMarks}</b> / ${s.maxMarks}</td>
                  <td style="padding:12px 8px;"><span class="tag">${s.accuracy}%</span></td>
                  <td style="padding:12px 8px;color:var(--teal);font-weight:600;">${proj}</td>
                  <td style="padding:12px 8px;color:var(--muted);">${s.date}</td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    `;
  },

  showNtaInstructions(preset) {
    this.pendingMockPreset = preset;
    const modal = document.getElementById('ntaInstructionsModal');
    const chk = document.getElementById('ntaAgreeCheckbox');
    const btn = document.getElementById('ntaBeginExamBtn');
    const title = document.getElementById('ntaModalExamTitle');
    if (chk) chk.checked = false;
    if (btn) {
      btn.disabled = true;
      btn.style.opacity = '0.5';
      btn.style.cursor = 'not-allowed';
    }
    if (title) {
      const names = {
        'standard_01': 'NEET Mock 01: All-India National Benchmark',
        'aiims_02': 'NEET Mock 02: AIIMS Super-Challenger Paper',
        'ncert_03': 'NEET Mock 03: NCERT Pure Line-by-Line Paper',
        'pyq_04': 'NEET Mock 04: Past 5-Year High-Yield Repeats',
        'trap_05': 'NEET Mock 05: Speed Trap & Negative-Bleed Buster'
      };
      title.textContent = names[preset] || 'Official NTA Full Mock Examination';
    }
    if (modal) modal.style.display = 'flex';
  },

  closeNtaInstructions() {
    const modal = document.getElementById('ntaInstructionsModal');
    if (modal) modal.style.display = 'none';
    this.pendingMockPreset = null;
  },

  toggleNtaBeginButton() {
    const chk = document.getElementById('ntaAgreeCheckbox');
    const btn = document.getElementById('ntaBeginExamBtn');
    if (btn && chk) {
      btn.disabled = !chk.checked;
      btn.style.opacity = chk.checked ? '1' : '0.5';
      btn.style.cursor = chk.checked ? 'pointer' : 'not-allowed';
    }
  },

  confirmAndLaunchFullMock() {
    const preset = this.pendingMockPreset || 'standard_01';
    this.closeNtaInstructions();
    this.executeFullMockLaunch(preset);
  },

  launchFullMockPreset(preset) {
    this.showNtaInstructions(preset);
  },

  async executeFullMockLaunch(preset) {
    await this.ensureReady();

    // 1. Fetch 50 Physics (35 Sec A + 15 Sec B)
    const pAll = await db.questions.where('subject').equals('Physics').toArray();
    // 2. Fetch 50 Chemistry (35 Sec A + 15 Sec B)
    const cAll = await db.questions.where('subject').equals('Chemistry').toArray();
    // 3. Fetch 50 Botany (35 Sec A + 15 Sec B)
    let bAll = await db.questions.where('subject').equals('Botany').toArray();
    // 4. Fetch 50 Zoology (35 Sec A + 15 Sec B)
    let zAll = await db.questions.where('subject').equals('Zoology').toArray();

    // Fallback if tagged Biology
    if (!bAll.length && !zAll.length) {
      const bio = await db.questions.where('subject').equals('Biology').toArray();
      bAll = bio.slice(0, Math.floor(bio.length / 2));
      zAll = bio.slice(Math.floor(bio.length / 2));
    }

    let pPool = this.shuffle(pAll);
    let cPool = this.shuffle(cAll);
    let bPool = this.shuffle(bAll);
    let zPool = this.shuffle(zAll);

    let title = 'NEET-UG Full Mock 01 (National Benchmark)';
    if (preset === 'aiims_02') {
      title = 'NEET Full Mock 02: AIIMS Challenger Paper';
      pPool.sort((a,b) => (b.difficulty === 'hard' ? 1 : 0) - (a.difficulty === 'hard' ? 1 : 0));
      cPool.sort((a,b) => (b.difficulty === 'hard' ? 1 : 0) - (a.difficulty === 'hard' ? 1 : 0));
    } else if (preset === 'ncert_03') {
      title = 'NEET Full Mock 03: NCERT Pure Line-by-Line';
      bPool.sort((a,b) => (b.question_type === 'statement_based' ? 1 : 0) - (a.question_type === 'statement_based' ? 1 : 0));
      zPool.sort((a,b) => (b.question_type === 'statement_based' ? 1 : 0) - (a.question_type === 'statement_based' ? 1 : 0));
    } else if (preset === 'pyq_04') {
      title = 'NEET Full Mock 04: Past 5-Year High-Yield Repeats';
    } else if (preset === 'trap_05') {
      title = 'NEET Full Mock 05: Speed Trap & Negative-Bleed Buster';
      pPool.sort((a,b) => (b.question_type === 'diagnostic_trap' ? 1 : 0) - (a.question_type === 'diagnostic_trap' ? 1 : 0));
      cPool.sort((a,b) => (b.question_type === 'diagnostic_trap' ? 1 : 0) - (a.question_type === 'diagnostic_trap' ? 1 : 0));
    }

    // Assemble 50 questions per subject with Section A & Section B tags
    const pQs = pPool.slice(0, 50).map((q, i) => ({ ...q, subject: 'Physics', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
    const cQs = cPool.slice(0, 50).map((q, i) => ({ ...q, subject: 'Chemistry', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
    const bQs = bPool.slice(0, 50).map((q, i) => ({ ...q, subject: 'Botany', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
    const zQs = zPool.slice(0, 50).map((q, i) => ({ ...q, subject: 'Zoology', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));

    const paper = [...pQs, ...cQs, ...bQs, ...zQs];
    this.beginSession(paper, title, true, false, 200 * 60, true);
  },

  async launchSubjectMock(subject, count, durationMins) {
    await this.ensureReady();
    let questions = [];

    if (subject === 'Biology') {
      const bAll = await db.questions.where('subject').equals('Botany').toArray();
      const zAll = await db.questions.where('subject').equals('Zoology').toArray();
      const bSlice = this.shuffle(bAll).slice(0, 50).map((q, i) => ({ ...q, subject: 'Botany', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
      const zSlice = this.shuffle(zAll).slice(0, 50).map((q, i) => ({ ...q, subject: 'Zoology', section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
      questions = [...bSlice, ...zSlice];
    } else {
      const all = await db.questions.where('subject').equals(subject).toArray();
      questions = this.shuffle(all).slice(0, count).map((q, i) => ({ ...q, subject, section: i < 35 ? 'A' : 'B', secIndex: i < 35 ? i + 1 : i - 34 }));
    }

    this.beginSession(questions, `${subject} Complete Paper (${count} Qs)`, true, false, durationMins * 60, true);
  },

  startCustomMockModal() {
    const modal = document.getElementById('customMockModal');
    if (modal) modal.style.display = 'flex';
  },

  closeCustomMockModal() {
    const modal = document.getElementById('customMockModal');
    if (modal) modal.style.display = 'none';
  },

  async launchCustomMockFromModal() {
    const syllabus = document.getElementById('cmSyllabus').value;
    const count = Number(document.getElementById('cmCount').value);
    const timerMins = Number(document.getElementById('cmTimer').value);
    const diff = document.getElementById('cmDiff').value;

    this.closeCustomMockModal();
    await this.ensureReady();

    let collection = db.questions.toCollection();
    if (syllabus === '11' || syllabus === '12') {
      collection = db.questions.where('classNum').equals(syllabus);
    }

    let all = await collection.toArray();
    if (syllabus === 'PC') {
      all = all.filter(q => q.subject === 'Physics' || q.subject === 'Chemistry');
    } else if (syllabus === 'BIO') {
      all = all.filter(q => q.subject === 'Botany' || q.subject === 'Zoology' || q.subject === 'Biology');
    }

    if (diff !== 'mixed') {
      all = all.filter(q => q.difficulty === diff);
    }

    const selected = this.shuffle(all).slice(0, count).map((q, i) => ({
      ...q,
      section: i < 35 ? 'A' : 'B',
      secIndex: i < 35 ? i + 1 : i - 34
    }));

    if (!selected.length) return alert('No questions found matching this filter.');

    const durationSec = timerMins > 0 ? timerMins * 60 : 0;
    this.beginSession(selected, `Custom NEET Mock (${selected.length} Qs)`, true, false, durationSec, count >= 100);
  },

  // ==================== CBT EXAM & DRILL ENGINE ====================
});
