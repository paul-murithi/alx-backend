#!/usr/bin/yarn dev
import { createClient, print } from 'redis';

//creates a redis client 
const client = createClient();

// Handle connection event
client.on('connect', () => {
    console.log('Redis client connected to server');
});

//Handle error event
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

const setNewSchool = (schoolName, value) => {
    client.SET(schoolName, value, print);
  };
  
  const displaySchoolValue = (schoolName) => {
    client.GET(schoolName, (_err, reply) => {
      console.log(reply);
    });
  };
  
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');