<script lang="ts">
  import { MessageSquare, Send } from 'lucide-svelte'
  let messages: {id: number, role: 'user' | 'assistant', text: string, timestamp: string}[] = [
    {id:1, role:'assistant', text:'Welcome to OpRAG Chat. Ask me anything about your indexed documents.', timestamp: new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}
  ]
  let input = ''

  function send() {
    if(!input.trim()) return
    const now = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})
    messages = [...messages, {id: Date.now(), role: 'user', text: input, timestamp: now}]
    setTimeout(() => {
      messages = [...messages, {id: Date.now()+1, role: 'assistant', text: 'This is a mock response. Connect to your backend to get real answers from your documents.', timestamp: new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})}]
    }, 800)
    input = ''
  }
</script>

<div class="chat-container">
  <div class="messages-area">
    {#each messages as m}
      <div class="message {m.role}">
        <div class="message-avatar">
          {m.role === 'user' ? '👤' : '🤖'}
        </div>
        <div class="message-content">
          <div class="message-bubble">{m.text}</div>
          <div class="message-meta">{m.timestamp}</div>
        </div>
      </div>
    {/each}
  </div>

  <div style="padding: 20px; background: var(--panel); border-top: 1px solid var(--card-border); display: flex; gap: 12px;">
    <input 
      class="input" 
      placeholder="Ask a question about your documents..." 
      bind:value={input} 
      on:keydown={(e) => e.key === 'Enter' && send()}
      style="flex: 1;"
    />
    <button class="btn" on:click={send} disabled={!input.trim()}>
      <Send size={18} />
    </button>
  </div>
</div>