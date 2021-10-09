#	PHARMACY BILLING AND INVENTORY MANAGEMENT SYSTEM (v0.1)
Our pharmacy billing and inventory management system - SED Pharma is a system that can be used for keeping track of pharmaceutical items that we currently have in stock, manually update them, get reports periodically as well as fully working command line interface for purchasing items by prescription or as a bulk order. We have built a beautiful tabular UI that makes it very easy to display large amounts of data systematically. There are modules which can be used for checking purchase history or any other logs. This system eliminates the need to use manual work such as manual logging, manually updating excel sheets etc. and implements an all in one solultion which is tightly incorporated into our billing system and works flawlessly with exceptionally good error handling.

##	Project Modules:
- Billing: The staff at the billing counter can use this to generate an order.
	- Has option to search for avaiable drugs (using sequence matching)
	- Indivigual: Order for a single person, has final order edit option as well as logging.
	- Bulk: Bulk orders can be done by using a csv file with order details, file import option is available as it scans all files in a folder and processing bulk order files. Also supports final order edit options.
	- Bill generation: generates bill for all order options.
- Inventory: Access inventory specific tools. (requires admin privileges)
	- Manual search and update of items in stock.
	- Stock updating: Update the current stock by importing items. The provider has to supply a csv file including details of items(name,qty,expiry etc.) and our system can access files within our user interface and can import and process it to update stock.
	- Clearance: Extract and discard expired items currently in stock.
- Management: Contains various submodules for updating global values such as tax, logs etc.. (requires admin previlages)
	- Periodic user logs which includes bill, date/time, order details etc..
	- logging for application debugging.
- Reports: Statistical reports on sales. (requires admin privileges)
	- Itemwise, Periodic(weekly/monthly/yearly), overall sales reports.
	- Graph generation: Graph generation based on the above sales reports.

##	Dependencies:
- Python 3.X installation
- Python Standard library
