<script lang="ts">
  import { Upload, FileText, Trash2, CheckCircle } from 'lucide-svelte'
  let files: File[] = []
  let indexing = false
  let dragOver = false
  let indexProgress = 0

  function onFiles(e: Event) {
    files = Array.from((e.target as HTMLInputElement).files || [])
  }

  function onDrop(e: DragEvent) {
    e.preventDefault()
    dragOver = false
    if (e.dataTransfer?.files) {
      files = Array.from(e.dataTransfer.files)
    }
  }

  function onDragOver(e: DragEvent) {
    e.preventDefault()
    dragOver = true
  }

  function onDragLeave() {
    dragOver = false
  }

  function removeFile(idx: number) {
    files = files.filter((_, i) => i !== idx)
  }

  async function indexNow() {
    if(!files.length) return alert('Please select files to ingest')
    indexing = true
    indexProgress = 0
    const interval = setInterval(() => {
      indexProgress += Math.random() * 30
      if(indexProgress >= 100) {
        clearInterval(interval)
        indexProgress = 100
        setTimeout(() => {
          indexing = false
          files = []
          indexProgress = 0
        }, 500)
      }
    }, 300)
  }
</script>

<div class="card">
  <div class="mb-6">
    <h3 class="text-lg font-semibold text-gray-900 mb-2">Upload Documents</h3>
    <p class="text-sm text-gray-600">Drag and drop or click to select files (PDF, TXT, DOCX)</p>
  </div>

  <div class="drop-zone" class:drag-over={dragOver} on:drop={onDrop} on:dragover={onDragOver} on:dragleave={onDragLeave} role="region" aria-label="File drop zone">
    <input type="file" multiple on:change={onFiles} id="file-input" style="display:none" />
    <label for="file-input" class="cursor-pointer" style="display: block;">
      <div style="margin: 0 auto 12px; color: var(--accent); display: flex; justify-content: center;">
        <Upload size={32} />
      </div>
      <div class="font-semibold text-gray-900 mb-1">Drop files here or click to browse</div>
      <p class="text-sm text-gray-500">Supports PDF, TXT, DOCX and more</p>
    </label>
  </div>

  {#if files.length > 0}
    <div class="mt-6">
      <h4 class="font-semibold text-gray-900 mb-3">Selected Files ({files.length})</h4>
      <ul class="file-list">
        {#each files as f, idx}
          <li class="file-item">
            <FileText size={18} style="color: var(--accent); flex-shrink: 0;" />
            <div class="flex-1 min-w-0">
              <div class="font-medium text-gray-900 truncate">{f.name}</div>
              <div class="text-xs text-gray-500">{(f.size / 1024).toFixed(1)} KB</div>
            </div>
            <button class="text-gray-400 hover:text-red-500 transition" on:click={() => removeFile(idx)}>
              <Trash2 size={18} />
            </button>
          </li>
        {/each}
      </ul>
    </div>
  {/if}

  {#if indexing}
    <div class="mt-6">
      <div class="flex items-center gap-2 mb-2">
        <div class="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></div>
        <span class="text-sm font-medium text-gray-900">Indexing documents...</span>
      </div>
      <div class="w-full bg-gray-200 rounded-full h-2">
        <div class="bg-blue-600 h-2 rounded-full transition-all" style="width: {indexProgress}%"></div>
      </div>
      <div class="text-xs text-gray-500 mt-2">{Math.round(indexProgress)}%</div>
    </div>
  {:else}
    <div class="mt-6">
      <button 
        class="btn" 
        on:click={indexNow} 
        disabled={!files.length}
        style="width: 100%;"
      >
        Index Documents
      </button>
    </div>
  {/if}
</div>
