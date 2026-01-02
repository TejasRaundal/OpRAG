<script lang="ts">
  import { createEventDispatcher } from 'svelte'
  const dispatch = createEventDispatcher()
  export let route: 'chat' | 'ingest' | 'settings' = 'chat'

  function go(to: typeof route) {
    dispatch('navigate', to)
  }
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
</div>
