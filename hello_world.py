from datetime import date

# Get the current date and time
current_date_time = date.today()
print(current_date_time)
# Format the date as a string
#formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
#print("Formatted date and time:", formatted_date_time)

print("Hello world")
bucket = "Banana"
jumlah = 12
print(bucket)
print(type(bucket)) #melihat tipe data variable
print (bucket+" "+str(jumlah)) #str integer to string
fruits = ['Pisang','Jambu','Nanas'] #list
print(fruits[1:2])
fruits.append('Anggur') #tambah data list
print(fruits)
database =['Oracle','Postgres']#Extend data list
fruits.extend(database)
print(fruits)
fruits[2]='Durian' #update item data list
print(fruits)
fruits.remove("Anggur") #remove by text
print(fruits)
fruits.pop(0) 
print(fruits) #(remove, del, pop)
set_hewan = {"Kucing", "Anjing","Semut"}
print(set_hewan)
set_hewan.add("gajah")
print(set_hewan)
set_kendaraan=("motor","sepeda")
set_hewan.update(set_kendaraan)
print(set_hewan)