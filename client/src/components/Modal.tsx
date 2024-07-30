export const Modal = ({ message, onClose }: { message: string, onClose: () => void }) => {

    const getMessage = (message: string) => {
        switch (message) {
            case 'x WIN': return 'Player ✖ wins the game!';
            case 'o WIN': return 'Player ⭘ wins the game!';
            case 'DRAW': return 'It\'s a tie!';
        }
    }

    return (
        <>
            <div className="modal-overlay" onClick={onClose}></div>
            <div className="modal">
                <h2>{getMessage(message)}</h2>
                <button onClick={onClose}>Close</button>
            </div>
        </>
    );
};