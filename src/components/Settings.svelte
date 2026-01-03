<script lang="ts">
  import { onMount } from 'svelte'
  let qdrantHost = 'http://localhost:6333'
  let pgConn = 'postgres://user:pass@localhost:5432/oprag'
  let onnxPath = '/path/to/model.onnx'

  function save() {
    // in prod use Tauri filesystem or secure storage
    alert('Saved (mock)')
  }

  async function testConnection(type: 'qdrant' | 'postgres') {
    // mock test
    alert(`${type} connection test: OK (mock)`)
  }
</script>

<div class="card">
  <h3>⚙️ Settings</h3>
  <div style="margin-top:16px;display:flex;flex-direction:column;gap:16px">
    <div>
      <label for="qdrantHost" style="display:block;margin-bottom:4px;font-weight:500">Qdrant Host</label>
      <input id="qdrantHost" class="input" bind:value={qdrantHost} style="width:100%" />
      <button class="btn" style="margin-top:8px" on:click={() => testConnection('qdrant')}>Test Connection</button>
    </div>

    <div>
      <label for="pgConn" style="display:block;margin-bottom:4px;font-weight:500">PostgreSQL Connection</label>
      <input id="pgConn" class="input" bind:value={pgConn} style="width:100%" />
      <button class="btn" style="margin-top:8px" on:click={() => testConnection('postgres')}>Test Connection</button>
    </div>

    <div>
      <label for="onnxPath" style="display:block;margin-bottom:4px;font-weight:500">ONNX Model Path</label>
      <input id="onnxPath" class="input" bind:value={onnxPath} style="width:100%" />
    </div>

    <div style="margin-top:8px">
      <button class="btn" on:click={save}>💾 Save Settings</button>
    </div>
  </div>
</div>