name = 'Книга тайн №1'

description = 'Красная с золотым оттиском руки и цифрой 1'

price = 1000
	
usable = True

def on_use(user, reply):
	if user.has_item('mystery_book_2') and user.has_item('mystery_book_3'):
		reply('Раздался хлопок и из ниоткуда возникла дверь.')

		user.remove_item('mystery_book_1')
		user.remove_item('mystery_book_2')
		user.remove_item('mystery_book_3')

		user.open_room(reply, 'special', 'bill_cypher')
	else:
		reply('Чего-то не хватает')
