// Import the Redis client
import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
 host: '127.0.0.1',
 port: 6379
});

// Add event listeners for connection and error events
client.on('ready', () => {
 console.log('Redis client connected to the server');
});

client.on('error', (error) => {
 console.log(`Redis client not connected to the server: ${error.message}`);
});
