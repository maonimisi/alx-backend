import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client);

(async () => {
  client.on('error', (err) => console.log("Redis client not connected to the server:", err));
  client.on('connect', ()=> console.log("Redis client connected to the server"));
})();

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

async function displaySchoolValue(schoolName) {
  const reply = await asyncGet(schoolName);
    console.log(reply);
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
