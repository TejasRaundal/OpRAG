<script lang="ts">
  import { createEventDispatcher } from 'svelte'
  import { MessageSquare, Upload, Settings, Sun, Moon } from 'lucide-svelte'
  const dispatch = createEventDispatcher()
  export let route: 'chat' | 'ingest' | 'settings' = 'chat'

  import { onMount } from 'svelte'

  function go(to: typeof route) {
    dispatch('navigate', to)
  }

  function toggleTheme() {
    const isDark = document.documentElement.classList.toggle('dark')
    try { localStorage.setItem('oprag:dark', isDark ? '1' : '0') } catch(e) {}
  }

  onMount(() => {
    try {
      const saved = localStorage.getItem('oprag:dark')
      if (saved === '1') document.documentElement.classList.add('dark')
      else document.documentElement.classList.remove('dark')
    } catch (e) {
      document.documentElement.classList.remove('dark')
    }
  })
</script>

<div class="card">
  <h3 class="text-xl font-bold text-gray-900 mb-6">OpRAG</h3>
  <div class="tab">
    <button class:active={route === 'chat'} on:click={() => go('chat')}>
      <MessageSquare size={18} class="mr-2" />
      Chat
    </button>
    <button class:active={route === 'ingest'} on:click={() => go('ingest')}>
      <Upload size={18} class="mr-2" />
      Ingest
    </button>
    <button class:active={route === 'settings'} on:click={() => go('settings')}>
      <Settings size={18} class="mr-2" />
      Settings
    </button>
  </div>

  <div class="mt-6 text-sm text-gray-600">
    <div class="font-medium">Mode: On‑Premise</div>
    <div class="mt-1">Stack: Svelte · FastAPI · ONNX · Qdrant</div>
  </div>

  <div class="theme-toggle">
    <span class="text-sm text-gray-600">Theme</span>
    <button on:click={toggleTheme}>
      {#if document.documentElement.classList.contains('dark')}
        <Sun size={16} />
      {:else}
        <Moon size={16} />
      {/if}
    </button>
  </div>
</div>

<style>
  .logo { display: flex; align-items: center; margin-bottom: 16px; }
  .logo h3 { color: var(--accent); font-weight: 700; }
</style>
