# Ex.04 Design a Website for Server Side Processing
## Date:27.02.2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:

```
<html>
    <head>
        <title>Hari Prasath.M</title>
        <style>
            .box
{
    border: solid 11px oklab(27.063% 0.0017 -0.15899);
    background-color: antiquewhite;
    padding: 50px;
    margin-left: 500px;
    margin-right: 500px;
    margin-top: 100px;
}
body
{
    background-color: rgb(112, 255, 80);
    text-align: center;
}
        </style>>
    </head>
    <body>
        <div class="box">
            <h1>Total bill Calculation</h1><br>
            <h3>Hari prasath-(25018172)</h3>
            <br>
            <form method="post">
                {% csrf_token %}
                <label>Price : </label><input type="text" name="Price"><br>
                <label>GST : </label><input type="text" name="GST"><br><br>
                <input type="submit" value="Calculate"><br><br>
                <label>Bill</label><input type="text" value="{{ bill }}">
            </form>
        </div>
    </body>
</html>

views.py

from django.shortcuts import render
def calculate_bill(request):
	p=int(request.POST.get('Price',0))
	gst=int(request.POST.get('GST',0))
	bill = p + (p*(gst/100)) if request.method=='POST' else 0
	print("Price=",p)
	print("GST=",gst)
	print("Total Bill=",bill)
	return render(request,'myapp/hariGST.html',{'p':p,'gst':gst,'bill':bill})

  urls.py
  
  from django.urls import path
from myapp import views
urlpatterns = [path('', views.calculate_bill, name='bill')]

## OUTPUT - SERVER SIDE:

c:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot (26).png

## OUTPUT - WEBPAGE:

c:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot (27).png


## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
