<<<<<<< HEAD
#!/bin/bash
#body display
curl -s -w "%{http_code}\n" $1
=======
#!/bin/bash
#body display
curl -Lsi "$1" 
>>>>>>> 25ec70f2a76f8bd42c11fbe6551a1bbe62bc1573
