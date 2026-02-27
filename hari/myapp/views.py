from django.shortcuts import render
def calculate_bill(request):
	p=int(request.POST.get('Price',0))
	gst=int(request.POST.get('GST',0))
	bill = p + (p*(gst/100)) if request.method=='POST' else 0
	print("Price=",p)
	print("GST=",gst)
	print("Total Bill=",bill)
	return render(request,'myapp/hariGST.html',{'p':p,'gst':gst,'bill':bill})