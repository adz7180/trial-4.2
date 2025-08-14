<template>
  <div class="app-container">
    <!-- Navbar -->
    <header class="navbar">
      <div class="navbar-left">
        <RouterLink to="/" class="logo" aria-label="HexaNest Home">
          <!-- Inline black-on-white HexaNest Logo -->
          <svg class="mark" viewBox="0 0 120 120" role="img" aria-label="HexaNest Logo">
            <path d="M60 8 16 33v54l44 25 44-25V33L60 8Zm0 10 34 19v46L60 102 26 83V37l34-19Z" />
            <path d="M60 36 39 48v30l21 12 21-12V48L60 36Zm0 10 13 8v22l-13 7-13-7V54l13-8Z" />
            <rect x="57" y="66" width="6" height="20" rx="3" />
          </svg>
          <span class="brand-name">HEXANEST</span>
        </RouterLink>

        <nav class="nav-links">
          <RouterLink to="/" exact-active-class="active-link">Home</RouterLink>
          <RouterLink to="/scan" exact-active-class="active-link">Scan to 3D</RouterLink>
          <RouterLink to="/presets" exact-active-class="active-link">Preset Homes</RouterLink>
        </nav>
      </div>

      <div class="navbar-right">
        <RouterLink to="/login" class="btn btn-outline">Log In</RouterLink>
        <RouterLink to="/signup" class="btn btn-primary">Sign Up</RouterLink>
      </div>
    </header>

    <!-- Main Content -->
    <main>
      <!-- Hero Section -->
      <section class="hero-section" id="hero">
        <div class="hero-text">
          <h1>Design your home in real time.</h1>
          <p>Walk through, customize, and finalize every detail with ultra-real 4K visuals. From blueprint to photorealistic model—instantly.</p>
          <div class="hero-cta">
            <RouterLink to="/scan" class="btn btn-primary btn-large">Upload a Blueprint</RouterLink>
            <RouterLink to="/presets" class="btn btn-outline btn-large">Explore Preset Homes</RouterLink>
          </div>
          <div class="hero-badges">
            <span>4K Visuals</span>
            <span>Real-time Editing</span>
            <span>Room-by-Room Materials</span>
          </div>
        </div>

        <div class="hero-image" aria-hidden="true">
          <!-- Replace with your asset if desired -->
          <div class="glass-card"></div>
        </div>
      </section>

      <!-- Features Section -->
      <section class="features-section" aria-label="Key features of HexaNest" id="features">
        <h2>Built for creators, architects, and homeowners</h2>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon minimal-icon" aria-hidden="true"></div>
            <h3>Blueprint Scanning</h3>
            <p>Turn 2D blueprints into navigable, editable 3D models—walls, rooms, and openings detected.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon minimal-icon" aria-hidden="true"></div>
            <h3>Full Customization</h3>
            <p>Swap materials, fixtures, lighting, and furniture instantly with photoreal precision.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon minimal-icon" aria-hidden="true"></div>
            <h3>Share & Collaborate</h3>
            <p>Organize projects into folders, invite feedback, and export renders and floor plans.</p>
          </div>
        </div>
      </section>

      <!-- Subscription Plans -->
      <section class="plans-section" aria-label="Subscription plans" id="plans">
        <h2>Choose your plan</h2>
        <p class="subtitle">Start with a full-featured free trial. Upgrade anytime.</p>

        <div class="plans-grid">
          <article class="plan-card">
            <header>
              <h3>Free Trial</h3>
              <p class="plan-price"><span class="price">$0</span> / 7 days</p>
            </header>
            <ul class="plan-features">
              <li>Scan 1 blueprint to 3D</li>
              <li>Preset home exploration</li>
              <li>Standard materials</li>
              <li>Shareable link</li>
            </ul>
            <RouterLink to="/signup" class="btn btn-outline btn-block">Start Free Trial</RouterLink>
          </article>

          <article class="plan-card popular">
            <header>
              <h3>Premium</h3>
              <p class="plan-price"><span class="price">$30</span> / month</p>
              <span class="popular-badge">Most Popular</span>
            </header>
            <ul class="plan-features">
              <li>Unlimited preset homes</li>
              <li>Scan-to-3D with full editing</li>
              <li>All materials & finishes</li>
              <li>Exports (renders & floor plans)</li>
              <li>Project folders & autosave</li>
              <li>Priority support</li>
            </ul>
            <RouterLink to="/subscribe" class="btn btn-primary btn-block">Upgrade to Premium</RouterLink>
          </article>

          <article class="plan-card">
            <header>
              <h3>Company</h3>
              <p class="plan-price"><span class="price">$79</span> / month</p>
            </header>
            <ul class="plan-features">
              <li>Team collaboration</li>
              <li>Brand kit & watermark</li>
              <li>Contractor sharing</li>
              <li>API & Admin dashboard</li>
              <li>Advanced exports (4K/8K)</li>
            </ul>
            <RouterLink to="/contact" class="btn btn-outline btn-block">Contact Sales</RouterLink>
          </article>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>© {{ new Date().getFullYear() }} HexaNest. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<!-- Global (non-scoped) styles to guarantee scrolling and smooth behavior -->
<style lang="scss">
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  scroll-behavior: smooth;
}

#app, .app-container {
  min-height: 100%;
}

.app-container {
  overflow-x: hidden; /* no sideways scroll */
  overflow-y: auto;   /* ensure vertical scroll */
}
</style>

<style scoped lang="scss">
/* ===== Brand System (Apple/Tesla-inspired) ===== */
$bg: #FFFFFF;                 // primary background
$soft: #FAFAFA;               // light section alt
$ink: #1C1C1C;                // charcoal text
$muted: #6B6B6B;              // secondary text
$line: #EDEDED;               // hairline
$teal: #014D4E;               // deep-teal primary
$champagne: #C6A664;          // luxury accent
$radius: 22px;

/* Derived */
$shadow-soft: 0 10px 30px rgba(0,0,0,.08);
$shadow-strong: 0 25px 70px rgba(0,0,0,.16);

* { box-sizing: border-box; }
.app-container {
  font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  background: $bg; color: $ink; min-height: 100vh;
  display: flex; flex-direction: column;
}

/* ===== Navbar ===== */
.navbar {
  position: sticky; top: 0; z-index: 1000;
  display: flex; justify-content: space-between; align-items: center;
  padding: 1rem 3rem;
  background: rgba(255, 255, 255, 0.88);
  backdrop-filter: saturate(180%) blur(10px);
  border-bottom: 1px solid transparent;
  transition: border-color .25s ease, box-shadow .25s ease;
  box-shadow: 0 4px 12px rgba(0,0,0,.06);

  .navbar-left {
    display: flex; align-items: center; gap: 2rem;

    .logo {
      display: flex; align-items: center; gap: .75rem;
      color: inherit; text-decoration: none; user-select: none;

      .mark { width: 40px; height: 40px; fill: currentColor; color: $ink; }
      .brand-name { font-weight: 900; letter-spacing: .08em; }
    }

    .nav-links {
      display: flex; gap: 2rem;

      a {
        font-weight: 600; color: $muted; text-decoration: none; font-size: 1.05rem;
        padding-bottom: 3px; border-bottom: 3px solid transparent; transition: all .25s ease;

        &.active-link, &:hover { color: $teal; border-color: $teal; }
      }
    }
  }

  .navbar-right {
    display: flex; gap: 1rem;

    a.btn {
      padding: .6rem 1.6rem; font-weight: 700; font-size: 1rem;
      border-radius: $radius; cursor: pointer; transition: all .25s ease;
      text-align: center; text-decoration: none
