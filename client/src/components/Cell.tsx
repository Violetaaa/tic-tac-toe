export const Cell = ({ children, onClick }: { children: React.ReactNode, index: number, onClick: () => void }) => {
    return (
        <div
            className="cell"
            onClick={onClick}
        >
            {children}
        </div>
    )
}