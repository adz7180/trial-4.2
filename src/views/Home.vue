<template>
  <div class="home">
    <!-- Navbar -->
    <nav class="navbar">
      <RouterLink to="/" class="logo">
        <img src="@/assets/logo.png" alt="HomeStyle" />
      </RouterLink>
      <ul class="nav-links">
        <li><RouterLink to="/scan">Scan to 3D</RouterLink></li>
        <li><RouterLink to="/customize">Customize</RouterLink></li>
        <li><RouterLink to="/public">Explore Public</RouterLink></li>
      </ul>
      <button class="menu-toggle" @click="open = !open">
        <svg viewBox="0 0 24 24"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </nav>

    <!-- Mobile Nav -->
    <transition name="fade">
      <ul v-if="open" class="mobile-links">
        <li><RouterLink to="/scan" @click="open=false">Scan to 3D</RouterLink></li>
        <li><RouterLink to="/customize" @click="open=false">Customize</RouterLink></li>
        <li><RouterLink to="/public" @click="open=false">Explore Public</RouterLink></li>
      </ul>
    </transition>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-content">
        <h1>Design Your Dream Home</h1>
        <p>Scan, customize & visualize in hyper‑realistic 3D</p>
        <div class="cta">
          <RouterLink to="/scan" class="btn btn-primary">Scan Blueprint</RouterLink>
          <RouterLink to="/customize" class="btn btn-outline">Start Designing</RouterLink>
        </div>
      </div>
      <div class="hero-image">
        <img src="@/assets/hero-preview.png" alt="3D Preview" />
      </div>
    </section>

    <!-- Features -->
    <section class="features">
      <h2>Everything You Need</h2>
      <div class="feature-grid">
        <div class="feature-card">
          <div class="icon-wrapper">
            <img src="@/assets/scan-icon.png" alt="" />
          </div>
          <h3>Scan Blueprints</h3>
          <p>Instantly convert 2D plans into editable 3D models.</p>
        </div>
        <div class="feature-card">
          <div class="icon-wrapper">
            <img src="@/assets/edit-icon.png" alt="" />
          </div>
          <h3>Full Customization</h3>
          <p>Change floors, walls, lighting & furniture in real time.</p>
        </div>
        <div class="feature-card">
          <div class="icon-wrapper">
            <img src="@/assets/share-icon.png" alt="" />
          </div>
          <h3>Explore & Share</h3>
          <p>Publish your designs or browse the community gallery.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
const open = ref(false);
</script>

<style scoped lang="scss">
// Color palette
$white: #ffffff;
$black: #000;
$primary: #007AFF;
$text-dark: #1A1A1A;
$bg-light: #F5F5F7;

// Global reset
.home {
  font-family: 'Inter', sans-serif;
  color: $text-dark;
  background: $bg-light;
  overflow-x: hidden;
  min-height: 100vh;
}

// Navbar
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2rem;
  background: rgba($white, 0.75);
  backdrop-filter: blur(12px);
  box-shadow: 0 2px 10px rgba($black, 0.05);

  .logo img {
    height: 2.5rem;
  }

  .nav-links {
    display: flex;
    gap: 2rem;

    a {
      position: relative;
      text-decoration: none;
      color: $text-dark;
      font-weight: 600;
      transition: color 0.3s;

      &::after {
        content: '';
        position: absolute;
        bottom: -0.25rem;
        left: 0;
        width: 0;
        height: 2px;
        background: $primary;
        transition: width 0.3s;
      }
      &:hover {
        color: $primary;
        &::after {
          width: 100%;
        }
      }
    }
  }

  .menu-toggle {
    display: none;
    background: none;
    border: none;
    svg {
      width: 1.75rem;
      height: 1.75rem;
      stroke: $text-dark;
      stroke-width: 2;
    }
  }
}

.mobile-links {
  position: absolute;
  top: 100%;
  right: 0;
  background: $white;
  width: 100%;
  list-style: none;
  padding: 1rem 2rem;
  box-shadow: 0 4px 12px rgba($black, 0.1);

  li + li {
    margin-top: 1rem;
  }
  a {
    color: $text-dark;
    font-weight: 600;
    font-size: 1.1rem;
  }
}

// Hero
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6rem 2rem;

  .hero-content {
    max-width: 40rem;

    h1 {
      font-size: 3.5rem;
      line-height: 1.1;
      margin-bottom: 1rem;
    }
    p {
      font-size: 1.25rem;
      margin-bottom: 2rem;
      color: darken($text-dark, 10%);
    }
    .cta {
      display: flex;
      gap: 1.5rem;

      .btn {
        padding: 0.875rem 2rem;
        font-weight: 700;
        border-radius: 0.75rem;
        transition: transform 0.3s, box-shadow 0.3s;

        &.btn-primary {
          background: $primary;
          color: $white;
          box-shadow: 0 8px 20px rgba($primary, 0.3);
          &:hover { transform: translateY(-3px); }
        }
        &.btn-outline {
          background: transparent;
          border: 2px solid $primary;
          color: $primary;
          &:hover {
            background: $primary;
            color: $white;
            transform: translateY(-3px);
          }
        }
      }
    }
  }

  .hero-image img {
    max-width: 500px;
    border-radius: 2rem;
    box-shadow: 0 20px 40px rgba($black, 0.1);
    transition: transform 0.5s;
    &:hover { transform: scale(1.02); }
  }
}

// Features
.features {
  text-align: center;
  padding: 6rem 2rem;
  background: $white;

  h2 {
    font-size: 2.5rem;
    margin-bottom: 3rem;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
    gap: 2.5rem;

    .feature-card {
      background: rgba($white, 0.6);
      backdrop-filter: blur(8px);
      border-radius: 1.5rem;
      padding: 2rem;
      box-shadow: 0 10px 30px rgba($black, 0.05);
      transition: transform 0.3s;

      &:hover { transform: translateY(-5px); }

      .icon-wrapper {
        width: 3rem;
        height: 3rem;
        margin: 0 auto 1rem;
      }
      h3 {
        font-size: 1.25rem;
        margin-bottom: 0.75rem;
        color: $text-dark;
      }
      p {
        color: darken($text-dark, 20%);
        font-size: 1rem;
        line-height: 1.5;
      }
    }
  }
}

// Responsive
@media (max-width: 768px) {
  .navbar .nav-links { display: none; }
  .navbar .menu-toggle { display: block; }
  .hero { flex-direction: column; text-align: center; gap: 3rem; }
}
</style>

