import { useContext, useEffect, useState } from 'react';
import { AppContext } from '../AppContext';
import { createMatch, getStatus, postMovement } from '../services/matchService';
import { Cell } from './Cell';
import { Movement } from '../models/Movement';
import { BoardCell } from '../models/BoardCell';
import { Match } from '../models/Match';

export enum Player {
    x = '✖',
    o = '⭘'
}

const emptyBoard: BoardCell[] = [
    { col: 1, row: 1, value: "" },
    { col: 2, row: 1, value: "" },
    { col: 3, row: 1, value: "" },
    { col: 1, row: 2, value: "" },
    { col: 2, row: 2, value: "" },
    { col: 3, row: 2, value: "" },
    { col: 1, row: 3, value: "" },
    { col: 2, row: 3, value: "" },
    { col: 3, row: 3, value: "" },
];


export const Board = () => {

    const context = useContext(AppContext);
    const [board, setBoard] = useState<BoardCell[]>(emptyBoard);
    const [turn, setTurn] = useState<Player>(Player.x);
    const [matchState, setMatchState] = useState<string>(null);

    const { id } = context;

    useEffect(() => {
        const fetchStatus = async () => {
            const match: Match = await getStatus(id);
            setBoard(match.board);
            setTurn(match.currentPlayer);
            setMatchState(match.state);
        };

        fetchStatus();
    }, [id]);

    const retryGame = () => {
        createMatch().then((res) => {
            context.setId(res);
        })
    }

    const handleClick = (x: number, y: number) => {
        console.log('click', { x, y })
        const movement: Movement = { matchId: id, playerId: turn, square: { x: x, y: y } };
        postMovement(movement).then(() => {
            getStatus(id).then((res) => {
                setBoard(res.board);
                setTurn(res.currentPlayer === (Player.x) ? Player.o : Player.x)
                setMatchState(res.state)
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
                            <Cell key={index} index={index} onClick={() => handleClick(cell.col, cell.row)}>
                                {cell.value}
                            </Cell>
                        )
                    })
                }
            </section>
        </main>
    );
};