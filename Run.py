import re

# Making Backup of file

f1 = open('/home/guest/Documents/Programs/BPO/input.txt','r')
filedata = f1.read()
f1.close()

# Reducing spaces and adding line breaks for further operations

filedata = re.sub(">",">\n",filedata)
filedata = re.sub("<","\n<",filedata)

for x in range(0,100):
	filedata = filedata.replace('  ',' ')

filedata = filedata.replace('< ','<')
filedata = filedata.replace(' >','>')
filedata = filedata.replace('< /','</')
filedata = filedata.replace('</ ','</')
filedata = filedata.replace('/ >','/>')
filedata = filedata.replace(' />','/>')

for x in range(0,100):
	filedata = filedata.replace('\n\n','\n')

f3 = open('/home/guest/Documents/Programs/BPO/backup.txt','w')
f3.write(filedata)
f3.close()

# Replace <h4  with <div

filedata = filedata.replace('<h4 ','<div ')

# Replacing <h4> with <div>

filedata = filedata.replace('<h4>','<div>')
filedata = filedata.replace('</h4>','</div>')

# Removing all div and style constraints

filedata = re.sub("<div[^>]*>","",filedata)
filedata = re.sub("<div>","",filedata)
filedata = re.sub("</div>","",filedata)
filedata = re.sub("style[^>]*=[^>]*\"[^>]*\"","",filedata)

# Removing page break and later add it on top cleanly

filedata = re.sub("<[^>]*more[^>]*>","",filedata)

# Replacing >&nbsp;</ with ><br /><

filedata = filedata.replace('>\n&nbsp;\n</','>\n<br />\n</')

# Replacing &nbsp; with space

filedata = filedata.replace('&nbsp;',' ')

# Replacing <br/> with <br />

filedata = filedata.replace('<br/>','<br />')

# Removing <span>

filedata = filedata.replace('<span>','')
filedata = filedata.replace('</span>','')

# Removing <p>

filedata = filedata.replace('<p>','')
filedata = filedata.replace('</p>','')

# Replacing bold with strong

filedata = filedata.replace('<b>','<strong>')
filedata = filedata.replace('</b>','</strong>')

# Removing useless tags aroung useful tags

filedata = filedata.replace('<strong>\n<br />\n</strong>','<br />')

# Replacing i with em

filedata = filedata.replace('<i>','<em>')
filedata = filedata.replace('</i>','</em>')

# Aligning images to center

filedata = re.sub("<img ","<div style=\"text-align: center;\">\n<img ",filedata)

# Removing <a> from image

filedata = re.sub("<a[^>]*href[^>]*.jpg[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.jpeg[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.png[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.gif[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.JPG[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.JPEG[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.PNG[^>]*>","",filedata)
filedata = re.sub("<a[^>]*href[^>]*.GIF[^>]*>","",filedata)

# Reducing spaces and adding line breaks again

filedata = re.sub(">",">\n",filedata)
filedata = re.sub("<","\n<",filedata)

for x in range(0,100):
	filedata = filedata.replace('  ',' ')

filedata = filedata.replace('< ','<')
filedata = filedata.replace(' >','>')
filedata = filedata.replace('< /','</')
filedata = filedata.replace('</ ','</')
filedata = filedata.replace('/ >','/>')
filedata = filedata.replace(' />','/>')

for x in range(0,100):
	filedata = filedata.replace('\n\n','\n')

# Run this program recursively to clean again

f2 = open('/home/guest/Documents/Programs/BPO/input.txt','w')
f2.write(filedata)
f2.close()

# Writing into output file with ending

f1 = open('/home/guest/Documents/Programs/BPO/input.txt','r')
f4 = open('/home/guest/Documents/Programs/BPO/output.txt','w')
f4.write("<!--more-->")

for line in f1:
	if '<img ' in line:
		f4.write(line)
		f4.write('</div>\n')
	else:
		f4.write(line)

f4.close()

# Giving a compressed output

f5 = open('/home/guest/Documents/Programs/BPO/output.txt','r')
filedata = f5.read()

for x in range(0,100):
	filedata = filedata.replace('\n','')

f5.close()

f6 = open('/home/guest/Documents/Programs/BPO/compressed.txt','w')
f6.write(filedata)
f6.close()
