// js/flashcards.js - Interactive Spaced Repetition Formula & NCERT Flashcards Deck
window.App = window.App || {};

Object.assign(window.App, {
  fcCards: [],
  fcIndex: 0,
  fcFlipped: false,
  fcSubjFilter: 'ALL',
  fcClassFilter: 'ALL',
  fcChapFilter: 'ALL',
  fcStatusFilter: 'ALL',
  fcState: {}, // cardId -> { status: 'new'|'mastered'|'review', starred: boolean }

  loadFlashcardState() {
    try {
      const saved = localStorage.getItem('PREPWISE_FC_STATE');
      this.fcState = saved ? JSON.parse(saved) : {};
    } catch (e) {
      this.fcState = {};
    }
  },

  saveFlashcardState() {
    try {
      localStorage.setItem('PREPWISE_FC_STATE', JSON.stringify(this.fcState));
    } catch (e) {}
  },

  initFlashcards() {
    this.loadFlashcardState();
    const raw = window.PREPWISE_FLASHCARDS || [];
    this.fcCards = [...raw];
    this.populateFlashcardFilters();
    this.applyFlashcardFilters();
  },

  populateFlashcardFilters() {
    const chapSelect = document.getElementById('fcChapSelect');
    if (!chapSelect) return;

    const chaps = new Set();
    const raw = window.PREPWISE_FLASHCARDS || [];
    raw.forEach(c => {
      if (this.fcClassFilter !== 'ALL' && c.classNum !== this.fcClassFilter) return;
      if (this.fcSubjFilter !== 'ALL' && c.subject !== this.fcSubjFilter) return;
      chaps.add(c.chapter);
    });

    chapSelect.innerHTML = '<option value="ALL">All Chapters in Selection</option>' +
      [...chaps].sort().map(ch => `<option value="${ch}">${ch}</option>`).join('');
  },

  setFcSubj(subj) {
    this.fcSubjFilter = subj;
    document.querySelectorAll('.fc-subj-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.subj === subj);
    });
    this.populateFlashcardFilters();
    this.applyFlashcardFilters();
  },

  setFcClass(cls) {
    this.fcClassFilter = cls;
    document.querySelectorAll('.fc-class-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.cls === cls);
    });
    this.populateFlashcardFilters();
    this.applyFlashcardFilters();
  },

  onFcChapChange(chap) {
    this.fcChapFilter = chap;
    this.applyFlashcardFilters();
  },

  setFcStatus(status) {
    this.fcStatusFilter = status;
    document.querySelectorAll('.fc-status-btn').forEach(b => {
      b.classList.toggle('active', b.dataset.status === status);
    });
    this.applyFlashcardFilters();
  },

  applyFlashcardFilters() {
    const raw = window.PREPWISE_FLASHCARDS || [];
    this.fcCards = raw.filter(c => {
      if (this.fcSubjFilter !== 'ALL' && c.subject !== this.fcSubjFilter) return false;
      if (this.fcClassFilter !== 'ALL' && c.classNum !== this.fcClassFilter) return false;
      if (this.fcChapFilter !== 'ALL' && c.chapter !== this.fcChapFilter) return false;

      const st = this.fcState[c.id] || { status: 'new', starred: false };
      if (this.fcStatusFilter === 'starred' && !st.starred) return false;
      if (this.fcStatusFilter === 'review' && st.status !== 'review') return false;
      if (this.fcStatusFilter === 'mastered' && st.status !== 'mastered') return false;

      return true;
    });

    this.fcIndex = 0;
    this.fcFlipped = false;
    this.renderCurrentFlashcard();
    this.updateFlashcardStats();
  },

  shuffleFlashcards() {
    for (let i = this.fcCards.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.fcCards[i], this.fcCards[j]] = [this.fcCards[j], this.fcCards[i]];
    }
    this.fcIndex = 0;
    this.fcFlipped = false;
    this.renderCurrentFlashcard();
  },

  flipFlashcard() {
    const cardEl = document.getElementById('flashcardElement');
    if (!cardEl) return;
    this.fcFlipped = !this.fcFlipped;
    cardEl.classList.toggle('is-flipped', this.fcFlipped);
  },

  nextFlashcard() {
    if (!this.fcCards.length) return;
    this.fcIndex = (this.fcIndex + 1) % this.fcCards.length;
    this.fcFlipped = false;
    this.renderCurrentFlashcard();
  },

  prevFlashcard() {
    if (!this.fcCards.length) return;
    this.fcIndex = (this.fcIndex - 1 + this.fcCards.length) % this.fcCards.length;
    this.fcFlipped = false;
    this.renderCurrentFlashcard();
  },

  markFlashcard(status) {
    if (!this.fcCards.length) return;
    const card = this.fcCards[this.fcIndex];
    if (!card) return;

    if (!this.fcState[card.id]) {
      this.fcState[card.id] = { status: 'new', starred: false };
    }
    this.fcState[card.id].status = status;
    this.saveFlashcardState();
    this.updateFlashcardStats();
    this.nextFlashcard();
  },

  toggleStarFlashcard() {
    if (!this.fcCards.length) return;
    const card = this.fcCards[this.fcIndex];
    if (!card) return;

    if (!this.fcState[card.id]) {
      this.fcState[card.id] = { status: 'new', starred: false };
    }
    this.fcState[card.id].starred = !this.fcState[card.id].starred;
    this.saveFlashcardState();
    this.renderCurrentFlashcard();
    this.updateFlashcardStats();
  },

  renderCurrentFlashcard() {
    const cardEl = document.getElementById('flashcardElement');
    const emptyEl = document.getElementById('fcEmptyState');
    const counterEl = document.getElementById('fcCounter');
    const progressEl = document.getElementById('fcProgressBar');
    const starBtn = document.getElementById('fcStarBtn');

    if (!cardEl) return;

    if (!this.fcCards.length) {
      cardEl.style.display = 'none';
      if (emptyEl) emptyEl.style.display = 'block';
      if (counterEl) counterEl.textContent = '0 / 0';
      if (progressEl) progressEl.style.width = '0%';
      return;
    }

    cardEl.style.display = 'block';
    if (emptyEl) emptyEl.style.display = 'none';
    cardEl.classList.toggle('is-flipped', this.fcFlipped);

    const c = this.fcCards[this.fcIndex];
    const st = this.fcState[c.id] || { status: 'new', starred: false };

    if (counterEl) counterEl.textContent = `${this.fcIndex + 1} / ${this.fcCards.length}`;
    if (progressEl) progressEl.style.width = `${Math.round(((this.fcIndex + 1) / this.fcCards.length) * 100)}%`;

    if (starBtn) {
      starBtn.textContent = st.starred ? '★ Starred' : '☆ Star Card';
      starBtn.style.color = st.starred ? '#f59e0b' : 'var(--muted)';
    }

    const frontSubjPill = document.getElementById('fcFrontSubj');
    const frontClassPill = document.getElementById('fcFrontClass');
    const frontChap = document.getElementById('fcFrontChap');
    const frontText = document.getElementById('fcFrontText');

    const backSubjPill = document.getElementById('fcBackSubj');
    const backText = document.getElementById('fcBackText');
    const backMnemonic = document.getElementById('fcBackMnemonic');
    const backTrap = document.getElementById('fcBackTrap');

    const subjTagClass = c.subject === 'Physics' ? 'tag-physics' : (c.subject === 'Chemistry' ? 'tag-chemistry' : (c.subject === 'Botany' ? 'tag-botany' : 'tag-zoology'));

    if (frontSubjPill) { frontSubjPill.textContent = c.subject; frontSubjPill.className = `tag ${subjTagClass}`; }
    if (frontClassPill) { frontClassPill.textContent = `Class ${c.classNum}`; }
    if (frontChap) { frontChap.textContent = `${c.chapter} · ${c.subtopic || ''}`; }
    if (frontText) { frontText.innerHTML = this.renderMarkdownAndMath(c.front); }

    if (backSubjPill) { backSubjPill.textContent = c.yield || 'High Yield'; }
    if (backText) { backText.innerHTML = this.renderMarkdownAndMath(c.back); }

    if (backMnemonic) {
      if (c.mnemonic) {
        backMnemonic.style.display = 'block';
        backMnemonic.innerHTML = `<b>💡 NEET Memory Hook:</b> ${this.renderMarkdownAndMath(c.mnemonic)}`;
      } else {
        backMnemonic.style.display = 'none';
      }
    }

    if (backTrap) {
      if (c.trap) {
        backTrap.style.display = 'block';
        backTrap.innerHTML = `<b>⚠️ NTA Distractor Trap Alert:</b> ${this.renderMarkdownAndMath(c.trap)}`;
      } else {
        backTrap.style.display = 'none';
      }
    }

    // Auto-render math in card if KaTeX is present
    if (typeof renderMathInElement === 'function') {
      try {
        renderMathInElement(cardEl, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false }
          ],
          throwOnError: false
        });
      } catch (e) {}
    }
  },

  renderMarkdownAndMath(text) {
    if (!text) return '';
    let html = text
      .replace(/\*\*(.*?)\*\*/g, '<b>$1</b>')
      .replace(/\*(.*?)\*/g, '<i>$1</i>')
      .replace(/\n/g, '<br>');
    return html;
  },

  updateFlashcardStats() {
    const raw = window.PREPWISE_FLASHCARDS || [];
    let mastered = 0;
    let review = 0;
    let starred = 0;

    Object.values(this.fcState).forEach(s => {
      if (s.status === 'mastered') mastered++;
      if (s.status === 'review') review++;
      if (s.starred) starred++;
    });

    const mEl = document.getElementById('fcMasteredCount');
    const rEl = document.getElementById('fcReviewCount');
    const sEl = document.getElementById('fcStarredCount');
    const tEl = document.getElementById('fcTotalCount');

    if (mEl) mEl.textContent = mastered;
    if (rEl) rEl.textContent = review;
    if (sEl) sEl.textContent = starred;
    if (tEl) tEl.textContent = raw.length;
  },

  showFlashcards() {
    this.showView('flashcardsView');
    this.initFlashcards();
  }
});
