from django.http import HttpResponse
def index(request):
    return HttpResponse('''
    <head><link href="https://fonts.googleapis.com/css?family=Abel" rel="stylesheet"></head>
    <style> .h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6 {
   margin-bottom: .5rem;
   font-family: 'abel', sans-serif;
   font-weight: 700;
   line-height: 1.2
   } body {
   font-size: 1rem;
   background-color: Cyan}</style>
 
 
    <h1>My Website</h1> <a href="https://rohandas28.github.io/"> Click To Visit My Tiny Little Website!</a>
    <h1>Harry Bhai Ka Website </h1> <a href="https://www.codewithharry.com/"> Click To Visit The Best Website!</a>
    <h1>My Favourite Movie </h1> <a href= "https://www.google.com/search?q=interstellar&oq=interstellar&aqs=chrome..69i57j69i65.6672j0j1&sourceid=chrome&ie=UTF-8"> Click to See!</a>
    <h1>My Favourite Youtube creator </h1> <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww"> Click To Visit And Subscribe To Him!</a>
    <h1>Psst! Follow Me On Github! LoL!</h1> <a href="https://github.com/RohanDas28"> Click To Visit And Follow!</a>
    ''')
def about(request):
    return HttpResponse('lol')
  