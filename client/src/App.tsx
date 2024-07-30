import './App.css'
import { AppProvider } from './AppContext';
import { Board } from './components/Board';

const App = ({ matchId }: { matchId: number }) => {
  return (
    <AppProvider matchId={matchId}>
      <Board />
    </AppProvider>
  )
}

export default App
