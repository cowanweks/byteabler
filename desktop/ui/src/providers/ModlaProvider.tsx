import React, { createContext, useState, useContext, ReactNode } from 'react';
import { Modal, ModalProps } from 'antd';


interface ModalOptions extends Omit<ModalProps, 'visible' | 'title' | 'onCancel' | 'onOk'> {
	customClassName?: string
}

interface ModalContextProps {
	showModal: (content: ReactNode, title?: string, options?: ModalOptions) => void;
	hideModal: () => void;
}


const ModalContext = createContext<ModalContextProps | undefined>(undefined);

export const useModal = () => {
	//
	const context = useContext(ModalContext);
	if (!context) {
		throw new Error('useModal must be used within a ModalProvider');
	}
	return context;
};


export const ModalProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
	const [isOpen, setIsOpen] = useState(false);
	const [modalTitle, setModalTitle] = useState<string | undefined>('');
	const [modalContent, setModalContent] = useState<ReactNode>(null);
	const [modalOptions, setModalOptions] = useState<ModalOptions>({});

	const showModal = (content: ReactNode, title?: string, options?: ModalOptions) => {
		setModalTitle(title);
		setModalContent(content);
		setIsOpen(true);
		setModalOptions(options || {});
	};

	const hideModal = () => {
		setIsOpen(false);
	};

	return (
		<ModalContext.Provider value={{ showModal, hideModal }}>
			{children}
			<Modal
				title={modalTitle}
				open={isOpen}
				onCancel={hideModal}
				onOk={hideModal}
				closable={false}
				maskClosable
				destroyOnClose={true}
				className={`
				${modalOptions.customClassName}
				select-none
				`}
				{...modalOptions}
				footer={false}
			>
				{modalContent}
			</Modal>
		</ModalContext.Provider>
	);
};