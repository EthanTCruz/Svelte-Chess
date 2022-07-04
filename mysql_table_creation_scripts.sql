CREATE TABLE `user` (
`username` varchar(32) NOT NULL,
`password` varchar(32) NOT NULL,
`user_id` varchar(255) NOT NULL,
PRIMARY KEY (`user_id`)
);
 CREATE TABLE `current_games`
(                                                                          `game_id` varchar(255) NOT NULL,                                                                                        `white_player_id` varchar(255) NOT NULL,                                                                                `black_player_id` varchar(255) NOT NULL,                                                                                `move_no` int NOT NULL,                                                                                                 `pieces_and_positions` varchar(255) NOT NULL,                                                                           `turn` char(1) NOT NULL,                                                                                                KEY `black_player_id_idx` (`black_player_id`),                                                                          KEY `white_player_id_idx` (`white_player_id`),                                                                          CONSTRAINT `b_id` FOREIGN KEY (`black_player_id`) REFERENCES `user` (`user_id`),                                        CONSTRAINT `w_id` FOREIGN KEY (`white_player_id`) REFERENCES `user` (`user_id`)
);
CREATE TABLE `past_games` (
`game_id` int NOT NULL,
`white_player_id` varchar(255) NOT NULL,
`black_player_id` varchar(255) NOT NULL,
`move_no` int NOT NULL,
`move` varchar(16) NOT NULL,
`game_status` varchar(16) NOT NULL,
KEY `black_player_id_idx` (`black_player_id`),
KEY `white_player_id_idx` (`white_player_id`),
CONSTRAINT `black_player_id` FOREIGN KEY (`black_player_id`) REFERENCES `user` (`user_id`),
CONSTRAINT `white_player_id` FOREIGN KEY (`white_player_id`) REFERENCES `user` (`user_id`)
);
