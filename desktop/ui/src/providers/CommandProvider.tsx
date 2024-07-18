import { CommandDialog } from "@components/ui/command";
import React, { createContext, useState, useContext, ReactNode } from 'react';

interface CommandProps {
	isOpen: boolean;
	showCommandDialog: (content: ReactNode) => void;
	hideCommandDialog: () => void;
}


const CommandDialogContext = createContext<CommandProps | undefined>(undefined);

export const useCommandDialog = () => {
	const context = useContext(CommandDialogContext);

	if (!context) {
		throw new Error('useCommandDialog must be used within a CommandDialogProvider');
	}
	return context;
}


export const CommandDialogProvider: React.FC<{ children: ReactNode }> = ({ children }) => {

	const [isOpen, setIsOpen] = useState(false);
	const [commandDialogContent, setCommandDialogContent] = useState<ReactNode>(null);

	const showCommandDialog = (content: ReactNode) => {
		setCommandDialogContent(content);
		setIsOpen(true)
	}

	const hideCommandDialog = () => { setIsOpen(false) }

	return (
		<CommandDialogContext.Provider value={{ isOpen, showCommandDialog, hideCommandDialog }}>
			{children}
			<CommandDialog open={isOpen} onOpenChange={setIsOpen} >
				{commandDialogContent}
			</CommandDialog>
		</CommandDialogContext.Provider>
	)
}