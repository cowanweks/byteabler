import { createContext, ReactNode, useContext, useState } from "react";


const ThemeContext = createContext<{
    theme: string,
    setTheme: (value: 'dark' | 'light' | 'auto') => void
}>({
    theme: 'light',
    setTheme: () => { }
})

export const ThemeProvider = ({ children }: { children: ReactNode }) => {

    const [theme, setTheme] = useState<'dark' | 'light' | 'auto'>('light');

    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            {children}
        </ThemeContext.Provider>
    );
};

export const useTheme = () => useContext(ThemeContext);