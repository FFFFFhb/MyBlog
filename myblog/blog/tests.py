from django.test import TestCase
from blog.checkName import emails
import re         

class MyTestCase(TestCase):
	def test_emails(self):
		e = 'fenghaobin@qq.com'
		b = 'abc'
		c = 'fenghaobin'
		d = 'fenghaobin@'
		z= emails(b)
		self.assertEqual(z,True,'method emails test failed')
		

