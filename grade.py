project=int(input("Enter the Project Score"))
internal=int(input("Enter the Project Score"))
external=int(input("Enter the Project Score"))
if project>=50 and internal>=50 and external>=50:
   pro=(70/100)*project
   inte=(10/100)*internal
   exe=(20/100)*external
   total=pro+exe+inte
   if total>90 :
       print("A grade")
   elif total>=80 :
       print("B grade")
   else:
       print("C grade")
else:
   if project<50:
       print("failed in project ",project)
   if internal < 50:
       print("failed in internal ", internal)
   if external < 50:
       print("failed in external ", external)