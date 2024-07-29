import React, { createContext, useState, useContext, ReactNode } from 'react';
import { message } from "antd"

type ToastProps = {
	showToast: (type: 'success' | 'info' | 'error' | 'warning', content?: string) => void | undefined,
}



const ToastContext = createContext<ToastProps | undefined>({});


export const useToast = () => {
	const context = useContext(ToastContext);

	if (!context) {
		throw new Error('useToast must be used within a ToastProvider');
	}
	return context;
}


export const ToastProvider: React.FC<{ children: ReactNode }> = ({ children }) => {

	const [messageApi, contextHolder] = message.useMessage();

	const showToast = (type: 'success' | 'info' | 'error' | 'warning' = 'info', content?: string) => {

		messageApi.open({
			type: type,
			content: content,
		});
	}

	return (
		<ToastContext.Provider value={{ showToast }}>
			{contextHolder}
			{children}
		</ToastContext.Provider>
	)
}