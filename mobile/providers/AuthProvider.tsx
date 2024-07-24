import { createContext, ReactNode, useContext, useState } from "react";


const AuthContext = createContext<{
    loggedIn: boolean,
    setLoggedIn: (value: boolean) => void
}>({ loggedIn: false, setLoggedIn: () => { } })

export const AuthProvider = ({ children }: { children: ReactNode }) => {

    const [loggedIn, setLoggedIn] = useState(false);

    return (
        <AuthContext.Provider value={{ loggedIn, setLoggedIn }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);