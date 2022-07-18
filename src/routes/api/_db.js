import { v4 as uuidv4 } from 'uuid';

//plan on replacing hard coded credentials with sql queries

const users = [
	{
		username: 'user',

		password: 'test',
	},
];

let sessions = [];

export const getUserByUsername = async (username) => {
	const existingUser = users.find((user) => user.username === username);
	if (!existingUser) return Promise.resolve(null);
	return Promise.resolve(existingUser);
};


export const createSession = (username) => {
	const session = {
		id: uuidv4(),
		username,
	};
	sessions.push(session);
	return Promise.resolve(session);
};

export const getSession = (id) => {
	const session = sessions.find((session) => session.id === id);
	if (!session) return Promise.resolve(null);
	return Promise.resolve(session);
};

export const removeSession = (id) => {
	const session = sessions.find((session) => session.id === id);
	if (!session) return Promise.reject(new Error('Session not found'));
	sessions = sessions.filter((session) => session.id !== id);
	return Promise.resolve(session);
};
