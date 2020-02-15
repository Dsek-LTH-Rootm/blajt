import { request } from 'http';
//Test connection
interface RgbValues {
    red: number;
    green: number;
    blue: number;
}

const fs = require('fs');

const req = request(
    {
        host: 'pling',
        path: './rgb.json',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    },
    response => {
        console.log(response.statusCode);
    }
);

req.end();
//Listen for values
let rawdata = fs.readFileSync('rgb.json');
console.log(rawdata);
let p: RgbValues = JSON.parse(rawdata);
//Check if values are in correct span
console.log(p.red);

//Forward received values if correct
