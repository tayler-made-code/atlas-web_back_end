// Import the Redis client
import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient({
 host: '127.0.0.1',
 port: 6379
});

// Add event listeners for connection and error events
subscriber.on('connect', () => {
 console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
 console.log(`Redis client not connected to the server: ${error.message}`);
});

// Subscribe to the channel
subscriber.subscribe('holberton school channel');

// Listen for messages on the channel
subscriber.on('message', (channel, message) => {
 console.log(message);
 if (message === 'KILL_SERVER') {
   subscriber.unsubscribe('holberton school channel');
   subscriber.quit();
 }
});
