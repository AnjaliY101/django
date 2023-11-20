from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def a(request):
    print(dir(request))
    return HttpResponse(f"""
        Whale sharks have teeth in their eyes.
        This fact served on port {request.get_port()}
                                        """)

def login_form(request):
    return HttpResponse( """
<html>
    <head>
        <style>
                        #test{
  height:200px;
  width:200px;
  background-color:blue
}

#b{
  height:20px;
  width: 40 px;
  background-color: green
}
        </style>
    </head>
    <body>
                        <form id="test" action="/polls/login_submit">


<label name = username> Username: <input /> </label>

<label name = password> Password: <input type=password /> </label>



<label />

<submit id="b">
                        Submit
                        
</submit>

</form>
    </body>                        
</html>
                        """)

def handle_login (request):
    if request.method=="POST":
        data = request.POST
        print(data)
