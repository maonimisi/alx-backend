import redis from 'redis';

const a = 1
const client = redis.createClient();

(async () => {
  client.on('error', (err) => console.log("Redis client not connected to the server:", err));
  client.on('connect', ()=> console.log("Redis client connected to the server"));
})();

client.subscribe('Holberton school channel');

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    process.exit(0);
  }
});
