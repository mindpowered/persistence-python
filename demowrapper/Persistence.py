class Persistence:
	"""
	Provides a way of storing data for mindpowered packages.
	When mindpowered packages need to persist data, they will use Get and Mutate, which in turn will call the Mutators and Getters you have set up.
	You can set up the Mutators and Getters however you like whether to access a database such as MySQL or MongoDB, or simply write and read from text files.
	Note: when using a mapping (updateMapper, queryMapper, resultMapper), the data will be passed in as the first argument to the mapping function.
	"""

	def AddMutator(recordType: int, operationName: int, strategyMethod: int, updateMapper: int, useRecordDataAsParams: int):
		"""		Set up a Mutator to change stored data
		Args:
			recordType (int):type of record being changed (eg. databsae table name)
			operationName (int):action being performed on the record (eg. insert, update)
			strategyMethod (int):method to call to actually perform the mutation
			updateMapper (int):method to call on recordData before calling strategyMethod with the results
			useRecordDataAsParams (int):if set to true, the recordData will be passed as the arguments to strategyMethod, rather than as the first argument
		"""
	def AddGetter(recordType: int, operationName: int, strategyMethod: int, queryMapper: int, resultMapper: int, useQueryValuesAsParams: int):
		"""		Set up a Getter to retrieve data
		Args:
			recordType (int):type of record being retrieved (eg. databsae table name)
			operationName (int):query being performed for the record type (eg. findById, findByName, findActive, getInsertedId)
			strategyMethod (int):method to call to actually perform the data retrieval
			queryMapper (int):method to call on queryValues before calling strategyMethod with the results
			resultMapper (int):method to call on data returned from the strategyMethod before returning the results
			useQueryValuesAsParams (int):if set to true, the queryValues will be passed as the arguments to strategyMethod, rather than as the first argument
		"""
	def Mutate(recordType: int, operationName: int, recordData: int):
		"""		Use a Mutator to change stored data
		Args:
			recordType (int):type of record being changed (eg. databsae table name)
			operationName (int):action being performed on the record (eg. insert, update)
			recordData (int):data being updated or saved by passing through updateMapper and then strategyMethod
		"""
	def Get(recordType: int, operationName: int, queryValues: int) -> bool:
		"""		Use a Getter to retrieve data
		Args:
			recordType (int):type of record being retrieved (eg. databsae table name)
			operationName (int):query being performed for the record type (eg. findById, findByName, findActive, getInsertedId)
			queryValues (int):values that will be passed through queryMapper and then strategyMethod to perform the query
		Returns:
			RET HERE
		"""
#END
