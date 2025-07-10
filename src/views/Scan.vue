<template>
  <div class="scan">
    <div class="header">
      <h1>Scan Blueprint to 3D</h1>
      <p>Upload a PDF or image. AI generates a photorealistic, editable 3D home.</p>
    </div>
    <div class="upload-area">
      <input type="file" @change="upload" accept=".pdf,image/*" />
    </div>
    <div v-if="modelUrl" class="viewer">
      <SceneViewer :modelUrl="modelUrl" />
    </div>
    <div v-if="suggestions.length" class="suggestions">
      <h2>Design Suggestions</h2>
      <ul><li v-for="(s,i) in suggestions" :key="i">{{ s }}</li></ul>
    </div>
  </div>
</template>

<script>
import SceneViewer from '@/components/SceneViewer.vue';
export default {
  name: 'Scan',
  components: { SceneViewer },
  data() { return { modelUrl: null, suggestions: [] }; },
  methods: {
    async upload(e) {
      const file = e.target.files[0];
      if (!file) return;
      const form = new FormData();
      form.append('file', file);
      try {
        const res = await fetch('/api/scan', { method:'POST', body: form });
        const data = await res.json();
        if (data.success) {
          this.modelUrl = data.modelPath;
          this.suggestions = data.suggestions;
        } else {
          alert('Scan failed.');
        }
      } catch {
        alert('Upload error.');
      }
    }
  }
};
</script>

<style scoped>
.scan { padding:40px; text-align:center; }
.upload-area { margin:20px auto; }
.viewer { margin-top:40px; width:100%; height:600px; }
.suggestions { margin-top:20px; display:inline-block; text-align:left; }
</style>
