<template>
  <div class="page">
    <!-- Top Bar / Navbar -->
    <header class="navbar">
      <div class="navbar-left">
        <RouterLink to="/" class="logo" aria-label="HexaNest Home">
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
    <main class="main">
      <!-- Hero / Header -->
      <section class="hero">
        <div class="hero-text">
          <h1>Scan Blueprint to 3D</h1>
          <p>Upload a PDF or image. Our AI generates a photoreal, editable 3D home — ready to customize.</p>
          <div class="badges">
            <span>PDF / JPG / PNG</span>
            <span>Wall & Room Detection</span>
            <span>Editable Materials</span>
          </div>
        </div>
        <div class="hero-visual" aria-hidden="true">
          <div class="glass-card"></div>
        </div>
      </section>

      <!-- Uploader -->
      <section class="uploader" aria-label="Upload blueprint">
        <div
          class="dropzone"
          :class="{ dragover: isDragOver, hasfile: fileName }"
          @dragover.prevent="onDragOver"
          @dragleave.prevent="onDragLeave"
          @drop.prevent="onDrop"
        >
          <input
            ref="fileInput"
            type="file"
            class="file-input"
            accept=".pdf,image/*"
            @change="onPickFile"
            aria-label="Upload a PDF or image"
          />
          <div class="drop-inner">
            <div class="dz-icon"></div>
            <div class="dz-text">
              <strong>Drag & drop</strong> your blueprint here<br />
              or <button class="linklike" @click="triggerFile">browse</button> to upload
            </div>
            <div class="dz-sub">Accepted: PDF, PNG, JPG • Max 50MB</div>
            <div v-if="fileName" class="dz-file">Selected: {{ fileName }}</div>
          </div>
        </div>

        <div class="actions">
          <button class="btn btn-primary" :disabled="!selectedFile || loading" @click="startScan">
            {{ loading ? 'Scanning…' : 'Generate 3D Model' }}
          </button>
          <button class="btn btn-outline" :disabled="!selectedFile || loading" @click="clearFile">
            Clear
          </button>
        </div>

        <!-- Progress & Errors -->
        <div v-if="loading" class="progress">
          <div class="bar"><span
