<template>
  <div class="app-container">
    <!-- Navbar -->
    <header class="navbar">
      <div class="navbar-left">
        <RouterLink to="/" class="logo" aria-label="HexaNest Home">
          <img src="@/assets/logo.png" alt="HexaNest Logo" />
          <span class="brand-name">HexaNest</span>
        </RouterLink>
        <nav class="nav-links">
          <RouterLink to="/" exact-active-class="active-link">Home</RouterLink>
          <RouterLink to="/scan" exact-active-class="active-link">Scan to 3D</RouterLink>
          <RouterLink to="/customize" exact-active-class="active-link">Customize</RouterLink>
        </nav>
      </div>
      <div class="navbar-right">
        <RouterLink to="/login" class="btn btn-outline">Login</RouterLink>
        <RouterLink to="/signup" class="btn btn-primary">Sign Up</RouterLink>
      </div>
    </header>

    <!-- Main Content -->
    <main>
      <!-- Hero Section -->
      <section class="hero-section">
        <div class="hero-text">
          <h1>Build Your Dream Home with HexaNest</h1>
          <p>Scan blueprints, customize interiors, and visualize in ultra-realistic 3D.</p>
          <div class="hero-cta">
            <RouterLink to="/scan" class="btn btn-primary btn-large">Scan Blueprint</RouterLink>
            <RouterLink to="/customize" class="btn btn-outline btn-large">Start Designing</RouterLink>
          </div>
        </div>
        <div class="hero-image">
          <img src="@/assets/hero-home.png" alt="3D home design preview" />
        </div>
      </section>

      <!-- Features Section -->
      <section class="features-section" aria-label="Key features of HexaNest">
        <h2>Why HexaNest?</h2>
        <div class="features-grid">
          <div class="feature-card">
            <img src="@/assets/icons/blueprint.svg" alt="" class="feature-icon" />
            <h3>Blueprint Scanning</h3>
            <p>Turn your 2D blueprints into fully editable 3D models instantly.</p>
          </div>
          <div class="feature-card">
            <img src="@/assets/icons/customization.svg" alt="" class="feature-icon" />
            <h3>Full Customization</h3>
            <p>Modify floors, walls, furniture, lighting, and more in real-time.</p>
          </div>
          <div class="feature-card">
            <img src="@/assets/icons/share.svg" alt="" class="feature-icon" />
            <h3>Share & Collaborate</h3>
            <p>Publish your designs or browse community projects for inspiration.</p>
          </div>
        </div>
      </section>

      <!-- Subscription Plans -->
      <section class="plans-section" aria-label="Subscription plans">
        <h2>Choose Your Plan</h2>
        <div class="plans-grid">
          <article class="plan-card">
            <header>
              <h3>Free Trial</h3>
              <p class="plan-price"><span class="price">$0</span> / 3 days</p>
            </header>
            <ul class="plan-features">
              <li>Access to basic features</li>
              <li>Limited customization options</li>
              <li>3-day trial period</li>
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
              <li>Full customization access</li>
              <li>Download & export your designs</li>
              <li>Priority support</li>
            </ul>
            <RouterLink to="/subscribe" class="btn btn-primary btn-block">Subscribe Now</RouterLink>
          </article>

          <article class="plan-card">
            <header>
              <h3>Company</h3>
              <p class="plan-price"><span class="price">$60</span> / month</p>
            </header>
            <ul class="plan-features">
              <li>Multi-user collaboration</li>
              <li>API access & contractor matching</li>
              <li>Dedicated account manager</li>
            </ul>
            <RouterLink to="/contact" class="btn btn-outline btn-block">Contact Sales</RouterLink>
          </article>
        </div>
      </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
      <p>© 2025 HexaNest. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped lang="scss">
$app-primary: #0066ff;
$app-primary-light: #cce4ff;
$app-bg: #f9fafb;
$app-text: #1a1a1a;
$app-text-muted: #555;
$app-radius: 20px;
$app-shadow: rgba(0, 102, 255, 0.25);

* {
  box-sizing: border-box;
}

