Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import webbrowser, time
... 
... url = input("Enter link: ")
... 
... while True:
...  try:
...   dur = int(input("Watch time: "))
...   break
...  except:
...   print("\nEnter a number!\n")
... 
... while True:
...  try:
...   wtc = int(input("How many views: "))
...   break
...  except:
...   print("\nEnter a number!\n")
... 
... for i in range(wtc):
...  webbrowser.open_new(url)
