import redis from 'redis';

// Create a redis client
const publisher = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

// Add event listeners for connection and error events
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

publisher.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to publish a message after a delay
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

// Call the function with the specified message and delays
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
