import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { createMatch } from './services/matchService.tsx';

const initApp = async () => {
  const matchId = await createMatch();
  ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
      <App matchId={matchId} />
    </React.StrictMode>,
  )
}

initApp();