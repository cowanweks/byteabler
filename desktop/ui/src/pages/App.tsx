import "@styles/App.scss";
import { Header, Footer, SideBar } from "@components/index";
import { Outlet } from "react-router-dom"

function App() {


  return (
    <div id="App">
      <Header />
      <SideBar />
      <div id="Content" className="">
        <Outlet />
      </div>
      <Footer />
    </div>
  )
}

export default App
