const request = require('request');
const lineReader = require('line-reader');

token = "ODczNjYxNTIxODUzNTYyOTEw.YQ7qsg.XUAKHF6gpK3xzFdEcRGPQNQfpAM"
guildID = "884020570491093004"

headers = {'Authorization': "Bot " + token}
lineReader.eachLine('members.txt', function(id) {
    const options = {
        url: `https://discord.com/api/v8/guilds/${guildID}/bans/${id}?reason=lol`,
        method: 'PUT',
        headers: headers,
    }
    request(options, function(err, res, body) {
        console.log(`Request Sent: Banned ${id} Succesfully.`);
    });
})