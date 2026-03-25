import { useState } from 'react'
import './App.css'

function App() {
  const [prompt, setPrompt] = useState('')

  const handleGenerate = async () => {
    // TODO: Call API to generate content
  }

  return (
    <div className="container">
      <h1>AI Curriculum Animation Platform</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter a topic to generate curriculum content..."
      />
      <button onClick={handleGenerate}>Generate</button>
    </div>
  )
}

export default App
