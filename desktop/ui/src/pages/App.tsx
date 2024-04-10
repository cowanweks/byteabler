import '@styles/App.scss'
import { Header } from '@/components'
import { Text } from '@/components/input'


/**
 * The main App component that serves as the entry point for the application.
 * It imports the necessary styles and components, and renders the Header component.
 */

export default function App() {


  return (<div class="App">
    <Header />
    <Text label='UserName' placeholder='UserName' />
  </div>)
}
