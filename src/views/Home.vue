<template>
  <div class="home-page font-sans text-white bg-gray-900">
    <!-- Navbar -->
    <nav class="flex items-center justify-between p-6">
      <div class="text-2xl font-bold">MyHomeApp</div>
      <ul class="flex space-x-6">
        <li><a href="/" class="hover:text-blue-400">Home</a></li>
        <li><a href="/scan" class="hover:text-blue-400">Scan</a></li>
        <li><a href="/customize" class="hover:text-blue-400">Customize</a></li>
        <li><a href="/pricing" class="hover:text-blue-400">Pricing</a></li>
        <li><a href="/products" class="hover:text-blue-400">Products</a></li>
      </ul>
    </nav>

    <!-- Header Section -->
    <header class="text-center py-20 px-4">
      <h1 class="text-5xl font-bold mb-4">Design Your Dream Home in Real-Time</h1>
      <p class="text-lg text-gray-300 mb-8">Walk through and customize homes with ultra realistic 4K visuals</p>
      <div class="flex justify-center space-x-4">
        <button class="w-48 h-12 bg-blue-600 hover:bg-blue-500 rounded-lg font-bold uppercase">Try Free</button>
        <button class="w-48 h-12 border border-white hover:bg-white hover:text-gray-900 rounded-lg font-bold uppercase bg-transparent">Watch Demo</button>
      </div>
    </header>

    <!-- Hero Image Area -->
    <section class="text-center px-4 mb-20">
      <div class="max-w-3xl mx-auto rounded-xl overflow-hidden shadow-lg">
        <img src="/images/hero-living-room.jpg" alt="Modern Living Room" class="w-full h-auto" />
      </div>
      <div class="flex justify-center space-x-4 mt-6">
        <button class="w-48 h-12 bg-gray-800 bg-opacity-60 hover:bg-opacity-80 rounded-lg uppercase">Explore Preview</button>
        <button class="w-48 h-12 bg-gray-800 bg-opacity-60 hover:bg-opacity-80 rounded-lg uppercase">Enter Studio</button>
      </div>
    </section>

    <!-- Features Section -->
    <section class="px-4 mb-20">
      <h2 class="text-3xl font-bold text-center mb-8">Features</h2>
      <div class="flex justify-center space-x-12">
        <div class="flex flex-col items-center">
          <i class="icon-scan text-blue-400 text-4xl mb-2"></i>
          <span>Scan Blueprints</span>
        </div>
        <div class="flex flex-col items-center">
          <i class="icon-edit text-blue-400 text-4xl mb-2"></i>
          <span>Real-Time Editing</span>
        </div>
        <div class="flex flex-col items-center">
          <i class="icon-drag text-blue-400 text-4xl mb-2"></i>
          <span>Drag & Drop</span>
        </div>
        <div class="flex flex-col items-center">
          <i class="icon-share text-blue-400 text-4xl mb-2"></i>
          <span>Share to Contractors</span>
        </div>
      </div>
    </section>

    <!-- Pricing Section -->
    <section class="px-4 mb-20">
      <h2 class="text-3xl font-bold text-center mb-8">Pricing</h2>
      <div class="flex justify-center space-x-8">
        <div class="bg-gray-800 p-6 rounded-lg shadow-lg w-80">
          <h3 class="text-xl font-bold mb-4">Monthly</h3>
          <p class="text-4xl font-bold mb-4">$14.99/mo</p>
          <ul class="mb-6 space-y-2">
            <li>4K walkthrough</li>
            <li>Drag-and-drop</li>
            <li>Customization</li>
            <li>Blueprint scanning</li>
            <li>Share</li>
          </ul>
          <button class="w-full h-12 bg-blue-600 hover:bg-blue-500 rounded-lg uppercase font-bold">Get Started</button>
        </div>
        <div class="bg-gray-800 p-6 rounded-lg shadow-lg w-80">
          <h3 class="text-xl font-bold mb-4">Yearly</h3>
          <p class="text-4xl font-bold mb-4">$179.99/yr</p>
          <ul class="mb-6 space-y-2">
            <li>4K walkthrough</li>
            <li>Drag-and-drop</li>
            <li>Customization</li>
            <li>Blueprint scanning</li>
            <li>Share</li>
          </ul>
          <button class="w-full h-12 bg-blue-600 hover:bg-blue-500 rounded-lg uppercase font-bold">Get Started</button>
        </div>
      </div>
    </section>

    <!-- Public Products Section -->
    <section class="px-4 mb-20">
      <h2 class="text-3xl font-bold text-center mb-8">Public Products</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
        <div v-for="n in 4" :key="n" class="bg-gray-800 rounded-lg overflow-hidden shadow-lg">
          <img :src="`/images/house${n}.jpg`" alt="Builder {{n}}" class="w-full h-48 object-cover" />
          <div class="text-center py-4 bg-blue-600">
            <span class="font-bold">Builder {{ n }}</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
.home-page {
  background-color: #1C1F2B;
}
.rounded-lg { border-radius: 12px; }
.icon-scan::before { content: '\f02d'; /* FontAwesome scan icon */ }
.icon-edit::before { content: '\f044'; }
.icon-drag::before { content: '\f247'; }
.icon-share::before { content: '\f1e0'; }
i[class^="icon-"] {
  font-family: 'Font Awesome 5 Free';
  font-weight: 900;
}
</style>
