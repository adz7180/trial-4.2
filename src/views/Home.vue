<template>
  <div class="min-h-screen bg-[#1C1F2B] text-white font-inter">
    <!-- Navbar -->
    <nav class="container mx-auto flex items-center justify-between py-6 px-4">
      <div class="text-2xl font-bold">HomeStyle</div>
      <ul class="hidden md:flex space-x-8 text-lg">
        <li><RouterLink to="/" class="hover:text-blue-400 transition">Home</RouterLink></li>
        <li><RouterLink to="/scan" class="hover:text-blue-400 transition">Scan</RouterLink></li>
        <li><RouterLink to="/customize" class="hover:text-blue-400 transition">Customize</RouterLink></li>
        <li><RouterLink to="/pricing" class="hover:text-blue-400 transition">Pricing</RouterLink></li>
        <li><RouterLink to="/products" class="hover:text-blue-400 transition">Products</RouterLink></li>
      </ul>
      <div class="md:hidden">
        <button @click="open = !open">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
      </div>
    </nav>
    <!-- Mobile Menu -->
    <transition name="fade">
      <div v-if="open" class="md:hidden bg-[#1C1F2B] px-4 pb-4">
        <ul class="space-y-4">
          <li><RouterLink to="/" class="block" @click="open=false">Home</RouterLink></li>
          <li><RouterLink to="/scan" class="block" @click="open=false">Scan</RouterLink></li>
          <li><RouterLink to="/customize" class="block" @click="open=false">Customize</RouterLink></li>
          <li><RouterLink to="/pricing" class="block" @click="open=false">Pricing</RouterLink></li>
          <li><RouterLink to="/products" class="block" @click="open=false">Products</RouterLink></li>
        </ul>
      </div>
    </transition>

    <!-- Hero -->
    <section class="text-center py-20 px-4">
      <h1 class="text-5xl md:text-6xl font-extrabold leading-tight mb-4">Design Your Dream Home<br/>in Real-Time</h1>
      <p class="text-gray-300 text-lg md:text-xl mb-8">Walk through and customize homes with ultra-realistic 4K visuals</p>
      <div class="flex flex-col sm:flex-row justify-center gap-4">
        <RouterLink to="/scan" class="w-48 py-3 bg-blue-600 hover:bg-blue-500 rounded-xl text-white font-semibold uppercase transition text-center">Try Free</RouterLink>
        <RouterLink to="/demo" class="w-48 py-3 border border-white hover:bg-white hover:text-gray-900 rounded-xl text-white font-semibold uppercase transition text-center">Watch Demo</RouterLink>
      </div>
    </section>

    <!-- Hero Image -->
    <section class="flex justify-center px-4">
      <div class="relative max-w-4xl w-full rounded-2xl overflow-hidden bg-white/10 backdrop-blur-lg shadow-xl">
        <img src="/images/hero-living-room.jpg" alt="Modern Living Room" class="w-full h-auto object-cover" />
        <div class="absolute bottom-6 left-1/2 transform -translate-x-1/2 flex gap-4">
          <RouterLink to="/preview" class="px-6 py-3 bg-gray-800 hover:bg-gray-700 rounded-xl text-white font-medium transition">Explore Preview</RouterLink>
          <RouterLink to="/studio" class="px-6 py-3 bg-gray-800 hover:bg-gray-700 rounded-xl text-white font-medium transition">Enter Studio</RouterLink>
        </div>
      </div>
    </section>

    <!-- Features -->
    <section class="py-20 px-4">
      <h2 class="text-3xl md:text-4xl font-bold text-center mb-12">Features</h2>
      <div class="max-w-4xl mx-auto grid grid-cols-2 sm:grid-cols-4 gap-12 text-center">
        <FeatureCard icon="/icons/scan.svg" label="Scan Blueprints" />
        <FeatureCard icon="/icons/edit.svg" label="Real-Time Editing" />
        <FeatureCard icon="/icons/drag.svg" label="Drag & Drop" />
        <FeatureCard icon="/icons/share.svg" label="Share to Contractors" />
      </div>
    </section>

    <!-- Pricing -->
    <section class="py-20 px-4 bg-[#191C2A]">
      <h2 class="text-3xl md:text-4xl font-bold text-center mb-12">Pricing</h2>
      <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8">
        <PricingCard
          title="Monthly"
          price="$14.99"
          unit="/mo"
          features="['4K Walkthrough', 'Drag & Drop', 'Customization', 'Blueprint Scanning', 'Share']"
        />
        <PricingCard
          title="Yearly"
          price="$179.99"
          unit="/yr"
          features="['4K Walkthrough', 'Drag & Drop', 'Customization', 'Blueprint Scanning', 'Share']"
        />
      </div>
    </section>

    <!-- Public Products -->
    <section class="py-20 px-4">
      <h2 class="text-3xl md:text-4xl font-bold text-center mb-12">Public Products</h2>
      <div class="max-w-4xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-8">
        <ProductCard v-for="n in 4" :key="n" :image="`/images/house${n}.jpg`" :label="`Builder ${n}`" />
      </div>
    </section>
  </div>
</template>

<script>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import FeatureCard from '@/components/FeatureCard.vue';
import PricingCard from '@/components/PricingCard.vue';
import ProductCard from '@/components/ProductCard.vue';

export default {
  name: 'HomePage',
  components: { RouterLink, FeatureCard, PricingCard, ProductCard },
  setup() {
    const open = ref(false);
    return { open };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

.font-inter { font-family: 'Inter', sans-serif; }
.fade-enter-active, .fade-leave-active { transition: opacity .3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
