import Channel from './common/Channel.js';
import Config from './config.js';

const irc = require('irc');

export default class TheBOT {
	catchAlls = [];
	client = null;
	commands = {};
	modules = {};

	constructor () {
		this.commands = {};
		this.catchAlls = [];
		this.doKicks = [];
		this.doTopics = [];
		this.minuteInvokes = [];
		
	}
	
	init () {
		this.client = new irc.client(Config.irc.server, Config.irc.botname, {
			channels: _.keys(Config.irc.channels),
		autoConnect: false,
		autoRejoin: true,
		retryCount: 10,
		userName: Config.irc.botname
		});
		
		this.client.activateFloodProtection();
		this.users = {};
		//get users
		
		this.client.connect();
	}
}

