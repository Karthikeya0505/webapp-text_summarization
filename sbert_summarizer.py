from transformers import pipeline 

body = 'Google is currently the first name that pops into your head when you enter the online world. Nearly everyone who uses the Internet is familiar with this word and uses it in various ways, yet relatively few people fully understand what Google is. In actuality, Google is a multinational technology corporation that offers users free services and goods relating to the Internet. Online ad techniques, cloud computing for search, software, hardware, etc., are all included in this service.One of the creators of Sun Microsystems, Andy Bechelshim, provided the initial funding for Google. It received this financing when Google had no market presence and was not making any money. After understanding its success, three other "Angel Investors" requested funding. These three angel investors were David Cheriton, a physics professor at Stanford University, Ram Sriram, an entrepreneur, and Jeff Bezos, the creator of Amazon.com. Google got $25 million in funding on July 7, 1999, after these investments in late 1998 and early 1999. In this fundraising, there were several investors. The venture capital firm Kleiner Perkins Cofield & Byers and (Sequoia Capita) Sequoia Capita were two of these significant investors.'

summarizer = pipeline("summarization")

ptorch = summarizer(body, min_length=5, max_length=20)

a=ptorch[0]['summary_text']
print(len(a.split(" ")))
