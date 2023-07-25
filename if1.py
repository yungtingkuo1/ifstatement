items = int(input("Enter number of packages sent:"))

package_weight = 0
sent_package = 0
total_sent_weight = 0


for item in range(items):     
    weight = int(input(f"Enter weight of item number {item + 1}:"))
    if weight < 1 or weight > 10:
        print("Weight can only between 1 and 10 kg!")
        break
 
    #package_weight = package_wegiht + weight
    package_weight += weight

    if package_weight > 20:
        sent_package += 1
        total_sent_weight += package_weight - weight
        package_weight = weight
if package_weight > 0: 
    sent_package += 1
    total_sent_weight += package_weight


print(f"Sent packages{sent_package}")
print(f"Sent weight:{total_sent_weight}")


