import { createContext, ReactNode, useContext, useState } from "react";


const AuthContext = createContext<{
    user: string | undefined,
    role: string | undefined,
    loggedIn: boolean | undefined,
    setUser: (value: string) => void,
    setRole: (value: string) => void,
    setLoggedIn: (value: boolean) => void
}>({
    user: undefined, role: undefined, loggedIn: false,
    setUser: () => { }, setRole: () => { }, setLoggedIn: () => { }
})

export const AuthProvider = ({ children }: { children: ReactNode }) => {

    const [user, setUser] = useState<string | undefined>('');
    const [role, setRole] = useState<string | undefined>('');
    const [loggedIn, setLoggedIn] = useState<boolean | undefined>(false);

    return (
        <AuthContext.Provider value={{ user, setUser, role, setRole, loggedIn, setLoggedIn }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);