.app-container {
  font-family: 'Inter', sans-serif;
  background: $app-bg;
  color: $app-text;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 3rem;
  background: rgba(255 255 255 / 0.9);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  position: sticky;
  top: 0;
  z-index: 1000;

  .navbar-left {
    display: flex;
    align-items: center;
    gap: 2rem;

    .logo {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 900;
      font-size: 1.5rem;
      color: $app-primary;
      text-decoration: none;
      user-select: none;

      img {
        width: 40px;
        height: 40px;
        object-fit: contain;
      }
    }

    .nav-links {
      display: flex;
      gap: 2rem;

      a {
        font-weight: 600;
        color: $app-text-muted;
        text-decoration: none;
        font-size: 1.1rem;
        padding-bottom: 3px;
        border-bottom: 3px solid transparent;
        transition: all 0.3s ease;

        &.active-link,
        &:hover {
          color: $app-primary;
          border-color: $app-primary;
        }
      }
    }
  }

  .navbar-right {
    display: flex;
    gap: 1rem;

    a.btn {
      padding: 0.6rem 1.6rem;
      font-weight: 700;
      font-size: 1rem;
      border-radius: $app-radius;
      cursor: pointer;
      transition: all 0.3s ease;
      text-align: center;
      text-decoration: none;
      user-select: none;

      &.btn-primary {
        background-color: $app-primary;
        color: white;
        border: none;
        box-shadow: 0 5px 15px $app-shadow;

        &:hover {
          background-color: darken($app-primary, 10%);
          box-shadow: 0 8px 25px rgba(0, 102, 255, 0.4);
        }
      }

      &.btn-outline {
        background-color: transparent;
        color: $app-primary;
        border: 2.5px solid $app-primary;

        &:hover {
          background-color: $app-primary;
          color: white;
          box-shadow: 0 8px 25px rgba(0, 102, 255, 0.3);
        }
      }
    }
  }
}

/* Main */
main {
  flex: 1;
  padding: 3rem 6rem;
  display: flex;
  flex-direction: column;
  gap: 6rem;

  @media (max-width: 900px) {
    padding: 2rem 2rem;
  }
}

/* Hero Section */
.hero-section {
  display: flex;
  align-items: center;
  gap: 4rem;

  @media (max-width: 850px) {
    flex-direction: column;
    text-align: center;
  }

  .hero-text {
    flex: 1;

    h1 {
      font-size: 3.75rem;
      font-weight: 900;
      margin-bottom: 1rem;
      color: $app-primary;
      line-height: 1.1;
      user-select: none;
      text-shadow: 1px 1px 6px rgba($app-primary, 0.35);
    }

    p {
      font-size: 1.5rem;
      margin-bottom: 2.5rem;
      color: $app-text-muted;
      font-weight: 500;
      max-width: 450px;
      user-select: none;
    }

    .hero-cta {
      display: flex;
      gap: 2rem;
      flex-wrap: wrap;
      justify-content: flex-start;

      @media (max-width: 850px) {
        justify-content: center;
      }

      .btn-large {
        font-size: 1.25rem;
        padding: 1rem 3rem;
        border-radius: $app-radius;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
      }
    }
  }

  .hero-image {
    flex: 1;

    img {
      width: 100%;
      max-width: 550px;
      border-radius: 30px;
      box-shadow: 0 30px 80px rgba($app-primary, 0.25);
      transition: transform 0.6s ease;

      &:hover {
        transform: scale(1.05) rotate(-1deg);
      }
    }
  }
}

/* Features Section */
.features-section {
  text-align: center;

  h2 {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 3.5rem;
    user-select: none;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3.5rem;

    .feature-card {
      background: white;
      border-radius: 24px;
      padding: 2.5rem 2rem;
      box-shadow: 0 15px 40px rgba($app-primary, 0.1);
      transition: transform 0.3s ease;
      cursor: default;

      &:hover {
        transform: translateY(-12px);
        box-shadow: 0 25px 60px rgba($app-primary, 0.2);
      }

      .feature-icon {
        width: 60px;
        margin-bottom: 1.5rem;
        filter: drop-shadow(0 3px 5px rgba($app-primary, 0.3));
      }

      h3 {
        font-size: 1.5rem;
        margin-bottom: 0.75rem;
        color: $app-primary;
        font-weight: 900;
      }

      p {
        font-size: 1.1rem;
        color: $app-text-muted;
        line-height: 1.4;
      }
    }
  }
}

