import '@styles/App.scss'
import { Button } from '@shadcn-ui/button';
import { useState } from 'react'

function App() {

  const [theme, setTheme] = useState('light');

  return (
    <div className={theme == 'dark' ? 'dark' : 'light'}>
      <Button onClick={() => setTheme('dark')}> Click Me!</Button>
    </div>
  )
}

export default App
