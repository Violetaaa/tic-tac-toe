import React, { createContext, Dispatch, SetStateAction, useState } from 'react';

type AppContextType = {
    id: number;
    setId: Dispatch<SetStateAction<number>>;
};

export const AppContext = createContext<AppContextType>({ id: 0, setId: () => { } });


export const AppProvider = ({ children, matchId }: { children: React.ReactNode, matchId: number }) => {

    const [id, setId] = useState<number>(matchId);

    return (
        <AppContext.Provider value={{ id, setId }}>
            {children}
        </AppContext.Provider>
    );
};
