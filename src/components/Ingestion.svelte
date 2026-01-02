<script lang="ts">
  let files: File[] = []
  let indexing = false

  function onFiles(e: Event) {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    files = Array.from(e.target.files || [])
  }

  async function indexNow() {
    if(!files.length) return alert('Select files to ingest')
    indexing = true
    // stub: call backend /index endpoint
    setTimeout(()=>{ indexing = false; alert('Indexed (mock)') }, 800)
  }
</script>

<div class="card">
  <h3>Ingestion</h3>
  <div style="margin-top:8px">
    <input type="file" multiple on:change={onFiles} />
    <div style="margin-top:12px;color:var(--muted)">
      {#if files.length}
        <div>Files selected:</div>
        <ul>
          {#each files as f}
            <li>{f.name}</li>
          {/each}
        </ul>
      {:else}
        <div>No files selected</div>
      {/if}
    </div>

    <div style="margin-top:12px">
      <button on:click={indexNow} disabled={indexing} style="padding:8px 12px;border-radius:6px;background:var(--accent);border:none;color:#052018">Index Files</button>
    </div>
  </div>
</div>