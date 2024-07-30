import { useContext, useEffect, useState } from 'react';
import { AppContext } from '../AppContext';
import { createMatch, getStatus, postMovement } from '../services/matchService';
import { Cell } from './Cell';
import { Movement } from '../models/Movement';
import { BoardCell } from '../models/BoardCell';
import { Match } from '../models/Match';
import { Player, PlayerMapper } from '../models/Player';
import { emptyBoard } from '../utils';
import { Modal } from './Modal';


export const Board = () => {

    const context = useContext(AppContext);
    const [board, setBoard] = useState<BoardCell[]>(emptyBoard);
    const [player, setPlayer] = useState<Player>(Player.x);
    const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
    const [status, setStatus] = useState<string>('');

    const { id } = context;

    useEffect(() => {
        const fetchStatus = async () => {
            const match: Match = await getStatus(id);
            setBoard(match.board);
            setPlayer(PlayerMapper.toFrontModel(match.currentPlayer));
            setStatus(match.status);
        };

        fetchStatus();
    }, [id]);

    useEffect(() => {
        if (status && status != 'ON GOING' && status != 'INIT') setIsModalOpen(true)
    }, [status]);

    const retryGame = () => {
        createMatch().then((res) => {
            context.setId(res);
        })
        setBoard(emptyBoard);
        setIsModalOpen(false);
    }

    const handleClick = (x: number, y: number) => {
        const movement: Movement = { matchId: id, playerId: PlayerMapper.toBackModel(player), square: { x: x, y: y } };
        postMovement(movement).then(() => {
            getStatus(id).then((res) => {
                setBoard(res.board);
                setPlayer(PlayerMapper.toFrontModel(res.currentPlayer))
                setStatus(res.status);
            })
        })
    }

    return (
        <main className='board'>
            <button onClick={retryGame}>Retry</button>
            <section className="game">
                {
                    board.map((cell, index) => {
                        return (
                            <Cell key={index} index={index} onClick={() => handleClick(cell.row, cell.col)}>
                                {cell.value ? PlayerMapper.toFrontModel(cell.value) : cell.value}
                            </Cell>
                        )
                    })
                }
            </section>
            <section>
                {isModalOpen &&
                    <Modal
                        message={status}
                        onClose={() => retryGame()}
                    />
                }
            </section>
        </main>
    );
};