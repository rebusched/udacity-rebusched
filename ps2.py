form="""
<!--Basert på samarbeid mellom Benedicte og Peter-->
<form method="post">
	<h2>Enter some text to ROT13:</h2>
	<p>
	  <label><textarea name="rot13text" id="rot13text" cols="45" rows="5">%(rot13text)s</textarea></label>
	</p>
	<p>
	  <label><input type="submit" name="button" id="button" value="Submit" /></label>
	</p>
</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, rot13text=""):
		self.response.out.write(form % {"rot13text": rot13text})
	
	def get(self):
		self.write_form()
		
	def post(self):
		user_rot13 = self.request.get('rot13text')
		rot13 = rot13_engine(self.request.get('rot13text'))
		
		if not (rot13text):
			self.write_form("Error: You must provide some text!")
		else:
			self.response.out.write("Takker og bukker!")
			
	def rot13_engine(rot13text):
		i = 0
		new_rot13text = []
		new_word = ""
		valid_chars = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "æ", "Æ", "ø", "Ø", "å", "Å"]

		for c in rot13text:	
			for i in range(len(valid_chars)):
				if c == valid_chars[i]:
					converted_char = convert_rot13(c, i)
					new_rot13text[i] = converted_char
					
		for i in range(len(new_rot13text)):
			new_word = new_word + new_rot13text[i]
			
		return new_word
			
	def convert_rot13(c, i):
		new_i = i + 13
		
		if new_i > 58:
			new_i = new_i - 58
		
		c = valid_chars[new_i]
		
		return c
			
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)