import { BoardCell } from "./BoardCell";

export interface Match {
    matchId: number;
    currentPlayer: string, //Player
    status: string,
    board: BoardCell[]
}

