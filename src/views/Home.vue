<template>
  <div class="home">
    <!-- Navbar -->
    <nav class="navbar">
      <RouterLink to="/" class="logo" aria-label="Home">
        <img src="@/assets/logo.png" alt="HomeStyle" />
      </RouterLink>
      <ul class="nav-links">
        <li><RouterLink to="/scan">Scan to 3D</RouterLink></li>
        <li><RouterLink to="/customize">Customize</RouterLink></li>
        <!-- Removed Explore Public -->
      </ul>
      <button class="menu-toggle" @click="open = !open" aria-label="Toggle menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </nav>

    <!-- Mobile Nav -->
    <transition name="fade">
      <ul v-if="open" class="mobile-links" role="menu">
        <li role="menuitem"><RouterLink to="/scan" @click="open=false">Scan to 3D</RouterLink></li>
        <li role="menuitem"><RouterLink to="/customize" @click="open=false">Customize</RouterLink></li>
        <!-- Removed Explore Public -->
      </ul>
    </transition>

    <!-- Hero -->
    <section class="hero" role="banner">
      <div class="hero-content">
        <h1>Design Your Dream Home</h1>
        <p>Scan, customize & visualize in hyper‑realistic 3D</p>
        <div class="cta">
          <RouterLink to="/scan" class="btn btn-primary">Scan Blueprint</RouterLink>
          <RouterLink to="/customize" class="btn btn-outline">Start Designing</RouterLink>
        </div>
      </div>
      <div class="hero-image" aria-hidden="true">
        <img src="@/assets/hero-preview.png" alt="3D Preview of home design" />
      </div>
    </section>

    <!-- Features -->
    <section class="features" aria-label="Key features">
      <h2>Everything You Need</h2>
      <div class="feature-grid">
        <div class="feature-card" tabindex="0">
          <div class="icon-wrapper">
            <img src="@/assets/scan-icon.png" alt="Scan icon" />
          </div>
          <h3>Scan Blueprints</h3>
          <p>Instantly convert 2D plans into editable 3D models.</p>
        </div>
        <div class="feature-card" tabindex="0">
          <div class="icon-wrapper">
            <img src="@/assets/edit-icon.png" alt="Edit icon" />
          </div>
          <h3>Full Customization</h3>
          <p>Change floors, walls, lighting & furniture in real time.</p>
        </div>
        <div class="feature-card" tabindex="0">
          <div class="icon-wrapper">
            <img src="@/assets/share-icon.png" alt="Share icon" />
          </div>
          <h3>Share Designs</h3>
          <p>Publish your creations or browse community projects.</p>
        </div>
      </div>
    </section>

    <!-- Subscription Plans -->
    <section class="subscription" aria-label="Subscription plans">
      <h2>Choose Your Plan</h2>
      <div class="plans-grid">
        <div class="plan-card">
          <h3>Free Trial</h3>
          <p class="price">$0 <span>/ 3 days</span></p>
          <ul>
            <li>Access to basic features</li>
            <li>Limited customization options</li>
            <li>3-day trial period</li>
          </ul>
          <button class="btn btn-outline">Start Free Trial</button>
        </div>
        <div class="plan-card popular">
          <h3>Premium</h3>
          <p class="price">$30 <span>/ month</span></p>
          <ul>
            <li>Full access to all customization</li>
            <li>Download designs & export options</li>
            <li>Priority support</li>
          </ul>
          <button class="btn btn-primary">Subscribe Now</button>
        </div>
        <div class="plan-card">
          <h3>Company</h3>
          <p class="price">$60 <span>/ month</span></p>
          <ul>
            <li>Multi-user collaboration</li>
            <li>API access & contractor matching</li>
            <li>Dedicated account manager</li>
          </ul>
          <button class="btn btn-outline">Contact Sales</button>
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
// Colors
$white: #ffffff;
$black: #000000;
$primary: #0066FF;
$primary-light: #cce0ff;
$text-dark: #222222;
$text-muted: #555555;
$bg-light: #f9fafb;
$shadow-light: rgba(0,0,0,0.05);
$shadow-strong: rgba(0,0,0,0.15);

