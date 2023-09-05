CREATE TABLE `past_games` (
`game_id` int NOT NULL,
`white_player_id` int NOT NULL,
`black_player_id` int NOT NULL,
`move_no` int NOT NULL,
`move` varchar(16) NOT NULL,
`game_status` varchar(16) NOT NULL,
`pieces_and_positions` varchar(255) NOT NULL,
`id` int NOT NULL AUTO_INCREMENT,
PRIMARY KEY (`id`),
KEY `black_player_id_idx` (`black_player_id`),
KEY `white_player_id_idx` (`white_player_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `current_games` (
`game_id` int NOT NULL AUTO_INCREMENT,
`white_player_id` varchar(255) NOT NULL,
`black_player_id` varchar(255) NOT NULL,
`move_no` int NOT NULL,
`pieces_and_positions` varchar(255) NOT NULL,
`turn` char(1) NOT NULL,
PRIMARY KEY (`game_id`),
KEY `black_player_id_idx` (`black_player_id`),
KEY `white_player_id_idx` (`white_player_id`),
CONSTRAINT `b_id` FOREIGN KEY (`black_player_id`) REFERENCES `user` (`user_id`),
CONSTRAINT `w_id` FOREIGN KEY (`white_player_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `user` (
`username` varchar(32) NOT NULL,
`password` varchar(32) NOT NULL,
`user_id` varchar(255) NOT NULL,
PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;