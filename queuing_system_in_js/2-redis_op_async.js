// Import the Redis client
import redis from 'redis';
import { promisify } from 'util';

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

// convert client.get to a promise-based function
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  // It should set in Redis the value for the key schoolName
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  // log to the console the value for the key passed as argument
  try { 
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.error('Error getting school value', error);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
