import preprocess from 'svelte-preprocess';
import adapter from '@sveltejs/adapter-node';
import { Server } from 'socket.io';


const webSocketServer = {
	name: 'webSocketServer',
	configureServer(server) {
	  const io = new Server(server.httpServer)
  
	  io.on('connection', (socket) => {
		socket.emit('eventFromServer', 'Hello, World 👋')
	  })
	},
  }

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [
		preprocess({
			postcss: true,
		}),
	],
	kit: {
		adapter: adapter(),
		vite: {
		  plugins: [webSocketServer],
		},
	  },
};

export default config;



