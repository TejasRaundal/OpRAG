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
    <div class="header">
      <h2 class="text-xl font-bold text-gray-900">
        {#if route === 'chat'}
          💬 Chat with your Documents
        {:else if route === 'ingest'}
          📁 Ingest Documents
        {:else}
          ⚙️ Configuration
        {/if}
      </h2>
      <div class="text-sm text-gray-500">
        {#if route === 'chat'}
          Ask questions about your indexed documents
        {:else if route === 'ingest'}
          Upload and index your documents
        {:else}
          Manage connections and settings
        {/if}
      </div>
    </div>
    <div class="content">
      {#if route === 'chat'}
        <Chat />
      {:else if route === 'ingest'}
        <Ingestion />
      {:else}
        <Settings />
      {/if}
    </div>
  </main>
</div>
