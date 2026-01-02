<script lang="ts">
  import { createEventDispatcher } from 'svelte'
  const dispatch = createEventDispatcher()
  export let route: 'chat' | 'ingest' | 'settings' = 'chat'

  import { onMount } from 'svelte'

  function go(to: typeof route) {
    dispatch('navigate', to)
  }

  function setTheme(isDark: boolean) {
    if (isDark) document.documentElement.classList.add('dark')
    else document.documentElement.classList.remove('dark')
    try { localStorage.setItem('oprag:dark', isDark ? '1' : '0') } catch(e) {}
  }

  function toggleTheme() {
    const isDark = document.documentElement.classList.toggle('dark')
    try { localStorage.setItem('oprag:dark', isDark ? '1' : '0') } catch(e) {}
  }

  onMount(() => {
    try {
      const saved = localStorage.getItem('oprag:dark')
      if (saved === '1') setTheme(true)
      else setTheme(false)
    } catch (e) {
      setTheme(false)
    }
  })
</script>

<div class="card">
  <h3>OpRAG</h3>
  <div style="margin-top:12px" class="tab">
    <button class:active={route === 'chat'} on:click={() => go('chat')}>Chat</button>
    <button class:active={route === 'ingest'} on:click={() => go('ingest')}>Ingest</button>
    <button class:active={route === 'settings'} on:click={() => go('settings')}>Settings</button>
  </div>

  <div style="margin-top:18px;color:var(--muted);font-size:13px">
    <div><strong>Mode:</strong> On‑Premise</div>
    <div style="margin-top:6px"><strong>Stack:</strong> Svelte · FastAPI · ONNX · Qdrant</div>
  </div>

  <div class="theme-toggle">
    <span style="color:var(--muted);font-size:13px">Theme</span>
    <button on:click={toggleTheme}>Toggle Dark</button>
  </div>
</div>
