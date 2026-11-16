// js/engine.js - NTA CBT Simulation & Practice Engine (Section A/B, Progressive Hints, Adaptive Solutions)
window.App = window.App || {};

Object.assign(window.App, {
  
  // ==================== TIMED ENDLESS MARATHON ENGINE ====================
  isTimedEndless: false,
  teTimer: null,
  teSecLeft: 3600,
  teTotalSec: 3600,
  teAttemptsCount: 0,
  teCorrectCount: 0,
  teWrongCount: 0,
  teChapters: [],
  teDifficulty: 'random',

  async startTimedEndlessSession() {
    await this.ensureReady();
    const customMins = parseInt(document.getElementById('teCustomMinutes')?.value, 10);
    const durationMins = (customMins && customMins > 0) ? customMins : 60;
    const diff = document.querySelector('input[name=teDiff]:checked')?.value || 'random';
    
    if (!this.teSelectedChapters || this.teSelectedChapters.size === 0) {
      return alert('Please select at least one topic for your marathon.');
    }

    this.isTimedEndless = true;
    this.isMock = false;
    this.isFullNTA = false;
    this.isBlind = false;
    this.teDurationSec = durationMins * 60;
    this.teSecLeft = durationMins * 60;
    this.teChapters = Array.from(this.teSelectedChapters);
    this.teDifficulty = diff;
    this.teAttemptsCount = 0;
    this.teCorrectCount = 0;
    this.teWrongCount = 0;
    this.streak = 0;
    this.session = [];
    this.states = [];
    this.index = 0;

    this.showView('practice');
    document.getElementById('practiceEyebrow').textContent = `⏱ Timed Marathon (${durationMins} Mins)`;
    document.getElementById('practiceTitle').textContent = `${this.teChapters.length} Selected Topics (${diff.toUpperCase()})`;
    
    // UI elements
    const finishBtn = document.getElementById('teEarlyFinishBtn');
    if (finishBtn) finishBtn.style.display = 'block';
    const cdEl = document.getElementById('mockCountdown');
    if (cdEl) {
      cdEl.style.display = 'block';
      cdEl.classList.remove('timer-pulse-red');
    }
    const paceEl = document.getElementById('cbtPacingBadge');
    if (paceEl) {
      paceEl.style.display = 'block';
      paceEl.textContent = '⏱️ Pacing: 0s / Q';
    }

    document.getElementById('cbtPaletteWrap').style.display = 'none';
    document.getElementById('cbtSubjectTabsWrap').style.display = 'none';
    document.getElementById('confidenceStreakBadge').style.display = 'none';

    // Start countdown timer
    clearInterval(this.teTimer);
    clearInterval(this.mockTimer);
    this.teTimer = setInterval(() => {
      this.teSecLeft--;
      const hours = Math.floor(this.teSecLeft / 3600);
      const mins = Math.floor((this.teSecLeft % 3600) / 60);
      const secs = String(this.teSecLeft % 60).padStart(2, '0');
      if (cdEl) {
        cdEl.textContent = hours > 0 ? `${hours}:${String(mins).padStart(2,'0')}:${secs}` : `${mins}:${secs}`;
        if (this.teSecLeft <= 300) {
          cdEl.classList.add('timer-pulse-red');
        }
      }

      // Update live pacing
      if (this.teAttemptsCount > 0 && paceEl) {
        const elapsed = this.teDurationSec - this.teSecLeft;
        const avg = Math.round(elapsed / this.teAttemptsCount);
        paceEl.textContent = `⏱️ Pace: ${avg}s/Q (${this.teAttemptsCount} Qs Attempted)`;
      }

      if (this.teSecLeft <= 0) {
        clearInterval(this.teTimer);
        alert('⏱ Marathon time is up! Submitting your marathon results.');
        this.finishTimedEndlessSession();
      }
    }, 1000);

    // Load first question
    await this.loadNextTimedEndlessQuestion();
  },

  async loadNextTimedEndlessQuestion() {
    const chap = this.teChapters[Math.floor(Math.random() * this.teChapters.length)];
    await this.ensureChapterLoaded(chap);

    const diff = (this.teDifficulty === 'random')
      ? ['easy', 'medium', 'hard'][Math.floor(Math.random() * 3)]
      : this.teDifficulty;

    let pool = await db.questions.where('chapter').equals(chap).filter(q => q.difficulty === diff).limit(40).toArray();
    if (!pool.length) {
      pool = await db.questions.where('chapter').equals(chap).limit(40).toArray();
    }

    let q;
    const usedIds = new Set(this.session.map(sq => sq.id));
    const available = pool.filter(cand => !usedIds.has(cand.id));

    if (available.length > 0) {
      q = available[Math.floor(Math.random() * available.length)];
    } else {
      // Procedural on-demand question synthesis
      q = this.generate10LakhQuestion(Date.now() + this.session.length, 'Physics', chap, null, diff);
    }

    this.session.push(q);
    this.states.push({
      picked: null,
      locked: false,
      review: false,
      visited: true,
      timeSpent: 0,
      unlockedHints: 0,
      hintsCollapsed: false,
      showFullSolution: false
    });

    this.renderQuestion();
  },

  async finishTimedEndlessSession() {
    clearInterval(this.teTimer);
    clearInterval(this.qTimer);

    const finishBtn = document.getElementById('teEarlyFinishBtn');
    if (finishBtn) finishBtn.style.display = 'none';

    const elapsedSec = Math.max(1, this.teDurationSec - this.teSecLeft);
    const durationMins = Math.round(elapsedSec / 60) || 1;
    const totalQ = this.teAttemptsCount;
    const cor = this.teCorrectCount;
    const wrg = this.teWrongCount;
    const net = (cor * 4) - wrg;
    const acc = totalQ ? Math.round((cor / totalQ) * 100) : 0;
    const avgPace = totalQ ? Math.round(elapsedSec / totalQ) : 0;

    await db.sessions.add({
      title: `⏱ Timed Marathon (${durationMins}m)`,
      netMarks: net,
      maxMarks: Math.max(1, totalQ * 4),
      accuracy: acc,
      isMock: false,
      date: new Date().toLocaleDateString('en-GB')
    });

    await this.updateTopStats();

    // Show summary modal
    const modal = document.getElementById('timedEndlessSummaryModal');
    const body = document.getElementById('teModalBody');
    if (modal && body) {
      body.innerHTML = `
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));gap:12px;margin-bottom:18px;">
          <div style="background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px;text-align:center;">
            <small style="color:var(--muted)">Questions Done</small>
            <div style="font-size:26px;font-weight:800;font-family:'Space Grotesk'">${totalQ}</div>
          </div>
          <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#166534">Correct (+4)</small>
            <div style="font-size:26px;font-weight:800;color:var(--emerald);font-family:'Space Grotesk'">${cor}</div>
          </div>
          <div style="background:#fff1f2;border:1px solid #fecdd3;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#9f1239">Wrong (-1)</small>
            <div style="font-size:26px;font-weight:800;color:var(--red);font-family:'Space Grotesk'">${wrg}</div>
          </div>
          <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#1e40af">Accuracy</small>
            <div style="font-size:26px;font-weight:800;color:#0284c7;font-family:'Space Grotesk'">${acc}%</div>
          </div>
          <div style="background:#faf5ff;border:1px solid #e9d5ff;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#6b21a8">Net Score</small>
            <div style="font-size:26px;font-weight:800;color:var(--purple);font-family:'Space Grotesk'">${net} pts</div>
          </div>
          <div style="background:#fefce8;border:1px solid #fef08a;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#854d0e">Avg Pacing</small>
            <div style="font-size:26px;font-weight:800;color:#b45309;font-family:'Space Grotesk'">${avgPace}s / Q</div>
          </div>
        </div>

        <div style="background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:14px;font-size:13.5px;line-height:1.5;">
          <b>Marathon Summary:</b> Practiced continuously across <b>${this.teChapters.length} topics</b> for <b>${durationMins} minutes</b>.
          ${wrg > 0 ? `<br><span style="color:var(--red)">• ${wrg} mistakes were automatically logged into your Mistake Vault for root-cause tagging and revision.</span>` : '<br><span style="color:var(--emerald)">• Clean sheet! Zero negative mark bleed in this entire marathon.</span>'}
        </div>
      `;
      modal.style.display = 'flex';
    }

    this.isTimedEndless = false;
  },


  beginSession(questions, title, isMock, isBlind, durationSec = 12000, isFullNTA = false) {
    this.session = questions;
    this.states = questions.map(() => ({
      picked: null,
      locked: false,
      review: false,
      visited: false,
      timeSpent: 0,
      unlockedHints: 0,
      hintsCollapsed: false,
      showFullSolution: false
    }));
    this.index = 0;
    this.isMock = isMock;
    this.isFullNTA = isFullNTA;
    this.isBlind = isBlind;
    this.streak = 0;
    this.mockSecLeft = durationSec;
    this.mockTotalSec = durationSec;
    this.activeSubjectTab = questions[0]?.subject || 'Physics';

    this.showView('practice');
    document.getElementById('practiceEyebrow').textContent = isMock ? 'Official NTA CBT Simulation' : (isBlind ? 'Blind Survival Mode' : 'Subtopic Drill');
    document.getElementById('practiceTitle').textContent = title;
    document.getElementById('confidenceStreakBadge').style.display = isBlind ? 'block' : 'none';
    document.getElementById('cbtPaletteWrap').style.display = isMock ? 'block' : 'none';
    document.getElementById('cbtSubjectTabsWrap').style.display = (isMock && isFullNTA) ? 'block' : 'none';
    document.getElementById('cbtPacingBadge').style.display = isMock ? 'block' : 'none';

    const cdEl = document.getElementById('mockCountdown');
    if (cdEl) {
      cdEl.style.display = (isMock && durationSec > 0) ? 'block' : 'none';
    }

    clearInterval(this.mockTimer);
    if (isMock && durationSec > 0) {
      this.mockTimer = setInterval(() => {
        this.mockSecLeft--;
        const hours = Math.floor(this.mockSecLeft / 3600);
        const mins = Math.floor((this.mockSecLeft % 3600) / 60);
        const secs = String(this.mockSecLeft % 60).padStart(2, '0');
        cdEl.textContent = hours > 0 ? `${hours}:${String(mins).padStart(2,'0')}:${secs}` : `${mins}:${secs}`;

        // Live pacing indicator
        const answeredCount = this.states.filter(s => s.picked !== null).length;
        const elapsedSec = this.mockTotalSec - this.mockSecLeft;
        if (answeredCount > 0 && elapsedSec > 0) {
          const avgPerQ = Math.round(elapsedSec / answeredCount);
          const paceEl = document.getElementById('cbtPacingBadge');
          if (paceEl) {
            let status = '⚡ Great pace (<60s)';
            if (avgPerQ > 90) status = '⚠️ Pace slow (>90s)';
            paceEl.textContent = `⏱️ Avg: ${avgPerQ}s/Q (${status})`;
          }
        }

        if (this.mockSecLeft <= 0) {
          clearInterval(this.mockTimer);
          alert('Time is up! Submitting your exam automatically.');
          this.finishSession();
        }
      }, 1000);
    }

    this.renderQuestion();
  },

  switchSubjectTab(subject) {
    this.activeSubjectTab = subject;
    const targetIdx = this.session.findIndex(q => q.subject === subject);
    if (targetIdx !== -1) {
      this.jumpToQuestion(targetIdx);
    }
  },

  async renderQuestion() {
    const q = this.session[this.index];
    const st = this.states[this.index];
    st.visited = true;

    if (q.subject) this.activeSubjectTab = q.subject;

    // Update Subject Tabs Active State
    document.querySelectorAll('.subj-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.textContent.toLowerCase().includes(this.activeSubjectTab.toLowerCase()));
    });

    // Update Section Indicator (Section A vs Section B)
    const secLabel = document.getElementById('cbtSectionLabel');
    const secProg = document.getElementById('cbtSectionProgress');
    if (secLabel && this.isFullNTA) {
      const isSecA = (q.section === 'A' || !q.section);
      secLabel.textContent = `${q.subject} · Section ${isSecA ? 'A (Q1–Q35: Mandatory)' : 'B (Q36–Q50: Attempt any 10)'}`;

      // Count attempted in this subject's Section B
      if (!isSecA) {
        const secBAttempted = this.session.filter((sq, si) => sq.subject === q.subject && sq.section === 'B' && this.states[si].picked !== null).length;
        if (secProg) secProg.textContent = `${secBAttempted} / 10 Attempted (Max 10)`;
      } else {
        const secAAttempted = this.session.filter((sq, si) => sq.subject === q.subject && (sq.section === 'A' || !sq.section) && this.states[si].picked !== null).length;
        if (secProg) secProg.textContent = `${secAAttempted} / 35 Attempted`;
      }
    }

    clearInterval(this.qTimer);
    this.qStartTime = Date.now();
    this.qTimer = setInterval(() => {
      const sec = st.timeSpent + Math.floor((Date.now() - this.qStartTime) / 1000);
      document.getElementById('questionTimer').textContent = `${String(Math.floor(sec/60)).padStart(2,'0')}:${String(sec%60).padStart(2,'0')}s`;
    }, 500);

    document.getElementById('progress').style.width = `${((this.index + 1) / this.session.length) * 100}%`;
    document.getElementById('confidenceStreakBadge').textContent = `⚡ Streak: ${this.streak}`;

    const isSaved = Boolean(await db.bookmarks.get(q.id));

    const meta = this.isBlind && !st.locked
      ? `Q${this.index + 1} of ${this.session.length} · [Metadata Hidden in Confidence Mode]`
      : `Q${this.index + 1} of ${this.session.length} · Class ${q.classNum} · ${q.subject} · ${q.subtopic} · ${q.difficulty.toUpperCase()}`;

    const showLockedFeedback = !this.isMock && st.locked;

    const hintData = this.getQuestionHints(q);
    const unlocked = st.unlockedHints || 0;

    let actionsHtml = '';
    if (this.isMock) {
      actionsHtml = `
        <button class="secondary" onclick="App.toggleBookmark()" title="${isSaved ? 'Remove Bookmark' : 'Save Bookmark'}">${isSaved ? '★ Saved' : '☆ Bookmark'}</button>
        <button class="secondary" onclick="App.markForReview()" title="Mark for Review">${st.review ? '⚑ Clear Review' : '⚑ Mark Review'}</button>
        <button class="secondary" onclick="App.clearResponse()" title="Clear Response">Clear Response</button>
        ${this.index > 0 ? `<button class="secondary" onclick="App.prevQuestion()" title="Previous Question">← Previous</button>` : ''}
        <button class="primary" onclick="App.cbtSaveAndNext()" title="Save & Next">${this.index === this.session.length - 1 ? 'Save & Review Paper' : 'Save & Next →'}</button>
      `;
    } else {
      let hintBtnText = '';
      let hintBtnTitle = '';
      if (unlocked === 0) {
        hintBtnText = `💡 Unlock Hint 1 of ${hintData.maxHints} (${q.difficulty.toUpperCase()})`;
        hintBtnTitle = `Reveal Hint 1`;
      } else if (unlocked < hintData.maxHints) {
        hintBtnText = `💡 Unlock Hint ${unlocked + 1} of ${hintData.maxHints}`;
        hintBtnTitle = `Reveal Hint ${unlocked + 1}`;
      } else {
        hintBtnText = st.hintsCollapsed ? `💡 Show All ${hintData.maxHints} Hints` : `▲ Hide Hints (${hintData.maxHints}/${hintData.maxHints})`;
        hintBtnTitle = `Toggle Hints`;
      }

      actionsHtml = `
        <button class="secondary" onclick="App.unlockNextHint()" title="${hintBtnTitle}">${hintBtnText}</button>
        <button class="secondary" onclick="App.toggleBookmark()" title="${isSaved ? 'Remove Bookmark' : 'Save Bookmark'}">${isSaved ? '★ Saved' : '☆ Bookmark'}</button>
        ${!st.locked
          ? `<button class="primary" onclick="App.lockAnswer()" title="Lock Answer">Lock Answer (+4 / -1)</button>`
          : `<button class="primary" onclick="App.nextQuestion()" title="Next Question">${this.index === this.session.length - 1 ? 'Finish Drill Report' : 'Next Question →'}</button>`}
      `;
    }

    let feedbackHtml = '';
    if (showLockedFeedback) {
      const isCorrect = st.picked === q.correct_option;
      if (isCorrect) {
        // Correct answer -> Full solution immediately!
        feedbackHtml = `
          <div class="feedback" style="display:block;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:16px;margin-top:14px;">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
              <strong style="color:var(--emerald);font-size:1.1rem;display:flex;align-items:center;gap:6px;">✓ Correct (+4 Marks)</strong>
              <span class="tag" style="background:#dcfce7;color:var(--emerald);font-weight:700;">Full Solution Active</span>
            </div>
            <div style="margin-top:10px;">${q.solution || ''}</div>
            <small style="display:block;margin-top:10px;color:var(--muted)">📖 ${q.ncert_ref || 'NCERT Standard Reference'}</small>
          </div>
        `;
      } else {
        // Wrong answer -> Show focused diagnostic explanation with hints 1, 2, 3 and trap alert, with on-demand full solution!
        feedbackHtml = `
          <div class="wrong-diagnostic-box">
            <div class="wrong-diagnostic-title">
              <span>✕ Incorrect (-1 Mark)</span>
              <span class="tag" style="background:#fee2e2;color:#be123c;font-weight:700;">Negative Mark Bleed</span>
            </div>
            <p style="font-size:0.92rem;color:#475569;margin-bottom:12px;line-height:1.5;">
              <b>Diagnostic Explanation:</b> You marked option <b>${st.picked !== null ? 'ABCD'[st.picked] : 'None'}</b>, but the correct answer is <b>${'ABCD'[q.correct_option]}</b>. Review the distractor trap and progressive concept hints below:
            </p>
            
            <!-- Trap breakdown -->
            <div class="sol-section sol-traps" style="margin-top:8px;">
              <b>⚠️ Why Selected / Other Options are Common Traps:</b><br>
              ${hintData.traps || 'Common mistake in algebraic sign, formula inversion, or forgetting boundary conditions.'}
            </div>

            <!-- Progressive Hints Review for this difficulty -->
            <div style="margin-top:12px;">
              <div style="font-weight:700;font-size:0.85rem;color:var(--ink);text-transform:uppercase;letter-spacing:0.02em;margin-bottom:6px;">
                💡 Progressive Concept Hints (${q.difficulty.toUpperCase()} Level - ${hintData.maxHints} Steps):
              </div>
              <div class="unlocked-hints-list">
                ${hintData.hints.map(h => `
                  <div class="hint-tier-box" style="background:#ffffff;border-color:#fecdd3;border-left:4px solid #f43f5e;">
                    <div class="hint-tier-header" style="color:#e11d48;">${h.badge}</div>
                    <div class="hint-tier-body">${h.content}</div>
                  </div>
                `).join('')}
              </div>
            </div>

            <!-- On-Demand Full Solution Expansion -->
            ${st.showFullSolution ? `
              <div class="full-sol-wrapper">
                <hr style="border:0;border-top:1px dashed #cbd5e1;margin:16px 0;">
                <div style="font-weight:700;color:var(--teal);margin-bottom:8px;font-size:1.05rem;">📖 Complete Step-by-Step Derivation & Core Principle:</div>
                <div>${q.solution || ''}</div>
                <button class="secondary" style="margin-top:12px;" onclick="App.toggleFullSolution()" title="Collapse Solution">▲ Collapse Full Solution</button>
              </div>
            ` : `
              <div style="margin-top:14px;">
                <button class="primary" style="background:var(--teal);width:100%;font-weight:700;" onclick="App.toggleFullSolution()" title="Reveal Full Solution">
                  📖 Reveal Full Step-by-Step Solution & Derivation →
                </button>
              </div>
            `}

            <small style="display:block;margin-top:12px;color:var(--muted)">📖 ${q.ncert_ref || 'NCERT Standard Reference'}</small>
          </div>
        `;
      }
    }

    document.getElementById('questionArea').innerHTML = `
      <div class="question-card">
        <div class="q-meta">
          <span title="Curriculum Path">${meta}</span>
          <span class="tag" title="Exam Tag">${q.year_tag || 'NEET Bank'}</span>
        </div>
        <div class="question">${q.question}</div>
        <div class="answers">
          ${q.options.map((opt, i) => {
            let cls = '';
            if (st.picked === i) cls += ' selected';
            if (showLockedFeedback) {
              if (i === q.correct_option) cls += ' correct';
              else if (st.picked === i) cls += ' wrong';
            }
            return `
              <button class="answer ${cls}" onclick="App.chooseOption(${i})" title="Option ${'ABCD'[i]}">
                <b>${'ABCD'[i]}</b><span>${opt}</span>
              </button>
            `;
          }).join('')}
        </div>

        <!-- Progressive Hints Container -->
        <div class="hints-container" id="hintsContainer">
          ${unlocked > 0 && !st.hintsCollapsed ? `
            <div class="unlocked-hints-list">
              ${hintData.hints.slice(0, unlocked).map(h => `
                <div class="hint-tier-box">
                  <div class="hint-tier-header">${h.badge}</div>
                  <div class="hint-tier-body">${h.content}</div>
                </div>
              `).join('')}
            </div>
          ` : ''}
        </div>

        ${feedbackHtml}

        <div class="actions">${actionsHtml}</div>
      </div>
    `;

    if (this.isMock) this.renderPalette();
    this.typesetMath();
  },

  renderPalette() {
    const pal = document.getElementById('cbtPalette');
    if (!pal) return;

    let itemsToRender = this.states.map((st, idx) => ({ st, idx }));
    if (this.isFullNTA) {
      // Filter palette to currently active subject tab
      itemsToRender = itemsToRender.filter(({ idx }) => this.session[idx].subject === this.activeSubjectTab);
    }

    pal.innerHTML = itemsToRender.map(({ st, idx }) => {
      let statusCls = '';
      if (st.review && st.picked !== null) statusCls = 'review answered';
      else if (st.review) statusCls = 'review';
      else if (st.picked !== null) statusCls = 'answered';
      else if (st.visited) statusCls = 'visited';
      return `<button class="pal-btn ${statusCls} ${idx === this.index ? 'active' : ''}" onclick="App.jumpToQuestion(${idx})">${idx + 1}</button>`;
    }).join('');
  },

  jumpToQuestion(idx) {
    if (idx < 0 || idx >= this.session.length) return;
    const st = this.states[this.index];
    st.timeSpent += Math.floor((Date.now() - this.qStartTime) / 1000);
    this.index = idx;
    this.renderQuestion();
  },

  chooseOption(i) {
    const st = this.states[this.index];
    if (st.locked) return;
    st.picked = i;
    this.renderQuestion();
  },

  clearResponse() {
    const st = this.states[this.index];
    if (st.locked) return;
    st.picked = null;
    this.renderQuestion();
  },

  markForReview() {
    const st = this.states[this.index];
    st.review = !st.review;
    this.renderPalette();
  },

  cbtSaveAndNext() {
    const st = this.states[this.index];
    st.timeSpent += Math.floor((Date.now() - this.qStartTime) / 1000);
    if (this.index < this.session.length - 1) {
      this.index++;
      this.renderQuestion();
    } else {
      this.confirmFinishSession();
    }
  },

  prevQuestion() {
    if (this.index > 0) {
      const st = this.states[this.index];
      st.timeSpent += Math.floor((Date.now() - this.qStartTime) / 1000);
      this.index--;
      this.renderQuestion();
    }
  },

  async nextQuestion() {
    if (this.isTimedEndless) {
      if (this.index < this.session.length - 1) {
        this.index++;
        this.renderQuestion();
      } else {
        await this.loadNextTimedEndlessQuestion();
        this.index++;
        this.renderQuestion();
      }
      return;
    }

    if (this.index < this.session.length - 1) {
      this.index++;
      this.renderQuestion();
    } else {
      this.finishSession();
    }
  },

  getQuestionHints(q) {
    const diff = (q.difficulty || 'medium').toLowerCase();
    
    // Extract sections if available in solution
    let principle = '';
    let derivation = '';
    let traps = '';

    if (q.solution) {
      const pMatch = q.solution.match(/sol-principle[^>]*><b>[^<]*<\/b>\s*([^<]+(?:<(?!\/div)[^>]*>[^<]*)*)/i);
      if (pMatch) principle = pMatch[1].replace(/<\/?[^>]+(>|$)/g, "").trim();

      const dMatch = q.solution.match(/sol-step[^>]*><b>[^<]*<\/b>(?:<br>)?\s*([\s\S]*?)(?=<div class=['"]sol-section sol-traps['"]|$)/i);
      if (dMatch) derivation = dMatch[1].trim();

      const tMatch = q.solution.match(/sol-traps[^>]*><b>[^<]*<\/b>(?:<br>)?\s*([\s\S]*?)(?=<\/div>|$)/i);
      if (tMatch) traps = tMatch[1].trim();
    }

    const h1 = q.hint || principle || "Focus on the fundamental NCERT law or formula governing this question.";
    const hints = [];

    if (diff === 'easy') {
      hints.push({
        tier: 1,
        badge: '💡 Hint 1: Core Formula & NCERT Principle',
        content: h1
      });
    } else if (diff === 'medium') {
      hints.push({
        tier: 1,
        badge: '💡 Hint 1: Core Law & Formula',
        content: h1
      });
      hints.push({
        tier: 2,
        badge: '⚡ Hint 2: Step-by-Step Setup Clue',
        content: derivation ? (derivation.split('<br>')[0] || derivation.substring(0, 190)) : "Identify knowns and targets, then substitute directly into the primary formula."
      });
    } else { // hard
      hints.push({
        tier: 1,
        badge: '💡 Hint 1: Governing NCERT Principle',
        content: h1
      });
      hints.push({
        tier: 2,
        badge: '⚡ Hint 2: Multi-Step Equation Relation',
        content: derivation ? (derivation.split('<br>')[0] || derivation.substring(0, 190)) : "Relate boundary conditions across both stages before solving for the final value."
      });
      hints.push({
        tier: 3,
        badge: '⚠️ Hint 3: Common Exam Trap Alert',
        content: traps ? (traps.split('<br>')[0] || traps.substring(0, 200)) : "Watch for inverse relationships, sign conventions, and unit mismatches."
      });
    }

    return {
      diff,
      maxHints: hints.length,
      hints,
      principle,
      derivation,
      traps
    };
  },

  unlockNextHint() {
    const q = this.session[this.index];
    const st = this.states[this.index];
    const hintData = this.getQuestionHints(q);
    if (!st.unlockedHints) st.unlockedHints = 0;
    if (st.unlockedHints < hintData.maxHints) {
      st.unlockedHints++;
      st.hintsCollapsed = false;
    } else {
      st.hintsCollapsed = !st.hintsCollapsed;
    }
    this.renderQuestion();
  },

  toggleFullSolution() {
    const st = this.states[this.index];
    st.showFullSolution = !st.showFullSolution;
    this.renderQuestion();
  },

  async lockAnswer() {
    const st = this.states[this.index];
    if (st.picked === null) return alert('Select an option before locking.');
    if (st.locked) return;

    st.locked = true;
    st.timeSpent += Math.floor((Date.now() - this.qStartTime) / 1000);

    const q = this.session[this.index];
    const isCorrect = st.picked === q.correct_option;

    if (this.isTimedEndless) {
      this.teAttemptsCount++;
      if (isCorrect) this.teCorrectCount++;
      else this.teWrongCount++;
    }

    if (isCorrect) {
      this.streak++;
    } else {
      this.streak = 0;
      await db.mistakes.put({
        questionId: q.id,
        subject: q.subject,
        chapter: q.chapter,
        subtopic: q.subtopic,
        errorTag: 'Concept Gap',
        timeSpent: st.timeSpent,
        q
      });
    }

    let quadrant = 'q1';
    if (isCorrect && st.timeSpent > 60) quadrant = 'q2';
    if (!isCorrect && st.timeSpent <= 30) quadrant = 'q3';
    if (!isCorrect && st.timeSpent > 30) quadrant = 'q4';

    await db.attempts.add({
      questionId: q.id,
      subject: q.subject,
      chapter: q.chapter,
      subtopic: q.subtopic,
      correct: isCorrect ? 1 : 0,
      timeSpent: st.timeSpent,
      quadrant,
      timestamp: Date.now()
    });

    this.renderQuestion();
  },

  confirmFinishSession() {
    const answered = this.states.filter(s => s.picked !== null).length;
    const review = this.states.filter(s => s.review).length;
    const unattempted = this.session.length - answered;

    if (confirm(`Exam Submission Confirmation:\n\n• Attempted: ${answered} Qs\n• Marked for Review: ${review} Qs\n• Unattempted: ${unattempted} Qs\n\nAre you sure you want to end this exam paper?`)) {
      this.finishSession();
    }
  },

  async finishSession() {
    clearInterval(this.qTimer);
    clearInterval(this.mockTimer);

    // Subject-wise tracking for NTA Section B rule
    const subjStats = {};
    let totalCorrect = 0, totalWrong = 0, totalUnattempted = 0;

    this.session.forEach((q, i) => {
      const st = this.states[i];
      const s = q.subject || 'General';
      if (!subjStats[s]) subjStats[s] = { secA_cor: 0, secA_wrg: 0, secB_cor: 0, secB_wrg: 0, secB_count: 0 };

      if (st.picked === null) {
        totalUnattempted++;
      } else {
        const isCor = st.picked === q.correct_option;
        if (q.section === 'B') {
          // NTA Rule: Only evaluate first 10 attempted questions in Section B
          if (subjStats[s].secB_count < 10) {
            subjStats[s].secB_count++;
            if (isCor) { subjStats[s].secB_cor++; totalCorrect++; }
            else { subjStats[s].secB_wrg++; totalWrong++; }
          }
        } else {
          if (isCor) { subjStats[s].secA_cor++; totalCorrect++; }
          else { subjStats[s].secA_wrg++; totalWrong++; }
        }
      }
    });

    const netMarks = (totalCorrect * 4) - totalWrong;
    const maxMarks = this.isFullNTA ? 720 : (this.session.length * 4);
    const accuracy = (totalCorrect + totalWrong) ? Math.round((totalCorrect / (totalCorrect + totalWrong)) * 100) : 0;

    // Projected AIR
    let airTag = 'Subtopic Reinforcement Recommended';
    if (netMarks >= 700) airTag = 'AIR 1 - 150 · AIIMS Delhi Allotment Zone';
    else if (netMarks >= 680) airTag = 'AIR 151 - 1,500 · Top Central Government Medical College';
    else if (netMarks >= 650) airTag = 'AIR 1,501 - 8,000 · Premier State GMC Zone';
    else if (netMarks >= 600) airTag = 'AIR 8,001 - 22,000 · Confirmed Government Medical Seat';
    else if (netMarks >= 550) airTag = 'AIR 22,001 - 50,000 · State Quota GMC Allotment';

    await db.sessions.add({
      title: document.getElementById('practiceTitle').textContent,
      netMarks,
      maxMarks,
      accuracy,
      isMock: this.isMock,
      date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    });

    // Subject Pills HTML
    const subBreakdownHtml = Object.entries(subjStats).map(([subj, data]) => {
      const sNet = ((data.secA_cor + data.secB_cor) * 4) - (data.secA_wrg + data.secB_wrg);
      const sMax = (subj === 'Biology' || (subj !== 'Physics' && subj !== 'Chemistry')) ? 360 : 180;
      return `
        <div class="stat-pill" style="flex:1;min-width:140px;">
          <small>${subj}</small>
          <b>${sNet} / ${sMax}</b>
          <span style="font-size:11px;color:var(--emerald);">+${(data.secA_cor+data.secB_cor)*4}</span>
          <span style="font-size:11px;color:var(--red);">-${data.secA_wrg+data.secB_wrg}</span>
        </div>
      `;
    }).join('');

    document.getElementById('questionArea').innerHTML = `
      <div class="report-card">
        <span class="tag" style="background:#dcfce7;color:var(--emerald)">Simulation Complete</span>
        <h2 style="font:700 32px 'Space Grotesk';margin:12px 0 4px">Report Card: ${netMarks} / ${maxMarks} Marks</h2>
        <div style="font:700 14px 'JetBrains Mono',monospace;color:var(--teal);margin-bottom:20px;">${airTag}</div>

        <div class="score-ring">
          <span>${accuracy}%</span>
          <small>Accuracy Rate</small>
        </div>

        <div class="report-stats">
          <div class="stat-pill"><small>Correct (+4)</small><b style="color:var(--emerald)">${totalCorrect} Qs</b></div>
          <div class="stat-pill"><small>Negative Bleed (-1)</small><b style="color:var(--red)">${totalWrong} Qs</b></div>
          <div class="stat-pill"><small>Unattempted (0)</small><b>${totalUnattempted} Qs</b></div>
          <div class="stat-pill"><small>Total Paper Qs</small><b>${this.session.length} Qs</b></div>
        </div>

        <h3 style="margin:20px 0 10px;text-align:left;">Sectional Score Breakdown</h3>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:24px;">
          ${subBreakdownHtml}
        </div>

        <div style="display:flex;justify-content:center;gap:12px;flex-wrap:wrap">
          <button class="primary" onclick="App.showMocksHub()">Return to Full Mocks Hub</button>
          <button class="secondary" onclick="App.showMistakes()">Inspect Mistakes Vault</button>
          <button class="secondary" onclick="App.showProgress()">View 4-Quadrant Matrix</button>
          <button class="secondary" onclick="App.showView('dashboard')">Command Dashboard</button>
        </div>
      </div>
    `;

    await this.updateTopStats();
    await this.updateMockKpis();
  },

  exitPractice() {
    clearInterval(this.qTimer);
    clearInterval(this.mockTimer);
    this.showView('mocksHubView');
  },

  // ==================== DASHBOARD & PRACTICE SETUP ====================,

  typesetMath() {
    if (window.renderMathInElement) {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ]
      });
    }
  },

  shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  },

  // 10-Lakh Procedural & Deterministic NEET-UG Question Synthesizer (60% Hard, 30% Medium, 10% Easy)
  generate10LakhQuestion(seed = 1, targetSubject, targetChapter, targetSubtopic, targetDiff) {
    const s = Math.abs(Number(seed) || 1);
    const subjList = ['Physics', 'Chemistry', 'Botany', 'Zoology'];
    const subj = targetSubject && targetSubject !== 'ALL' ? targetSubject : subjList[s % subjList.length];

    // Difficulty stratification: 60% Hard, 30% Medium, 10% Easy
    let diff = targetDiff && targetDiff !== 'mixed' ? targetDiff : null;
    if (!diff) {
      const r = (s * 9301 + 49297) % 233280 / 233280;
      if (r < 0.60) diff = 'hard';
      else if (r < 0.90) diff = 'medium';
      else diff = 'easy';
    }

    const id = `NEET_10LAKH_${subj.slice(0,3).toUpperCase()}_${String(s).padStart(7, '0')}`;
    let qText = '', opts = [], correctIdx = 0, hint = '', principle = '', steps = '', traps = '', chap = targetChapter || 'Core Discipline', st = targetSubtopic || 'High-Yield Concept';

    if (subj === 'Physics') {
      const type = (s % 8);
      if (type === 0) {
        chap = 'Kinematics'; st = 'Motion in a Straight Line';
        const u = 10 + (s % 6) * 5;
        const sDist = 20 + (s % 5) * 20;
        const a = (u * u) / (2 * sDist);
        const aStr = a.toFixed(2);
        qText = `A racing vehicle travelling along a rectilinear track at an initial velocity of $${u}\\text{ m/s}$ is decelerated uniformly to rest over a displacement of $${sDist}\\text{ m}$. What is the magnitude of its constant deceleration?`;
        const cor = `$${aStr}\\text{ m/s}^2$`;
        const wrg1 = `$${(u / sDist).toFixed(2)}\\text{ m/s}^2$`;
        const wrg2 = `$${((u * u) / sDist).toFixed(2)}\\text{ m/s}^2$`;
        const wrg3 = `$${(a * 2).toFixed(2)}\\text{ m/s}^2$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        while (opts.length < 4) opts.push(`$${(a + opts.length).toFixed(2)}\\text{ m/s}^2$`);
        correctIdx = opts.indexOf(cor);
        principle = 'Third equation of kinematics for uniform linear deceleration: $v^2 = u^2 - 2as$.';
        steps = `Given $u = ${u}\\text{ m/s}$, $v = 0$, $s = ${sDist}\\text{ m}$.<br>$$0 = (${u})^2 - 2a(${sDist}) \\implies a = \\frac{${u*u}}{${2*sDist}} = ${aStr}\\text{ m/s}^2.$$`;
        traps = 'Distractor traps: Forgetting the factor of 2 in $2as$ gives $u^2/s$; taking $u/s$ ignores quadratic velocity relation.';
        hint = 'Use $v^2 = u^2 + 2as$ with final velocity $v = 0$.';
      } else if (type === 1) {
        chap = 'Thermodynamics'; st = 'Carnot Engine & Efficiency';
        const T1 = 500 + (s % 4) * 100;
        const T2 = 250 + (s % 3) * 50;
        const eta = Math.round(((T1 - T2) / T1) * 100);
        const Q1 = 1200;
        const W = Math.round(Q1 * ((T1 - T2) / T1));
        qText = `A Carnot heat engine operates between temperatures $T_1 = ${T1}\\text{ K}$ and $T_2 = ${T2}\\text{ K}$. If it absorbs $Q_1 = ${Q1}\\text{ J}$ of heat from the source reservoir per cycle, what is the net useful work output per cycle?`;
        const cor = `$${W}\\text{ J}$`;
        const wrg1 = `$${Q1 - W}\\text{ J}$`;
        const wrg2 = `$${Math.round(Q1 * (T2 / T1))}\\text{ J}$`;
        const wrg3 = `$${Math.round(W * 1.5)}\\text{ J}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        while (opts.length < 4) opts.push(`$${W + opts.length * 50}\\text{ J}$`);
        correctIdx = opts.indexOf(cor);
        principle = 'Second Law of Thermodynamics: Carnot efficiency $\\eta = 1 - \\frac{T_2}{T_1} = \\frac{W}{Q_1}$.';
        steps = `$$\\eta = 1 - \\frac{${T2}}{${T1}} = ${(1 - T2/T1).toFixed(3)}.$$<br>$$W = \\eta \\times Q_1 = ${(1 - T2/T1).toFixed(3)} \\times ${Q1} = ${W}\\text{ J}.$$`;
        traps = 'Distractor calculates heat rejected to sink $Q_2 = Q_1 - W$ instead of work.';
        hint = 'Compute Carnot efficiency first ($\eta = 1 - T_2/T_1$), then multiply by heat absorbed $Q_1$.';
      } else if (type === 2) {
        chap = 'Rotational Motion'; st = 'Moment of Inertia & Pure Rolling';
        const mObj = 2 + (s % 3);
        const rObj = 0.5;
        qText = `A uniform solid sphere of mass $M = ${mObj}\\text{ kg}$ and radius $R = ${rObj}\\text{ m}$ rolls down a rough inclined plane of inclination $\\theta = 30^\\circ$ without slipping. What is the acceleration of its center of mass? (Take $g = 10\\text{ m/s}^2$)`;
        const aRoll = (10 * Math.sin(Math.PI / 6)) / (1 + 2/5);
        const aRollStr = aRoll.toFixed(2);
        const cor = `$${aRollStr}\\text{ m/s}^2$`;
        const wrg1 = `$${(10 * Math.sin(Math.PI / 6)).toFixed(2)}\\text{ m/s}^2$`;
        const wrg2 = `$${((10 * Math.sin(Math.PI / 6)) / (1 + 1/2)).toFixed(2)}\\text{ m/s}^2$`;
        const wrg3 = `$${(aRoll * 1.4).toFixed(2)}\\text{ m/s}^2$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Acceleration of body rolling down an incline without slipping: $a = \\frac{g\\sin\\theta}{1 + k^2/R^2}$, where $k^2/R^2 = 2/5$ for a solid sphere.';
        steps = `$$a = \\frac{10 \\times \\sin 30^\\circ}{1 + \\frac{2}{5}} = \\frac{5}{1.4} = ${aRollStr}\\text{ m/s}^2.$$`;
        traps = 'Option B calculates frictionless sliding ($g\\sin\\theta = 5\\text{ m/s}^2$); Option C uses cylinder/disc formula ($k^2/R^2 = 1/2$).';
        hint = 'For a solid sphere, rotational inertia factor is $I/(MR^2) = 2/5$.';
      } else if (type === 3) {
        chap = 'Electromagnetic Induction and AC'; st = 'LCR Series Resonance Circuit';
        const R = 20;
        const L = 0.2;
        const C = 5;
        const omega = Math.round(1 / Math.sqrt(L * C * 1e-6));
        qText = `In a series LCR resonant circuit, $R = ${R}\\,\\Omega$, $L = ${L}\\text{ H}$, and $C = ${C}\\,\\mu\\text{F}$. What are the resonant angular frequency ($\\omega_0$) and the Quality Factor ($Q$) of the circuit?`;
        const Q = (omega * L) / R;
        const cor = `$\\omega_0 = ${omega}\\text{ rad/s}, Q = ${Q.toFixed(1)}$`;
        const wrg1 = `$\\omega_0 = ${omega}\\text{ rad/s}, Q = ${(Q / 2).toFixed(1)}$`;
        const wrg2 = `$\\omega_0 = ${omega * 2}\\text{ rad/s}, Q = ${Q.toFixed(1)}$`;
        const wrg3 = `$\\omega_0 = 500\\text{ rad/s}, Q = ${(Q * 2).toFixed(1)}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Resonant frequency $\\omega_0 = \\frac{1}{\\sqrt{LC}}$ and Quality Factor $Q = \\frac{\\omega_0 L}{R} = \\frac{1}{R}\\sqrt{\\frac{L}{C}}$.';
        steps = `$$\\omega_0 = \\frac{1}{\\sqrt{0.2 \\times 5 \\times 10^{-6}}} = \\frac{1}{\\sqrt{10^{-6}}} = 1000\\text{ rad/s}.$$<br>$$Q = \\frac{1000 \\times 0.2}{20} = \\frac{200}{20} = 10.0.$$`;
        traps = 'Inverting $R$ or forgetting the square root in $\\sqrt{LC}$ are common errors.';
        hint = 'At resonance, inductive reactance equals capacitive reactance ($X_L = X_C$).';
      } else if (type === 4) {
        chap = 'Ray Optics and Optical Instruments'; st = 'Lens Maker\'s Formula & Thin Lens Combinations';
        const fAir = 20;
        const fWater = fAir * 4;
        qText = `A glass equiconvex thin lens ($n_g = 1.5$) has a focal length of $f = ${fAir}\\text{ cm}$ in air. What will be its focal length when completely immersed in water ($n_w = 4/3$)?`;
        const cor = `$f_w = +${fWater}\\text{ cm}$`;
        const wrg1 = `$f_w = +${fAir * 2}\\text{ cm}$`;
        const wrg2 = `$f_w = +${fAir}\\text{ cm}$`;
        const wrg3 = `$f_w = +${fAir / 2}\\text{ cm}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Lens Maker\'s equation: $\\frac{f_w}{f_a} = \\frac{n_g - 1}{\\frac{n_g}{n_w} - 1} = \\frac{1.5 - 1}{\\frac{1.5}{4/3} - 1} = \\frac{0.5}{0.125} = 4$.';
        steps = `$$f_w = 4 \\times f_a = 4 \\times ${fAir} = +${fWater}\\text{ cm}.$$`;
        traps = 'Many students assume focal length doubles; it quadruples because $(n_{\\text{rel}} - 1)$ drops by factor of 4.';
        hint = 'Calculate relative refractive index $n_{\text{rel}} = n_g / n_w = 1.125$.';
      } else if (type === 5) {
        chap = 'Wave Optics'; st = 'Young\'s Double Slit Experiment & Fringe Width';
        const lambda = 600;
        const d = 0.6;
        const D = 1.2;
        const beta = ((lambda * 1e-9 * D) / (d * 1e-3)) * 1000;
        qText = `In a Young\'s Double Slit Experiment, monochromatic light of wavelength $\\lambda = ${lambda}\\text{ nm}$ illuminates two slits separated by $d = ${d}\\text{ mm}$. If the interference screen is placed at distance $D = ${D}\\text{ m}$, what is the fringe width?`;
        const cor = `$\\beta = ${beta.toFixed(2)}\\text{ mm}$`;
        const wrg1 = `$\\beta = ${(beta * 2).toFixed(2)}\\text{ mm}$`;
        const wrg2 = `$\\beta = ${(beta / 2).toFixed(2)}\\text{ mm}$`;
        const wrg3 = `$\\beta = ${(beta * 10).toFixed(2)}\\text{ mm}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Fringe width formula in double-slit interference: $\\beta = \\frac{\\lambda D}{d}$.';
        steps = `$$\\beta = \\frac{(${lambda} \\times 10^{-9}\\text{ m}) \\times ${D}\\text{ m}}{${d} \\times 10^{-3}\\text{ m}} = ${beta.toFixed(2)} \\times 10^{-3}\\text{ m} = ${beta.toFixed(2)}\\text{ mm}.$$`;
        traps = 'Unit conversion errors between nanometers ($10^{-9}$), millimeters ($10^{-3}$), and meters.';
        hint = 'Convert all lengths to standard SI meters before applying $\beta = \lambda D / d$.';
      } else if (type === 6) {
        chap = 'Gravitation'; st = 'Escape Velocity & Orbital Speed';
        qText = `A satellite orbits Earth in a circular path at an altitude where orbital speed is $v_o$. What is the minimum additional percentage increase in speed required for the satellite to escape Earth\'s gravitational field entirely?`;
        const pctInc = 41.4;
        const cor = `$41.4\\%$ (since $v_e = \\sqrt{2} v_o \\approx 1.414 v_o$)`;
        const wrg1 = `$100\\%$ (doubling the speed)`;
        const wrg2 = `$50\\%$ increase`;
        const wrg3 = `$20.7\\%$ increase`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Relation between escape velocity and orbital velocity at the same radial distance: $v_e = \\sqrt{2} v_o$.';
        steps = `$$\\frac{\\Delta v}{v_o} = \\frac{\\sqrt{2}v_o - v_o}{v_o} = \\sqrt{2} - 1 \\approx 0.414 \\implies 41.4\\%.$$`;
        traps = 'Confusing doubling of kinetic energy ($K_e = 2 K_o$) with doubling of speed.';
        hint = 'Escape speed is $\sqrt{2}$ times circular orbital speed at the same radius.';
      } else {
        chap = 'Dual Nature and Radiation'; st = 'Photoelectric Effect & Einstein Equation';
        const phi = 2.0;
        const ePhoton = 3.5 + (s % 3) * 0.5;
        const kMax = (ePhoton - phi).toFixed(2);
        qText = `Monochromatic photons of energy $E = ${ePhoton}\\text{ eV}$ strike a clean photosensitive cesium metal surface with work function $\\phi_0 = ${phi}\\text{ eV}$. What is the stopping potential ($V_0$) required to halt all photoelectrons?`;
        const cor = `$V_0 = ${kMax}\\text{ V}$`;
        const wrg1 = `$V_0 = ${(ePhoton).toFixed(2)}\\text{ V}$`;
        const wrg2 = `$V_0 = ${(phi).toFixed(2)}\\text{ V}$`;
        const wrg3 = `$V_0 = ${(Number(kMax) / 2).toFixed(2)}\\text{ V}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Einstein\'s Photoelectric Equation: $K_{\\max} = e V_0 = h\\nu - \\phi_0$.';
        steps = `$$K_{\\max} = ${ePhoton}\\text{ eV} - ${phi}\\text{ eV} = ${kMax}\\text{ eV} \\implies V_0 = ${kMax}\\text{ V}.$$`;
        traps = 'Stopping potential equals maximum kinetic energy expressed in electron-volts converted directly to Volts.';
        hint = 'Stopping potential $V_0 = (h\nu - \phi_0) / e$.';
      }
    } else if (subj === 'Chemistry') {
      const type = (s % 7);
      if (type === 0) {
        chap = 'Equilibrium'; st = 'Buffer Solutions & Solubility Product (Ksp)';
        const pKa = 4.75;
        const salt = 0.2;
        const acid = 0.02;
        const pH = (pKa + 1).toFixed(2);
        qText = `An acidic buffer solution is prepared by mixing sodium acetate ($${salt}\\text{ M}$) and acetic acid ($${acid}\\text{ M}$). If $pK_a$ of acetic acid is $4.75$, what is the calculated $pH$ of the buffer at $298\\text{ K}$?`;
        const cor = `$pH = ${pH}$`;
        const wrg1 = `$pH = 4.75$`;
        const wrg2 = `$pH = ${(pKa - 1).toFixed(2)}$`;
        const wrg3 = `$pH = 7.00$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Henderson-Hasselbalch equation for acidic buffer: $pH = pK_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]}$.';
        steps = `$$pH = 4.75 + \\log\\left(\\frac{0.2}{0.02}\\right) = 4.75 + \\log(10) = 4.75 + 1.00 = ${pH}.$$`;
        traps = 'Inverting salt and acid concentration ratio subtracts 1 instead of adding 1.';
        hint = 'Use Henderson-Hasselbalch: $pH = pK_a + \log([\text{Salt}] / [\text{Acid}])$.';
      } else if (type === 1) {
        chap = 'Solutions'; st = 'Osmotic Pressure & Van\'t Hoff Factor (i)';
        const conc = 0.1;
        const alpha = 0.8;
        const iVal = (1 + 2 * alpha).toFixed(2);
        qText = `A $0.1\\text{ M}$ aqueous solution of barium chloride ($\\text{BaCl}_2$, strong electrolyte) undergoes $80\\%$ degree of ionization ($\\alpha = 0.80$). What is the value of the van \'t Hoff factor ($i$)?`;
        const cor = `$i = ${iVal}$`;
        const wrg1 = `$i = 3.00$ (assuming 100% dissociation)`;
        const wrg2 = `$i = 1.80$`;
        const wrg3 = `$i = 2.40$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Van \'t Hoff factor for dissociating electrolyte: $i = 1 + (n - 1)\\alpha$, where $n = 3$ for $\\text{BaCl}_2 \\rightarrow \\text{Ba}^{2+} + 2\\text{Cl}^-$.';
        steps = `$$i = 1 + (3 - 1)(0.80) = 1 + 2(0.80) = 1 + 1.60 = ${iVal}.$$`;
        traps = 'Assuming complete dissociation ($i = 3$) or miscounting ions ($n = 2$ instead of $3$).';
        hint = 'For $\text{BaCl}_2$, each formula unit dissociates into 3 ions ($n = 3$).';
      } else if (type === 2) {
        chap = 'Chemical Kinetics'; st = 'Arrhenius Equation & Activation Energy';
        const tHalf1 = 40;
        const k1 = (0.693 / tHalf1).toFixed(4);
        qText = `A first-order decomposition reaction has a half-life of $t_{1/2} = ${tHalf1}\\text{ minutes}$. What is the time required for $75\\%$ of the reactant to decompose?`;
        const t75 = tHalf1 * 2;
        const cor = `$t_{75\\%} = ${t75}\\text{ minutes}$ ($2$ half-lives)`;
        const wrg1 = `$t_{75\\%} = ${tHalf1 * 3}\\text{ minutes}$`;
        const wrg2 = `$t_{75\\%} = ${tHalf1 * 1.5}\\text{ minutes}$`;
        const wrg3 = `$t_{75\\%} = ${tHalf1}\\text{ minutes}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'For first order reactions, remaining fraction is $(1/2)^n$. At $75\\%$ completion, $25\\%$ ($1/4$) remains, which corresponds to exactly $n = 2$ half-lives.';
        steps = `$$t_{75\\%} = 2 \\times t_{1/2} = 2 \\times ${tHalf1} = ${t75}\\text{ minutes}.$$`;
        traps = 'Confusing $75\\%$ decomposed ($25\\%$ remaining, $2$ half-lives) with $87.5\\%$ decomposed ($3$ half-lives).';
        hint = 'When $75\%$ is consumed, $25\%$ ($1/4 = (1/2)^2$) remains.';
      } else if (type === 3) {
        chap = 'Electrochemistry'; st = 'Nernst Equation & Cell Potential';
        qText = `For the Daniell cell $\\text{Zn}(s) | \\text{Zn}^{2+}(0.01\\text{ M}) || \\text{Cu}^{2+}(1.0\\text{ M}) | \\text{Cu}(s)$ with standard potential $E^\\circ_{\\text{cell}} = 1.10\\text{ V}$, what is the EMF of the cell at $298\\text{ K}$?`;
        const emf = (1.10 - (0.0591 / 2) * Math.log10(0.01 / 1.0)).toFixed(3);
        const cor = `$E_{\\text{cell}} = +1.159\\text{ V}$`;
        const wrg1 = `$E_{\\text{cell}} = +1.041\\text{ V}$`;
        const wrg2 = `$E_{\\text{cell}} = +1.100\\text{ V}$`;
        const wrg3 = `$E_{\\text{cell}} = +0.805\\text{ V}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Nernst equation at $298\\text{ K}$: $E_{\\text{cell}} = E^\\circ_{\\text{cell}} - \\frac{0.0591}{n}\\log\\frac{[\\text{Zn}^{2+}]}{[\\text{Cu}^{2+}]}$.';
        steps = `$$E = 1.10 - \\frac{0.0591}{2}\\log(10^{-2}) = 1.10 - (0.02955)(-2) = 1.10 + 0.0591 = 1.159\\text{ V}.$$`;
        traps = 'Subtracting instead of adding when $\\log(10^{-2}) = -2$.';
        hint = 'Notice $[\\text{Zn}^{2+}]/[\\text{Cu}^{2+}] = 0.01 = 10^{-2}$, so $-\log(10^{-2}) = +2$.';
      } else if (type === 4) {
        chap = 'Coordination Compounds'; st = 'Crystal Field Theory (CFT) & Splitting';
        qText = `What is the calculated spin-only magnetic moment ($\\mu$) for an octahedral high-spin $\\text{Fe}^{3+}$ complex ($d^5$ configuration, weak field ligand)?`;
        const mu = Math.sqrt(5 * (5 + 2)).toFixed(2);
        const cor = `$\\mu = ${mu}\\text{ BM}$ ($5$ unpaired electrons)`;
        const wrg1 = `$\\mu = 1.73\\text{ BM}$ ($1$ unpaired electron in low-spin)`;
        const wrg2 = `$\\mu = 4.90\\text{ BM}$ ($4$ unpaired electrons)`;
        const wrg3 = `$\\mu = 0\\text{ BM}$ (diamagnetic)`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Spin-only magnetic moment formula: $\\mu = \\sqrt{n(n + 2)}\\text{ BM}$. For high-spin $d^5$ ($t_{2g}^3 e_g^2$), $n = 5$.';
        steps = `$$\\mu = \\sqrt{5(5 + 2)} = \\sqrt{35} \\approx 5.92\\text{ BM}.$$`;
        traps = 'Confusing high-spin ($n=5$) with low-spin strong field ($t_{2g}^5 e_g^0, n=1 \\implies \\sqrt{3} \\approx 1.73\\text{ BM}$).';
        hint = 'In weak field octahedral complexes, electrons occupy both $t_{2g}$ and $e_g$ singly before pairing.';
      } else if (type === 5) {
        chap = 'Chemical Thermodynamics'; st = 'Gibbs Free Energy & Equilibrium';
        qText = `For a chemical process with $\\Delta H = +40\\text{ kJ/mol}$ and $\\Delta S = +100\\text{ J/(mol}\\cdot\\text{K)}$, above what minimum temperature does the reaction become spontaneous at constant pressure?`;
        const T = Math.round((40 * 1000) / 100);
        const cor = `$T > ${T}\\text{ K}$ ($${T - 273}^\\circ\\text{C}$)`;
        const wrg1 = `$T < ${T}\\text{ K}$`;
        const wrg2 = `$T > 400\\text{ K}$`;
        const wrg3 = `$T > 250\\text{ K}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Spontaneity criterion: $\\Delta G = \\Delta H - T\\Delta S < 0 \\implies T > \\frac{\\Delta H}{\\Delta S}$.';
        steps = `$$T > \\frac{40,000\\text{ J/mol}}{100\\text{ J/(mol}\\cdot\\text{K)}} = ${T}\\text{ K}.$$`;
        traps = 'Forgetting to convert kilojoules to joules gives $0.4\\text{ K}$.';
        hint = 'Convert $\Delta H$ from $\text{kJ}$ to $\text{J}$ ($40\\text{ kJ} = 40,000\\text{ J}$).';
      } else {
        chap = 'Aldehydes Ketones and Carboxylic Acids'; st = 'Aldol Condensation & Cannizzaro Reaction';
        qText = `Which of the following organic carbonyl compounds undergoes self-oxidation and reduction (Cannizzaro reaction) upon treatment with concentrated ($50\\%$) aqueous $\\text{NaOH}$?`;
        const cor = `Formaldehyde ($\\text{HCHO}$) and Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$), due to absence of $\\alpha$-hydrogens`;
        const wrg1 = `Acetaldehyde ($\\text{CH}_3\\text{CHO}$)`;
        const wrg2 = `Acetone ($\\text{CH}_3\\text{COCH}_3$)`;
        const wrg3 = `Propionaldehyde ($\\text{CH}_3\\text{CH}_2\\text{CHO}$)`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Cannizzaro reaction occurs in aldehydes lacking $\\alpha$-hydrogen atoms, producing one molecule of alcohol and one molecule of carboxylic acid salt.';
        steps = `$$2\\text{HCHO} + \\text{NaOH} \\rightarrow \\text{CH}_3\\text{OH} + \\text{HCOONa}.$$ Aldehydes with $\\alpha$-hydrogens undergo Aldol condensation instead.`;
        traps = 'Marking acetaldehyde which has three $\\alpha$-hydrogens and undergoes aldol condensation.';
        hint = 'Cannizzaro reaction is exclusive to aldehydes with NO $\alpha$-hydrogens.';
      }
    } else if (subj === 'Botany') {
      const type = (s % 5);
      if (type === 0) {
        chap = 'Photosynthesis in Higher Plants'; st = 'Calvin Cycle (C3) & RuBisCO Kinetics';
        qText = `In $C_3$ versus $C_4$ photosynthetic pathways, how many total molecules of $\\text{ATP}$ and $\\text{NADPH}$ are stoichiometrically invested to produce one mole of hexose glucose?`;
        const cor = `$C_3: 18\\text{ ATP} + 12\\text{ NADPH}$; $C_4: 30\\text{ ATP} + 12\\text{ NADPH}$`;
        const wrg1 = `$C_3: 30\\text{ ATP} + 12\\text{ NADPH}$; $C_4: 18\\text{ ATP} + 12\\text{ NADPH}$`;
        const wrg2 = `$C_3: 12\\text{ ATP} + 18\\text{ NADPH}$; $C_4: 24\\text{ ATP} + 12\\text{ NADPH}$`;
        const wrg3 = `$C_3: 36\\text{ ATP} + 12\\text{ NADPH}$; $C_4: 36\\text{ ATP} + 12\\text{ NADPH}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Calvin cycle requires $3\\text{ ATP} + 2\\text{ NADPH}$ per $\\text{CO}_2$ ($18\\text{ ATP}$ total). $C_4$ plants require an extra $2\\text{ ATP}$ per $\\text{CO}_2$ for PEP regeneration ($30\\text{ ATP}$ total).';
        steps = `$$C_3: 6 \\times 3\\text{ ATP} = 18\\text{ ATP}.$$<br>$$C_4: 6 \\times 5\\text{ ATP} = 30\\text{ ATP}.$$`;
        traps = 'Inverting $C_3$ and $C_4$ energetics is a high-frequency exam pitfall.';
        hint = '$C_4$ plants pay an additional energy tax of 2 ATP per $\text{CO}_2$ to suppress photorespiration.';
      } else if (type === 1) {
        chap = 'Respiration in Plants'; st = 'Oxidative Phosphorylation & Respiratory Quotient';
        qText = `When tripalmitin fat ($\\text{C}_{51}\\text{H}_{98}\\text{O}_6$) is oxidized as the sole respiratory substrate in seeds, what is the stoichiometric Respiratory Quotient (RQ)?`;
        const cor = `$RQ = 0.7$ ($102\\text{ CO}_2 / 145\\text{ O}_2$)`;
        const wrg1 = `$RQ = 1.0$ (carbohydrate respiration)`;
        const wrg2 = `$RQ = 0.9$ (protein catabolism)`;
        const wrg3 = `$RQ = 1.33$ (organic acids)`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Respiratory Quotient: $RQ = \\frac{\\text{Volume of }\\text{CO}_2\\text{ evolved}}{\\text{Volume of }\\text{O}_2\\text{ consumed}}$. For fats, $RQ < 1.0$.';
        steps = `$$2\\text{C}_{51}\\text{H}_{98}\\text{O}_6 + 145\\text{O}_2 \\rightarrow 102\\text{CO}_2 + 98\\text{H}_2\\text{O} \\implies RQ = \\frac{102}{145} \\approx 0.7.$$`;
        traps = 'Marking $1.0$ which applies exclusively to hexose carbohydrates like glucose.';
        hint = 'Fats are oxygen-poor and consume substantially more $\text{O}_2$ for complete oxidation.';
      } else if (type === 2) {
        chap = 'Molecular Basis of Inheritance'; st = 'DNA Double Helix & Chargaff Rules';
        const aPct = 20 + (s % 6) * 2;
        const cPct = 50 - aPct;
        qText = `Quantitative analysis of a double-stranded duplex DNA sample indicates that Adenine represents $${aPct}\\%$ of the total nitrogenous bases. According to Chargaff\'s base-pairing rules, what is the percentage of Cytosine?`;
        const cor = `$${cPct}\\%$`;
        const wrg1 = `$${aPct}\\%$ (percentage of Thymine)`;
        const wrg2 = `$${100 - (aPct * 2)}\\%$`;
        const wrg3 = `$${Math.round(cPct / 2)}\\%$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Chargaff\'s equivalence rules: in duplex DNA, $A = T$ and $G = C$, hence $A + C = 50\\%$.';
        steps = `$$A = ${aPct}\\% \\implies T = ${aPct}\\% \\implies (A + T) = ${aPct * 2}\\%.$$<br>$$(G + C) = 100\\% - ${aPct * 2}\\% = ${100 - aPct * 2}\\% \\implies C = \\frac{${100 - aPct * 2}}{2} = ${cPct}\\%.$$`;
        traps = 'Marking ${aPct}% confuses Thymine (which equals Adenine) with Cytosine.';
        hint = 'Remember in double-stranded DNA: $A + C = G + T = 50\%$.';
      } else if (type === 3) {
        chap = 'Cell Cycle and Cell Division'; st = 'Meiosis I Prophase I & Crossing Over';
        qText = `During Meiosis I Prophase I, the formation of the synaptonemal complex between homologous chromosomes and the physical exchange of genetic material (crossing over) occur sequentially in which two stages?`;
        const cor = `Synapsis in Zygotene; Crossing over in Pachytene`;
        const wrg1 = `Crossing over in Zygotene; Synapsis in Pachytene`;
        const wrg2 = `Synapsis in Leptotene; Crossing over in Diplotene`;
        const wrg3 = `Chiasmata in Zygotene; Terminalisation in Pachytene`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Prophase I chronology: Leptotene (condensation) $\\rightarrow$ Zygotene (synapsis) $\\rightarrow$ Pachytene (crossing over via recombinase) $\\rightarrow$ Diplotene (chiasmata) $\\rightarrow$ Diakinesis (terminalisation).';
        steps = `Homologous pairing (synapsis) mediated by synaptonemal complex occurs in Zygotene. Recombination nodules and crossing over occur in Pachytene.`;
        traps = 'Inverting Zygotene and Pachytene events.';
        hint = 'Zygotene = Synapsis; Pachytene = Crossing over.';
      } else {
        chap = 'Biotechnology Principles and Processes'; st = 'Restriction Endonucleases & DNA Ligase';
        qText = `The restriction endonuclease EcoRI recognizes which specific hexanucleotide palindromic sequence and cuts to produce cohesive sticky ends?`;
        const cor = `$5'\\text{-GAATTC-3'}$, cutting between G and A`;
        const wrg1 = `$5'\\text{-GGATCC-3'}$ (BamHI)`;
        const wrg2 = `$5'\\text{-AAGCTT-3'}$ (HindIII)`;
        const wrg3 = `$5'\\text{-CTGCAG-3'}$ (PstI)`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'EcoRI cleaves between G and A within palindromic sequence $5'\\text{-GAATTC-3'}$, leaving single-stranded overhanging sticky ends.';
        steps = `$$5'\\text{-G}\\downarrow\\text{AATTC-3'}$$<br>$$3'\\text{-CTTAA}\\uparrow\\text{G-5'}$$.`;
        traps = 'Option B is BamHI; Option C is HindIII.';
        hint = 'EcoRI cuts specifically at GAATTC.';
      }
    } else {
      // Zoology
      const type = (s % 4);
      if (type === 0) {
        chap = 'Evolution'; st = 'Hardy-Weinberg Principle & Genetic Drift';
        const qVal = 0.2 + (s % 3) * 0.1;
        const pVal = Math.round((1 - qVal) * 10) / 10;
        const carrierPct = Math.round(2 * pVal * qVal * 100);
        qText = `In a panmictic population in Hardy-Weinberg equilibrium, the gene frequency of an autosomal recessive allele ($q$) is $${qVal.toFixed(1)}$. What is the expected percentage of heterozygous carriers in this population?`;
        const cor = `$${carrierPct}\\%$ ($2pq = 2 \\times ${pVal.toFixed(1)} \\times ${qVal.toFixed(1)}$)`;
        const wrg1 = `$${Math.round(pVal * pVal * 100)}\\%$ (homozygous dominant)`;
        const wrg2 = `$${Math.round(qVal * qVal * 100)}\\%$ (homozygous recessive)`;
        const wrg3 = `$${Math.round(pVal * qVal * 100)}\\%$ ($pq$ without factor 2)`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Hardy-Weinberg equilibrium equation: $p^2 + 2pq + q^2 = 1$, where heterozygous carrier frequency is $2pq$.';
        steps = `Given $q = ${qVal.toFixed(1)} \\implies p = 1 - ${qVal.toFixed(1)} = ${pVal.toFixed(1)}$.<br>$$2pq = 2(${pVal.toFixed(1)})(${qVal.toFixed(1)}) = ${(2 * pVal * qVal).toFixed(2)} \\implies ${carrierPct}\\%.`;
        traps = 'Forgetting coefficient 2 yields $pq$ (${Math.round(pVal * qVal * 100)}%), a classic distractor.';
        hint = 'Find $p = 1 - q$, then compute carrier frequency $2pq$.';
      } else if (type === 1) {
        chap = 'Excretory Products and Their Elimination'; st = 'Urine Formation & Counter-Current Mechanism';
        qText = `Under normal physiological conditions in a healthy human adult, what are the Glomerular Filtration Rate (GFR) and the approximate volume of final concentrated urine produced daily?`;
        const cor = `$\\text{GFR} = 125\\text{ mL/min}$ ($180\\text{ L/day}$); Urine $= 1.5\\text{ L/day}$ ($99\\%$ reabsorbed)`;
        const wrg1 = `$\\text{GFR} = 125\\text{ mL/min}$; Urine $= 18\\text{ L/day}$`;
        const wrg2 = `$\\text{GFR} = 180\\text{ mL/min}$; Urine $= 1.5\\text{ L/day}$`;
        const wrg3 = `$\\text{GFR} = 650\\text{ mL/min}$; Urine $= 5.0\\text{ L/day}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Nephron tubular reabsorption: Nearly $99\\%$ of the $180\\text{ L}$ of glomerular filtrate formed daily is reabsorbed by renal tubules, leaving $\\sim 1.5\\text{ L}$ excreted as urine.';
        steps = `$$\\text{GFR} = 125\\text{ mL/min} = 125 \\times 60 \\times 24 = 180,000\\text{ mL/day} = 180\\text{ L/day}.$$ Daily urine volume is $1-1.5\\text{ L}$.`;
        traps = 'Option D ($650\\text{ mL/min}$) is Renal Plasma Flow (RPF), not GFR.';
        hint = 'Glomerular filtration rate is 125 mL/min (180 L/day); 99% is reabsorbed.';
      } else if (type === 2) {
        chap = 'Body Fluids and Circulation'; st = 'Cardiac Cycle & ECG Waves (P, QRS, T)';
        const sv = 70;
        const hr = 72;
        const coL = ((sv * hr) / 1000).toFixed(2);
        qText = `A resting individual has a ventricular stroke volume of $SV = ${sv}\\text{ mL}$ and a heart rate of $HR = ${hr}\\text{ beats/min}$. What is the calculated cardiac output?`;
        const cor = `$CO \\approx ${coL}\\text{ L/min}$ (${sv * hr}\\text{ mL/min})`;
        const wrg1 = `$CO \\approx 7.20\\text{ L/min}$`;
        const wrg2 = `$CO \\approx 3.50\\text{ L/min}$`;
        const wrg3 = `$CO \\approx 10.0\\text{ L/min}$`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Cardiac Output equation: $CO = \\text{Stroke Volume} \\times \\text{Heart Rate}$.';
        steps = `$$CO = ${sv}\\text{ mL} \\times ${hr}\\text{ bpm} = ${sv * hr}\\text{ mL/min} = \\frac{${sv * hr}}{1000} = ${coL}\\text{ L/min}.$$`;
        traps = 'Confusing stroke volume ($70\\text{ mL}$) with end-diastolic volume ($120\\text{ mL}$).';
        hint = 'Cardiac output is stroke volume multiplied by heart rate.';
      } else {
        chap = 'Neural Control and Chemical Coordination'; st = 'Generation & Conduction of Nerve Impulse';
        qText = `During the generation of an action potential along an unmyelinated axon, the rapid initial depolarization phase is driven by:`;
        const cor = `Rapid influx of $\\text{Na}^+$ ions into the axoplasm through voltage-gated sodium channels`;
        const wrg1 = `Rapid efflux of $\\text{K}^+$ ions out of the axoplasm`;
        const wrg2 = `Inward pumping of $\\text{Cl}^-$ ions via active transport`;
        const wrg3 = `Complete closure of all membrane ion channels`;
        opts = this.shuffle([...new Set([cor, wrg1, wrg2, wrg3])]);
        correctIdx = opts.indexOf(cor);
        principle = 'Electrophysiology of action potential: Depolarization is caused by $\\text{Na}^+$ influx; Repolarization is caused by $\\text{K}^+$ efflux.';
        steps = `Upon threshold stimulation ($-55\\text{ mV}$), voltage-gated $\\text{Na}^+$ channels open, causing massive $\\text{Na}^+$ influx down its electrochemical gradient, flipping membrane potential from $-70\\text{ mV}$ to $+30\\text{ mV}$.`;
        traps = 'Option B describes Repolarization, which is driven by $\\text{K}^+$ efflux.';
        hint = 'Depolarization = Sodium influx; Repolarization = Potassium efflux.';
      }
    }

    const sol = `
      <div class='sol-section sol-principle'><b>📖 Core NCERT Principle:</b> ${principle}</div>
      <div class='sol-section sol-step' style='margin-top:8px;'><b>⚡ Step-by-Step Derivation & Logic:</b><br>${steps}</div>
      <div class='sol-section sol-traps' style='margin-top:8px;color:#b45309;'><b>⚠️ Why Other Options are Common Traps:</b><br>${traps}</div>
    `;

    return {
      id,
      classNum: '11',
      subject: subj,
      chapter: chap,
      subtopic: st,
      difficulty: diff,
      year_tag: '10 Lakh AI Master Engine',
      question: qText,
      options: opts,
      correct_option: correctIdx,
      hint,
      solution: sol,
      ncert_ref: `NCERT Master Syllabus, Chapter: ${chap}`
    };
  },

  generateProceduralQuestion(targetSubject, targetChapter, targetSubtopic, targetDiff) {
    const seed = Math.floor(Math.random() * 1000000) + 1;
    return this.generate10LakhQuestion(seed, targetSubject, targetChapter, targetSubtopic, targetDiff);
  },

  startInfiniteDrill(subject = 'ALL', count = 30) {
    const questions = [];
    for (let i = 0; i < count; i++) {
      questions.push(this.generateProceduralQuestion(subject));
    }
    this.
  // ==================== TIMED ENDLESS MARATHON ENGINE ====================
  isTimedEndless: false,
  teTimer: null,
  teSecLeft: 3600,
  teTotalSec: 3600,
  teAttemptsCount: 0,
  teCorrectCount: 0,
  teWrongCount: 0,
  teChapters: [],
  teDifficulty: 'random',

  async startTimedEndlessSession() {
    await this.ensureReady();
    const customMins = parseInt(document.getElementById('teCustomMinutes')?.value, 10);
    const durationMins = (customMins && customMins > 0) ? customMins : 60;
    const diff = document.querySelector('input[name=teDiff]:checked')?.value || 'random';
    
    if (!this.teSelectedChapters || this.teSelectedChapters.size === 0) {
      return alert('Please select at least one topic for your marathon.');
    }

    this.isTimedEndless = true;
    this.isMock = false;
    this.isFullNTA = false;
    this.isBlind = false;
    this.teDurationSec = durationMins * 60;
    this.teSecLeft = durationMins * 60;
    this.teChapters = Array.from(this.teSelectedChapters);
    this.teDifficulty = diff;
    this.teAttemptsCount = 0;
    this.teCorrectCount = 0;
    this.teWrongCount = 0;
    this.streak = 0;
    this.session = [];
    this.states = [];
    this.index = 0;

    this.showView('practice');
    document.getElementById('practiceEyebrow').textContent = `⏱ Timed Marathon (${durationMins} Mins)`;
    document.getElementById('practiceTitle').textContent = `${this.teChapters.length} Selected Topics (${diff.toUpperCase()})`;
    
    // UI elements
    const finishBtn = document.getElementById('teEarlyFinishBtn');
    if (finishBtn) finishBtn.style.display = 'block';
    const cdEl = document.getElementById('mockCountdown');
    if (cdEl) {
      cdEl.style.display = 'block';
      cdEl.classList.remove('timer-pulse-red');
    }
    const paceEl = document.getElementById('cbtPacingBadge');
    if (paceEl) {
      paceEl.style.display = 'block';
      paceEl.textContent = '⏱️ Pacing: 0s / Q';
    }

    document.getElementById('cbtPaletteWrap').style.display = 'none';
    document.getElementById('cbtSubjectTabsWrap').style.display = 'none';
    document.getElementById('confidenceStreakBadge').style.display = 'none';

    // Start countdown timer
    clearInterval(this.teTimer);
    clearInterval(this.mockTimer);
    this.teTimer = setInterval(() => {
      this.teSecLeft--;
      const hours = Math.floor(this.teSecLeft / 3600);
      const mins = Math.floor((this.teSecLeft % 3600) / 60);
      const secs = String(this.teSecLeft % 60).padStart(2, '0');
      if (cdEl) {
        cdEl.textContent = hours > 0 ? `${hours}:${String(mins).padStart(2,'0')}:${secs}` : `${mins}:${secs}`;
        if (this.teSecLeft <= 300) {
          cdEl.classList.add('timer-pulse-red');
        }
      }

      // Update live pacing
      if (this.teAttemptsCount > 0 && paceEl) {
        const elapsed = this.teDurationSec - this.teSecLeft;
        const avg = Math.round(elapsed / this.teAttemptsCount);
        paceEl.textContent = `⏱️ Pace: ${avg}s/Q (${this.teAttemptsCount} Qs Attempted)`;
      }

      if (this.teSecLeft <= 0) {
        clearInterval(this.teTimer);
        alert('⏱ Marathon time is up! Submitting your marathon results.');
        this.finishTimedEndlessSession();
      }
    }, 1000);

    // Load first question
    await this.loadNextTimedEndlessQuestion();
  },

  async loadNextTimedEndlessQuestion() {
    const chap = this.teChapters[Math.floor(Math.random() * this.teChapters.length)];
    await this.ensureChapterLoaded(chap);

    const diff = (this.teDifficulty === 'random')
      ? ['easy', 'medium', 'hard'][Math.floor(Math.random() * 3)]
      : this.teDifficulty;

    let pool = await db.questions.where('chapter').equals(chap).filter(q => q.difficulty === diff).limit(40).toArray();
    if (!pool.length) {
      pool = await db.questions.where('chapter').equals(chap).limit(40).toArray();
    }

    let q;
    const usedIds = new Set(this.session.map(sq => sq.id));
    const available = pool.filter(cand => !usedIds.has(cand.id));

    if (available.length > 0) {
      q = available[Math.floor(Math.random() * available.length)];
    } else {
      // Procedural on-demand question synthesis
      q = this.generate10LakhQuestion(Date.now() + this.session.length, 'Physics', chap, null, diff);
    }

    this.session.push(q);
    this.states.push({
      picked: null,
      locked: false,
      review: false,
      visited: true,
      timeSpent: 0,
      unlockedHints: 0,
      hintsCollapsed: false,
      showFullSolution: false
    });

    this.renderQuestion();
  },

  async finishTimedEndlessSession() {
    clearInterval(this.teTimer);
    clearInterval(this.qTimer);

    const finishBtn = document.getElementById('teEarlyFinishBtn');
    if (finishBtn) finishBtn.style.display = 'none';

    const elapsedSec = Math.max(1, this.teDurationSec - this.teSecLeft);
    const durationMins = Math.round(elapsedSec / 60) || 1;
    const totalQ = this.teAttemptsCount;
    const cor = this.teCorrectCount;
    const wrg = this.teWrongCount;
    const net = (cor * 4) - wrg;
    const acc = totalQ ? Math.round((cor / totalQ) * 100) : 0;
    const avgPace = totalQ ? Math.round(elapsedSec / totalQ) : 0;

    await db.sessions.add({
      title: `⏱ Timed Marathon (${durationMins}m)`,
      netMarks: net,
      maxMarks: Math.max(1, totalQ * 4),
      accuracy: acc,
      isMock: false,
      date: new Date().toLocaleDateString('en-GB')
    });

    await this.updateTopStats();

    // Show summary modal
    const modal = document.getElementById('timedEndlessSummaryModal');
    const body = document.getElementById('teModalBody');
    if (modal && body) {
      body.innerHTML = `
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));gap:12px;margin-bottom:18px;">
          <div style="background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:12px;text-align:center;">
            <small style="color:var(--muted)">Questions Done</small>
            <div style="font-size:26px;font-weight:800;font-family:'Space Grotesk'">${totalQ}</div>
          </div>
          <div style="background:#f0fdf4;border:1px solid #bbf7d0;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#166534">Correct (+4)</small>
            <div style="font-size:26px;font-weight:800;color:var(--emerald);font-family:'Space Grotesk'">${cor}</div>
          </div>
          <div style="background:#fff1f2;border:1px solid #fecdd3;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#9f1239">Wrong (-1)</small>
            <div style="font-size:26px;font-weight:800;color:var(--red);font-family:'Space Grotesk'">${wrg}</div>
          </div>
          <div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#1e40af">Accuracy</small>
            <div style="font-size:26px;font-weight:800;color:#0284c7;font-family:'Space Grotesk'">${acc}%</div>
          </div>
          <div style="background:#faf5ff;border:1px solid #e9d5ff;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#6b21a8">Net Score</small>
            <div style="font-size:26px;font-weight:800;color:var(--purple);font-family:'Space Grotesk'">${net} pts</div>
          </div>
          <div style="background:#fefce8;border:1px solid #fef08a;border-radius:10px;padding:12px;text-align:center;">
            <small style="color:#854d0e">Avg Pacing</small>
            <div style="font-size:26px;font-weight:800;color:#b45309;font-family:'Space Grotesk'">${avgPace}s / Q</div>
          </div>
        </div>

        <div style="background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:14px;font-size:13.5px;line-height:1.5;">
          <b>Marathon Summary:</b> Practiced continuously across <b>${this.teChapters.length} topics</b> for <b>${durationMins} minutes</b>.
          ${wrg > 0 ? `<br><span style="color:var(--red)">• ${wrg} mistakes were automatically logged into your Mistake Vault for root-cause tagging and revision.</span>` : '<br><span style="color:var(--emerald)">• Clean sheet! Zero negative mark bleed in this entire marathon.</span>'}
        </div>
      `;
      modal.style.display = 'flex';
    }

    this.isTimedEndless = false;
  },


  beginSession(questions, `⚡ Infinite Practice Mode (${subject === 'ALL' ? 'Multi-Subject' : subject} · 60% Hard)`, false, false);
  }
});
