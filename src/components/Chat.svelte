<script lang="ts">
  import { onMount } from 'svelte'
  let messages = [{id:1,role:'system',text:'Welcome to OpRAG — ask something about your documents.'}]
  let input = ''

  function send() {
    if(!input.trim()) return
    messages = [...messages, {id: Date.now(), role: 'user', text: input}]
    // placeholder for calling backend
    messages = [...messages, {id: Date.now()+1, role: 'assistant', text: '(mock) This is an example response. Integrate search + generator to get real answers.'}]
    input = ''
  }
</script>

<div class="card">
  <h3>Chat / RAG</h3>
  <div style="height:60vh;overflow:auto;border:1px solid rgba(255,255,255,0.02);padding:12px;margin-top:8px;border-radius:6px">
    {#each messages as m}
      <div style="margin-bottom:10px">
        <strong style="color:var(--accent)">{m.role}</strong> <span style="color:var(--muted);font-size:13px"> — {m.id}</span>
        <div style="margin-top:6px">{m.text}</div>
      </div>
    {/each}
  </div>

  <div style="margin-top:10px;display:flex;gap:8px">
    <input placeholder="Ask about your data..." bind:value={input} style="flex:1;padding:8px;border-radius:6px;border:1px solid rgba(255,255,255,0.03)" />
    <button on:click={send} style="padding:8px 12px;border-radius:6px;background:var(--accent);border:none;color:#052018">Send</button>
  </div>
</div>