# 
main_menu = """
==== CodeX Human Resource ====
1. Manage Interviewee
2. Manage Worker
0. Exit
==============================
"""
# When approving an interviewee, the system will automatically add the interviewee to the worker list, 
# and remove the interviewee from the interviewee list.
# When declining an interviewee, the system will automatically remove the interviewee from the interviewee list.
interviewee_menu = """
==== CodeX Human Resource ====
1. Add Interviewee
2. List Interviewee
3. Approve Interviewee
4. Decline Interviewee
0. Back
==============================
"""

# 
worker_menu = """
==== CodeX Human Resource ====
1. Add Worker
2. List Worker
3. Update Worker
4. Delete Worker
5. Evaluate Worker
0. Back
==============================
"""

interviewee_name = ""
interviewee_email = ""

worker_name = ""
worker_email = ""
worker_year_of_work = ""

while True:
    print(main_menu)
    main_menu_choice = input("Enter your choice: ")
    if main_menu_choice == "1":
        while True:
            print(interviewee_menu)
            interviewee_menu_choice = input("Enter your choice: ")
            if interviewee_menu_choice == "1":
                new_interviewee_name = input("Enter your name: ")
                new_interviewee_email = input("Enter your email: ")
                if(len(interviewee_name) == 0):
                    interviewee_name = new_interviewee_name
                    interviewee_email = new_interviewee_email
                else:
                    interviewee_name += "," + new_interviewee_name
                    interviewee_email += "," + new_interviewee_email
            elif interviewee_menu_choice in ["2", "3", "4"]:
                if(len(interviewee_name) == 0):
                    print("No interviewee found.")
                else:
                    start_name = 0
                    current_index = 0
                    for name_index in range(len(interviewee_name)):
                        if interviewee_name[name_index] == ",":
                            current_interviewee_name = interviewee_name[start_name:name_index]
                            start_email = 0
                            current_email_index = 0
                            for email_index in range(len(interviewee_email)):
                                if interviewee_email[email_index] == ",":
                                    current_interviewee_email = interviewee_email[start_email:email_index]
                                    if current_email_index == current_index:
                                        print(f"{current_index+1}. {current_interviewee_name} ({current_interviewee_email})")
                                        break
                                    current_email_index += 1
                                    start_email = email_index + 1
                            start_name = name_index + 1
                            current_index += 1
                        elif name_index == len(interviewee_name) -1 :
                            current_interviewee_name = interviewee_name[start_name:]
                            start_email = 0
                            current_email_index = 0
                            for email_index in range(len(interviewee_email)):
                                if interviewee_email[email_index] == ",":
                                    current_interviewee_email = interviewee_email[start_email:email_index]
                                    if current_email_index == current_index:
                                        print(f"{current_index+1}. {current_interviewee_name} ({current_interviewee_email})")
                                        break
                                    start_email = email_index + 1
                                    current_email_index += 1
                                else:
                                    if current_email_index == current_index:
                                        current_interviewee_email = interviewee_email[start_email:]
                                        print(f"{current_index+1}. {current_interviewee_name} ({current_interviewee_email})")
                                        break
                            
                if(interviewee_menu_choice in ["3", "4"]):
                    if(interviewee_menu_choice == "3"):
                        affected_index = int(input("Enter the interviewee index to approve (0 to cancel): "))
                    else:
                        affected_index = int(input("Enter the interviewee index to decline (0 to cancel): "))
                    
                    if(affected_index == 0): break
                    affected_index -= 1
                    if(affected_index > current_index ):
                        print("Selection is out of range.")
                        break
                    flag = False
                    
                    start_name = 0
                    current_name_index = 0
                    for name_index in range(len(interviewee_name)):
                        if(interviewee_name[name_index] == ","):
                            if(current_name_index == affected_index):
                                current_interviewee_name = interviewee_name[start_name:name_index]
                                if(interviewee_menu_choice == "3"):
                                    if(len(worker_name) == 0):
                                        worker_name = current_interviewee_name
                                    else:
                                        worker_name += f",{current_interviewee_name}"
                                inrterviewee_name = interviewee_name[:start_name] + interviewee_name[name_index:]
                                break
                            current_name_index += 1
                            start_name = name_index + 1
                        elif(name_index == len(interviewee_name) - 1):
                            if(current_name_index == affected_index):
                                current_interviewee_name = interviewee_name[start_name:]
                                if(interviewee_menu_choice == "3"):
                                    if(len(worker_name) == 0):
                                        worker_name = current_interviewee_name
                                    else:
                                        worker_name += f",{current_interviewee_name}"
                                interviewee_name = interviewee_name[:start_name]
                    
                    start_email = 0
                    current_email_index = 0
                    for email_index in range(len(interviewee_email)):
                        if(interviewee_email[email_index] == ","):
                            if(current_email_index == affected_index):
                                current_interviewee_email = interviewee_email[start_email:email_index]
                                if(interviewee_menu_choice == "3"):
                                    if(len(worker_email) == 0):
                                        worker_email = current_interviewee_email
                                    else:
                                        worker_email += f",{current_interviewee_email}"
                                interviewee_email = interviewee_email[:start_email] + interviewee_email[email_index:]
                                break
                            current_email_index += 1
                            start_email = email_index + 1
                        elif(email_index == len(interviewee_email) - 1):
                            if(current_email_index == affected_index):
                                current_interviewee_email = interviewee_email[start_email:]
                                if(interviewee_menu_choice == "3"):
                                    if(len(worker_email) == 0):
                                        worker_email = current_interviewee_email
                                    else:
                                        worker_email += f",{current_interviewee_email}"
                                interviewee_email = interviewee_email[:start_email]
                    if(len(worker_year_of_work) == 0):
                        worker_year_of_work = "0"
                    else:
                        worker_year_of_work += ",0"
            elif interviewee_menu_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
    elif main_menu_choice == "2":
        while True:
            print(worker_menu)
            worker_menu_choice = input("Enter your choice: ")
            if worker_menu_choice == "1":
                new_worker = input("Enter your name: ")
                new_email = input("Enter your email: ")
                new_year_of_work = input("Enter your year of work: ")
                if(len(worker_name) == 0):
                    worker_name = new_worker
                    worker_email = new_email
                    worker_year_of_work = new_year_of_work
                else:
                    worker_name += "," + new_worker
                    worker_email += "," + new_email
                    worker_year_of_work += "," + new_year_of_work

            elif worker_menu_choice in ["2", "3", "4", "5"]:
                if(len(worker_name) == 0):
                    print("No worker found.")
                else:
                    start_name = 0
                    current_name_index = 0
                    for name_index in range(len(worker_name)):
                        if worker_name[name_index] == ",":
                            new_worker = worker_name[start_name:name_index]
                            start_email = 0
                            current_email_index = 0
                            for email_index in range(len(worker_email)):
                                if worker_email[email_index] == ",":
                                    new_email = worker_email[start_email:email_index]
                                    if(current_email_index == current_name_index):
                                        break
                                    start_email = email_index + 1
                                    current_email_index += 1
                                elif email_index == len(worker_email):
                                    new_email = worker_email[start_email:]
                            
                            start_year_of_work = 0
                            current_year_of_work_index = 0
                            for year_of_work_index in range(len(worker_year_of_work)):
                                if worker_year_of_work[year_of_work_index] == ",":
                                    new_year_of_work = worker_year_of_work[start_year_of_work:year_of_work_index]
                                    if(current_year_of_work_index == current_name_index):
                                        break
                                    start_year_of_work = year_of_work_index + 1
                                    current_year_of_work_index += 1
                                elif year_of_work_index == len(worker_year_of_work):
                                    new_year_of_work = worker_year_of_work[start_year_of_work:]
                            print(f"{current_name_index+1}. {new_worker} ({new_email}) - {new_year_of_work} years")
                            start_name = name_index + 1
                            current_name_index += 1
                        elif name_index == len(worker_name) -1 :
                            new_worker = worker_name[start_name:]
                            start_email = 0
                            current_email_index = 0
                            for email_index in range(len(worker_email)):
                                if worker_email[email_index] == ",":
                                    new_email = worker_email[start_email:email_index]
                                    if(current_email_index == current_name_index):
                                        break
                                    start_email = email_index + 1
                                    current_email_index += 1
                                elif email_index == len(worker_email) -1:
                                    new_email = worker_email[start_email:]
                            
                            start_year_of_work = 0
                            current_year_of_work_index = 0
                            for year_of_work_index in range(len(worker_year_of_work)):
                                if worker_year_of_work[year_of_work_index] == ",":
                                    new_year_of_work = worker_year_of_work[start_year_of_work:year_of_work_index]
                                    if(current_year_of_work_index == current_name_index):
                                        break
                                    start_year_of_work = year_of_work_index + 1
                                    current_year_of_work_index += 1
                                elif year_of_work_index == len(worker_year_of_work) -1:
                                    new_year_of_work = worker_year_of_work[start_year_of_work:]
                            print(f"{current_name_index+1}. {new_worker} ({new_email}) - {new_year_of_work} years")

                        
                                

                # Update Worker, Delete Worker, Evaluate Worker
                if(worker_menu_choice in ["3", "4", "5"]):
                    if(worker_menu_choice == "3"):
                        affected_index = int(input("Enter the worker index to update: "))
                        new_worker_name = input("Enter new worker name: ")
                        new_email = input("Enter new worker email: ")
                        new_year_of_work = input("Enter new worker year of work: ")
                    elif(worker_menu_choice == "4"):
                        affected_index = int(input("Enter the worker index to delete: "))
                    else:
                        affected_index = int(input("Enter the worker index to evaluate: "))

                    if(affected_index == 0): break
                    affected_index -= 1
                    if(affected_index > current_name_index):
                        print("Selection is out of range.")
                        break

                    print("Editing git")

                    flag = False
                    start_name = 0
                    current_name_index = 0
                    for name_index in range(len(worker_name)):
                        if worker_name[name_index] == ",":
                            if(current_name_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_name = worker_name[:start_name] + new_worker_name + worker_name[name_index:]
                                elif(worker_menu_choice == "4"):
                                    worker_name = worker_name[:start_name] + worker_name[name_index+1:]
                                break
                            start_name = name_index + 1
                            current_name_index += 1
                        elif name_index == len(worker_name) -1 :
                            if(current_name_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_name = worker_name[:start_name] + new_worker_name
                                elif(worker_menu_choice == "4"):
                                    worker_name = worker_name[:start_name]                
                            

                    start_email = 0
                    current_email_index = 0
                    for email_index in range(len(worker_email)):
                        if worker_email[email_index] == ",":
                            if(current_email_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_email = worker_email[:start_email] + new_email  + worker_email[email_index:]
                                elif(worker_menu_choice == "4"):
                                    worker_email = worker_email[:start_email] + worker_email[email_index+1:]
                                break
                            current_email_index += 1
                            start_email = email_index + 1
                        elif email_index == len(worker_email) - 1:
                            if(current_email_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_email = worker_email[:start_email] + new_email
                                elif(worker_menu_choice == "4"):
                                    worker_email = worker_email[:start_email]
                        if flag: break
                    
                    start_year_of_work = 0
                    current_year_of_work_index = 0
                    for year_of_work_index in range(len(worker_year_of_work)):
                        if worker_year_of_work[year_of_work_index] == ",":
                            if(current_year_of_work_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_year_of_work = worker_year_of_work[:start_year_of_work] + new_year_of_work + worker_year_of_work[year_of_work_index:]
                                elif(worker_menu_choice == "4"):
                                    worker_year_of_work = worker_year_of_work[:start_year_of_work] + worker_year_of_work[year_of_work_index+1:]
                                break
                            current_year_of_work_index += 1
                            start_year_of_work = year_of_work_index + 1
                        elif year_of_work_index == len(worker_year_of_work) - 1:
                            if(current_year_of_work_index == affected_index):
                                if(worker_menu_choice == "3"):
                                    worker_year_of_work = worker_year_of_work[:start_year_of_work] + new_year_of_work
                                elif(worker_menu_choice == "4"):
                                    worker_year_of_work = worker_year_of_work[:start_year_of_work]
                        if flag: break

            elif worker_menu_choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
    elif main_menu_choice == "0":
        print("Thank you for using CodeX Human Resource.")
        break
    else:
        print("Invalid choice. Please try again.")