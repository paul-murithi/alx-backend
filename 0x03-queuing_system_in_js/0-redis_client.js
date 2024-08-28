import redis from 'redis';

//creates a redis client 
const client = redis.createClient();

// Handle connection event
client.on('connect', () => {
    console.log('Redis client connected to server');
});

//Handle error event
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});