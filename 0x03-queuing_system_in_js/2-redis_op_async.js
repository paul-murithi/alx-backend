#!/usr/bin/yarn dev
import { createClient, print } from 'redis';
import { promisify } from 'util';

//creates a redis client 
const client = createClient();

//Handle error event
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
  };
  
const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

// Handle connection event
client.on('connect', async () => {
  console.log('Redis client connected to server');
  await main();
});
