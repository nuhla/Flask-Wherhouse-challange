# Flask-Wherhouse-challange
- befor you start you need to unstall wkhtmltopdf from this link 
  https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe

- install it in your machin and edit the path (Enviroment varoables to get the bin folde )
  like this => "C:\Program Files\wkhtmltopdf\bin"

- update the env to eun main.py 
  $env:FLASK_APP = "main.py"

- update the env to work with debugg mode
  $env:FLASK_ENV = "development"

- run the program 
  flask run
