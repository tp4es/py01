# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_intro.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tide.oli <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/14 13:49:09 by tide.oli          #+#    #+#              #
#    Updated: 2026/04/14 13:49:09 by tide.oli         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_intro():
	name: str = "rose"
	height: int = 25
	age: int = 30
	print("=== Welcome to the Garden! ===")
	print(f"\nPlant: {name.capitalize()}\nHeight: {str(height)}cm\nAge: {str(age)} days\n")
	print("=== End of PROGRAM! ===")

if __name__ == "__main__":
	ft_garden_intro()