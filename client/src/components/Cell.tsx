export const Cell = ({ children, index, onClick }: { children: React.ReactNode, index: number, onClick: () => void }) => {
    return (
        <div
            className="cell"
            onClick={onClick}
        >
            {children}
        </div>
    )
}