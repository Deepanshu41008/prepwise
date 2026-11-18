// js/planner.js - Daily Targets, NEET Countdown, Study Streak & Activity Calendar
window.App = window.App || {};

Object.assign(window.App, {
  plannerTarget: 50,
  plannerExamDate: '2026-05-03T14:00:00', // Standard First Sunday of May
  plannerTimerInterval: null,

  loadPlannerSettings() {
    try {
      const savedTarget = localStorage.getItem('PREPWISE_DAILY_TARGET');
      if (savedTarget) this.plannerTarget = Number(savedTarget) || 50;

      const savedDate = localStorage.getItem('PREPWISE_EXAM_DATE');
      if (savedDate) this.plannerExamDate = savedDate;
    } catch (e) {}
  },

  savePlannerSettings() {
    try {
      localStorage.setItem('PREPWISE_DAILY_TARGET', this.plannerTarget);
      localStorage.setItem('PREPWISE_EXAM_DATE', this.plannerExamDate);
    } catch (e) {}
  },

  initPlanner() {
    this.loadPlannerSettings();
    this.startCountdownTicker();
    this.refreshPlannerData();
  },

  startCountdownTicker() {
    if (this.plannerTimerInterval) clearInterval(this.plannerTimerInterval);

    const updateCountdown = () => {
      const targetTime = new Date(this.plannerExamDate).getTime();
      const now = new Date().getTime();
      const diff = Math.max(0, targetTime - now);

      const days = Math.floor(diff / (1000 * 60 * 60 * 24));
      const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((diff % (1000 * 60)) / 1000);

      const dEl = document.getElementById('cdDays');
      const hEl = document.getElementById('cdHours');
      const mEl = document.getElementById('cdMins');
      const sEl = document.getElementById('cdSecs');

      if (dEl) dEl.textContent = String(days).padStart(2, '0');
      if (hEl) hEl.textContent = String(hours).padStart(2, '0');
      if (mEl) mEl.textContent = String(mins).padStart(2, '0');
      if (sEl) sEl.textContent = String(secs).padStart(2, '0');

      // Mini ticker on home dashboard
      const miniEl = document.getElementById('miniCountdownDays');
      if (miniEl) miniEl.textContent = `${days} Days to NEET`;
    };

    updateCountdown();
    this.plannerTimerInterval = setInterval(updateCountdown, 1000);
  },

  async refreshPlannerData() {
    const today = new Date().toISOString().split('T')[0];
    let attempts = [];
    try {
      if (window.db && db.attempts) {
        attempts = await db.attempts.toArray();
      }
    } catch (e) {}

    // 1. Calculate today's solved count and subject breakdown
    const todayAttempts = attempts.filter(a => {
      const d = a.timestamp ? new Date(a.timestamp).toISOString().split('T')[0] : today;
      return d === today;
    });

    const solvedToday = todayAttempts.length;
    const target = this.plannerTarget || 50;
    const pct = Math.min(100, Math.round((solvedToday / target) * 100));

    // Update circular progress ring
    const ringEl = document.getElementById('targetRingCircle');
    const ringText = document.getElementById('targetRingText');
    const ringSub = document.getElementById('targetRingSub');
    if (ringEl) {
      const radius = 54;
      const circumference = 2 * Math.PI * radius; // ~339.29
      const offset = circumference - (pct / 100) * circumference;
      ringEl.style.strokeDasharray = `${circumference} ${circumference}`;
      ringEl.style.strokeDashoffset = offset;
    }
    if (ringText) ringText.textContent = `${solvedToday} / ${target}`;
    if (ringSub) ringSub.textContent = `${pct}% of Daily Goal`;

    // 2. Calculate Streak
    const daysWithStudy = new Set();
    attempts.forEach(a => {
      if (a.timestamp) {
        daysWithStudy.add(new Date(a.timestamp).toISOString().split('T')[0]);
      }
    });

    // If student practiced today, add today
    if (solvedToday > 0) daysWithStudy.add(today);

    let streak = 0;
    let checkDate = new Date();
    // If today has 0, check if yesterday was active
    if (!daysWithStudy.has(today)) {
      checkDate.setDate(checkDate.getDate() - 1);
    }

    while (daysWithStudy.has(checkDate.toISOString().split('T')[0])) {
      streak++;
      checkDate.setDate(checkDate.getDate() - 1);
    }

    const streakEl = document.getElementById('plannerStreakVal');
    const streakBanner = document.getElementById('homeStreakVal');
    if (streakEl) streakEl.textContent = `${streak} ${streak === 1 ? 'Day' : 'Days'}`;
    if (streakBanner) streakBanner.textContent = `${streak} ${streak === 1 ? 'Day' : 'Days'}`;

    // 3. Subject Breakdown Today
    const subjs = { Physics: 0, Chemistry: 0, Botany: 0, Zoology: 0 };
    todayAttempts.forEach(a => {
      if (subjs[a.subject] !== undefined) subjs[a.subject]++;
    });

    const pBar = document.getElementById('subjBarPhy');
    const cBar = document.getElementById('subjBarChem');
    const bBar = document.getElementById('subjBarBot');
    const zBar = document.getElementById('subjBarZoo');

    const totalTodaySubjs = Math.max(1, solvedToday);
    if (pBar) pBar.style.width = `${Math.round((subjs.Physics / totalTodaySubjs) * 100)}%`;
    if (cBar) cBar.style.width = `${Math.round((subjs.Chemistry / totalTodaySubjs) * 100)}%`;
    if (bBar) bBar.style.width = `${Math.round((subjs.Botany / totalTodaySubjs) * 100)}%`;
    if (zBar) zBar.style.width = `${Math.round((subjs.Zoology / totalTodaySubjs) * 100)}%`;

    // 4. Render 30-Day Activity Calendar
    this.renderActivityCalendar(daysWithStudy, attempts);
  },

  renderActivityCalendar(activeDays, attempts) {
    const container = document.getElementById('activityCalendarGrid');
    if (!container) return;

    // Count Qs per day
    const dayCounts = {};
    attempts.forEach(a => {
      if (a.timestamp) {
        const d = new Date(a.timestamp).toISOString().split('T')[0];
        dayCounts[d] = (dayCounts[d] || 0) + 1;
      }
    });

    const tiles = [];
    const now = new Date();
    for (let i = 29; i >= 0; i--) {
      const d = new Date(now);
      d.setDate(d.getDate() - i);
      const dateStr = d.toISOString().split('T')[0];
      const count = dayCounts[dateStr] || 0;

      let level = 'lvl-0';
      if (count > 0 && count < 15) level = 'lvl-1';
      else if (count >= 15 && count < 40) level = 'lvl-2';
      else if (count >= 40 && count < 80) level = 'lvl-3';
      else if (count >= 80) level = 'lvl-4';

      const dayNum = d.getDate();
      const monthShort = d.toLocaleString('default', { month: 'short' });

      tiles.push(`
        <div class="cal-tile ${level}" title="${monthShort} ${dayNum}: ${count} questions solved">
          <small>${dayNum}</small>
        </div>
      `);
    }

    container.innerHTML = tiles.join('');
  },

  setDailyTarget(val) {
    this.plannerTarget = Math.max(5, Number(val) || 50);
    this.savePlannerSettings();
    document.querySelectorAll('.target-pill-btn').forEach(b => {
      b.classList.toggle('active', Number(b.dataset.target) === this.plannerTarget);
    });
    this.refreshPlannerData();
  },

  setExamDate(dateStr) {
    if (!dateStr) return;
    this.plannerExamDate = `${dateStr}T14:00:00`;
    this.savePlannerSettings();
    this.startCountdownTicker();
  },

  showPlanner() {
    this.showView('plannerView');
    this.initPlanner();
  }
});
