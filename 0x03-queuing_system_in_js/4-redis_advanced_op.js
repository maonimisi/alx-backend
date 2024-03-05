import redis from 'redis';

const client = redis.createClient();

(async () => {
  client.on('error', (err) => console.log("Redis client not connected to the server:", err));
  client.on('connect', ()=> console.log("Redis client connected to the server"));
})();

const name = 'HolbertonSchools';
const value = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};
for (const [key, val] of Object.entries(value)) {
  client.hset(name, key, val, (_, reply) => redis.print(`Reply: ${reply}`));
}
client.hgetall(name, (_, object) => console.log(object));
