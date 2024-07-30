import { useSideBar } from "@providers/index";
import BrandLogo from "@assets/1_WNvTs536S75sZ9Ku2K2nqg.webp"
import { Link, NavLink } from "react-router-dom";
import {
  HiOutlineCog8Tooth as SettingIcon,
  HiOutlineHomeModern as DepartmentIcon,
  HiOutlineSquare3Stack3D as UnitIcon,
  HiOutlineSquares2X2 as DashboardIcon,
  HiOutlineBuildingOffice as ClassIcon,
  HiOutlineBriefcase as TaskIcon,
  HiOutlineInboxArrowDown as FeedIcon
} from "react-icons/hi2"
import { PiStudent as ClassrepIcon } from "react-icons/pi";
import { Tooltip } from "antd";
import './SideBar.scss'

function SideBar() {

  const {
    isCollapsed,
  } = useSideBar();


  return (
    <aside id="SideBar" className="font-roboto bg-gray-100">
      <img src={BrandLogo} alt="" className="object-contain my-1 mx-auto border-dashed border-[2px] w-[190px]" />
      <ul>
        <Tooltip placement="right" title={isCollapsed ? "Home" : ""}>
          <NavLink to="home"
            style={(state) => console.log(state)}>
            <DashboardIcon size={24} />
            <li>Home</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Units" : ""}>
          <NavLink style={(state) => console.log(state)} to="unit" className="flex items-center gap-x-2 h-10 px-2">
            <UnitIcon size={24} />
            <li>Units</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Class Reps" : ""}>
          <NavLink activeClassName='is-active' to="classrep" className="flex items-center gap-x-2 h-10 px-2">
            <ClassrepIcon size={24} />
            <li>Class Reps</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Classes" : ""}>
          <NavLink activeClassName='is-active' to="class" className="flex items-center gap-x-2 h-10 px-2">
            <ClassIcon size={24} />
            <li>Classes</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Departments" : ""}>
          <NavLink activeClassName='is-active' to="department" className="flex items-center gap-x-2 h-10 px-2">
            <DepartmentIcon size={24} />
            <li>Departments</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Tasks" : ""}>
          <NavLink activeClassName='is-active' to="task" className="flex items-center gap-x-2 h-10 px-2">
            <TaskIcon size={24} />
            <li>Tasks</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Feed" : ""}>
          <NavLink activeClassName='is-active' to="feed" className="flex items-center gap-x-2 h-10 px-2">
            <FeedIcon size={24} />
            <li>Feed</li>
          </NavLink>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Settings" : ""}>
          <NavLink activeClassName='is-active' to="setting" className="flex items-center gap-x-2 h-10 px-2">
            <SettingIcon size={24} />
            <li>Settings</li>
          </NavLink>
        </Tooltip>
      </ul>
    </aside >
  );
}


export default SideBar;
