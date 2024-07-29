import { useSideBar } from "@providers/index";
import BrandLogo from "@assets/1_WNvTs536S75sZ9Ku2K2nqg.webp"
import { Link } from "react-router-dom";
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


function SideBar() {

  const {
    isCollapsed,
  } = useSideBar();


  return (
    <aside id="SideBar" className="font-roboto bg-gray-100">
      <img src={BrandLogo} alt="" className="object-contain my-1 mx-auto border-dashed border-[2px] w-[190px]" />
      <ul>
        <Tooltip placement="right" title={isCollapsed ? "Home" : ""}>
          <Link to="home" className="flex items-center gap-x-2 h-10 px-2">
            <DashboardIcon size={24} />
            <li>Home</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Units" : ""}>
          <Link to="unit" className="flex items-center gap-x-2 h-10 px-2">
            <UnitIcon size={24} />
            <li>Units</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Class Reps" : ""}>
          <Link to="classrep" className="flex items-center gap-x-2 h-10 px-2">
            <ClassrepIcon size={24} />
            <li>Class Reps</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Classes" : ""}>
          <Link to="class" className="flex items-center gap-x-2 h-10 px-2">
            <ClassIcon size={24} />
            <li>Classes</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Departments" : ""}>
          <Link to="department" className="flex items-center gap-x-2 h-10 px-2">
            <DepartmentIcon size={24} />
            <li>Departments</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Tasks" : ""}>
          <Link to="task" className="flex items-center gap-x-2 h-10 px-2">
            <TaskIcon size={24} />
            <li>Tasks</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Feed" : ""}>
          <Link to="feed" className="flex items-center gap-x-2 h-10 px-2">
            <FeedIcon size={24} />
            <li>Feed</li>
          </Link>
        </Tooltip>
        <Tooltip placement="right" title={isCollapsed ? "Settings" : ""}>
          <Link to="setting" className="flex items-center gap-x-2 h-10 px-2">
            <SettingIcon size={24} />
            <li>Settings</li>
          </Link>
        </Tooltip>
      </ul>
    </aside>
  );
}


export default SideBar;
