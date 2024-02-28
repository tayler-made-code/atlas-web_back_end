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
  console.error(`Redis client not connected tot he server: ${error.message}`);
});

// Function to create a hash in Redis
function createHash(hashname, keyValuePairs) {
  const keys = Object.keys(keyValuePairs);
  keys.forEach((key) => {
    client.hset(hashname, key, keyValuePairs[key], redis.print);
  });
}

// Function to display a hash from Redis
function displayHash(hashname) {
  client.hgetall(hashname, (error, reply) => {
    if (error) {
      console.error(`Error getting hash: ${error}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions
createHash('HolbertonSchools', {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
});

displayHash('HolbertonSchools');
