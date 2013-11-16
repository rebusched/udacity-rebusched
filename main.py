form="""
<form method="post">
	<h2>Enter some text to ROT13:</h2>
	<p>
	  <label><textarea name="rot13text" id="rot13text" cols="45" rows="5">%(rot13text)s</textarea></label>
	</p>
	<p>
	  <label><input type="submit" name="button" id="button" value="Submit" /></label>
	</p>
</form>
(Norwegian characters excluded)
"""

import webapp2

class MainPage(webapp2.RequestHandler):
	def write_form(self, rot13text=""):
		self.response.out.write(form % {"rot13text": rot13text})
	
	def get(self):
		self.write_form()
			
	"""
	def rot13_engine(rot13text):
		i = 0
		new_rot13text = []
		new_word = ""
		valid_chars = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]

		for c in rot13text:	
			for i in range(len(valid_chars)):
				if c == valid_chars[i]:
					converted_char = convert_rot13(c, i)
					new_rot13text[i] = converted_char
					
		for i in range(len(new_rot13text)):
			new_word = new_word + new_rot13text[i]
			
		return new_word
	"""
		
	def post(self):
		rot13text = self.request.get('rot13text');
		
		if not (rot13text):
			self.write_form("Error: You must provide some text!")
		else:
			new_word = ""
			valid_chars = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
			spec_chars = [",", "?", ":", "(", ")", ".", ";", "&", "#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "{", "}", "@"]
			forbidden_chars = ["<", ">", "/", "$", "'", "\""]
			
			for c in rot13text:	
				if c in spec_chars:
					new_word = new_word + c
				elif c in forbidden_chars:
					if c == "<":
						new_word = new_word + "!"
					if c == ">":
						new_word = new_word + "!"
					if c == "/":
						new_word = new_word + "!"
				elif c in valid_chars:
					i = 0
					new_i = 0
					for i in range(len(valid_chars)):
						if c == valid_chars[i]:
							new_i = i + 26
							
							if new_i > 51:
								new_i = new_i - 52
							
							cc = valid_chars[new_i]					
							
							new_word = new_word + cc
				elif c == ' ':
					new_word = new_word + " "
						
			self.write_form(new_word)
			print new_word

	"""
	def convert_rot13(c, i):
		new_i = i + 13
		
		if new_i > 58:
			new_i = new_i - 58
		
		c = valid_chars[new_i]
		
		return c
	"""
			
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)