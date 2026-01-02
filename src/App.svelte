<script lang="ts">
  import { onMount } from 'svelte'
  import Sidebar from './components/Sidebar.svelte'
  import Chat from './components/Chat.svelte'
  import Ingestion from './components/Ingestion.svelte'
  import Settings from './components/Settings.svelte'

  let route: 'chat' | 'ingest' | 'settings' = 'chat'

  function navigate(to: typeof route) {
    route = to
  }

  onMount(() => {
    // Placeholder: could load saved config or state here
  })
</script>

<div class="app">
  <aside class="sidebar">
    <Sidebar {route} on:navigate={(e) => navigate(e.detail)} />
  </aside>
  <main class="main">
    {#if route === 'chat'}
      <Chat />
    {:else if route === 'ingest'}
      <Ingestion />
    {:else}
      <Settings />
    {/if}
  </main>
</div>
