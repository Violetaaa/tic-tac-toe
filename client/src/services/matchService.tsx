import { Match } from "../models/Match";
import { Movement } from "../models/Movement";

const BASE_URL = 'http://localhost:5000';


export function getStatus(id: number): Promise<Match> {
    return fetch(`${BASE_URL}/status/${id}`, {
        method: 'GET',
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => {
        if (!res.ok) throw new Error('Response KO')
        return res.json()
    }).then((res: Match) => {
        return res
    })
}

export async function createMatch(): Promise<number> {
    const response = await fetch(`${BASE_URL}/create`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (!response.ok) {
        throw new Error('Response KO');
    }

    const data = await response.json();
    return data.matchId;
}

export function postMovement(movement: Movement): Promise<void> {
    return fetch(`${BASE_URL}/move`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(movement)
    }).then(res => {
        if (!res.ok) throw new Error('Response KO');
    });
}





