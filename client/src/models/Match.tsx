import { Player } from "../components/Board";
import { BoardCell } from "./BoardCell";

export interface Match {
    matchId: number;
    currentPlayer: Player, //Player
    state: string,
    board: BoardCell[]
}