// Fonts
$font-family: 'Inter', sans-serif;

// Root
.home {
  font-family: $font-family;
  background: $bg-light;
  color: $text-dark;
  min-height: 100vh;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  scroll-behavior: smooth;
}

// Navbar
.navbar {
  position: sticky;
  top: 0;
  z-index: 999;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 3rem;
  background: rgba($white, 0.85);
  backdrop-filter: saturate(180%) blur(20px);
  box-shadow: 0 4px 15px $shadow-light;
  transition: background 0.3s ease;

  .logo img {
    height: 3rem;
    user-select: none;
  }

  .nav-links {
    display: flex;
    gap: 2.5rem;

    a {
      font-weight: 600;
      font-size: 1.05rem;
      color: $text-dark;
      text-decoration: none;
      position: relative;
      padding-bottom: 4px;

      &:hover,
      &.router-link-exact-active {
        color: $primary;

        &::after {
          content: '';
          position: absolute;
          bottom: 0;
          left: 0;
          width: 100%;
          height: 3px;
          background: $primary;
          border-radius: 3px 3px 0 0;
        }
      }
    }
  }

  .menu-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    svg {
      width: 1.8rem;
      height: 1.8rem;
      stroke: $text-dark;
      stroke-width: 2.2;
      transition: stroke 0.3s;
      &:hover {
        stroke: $primary;
      }
    }
  }
}

// Mobile nav
.mobile-links {
  position: absolute;
  top: 100%;
  right: 0;
  width: 100%;
  background: $white;
  box-shadow: 0 6px 18px $shadow-strong;
  padding: 1.25rem 3rem;
  list-style: none;
  z-index: 998;

  li + li {
    margin-top: 1.2rem;
  }
  a {
    font-size: 1.15rem;
    font-weight: 600;
    color: $text-dark;
    text-decoration: none;

    &:hover {
      color: $primary;
    }
  }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.25s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

// Hero section
.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6rem 4rem;
  gap: 4rem;

  .hero-content {
    max-width: 480px;

    h1 {
      font-size: 3.75rem;
      line-height: 1.1;
      font-weight: 900;
      margin-bottom: 1rem;
      color: $primary;
      text-shadow: 1px 1px 8px rgba($primary, 0.3);
    }

    p {
      font-size: 1.5rem;
      margin-bottom: 2.5rem;
      color: darken($text-dark, 15%);
    }

    .cta {
      display: flex;
      gap: 1.75rem;

      .btn {
        border-radius: 12px;
        font-weight: 700;
        padding: 1rem 2.5rem;
        font-size: 1.125rem;
        box-shadow: 0 12px 30px rgba($primary, 0.35);
        cursor: pointer;
        transition: all 0.3s ease;

        &.btn-primary {
          background: $primary;
          color: $white;
          border: none;
          &:hover {
            background: darken($primary, 10%);
            box-shadow: 0 15px 40px rgba($primary, 0.5);
            transform: translateY(-4px);
          }
        }

        &.btn-outline {
          background: transparent;
          border: 3px solid $primary;
          color: $primary;
          &:hover {
            background: $primary;
            color: $white;
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba($primary, 0.35);
          }
        }
      }
    }
  }

  .hero-image img {
    width: 520px;
    border-radius: 32px;
    box-shadow: 0 40px 80px rgba($primary, 0.15);
    transition: transform 0.5s ease;

    &:hover {
      transform: scale(1.05) rotate(-1deg);
    }
  }
}

