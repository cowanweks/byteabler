import { createContext, ReactNode, useContext, useState } from "react";


const AuthContext = createContext<{
    user: string,
    role: string,
    loggedIn: boolean | undefined,
    setUser: (value: string) => void,
    setRole: (value: string) => void,
    setLoggedIn: (value: boolean) => void
}>({
    user: '', role: '', loggedIn: false,
    setUser: () => { }, setRole: () => { }, setLoggedIn: () => { }
})

export const AuthProvider = ({ children }: { children: ReactNode }) => {

    const [user, setUser] = useState<string>('');
    const [role, setRole] = useState<string>('');
    const [loggedIn, setLoggedIn] = useState<boolean | undefined>(false);

    return (
        <AuthContext.Provider value={{ user, setUser, role, setRole, loggedIn, setLoggedIn }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);