/* Plans Section */
.plans-section {
  background: linear-gradient(135deg, $app-primary-light 0%, lighten($app-primary-light, 15%) 100%);
  padding: 4rem 3rem;
  border-radius: 40px;
  color: $app-text;
  text-align: center;

  h2 {
    font-size: 3rem;
    font-weight: 900;
    margin-bottom: 3rem;
    user-select: none;
  }

  .plans-grid {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    justify-content: center;

    article.plan-card {
      background: white;
      border-radius: 28px;
      box-shadow: 0 15px 40px rgba($app-primary, 0.15);
      padding: 2.5rem 3rem;
      max-width: 320px;
      flex: 1 1 320px;
      display: flex;
      flex-direction: column;
      align-items: center;
      transition: box-shadow 0.3s ease;

      &.popular {
        border: 3.5px solid $app-primary;
        box-shadow: 0 25px 70px rgba($app-primary, 0.4);
        transform: translateY(-10px);
        position: relative;

        &::before {
          content: "Most Popular";
          position: absolute;
          top: -20px;
          right: 20px;
          background: $app-primary;
          color: white;
          padding: 0.25rem 1rem;
          font-weight: 700;
          border-radius: 14px;
          font-size: 0.875rem;
          user-select: none;
          box-shadow: 0 3px 10px rgba($app-primary, 0.5);
        }
      }

      header {
        margin-bottom: 2rem;

        h3 {
          font-size: 1.8rem;
          font-weight: 900;
          margin-bottom: 0.5rem;
        }

        .plan-price {
          font-size: 2.5rem;
          font-weight: 900;
          color: $app-primary;

          .price {
            font-weight: 900;
          }

          & > span {
            font-weight: 600;
            font-size: 1.15rem;
            color: $app-text-muted;
            margin-left: 0.25rem;
          }
        }
      }

      .plan-features {
        list-style: none;
        padding: 0;
        margin-bottom: 2.5rem;
        width: 100%;
        color: $app-text-muted;
        font-weight: 600;
        font-size: 1.05rem;
        line-height: 1.6;

        li {
          margin-bottom: 1.2rem;
          position: relative;
          padding-left: 1.6rem;

          &::before {
            content: "✓";
            position: absolute;
            left: 0;
            color: $app-primary;
            font-weight: 900;
            user-select: none;
          }
        }
      }

      .btn {
        width: 100%;
        padding: 1rem 0;
        font-weight: 700;
        font-size: 1.15rem;
        border-radius: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
        text-decoration: none;
        user-select: none;
        border: none;

        &.btn-primary {
          background-color: $app-primary;
          color: white;
          box-shadow: 0 15px 45px rgba($app-primary, 0.5);

          &:hover {
            background-color: darken($app-primary, 10%);
            box-shadow: 0 20px 60px rgba($app-primary, 0.6);
            transform: translateY(-3px);
          }
        }

        &.btn-outline {
          background-color: transparent;
          color: $app-primary;
          border: 3px solid $app-primary;

          &:hover {
            background-color: $app-primary;
            color: white;
            box-shadow: 0 15px 45px rgba($app-primary, 0.4);
            transform: translateY(-3px);
          }
        }

        &.btn-block {
          display: block;
        }
      }
    }
  }
}

/* Footer */
.footer {
  padding: 2rem 3rem;
  text-align: center;
  font-weight: 600;
  font-size: 1rem;
  color: $app-text-muted;
  user-select: none;
}

/* Responsive */
@media (max-width: 950px) {
  .hero-section {
    flex-direction: column;
    text-align: center;

    .hero-image img {
      max-width: 90vw;
      margin-top: 2rem;
      transform: none !important;
    }
  }

  main {
    padding: 2rem 2rem;
  }
}

@media (max-width: 700px) {
  .plans-section .plans-grid {
    flex-direction: column;
  }

  .navbar {
    padding: 1rem 1.5rem;

    .navbar-left {
      gap: 1rem;
    }

    .nav-links {
      gap: 1rem;
    }
  }
}
</style>
