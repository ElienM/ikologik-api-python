class AbstractIkologikObject(object):
	id: str = None
	createdDate: int = None
	modifiedDate: int = None

	def __init__(self):
		super().__init__()
