import React, { createContext, useState, useContext, ReactNode } from 'react';


interface SideBarProps {
	isCollapsed: boolean,
	toggleSideBar?: () => void;
}


const SideBarContext = createContext<SideBarProps | undefined>({ isCollapsed: true });

export const useSideBar = () => {
	const context = useContext(SideBarContext);

	if (!context) {
		throw new Error('useSideBar must be used within a SideBarProvider');
	}
	return context;
}


export const SideBarProvider: React.FC<{ children: ReactNode }> = ({ children }) => {

	const [isCollapsed, setIsCollapsed] = useState(true);


	const toggleSideBar = () => {
		//
		setIsCollapsed(!isCollapsed);
	}

	return (
		<SideBarContext.Provider value={{ isCollapsed, toggleSideBar }}>
			{children}
		</SideBarContext.Provider>
	)
}