#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

const client = createClient()

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

const updateHash = (hashName, fieldName, fieldValue) => {
    client.HSET(hashName, fieldName, fieldValue, print);
};

const printHash = (hashName) => {
    client.HGETALL(hashName, (_err, reply) => console.log(reply));
};

function main() {
    const hashValue = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };
    for (const [field, value] of Object.entries(hashValue)) {
        updateHash('HolbertonSchools', field, value);
    }
    printHash('HolbertonSchools');
}
client.on('connect', () => {
    console.log('Redis client connected to the server');
    main();
  });
