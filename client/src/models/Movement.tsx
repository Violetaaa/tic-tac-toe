export interface Square {
    x: number;
    y: number;
}

export interface Movement {
    matchId: number;
    playerId: string
    square: Square;
}