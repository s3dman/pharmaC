* [Documentation](./README.md)
* general:
	- [x] start program session in a new cmd instance
	- [x] tabulated ui
	- [x] step by step user input
	- [x] final edit purchase
	- [x] bill page
	- [x] tax options
	- [x] Show suffix for price
	- [x] Password login for admin pages
	- [x] save main db after each transaction(in ui.py), each value update(in inventorypage.py)
	- [ ] to add more logging
* Billing:
	- [x] generate bulk order from db/csv(all orders are to be considered as bulk orders at checkout)
	- [x] csv file error handle for bulk order
	- [x] bulkadd dont try to buy items if already not in stock but in bulkadd-db
	- [ ] search with name go back option if getting tired
* Inventory with item update features:
	- [x] search for items using name and get ID
	- [x] search with name go back option if getting tired
	- [x] name,qty,price eidtor no go back screen
	- [x] edit details(name and cost) of an item
	- [x] inventory search and edit name, qty,
	- [x] list whole inventory
	- [x] Bulk add
	- [x] remove expired
	- [x] remove expire function not working
* Management:
	- [x] stock updating from csv
	- [x] check expiry
	- [x] get expired items list
	- [x] Global value like tax etc updating
	- [x] Logfile
	- [x] password change option
* Purchase history:
	- [x] store purchase histoy of each person with dates
	- [x] way to access purchase history of induvigual and timely orders
	- [x] datefix
* Reports:
	- [x] item bar graph sale reports
	- [x] graph generation for sales reports
