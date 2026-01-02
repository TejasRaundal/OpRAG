export async function embed(text: string) {
  const res = await fetch('http://localhost:8000/embed', { method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({text})})
  return res.json()
}

export async function search(query: string) {
  const res = await fetch('http://localhost:8000/search', { method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({query})})
  return res.json()
}

export async function indexDocuments(docs: any[]) {
  const res = await fetch('http://localhost:8000/index', { method: 'POST', headers: {'content-type':'application/json'}, body: JSON.stringify({docs})})
  return res.json()
}