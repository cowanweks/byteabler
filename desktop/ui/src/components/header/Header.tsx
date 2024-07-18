import Search from './Search';
import { useCommandDialog, useSideBar } from "@providers/index";
import { useEffect } from 'react';
import { GoSidebarCollapse as ShowSideBarIcon, GoSidebarExpand as HideSideBarIcon } from "react-icons/go"
import { HiOutlineMagnifyingGlass as SearchIcon } from "react-icons/hi2"


export default function Header() {

  const {
    isCollapsed,
    toggleSideBar
  } = useSideBar();

  const {
    isOpen,
    showCommandDialog,
    hideCommandDialog
  } = useCommandDialog();

  useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault()

        if (!isOpen) {
          showCommandDialog(<Search />)
          return;
        }
        hideCommandDialog()
      }
    }

    document.addEventListener("keydown", down)
    return () => document.removeEventListener("keydown", down)
  }, [showCommandDialog, hideCommandDialog, isOpen])


  return (<nav id="Header" className="flex items-center gap-x-4 px-1 bg-gray-100">
    {isCollapsed ?
      <button onClick={toggleSideBar} className="flex justify-center items-center w-8 h-8">
        <ShowSideBarIcon size={24} />
      </button> :
      <button onClick={toggleSideBar} className="flex justify-center items-center w-8 h-8">
        <HideSideBarIcon size={24} />
      </button>}
    <div className="flex-grow"></div>
    <label htmlFor="SearchInput" className="flex relative">
      <button className='pointer-events-none absolute top-2 left-2'><SearchIcon className="stroke-gray-400" /></button>
      <input id='SearchInput' type="text" placeholder='Search anything...' className="w-48 h-8 pl-8 bg-gray-200 rounded-l" onFocus={() => {
        setTimeout(() => showCommandDialog(<Search />), 100)
      }} />
      <kbd className="h-8 pointer-events-none inline-flex select-none items-center gap-1 rounded-l-none rounded-r border bg-muted px-1.5 font-mono text-[10px] font-medium text-muted-foreground opacity-100">
        <span className="text-xs">⌘</span>K
      </kbd>
    </label>
    <div className="flex-grow"></div>
    <button>Hello</button>
  </nav>);
}