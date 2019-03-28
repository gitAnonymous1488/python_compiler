class read_ahead(object):
	def __init__ (self, file_str):
		self.file_str = file_str
		self.pos = 0
		self.bookmark_pos = 0

	def inc(self):
		if self.pos <= len(self.file_str):
			self.pos += 1

	def get_char(self):
		if self.pos < len(self.file_str):
			char = self.file_str[self.pos]
		else:
			char = ""

		self.inc()
		return char

	def get_current(self):
		return self.file_str[self.pos]

	def bookmark(self):
		self.bookmark_pos = self.pos

	def reset_to_bookmark(self):
		self.pos = self.bookmark_pos

	def set_bookmark(self, pos):
		self.bookmark_pos = pos


class token_list(object):
	def __init__(self):
		self.token_list = []
		self.pos = 0

	def add_token(self, token):
		self.token_list.append(token)

	def get_next_token(self):
		token = None
		if self.pos < len(self.token_list):
			token = self.token_list[self.pos]
			self.pos += 1
		return token



