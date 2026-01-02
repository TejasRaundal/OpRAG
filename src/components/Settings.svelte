<script lang="ts">
  import { onMount } from 'svelte'
  let qdrantHost = 'http://localhost:6333'
  let pgConn = 'postgres://user:pass@localhost:5432/oprag'
  let onnxPath = '/path/to/model.onnx'

  function save() {
    // in prod use Tauri filesystem or secure storage
    alert('Saved (mock)')
  }
</script>

<div class="card">
  <h3>Settings</h3>
  <div style="margin-top:12px;display:flex;flex-direction:column;gap:8px">
    <label>Qdrant Host
      <input bind:value={qdrantHost} style="width:100%;padding:8px;border-radius:6px;border:1px solid rgba(255,255,255,0.03)" />
    </label>

    <label>PostgreSQL Connection
      <input bind:value={pgConn} style="width:100%;padding:8px;border-radius:6px;border:1px solid rgba(255,255,255,0.03)" />
    </label>

    <label>ONNX Model Path
      <input bind:value={onnxPath} style="width:100%;padding:8px;border-radius:6px;border:1px solid rgba(255,255,255,0.03)" />
    </label>

    <div style="margin-top:8px">
      <button on:click={save} style="padding:8px 12px;border-radius:6px;background:var(--accent);border:none;color:#052018">Save</button>
    </div>
  </div>
</div>