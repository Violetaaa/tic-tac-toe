export enum Player {
    x = '✖',
    o = '⭘'
}

export const PlayerMapper = {
    toBackModel: (player: Player): string => {
        switch (player) {
            case Player.x: return 'x';
            case Player.o: return 'o';
            default: throw new Error('Invalid value');
        }
    },

    toFrontModel: (player: string): Player => {
        switch (player) {
            case 'x': return Player.x;
            case 'o': return Player.o;
            default: throw new Error('Invalid value');
        }
    }
};