// Features section
.features {
  background: $white;
  padding: 6rem 4rem;
  text-align: center;

  h2 {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 3.5rem;
    color: $text-dark;
  }

  .feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 3.5rem;

    .feature-card {
      background: rgba($primary-light, 0.35);
      border-radius: 24px;
      padding: 3rem 2.5rem;
      box-shadow: 0 15px 40px rgba($primary, 0.15);
      transition: transform 0.3s ease;
      cursor: default;

      &:hover {
        transform: translateY(-12px);
        box-shadow: 0 20px 60px rgba($primary, 0.3);
      }

      .icon-wrapper {
        width: 4.5rem;
        height: 4.5rem;
        margin: 0 auto 1.5rem;
        filter: drop-shadow(0 3px 3px rgba($primary, 0.3));
        img {
          width: 100%;
          height: 100%;
          object-fit: contain;
        }
      }

      h3 {
        font-size: 1.5rem;
        margin-bottom: 0.75rem;
        color: $primary;
        font-weight: 800;
      }

      p {
        font-size: 1.1rem;
        color: darken($text-dark, 20%);
        line-height: 1.4;
      }
    }
  }
}

// Subscription plans section
.subscription {
  background: linear-gradient(135deg, $primary-light 0%, lighten($primary-light, 15%) 100%);
  padding: 5rem 4rem;
  color: $text-dark;
  text-align: center;
  border-radius: 32px 32px 0 0;
  margin-top: auto; // Push to bottom if container flex

  h2 {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 3rem;
    color: darken($primary, 15%);
  }

  .plans-grid {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;

    .plan-card {
      background: $white;
      color: $text-dark;
      border-radius: 24px;
      box-shadow: 0 10px 30px $shadow-light;
      padding: 2.5rem 3rem;
      max-width: 280px;
      flex: 1 1 280px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: box-shadow 0.3s ease;

      &.popular {
        border: 3px solid $primary;
        box-shadow: 0 20px 60px rgba($primary, 0.4);
        transform: translateY(-8px);
      }

      h3 {
        font-size: 1.75rem;
        font-weight: 900;
        margin-bottom: 0.75rem;
      }

      .price {
        font-size: 2.25rem;
        font-weight: 900;
        margin-bottom: 2rem;
        color: $primary;

        span {
          font-size: 1rem;
          font-weight: 600;
          color: $text-muted;
          margin-left: 0.25rem;
        }
      }

      ul {
        list-style: none;
        padding: 0;
        margin-bottom: 2rem;
        width: 100%;
        color: $text-muted;
        font-weight: 600;
        font-size: 1rem;
        line-height: 1.5;

        li {
          margin-bottom: 1rem;
          position: relative;
          padding-left: 1.5rem;

          &::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: $primary;
            font-weight: 900;
          }
        }
      }

      button {
        padding: 0.9rem 2.5rem;
        border-radius: 16px;
        font-weight: 700;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.3s ease;

        &.btn-primary {
          background: $primary;
          border: none;
          color: $white;

          &:hover {
            background: darken($primary, 10%);
            box-shadow: 0 15px 40px rgba($primary, 0.6);
            transform: translateY(-3px);
          }
        }

        &.btn-outline {
          background: transparent;
          border: 3px solid $primary;
          color: $primary;

          &:hover {
            background: $primary;
            color: $white;
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba($primary, 0.35);
          }
        }
      }
    }
  }
}

// Responsive adjustments
@media (max-width: 992px) {
  .hero {
    flex-direction: column;
    padding: 4rem 2rem;
    text-align: center;

    .hero-image img {
      width: 90vw;
      max-width: 400px;
      margin: 0 auto;
      margin-top: 2rem;
      transform: none !important;
    }
  }

  .features .feature-grid {
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  }

  .subscription .plans-grid {
    flex-direction: column;
    gap: 2rem;
  }

  .navbar {
    padding: 1rem 2rem;
  }
}

@media (max-width: 480px) {
  .nav-links {
    display: none;
  }

  .menu-toggle {
    display: block;
  }
}
</style>
